from django.core.cache import cache

from .import models


def get_all_article(is_change=False):
    print("从缓存中获取数据。。。")
    articles = cache.get("all_article")
    if articles is None or is_change:
        print("redis中没有数据，从数据库中获取数据")
        articles = models.Article.objects.all()
        print("redis中没有数据，从数据库中获取数据")
        cache.set("all_article",articles)

    return articles


def get_all_user(is_change=False):
    print("从缓存中获取数据。。。")
    users = cache.get("all_user")
    if users is None or is_change:
        print("redis中没有数据，从数据库中获取数据")
        users = models.User.objects.all()
        print("redis中没有数据，从数据库中获取数据")
        cache.set("all_user",users)

    return users    
