import logging
import math
import uuid
import re
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.core.cache import cache
from io import BytesIO
from .import utils
from . import cache_utils
from django.http import JsonResponse
from django.views.decorators.http import require_GET,require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from . import models

@require_POST
@csrf_exempt
def check_user(request):
    username = request.POST["username"]
    try:
        User.objects.get(username=username)
        return JsonResponse({"msg": "该账号已被注册", "issuccess": False})
    except:
        return JsonResponse({"msg": "该账号可用", "issuccess": True})


@require_POST
@csrf_exempt
def check_login(request):
    username = request.POST["username"]
    try:
        User.objects.get(username=username)
        return JsonResponse({"msg": "该账号可用", "issuccess": True})
    except:
        return JsonResponse({"msg":"该账号尚未注册，请重新填写","issuccess":False})


def register(request):
    if request. method == "GET":
        context = {"msg": "请认真填写如下选项" }
        return render(request, "users/register.html", context)
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST.get("password").strip()
        password2 = request.POST.get("password2").strip()
        nikename = request.POST.get("nikename").strip()
        code = request.POST["code"].strip()
        if code == '':
            return render(request, "users/register.html", {"msg": "没有填写验证码，请重新注册！！"})
        msg = request.session["code"]
        if msg.lower() != code.lower():
            return render(request, "users/register.html", {"msg": "验证码有误！！"})
        if username == "":
            return render(request, "users/register.html", {"msg": "用户名称不能为空"})
        if len(password) < 6:
            return render(request, "users/register.html", {"msg": "密码长度不能小于6位"})
        if password !=password2:
            return render(request, "users/register.html", {"msg": "俩次密码不相等"})
        try:
            User.objects.get(username=username)
            return render(request, "users/register.html", {"msg": "该用户名已存在，请重新注册"})
        except:
            try:
                user = User.objects.create_user(username=username, password=password)
                print(user)
                userinfo = models.UserInfo(nikename=nikename, user=user)
                print(userinfo)
                user.save()
                userinfo.save()
                return render(request, "users/login.html", {"msg": "恭喜您，注册成功,请登录***"})
            except Exception as e :
                logger = logging.getLogger("django")
                logger.info("请认真填写如下选项")
                print(e)
                return render(request, "users/register.html", {"msg": "对不起，注册失败！！"})

def user_login(request):
    if request.method == "GET":
        try:
            next_url = request.GET["next"]
        except:
            next_url = "/users/info"
        print(next_url)
        return render(request, "users/login.html", {"msg": "请认真填写如下选项", "next_url":next_url})
    elif request.method == "POST":
        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        next_url = request.POST.get("next", "/users/info")
        print(next_url)
        #判断验证码
        if request.session.get("error_count") is None:
            request.session["error_count"] = 0
        if request.session["error_count"]>=3:
            code = request.POST["code"].strip()
            if code == '':
                return render(request, "users/login.html", {"msg": "没有填写验证码，请重新登录！！"})
            msg = request.session["code"]
            if msg.lower() != code.lower():
                return render(request, "users/login.html", {"msg": "验证码有误！！"})
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #将验证通过用户信息保存在request，
                login(request, user)
                del request.session["error_count"]
                return redirect(next_url)
                # return render(request, "users/info.html", {})
            else:
                request.session["error_count"] += 1
                return render(request, "users/login.html", {"msg": "你的账号已被锁定，请联系管理员！！"})
        else:
            request.session["error_count"] += 1
            return render(request, "users/login.html", {"msg": "用户名或密码错误！！"})

def user_logout(request):
    logout(request)
    return render(request, "users/login.html", {"msg": "退出成功,请重新登录"})

@login_required()
def info(request):
    return render(request, 'users/info.html', {})


def edit(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        return render(request, 'users/edit.html', {'user': user})
    elif request.method == "POST":
        userinfo = models.UserInfo.objects.get(user=request.user)
        print(userinfo)
        nikename = request.POST.get('nikename').strip()
        gender = request.POST.get('gender').strip()
        age = request.POST.get('age').strip()
        phone = request.POST.get('phone').strip()
        try:
            avatar = request.FILES.get('avatar',"static/image/header/pizhi.jpg")
            if age == "":
                return render(request, "users/info.html", {"msg": "年龄不能为空,请重新修改"})
            if nikename == "":
                return render(request, "users/info.html", {"msg": "昵称不能为空,请重新修改"})
            if phone == "":
                return render(request, "users/info.html", {"msg": "电话不能为空,请重新修改"})
            try:
                # userinfo(nikename=nikename, gender=gender, age=age, phone=phone, avatar=avatar,user=request.user)
                userinfo.nikename = nikename
                userinfo.gender = gender
                userinfo.age = age
                userinfo.phone = phone
                userinfo.avatar = avatar
                userinfo.save()
                return render(request, "users/info.html", {"msg": "修改成功"})
            except Exception as e:
                logger = logging.getLogger("django")
                logger.info("开始加载数据")
                print("错误信息是：===>", e)
                return render(request, "users/edit.html", {"msg": "修改失败！！"})
        except:
            try:
                userinfo.nikename = nikename
                userinfo.gender = gender
                userinfo.age = age
                userinfo.phone = phone
                userinfo.save()
                return render(request, "users/info.html", {"msg": "修改成功"})
            except Exception as e:
                logger = logging.getLogger("django")
                logger.info("开始加载数据")
                print("错误信息是：===>", e)
                return render(request, "users/edit.html", {"msg": "修改失败！！"})
def code(request):
    file = BytesIO()
    img, msg = utils.create_code()
    request.session["code"] = msg
    img.save(file, 'PNG')
    return HttpResponse(file.getvalue(), 'image/png')


def editpwd(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        return render(request, "users/editpwd.html", {})
    else:
        oldpwd = request.POST['oldpwd'].strip()
        newpwd = request.POST['newpwd'].strip()
        confirmpwd = request.POST['confirmpwd'].strip()
        if len(newpwd) < 6:
            return render(request, "users/editpwd.html", {"msg": "输入新密码小于6位"})
        if newpwd != confirmpwd:
            return render(request, "users/editpwd.html", {"msg": "俩次密码输入不相等"})
        user = auth.authenticate(username=request.user.username, password=oldpwd)
        print(request.user.username)
        print(oldpwd)
        print(user)
        if user is not None:
            if user.is_active:
                try:
                    user.set_password(newpwd)

                    user.save()
                    return redirect(reverse("users:user_login"))
                except Exception as e:
                    print(e)
                    return render(request, 'users/editpwd.html', {"msg": "密码修改失败，请重新修改"})
            else:
                return render(request, "users/login.html", {"msg": "你的账号已被锁定，请联系管理员！！"})
        else:
            return render(request, "users/editpwd.html", {"msg": "原密码错误，请重新修改"})

def address_add(request):
    if request.method == "GET":
        return render(request, "users/address_add.html", {})
    else:
        recv_name = request.POST['recv_name'].strip()
        recv_tel = request.POST['recv_tel'].strip()
        province = request.POST['province'].strip()
        city = request.POST['city'].strip()
        area = request.POST['area'].strip()
        street = request.POST['street'].strip()
        desc = request.POST['desc'].strip()
        try:
            #设置为默认地址
            request.POST['is_default'].strip()
            addresses = models.Address.objects.filter(user=request.user)
            for address in addresses:
                address.is_default = False
                address.save()
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, area=area,
                                     street=street, desc=desc, is_default=True, user=request.user)
            address.save()
        except:
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, area=area,
                                     street=street, desc=desc, user=request.user)
            address.save()
        return redirect(reverse("users:address_list"))


def address_list(request):
    addresses = models.Address.objects.filter(user=request.user)
    return render(request,"users/address_list.html",{"addresses": addresses})


def address_delete(request, a_id):
    try:
        address = models.Address.objects.get(pk=a_id)
        print(address)
        address.delete()
        return redirect(reverse("users:address_list"))
    except Exception as e:
        print(e)
        return redirect(reverse("users:address_list"))


def address_update(request, a_id):
    address = models.Address.objects.get(pk=a_id)
    if request.method == "GET":
        print(address)
        return render(request, "users/address_update.html", {"address": address})
    else:
        recv_name = request.POST['recv_name'].strip()
        recv_tel = request.POST['recv_tel'].strip()
        province = request.POST['province'].strip()
        city = request.POST['city'].strip()
        area = request.POST['area'].strip()
        street = request.POST['street'].strip()
        desc = request.POST['desc'].strip()
        try:
            #设置为默认地址
            request.POST['is_default'].strip()
            addresses = models.Address.objects.filter(user=request.user)
            for addre in addresses:
                addre.is_default = False
                addre.save()
            address.recv_name = recv_name
            address.recv_tel = recv_tel
            address.province = province
            address.city = city
            address.area = area
            address.street = street
            address.desc = desc
            address.is_default = True
            address.save()
        except:
            address.recv_name = recv_name
            address.recv_tel = recv_tel
            address.province = province
            address.city = city
            address.area = area
            address.street = street
            address.desc = desc
            address.save()
        return redirect(reverse("users:address_list"))