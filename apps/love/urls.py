# APP专用url配置
from django.urls import path
from .views import *

urlpatterns = [
    path('', loginView, name='loginlove'),  # 首页-登录
    path('show/man', showManView, name='showMan'),# 资料详情-男
    path('show/woman', showWomanView, name='showWoman'),# 资料详情-女
    path('activity', activityView, name='activity'),#活动
    path('log', logView, name='log'),  # 动态
    path('encounter', encounterView, name='encounter'),#随机邂逅
    path('matchlove', matchloveView, name='matchlove'),#寻觅-匹配
    path('me', meView, name='me'),# 知否-个人中心
    path('getinfo', getinfoView, name='getinfo'),#获取资料
    path('relation', relationView, name='relation'),  # 关系图
    path('chat', chatView, name='chat'),  # 聊天
    path('msg', msgView, name='msg'),  # 信息
    path('check', checkView, name='check'),  # 审核页
    path('lovebook', lovebookView, name='lovebook'),  # 脱单秘籍
    path('changepsd', changepsdView, name='changepsd'),  # 修改密码
    path('zflog', zflogView, name='zflog'),  # 知否运营日记

    path('img_post', img_postView, name='loveimg_post'),  # 存储头像
    path('register', register, name='loveregister'),  # 注册
    path('login', login, name='lovelogin'),  # 登录
    path('logout', logout, name='lovelogout'),  # 登出
    path('saveinfo', saveinfo, name='lovesaveinfo'),  # 保存资料
]

