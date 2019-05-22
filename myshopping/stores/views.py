from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
#页面重定向
from django.shortcuts import redirect
#路由重定向
from django.shortcuts import reverse
from . import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from goods.models import GoodsType,Goods

@login_required
def add(request):
    if request.method == "GET":
        return render(request, "stores/add.html", {})
    else:
        name = request.POST['name'].strip()
        intro = request.POST['intro'].strip()
        try:
            cover = request.FILES["cover"]
            #验证
            if name == "":
                return render(request, "stores/add.html", {"msg": "店铺名称不能为空"})
            if len(intro) > 300:
                return render(request, "stores/add.html", {"msg": "店铺名称不能超过300字"})
            store = models.Store(name=name, intro=intro, cover=cover, user=request.user)
        except:
            store = models.Store(name=name, intro=intro, user=request.user)
        store.save()
        # return redirect(reverse("stores:detail"))
        #调到店铺详情页面
        return redirect(reverse("stores:detail", kwargs={"s_id": store.id}))
@require_GET
@login_required
def list(request):
    stores = models.Store.objects.filter(user=request.user, status__in=[0,1])
    print(stores)
    return render(request, "stores/list.html", {"stores": stores})

@login_required
def update(request, s_id):
    if request.method == "GET":
        store = models.Store.objects.get(id=s_id)
        return render(request, "stores/update.html", {"store": store})
    else:
        store = models.Store.objects.get(id=s_id)
        name = request.POST['name'].strip()
        intro = request.POST['intro'].strip()
        try:
            cover = request.FILES["cover"]
            #验证
            if name == "":
                return render(request, "stores/update.html", {"msg": "店铺名称不能为空"})
            if len(intro) > 300:
                return render(request, "stores/update.html", {"msg": "店铺名称不能超过300字"})
            # store(name=name, intro=intro, cover=cover, user=request.user)
            store.name = name
            store.intro = intro
            store.cover = cover
        except:
            store.name = name
            store.intro = intro
        store.save()
        # return redirect(reverse("stores:list"))
        return redirect(reverse("stores:detail", kwargs={"s_id": store.id}))

@require_GET
@login_required()
def detail(request, s_id):
    store = models.Store.objects.get(pk=s_id)
    type1 = GoodsType.objects.filter(parent__isnull=True)
    goods = Goods.objects.filter(store=store)
    return render(request, "stores/detail.html",{"store": store, "type1": type1,"goods": goods})


@require_GET
@login_required()
def change(request, s_id, status):
    store = models.Store.objects.get(id=s_id)
    store.status = int(status)
    store.save()
    if store.status == 2:
        return redirect(reverse("stores:list"))
    return render(request, "stores/detail.html", {"store": store})



