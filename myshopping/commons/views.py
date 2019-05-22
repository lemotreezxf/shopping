import logging
import math
import uuid
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.shortcuts import render
from django.core.cache import cache
from . import models
from io import BytesIO
from .import utils
from goods.models import GoodsType,Goods

def index(request):
    # 第一个一级类型数据
    good_type1 = GoodsType.objects.filter(pk=10001)
    good_type1_2 = GoodsType.objects.filter(parent=good_type1)
    good1_list = Goods.objects.filter(goodsType__in=good_type1_2)
    print(good_type1)
    print(good_type1_2)
    print(good1_list)

    # 第2个一级类型数据
    good_type2 = GoodsType.objects.filter(pk=10002)
    good_type2_2 = GoodsType.objects.filter(parent=good_type2)
    good2_list = Goods.objects.filter(goodsType__in=good_type2_2)

    # 第3个一级类型数据
    good_type3 = GoodsType.objects.filter(pk=10003)
    good_type3_2 = GoodsType.objects.filter(parent=good_type3)
    good3_list = Goods.objects.filter(goodsType__in=good_type3_2)

    # 第4个一级类型数据
    good_type4 = GoodsType.objects.filter(pk=10004)
    good_type4_2 = GoodsType.objects.filter(parent=good_type4)
    good4_list = Goods.objects.filter(goodsType__in=good_type4_2)

    # 第5个一级类型数据
    good_type5 = GoodsType.objects.filter(pk=10005)
    good_type5_2 = GoodsType.objects.filter(parent=good_type5)
    good5_list = Goods.objects.filter(goodsType__in=good_type5_2)

    # 第6个一级类型数据
    good_type6 = GoodsType.objects.filter(pk=10006)
    good_type6_2 = GoodsType.objects.filter(parent=good_type6)
    good6_list = Goods.objects.filter(goodsType__in=good_type6_2)

    # 第7个一级类型数据
    good_type7 = GoodsType.objects.filter(pk=10007)
    good_type7_2 = GoodsType.objects.filter(parent=good_type7)
    good7_list = Goods.objects.filter(goodsType__in=good_type7_2)

    # 第8个一级类型数据
    good_type8 = GoodsType.objects.filter(pk=10008)
    good_type8_2 = GoodsType.objects.filter(parent=good_type8)
    good8_list = Goods.objects.filter(goodsType__in=good_type8_2)


    # 第9个一级类型数据
    good_type9 = GoodsType.objects.filter(pk=10008)
    good_type9_2 = GoodsType.objects.filter(parent=good_type9)
    good9_list = Goods.objects.filter(goodsType__in=good_type9_2)

    # 第10个一级类型数据
    good_type10 = GoodsType.objects.filter(pk=10010)
    good_type10_2 = GoodsType.objects.filter(parent=good_type10)
    good10_list = Goods.objects.filter(goodsType__in=good_type10_2)

    # 第11个一级类型数据
    good_type11 = GoodsType.objects.filter(pk=10011)
    good_type11_2 = GoodsType.objects.filter(parent=good_type11)
    good11_list = Goods.objects.filter(goodsType__in=good_type11_2)

    # 第12个一级类型数据
    good_type12 = GoodsType.objects.filter(pk=10012)
    good_type12_2 = GoodsType.objects.filter(parent=good_type12)
    good12_list = Goods.objects.filter(goodsType__in=good_type12_2)

    # 第13个一级类型数据
    good_type13 = GoodsType.objects.filter(pk=10013)
    good_type13_2 = GoodsType.objects.filter(parent=good_type13)
    good13_list = Goods.objects.filter(goodsType__in=good_type13_2)

    # 第14个一级类型数据
    good_type14 = GoodsType.objects.filter(pk=10014)
    good_type14_2 = GoodsType.objects.filter(parent=good_type14)
    good14_list = Goods.objects.filter(goodsType__in=good_type14_2)

    # 第15个一级类型数据
    good_type15 = GoodsType.objects.filter(pk=10015)
    good_type15_2 = GoodsType.objects.filter(parent=good_type15)
    good15_list = Goods.objects.filter(goodsType__in=good_type15_2)

    # 第16个一级类型数据
    good_type16 = GoodsType.objects.filter(pk=10016)
    good_type16_2 = GoodsType.objects.filter(parent=good_type16)
    good16_list = Goods.objects.filter(goodsType__in=good_type16_2)


    allGoodsType = GoodsType.objects.filter(parent__isnull=True)
    return render(request, "index.html",{"allGoodsType": allGoodsType, \
                                         "good1_list": good1_list, \
                                         "good2_list": good2_list, \
                                         "good3_list": good3_list, \
                                         "good4_list": good4_list, \
                                         "good5_list": good5_list, \
                                         "good6_list": good6_list, \
                                         "good7_list": good7_list, \
                                         "good8_list": good8_list, \
                                         "good9_list": good9_list, \
                                         "good10_list": good10_list, \
                                         "good11_list": good11_list, \
                                         "good12_list": good12_list, \
                                         "good13_list": good13_list, \
                                         "good14_list": good14_list, \
                                         "good15_list": good15_list, \
                                         "good16_list": good16_list, \
                                         })
