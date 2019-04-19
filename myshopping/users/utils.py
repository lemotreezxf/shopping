from django.shortcuts import render
import hashlib
import hmac
# from mysite import settings
from django.conf import settings
import random,string
from PIL import Image,ImageDraw,ImageFont,ImageFilter

def require_login(fn):
    '''
    判断用户是否登录的装饰器
    :param fn:
    :return:
    '''
    print("--------装饰器--------")
    def inner(request,*args,**kwargs):
        #判断用户是否登录
        loginUser = request.session.get("loginUser",None)
        if loginUser is not None:
            return fn(request,*args,**kwargs)
        else:
            #打到登录页面，请他登录
            return render(request,"blog/login.html",{"msg":"你还没有登录请重新登录！！！"})
    return inner


def hashlib_hmc(password):
    '''
    使用hmac模块完成对用户密码的加密
    :param password: 用户密码
    :return:返回一个加密后的密文
    '''
    return hmac.new(password.encode("utf-8"),settings.SALT.encode("utf-8"),"MD5").hexdigest()

def get_random_char(count=4):
 # 生成随机字符串
 # string 模块包含各种字符串，以下为小写字母加数字
     ran = string.ascii_lowercase + string.digits
     char = ''
     for i in range(count):
        char += random.choice(ran)
     return char
# 返回一个随机的 RGB 颜色
def get_random_color():
    return (random.randint(50,250),random.randint(55,150),random.randint(55,150))

def create_code():
 # 创建图片，模式，大小，背景色
     img = Image.new('RGB', (120,30), (223,240,216))
     #创建画布
     draw = ImageDraw.Draw(img)
     # 设置字体
     font = ImageFont.truetype('arial.ttf', 25)
     code = get_random_char()
     # 将生成的字符画在画布上
     for t in range(4):
        draw.text((30*t+5,0),code[t],get_random_color(),font)
     # 生成干扰点
     for _ in range(random.randint(0,50)):
     # 位置，颜色
        draw.point((random.randint(0, 120),
random.randint(0, 30)),fill=get_random_color())
 # 使用模糊滤镜使图片模糊
 #     img = img.filter(ImageFilter.BLUR)
     # 保存
     # img.save(''.join(code)+'.jpg','jpeg')
     return img,code
if __name__ == '__main__':
    print(create_code())