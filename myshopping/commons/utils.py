from django.shortcuts import render
import hashlib
import hmac
from django.conf import settings
import random,string
from PIL import Image,ImageDraw,ImageFont,ImageFilter


#验证码
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