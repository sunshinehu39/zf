from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
import base64, random, datetime
from .models import *
# 分页器
from django.core.paginator import Paginator

hobbiesstring = '读书，做饭，美食，追剧，旅游，登山，徒步，摄影，演讲，写作，英语，编程，吉他，古琴，古筝，钢琴，动漫，唱歌，跳舞，花艺，茶艺，瑜伽，游泳，网球，桌球，宠物，购物，电竞，乒乓，羽毛球'

# 视图—首页登录
def loginView(request):
    showregister = request.GET.get('showregister', False)
    passwordmsg = request.GET.get('passwordmsg', '请输入您的密码！')
    accounts = request.GET.get('accounts', '')
    registermsg = request.GET.get('registermsg', '请输入您要注册的帐号！')
    passwordfocus = request.GET.get('passwordfocus', False)
    return render(request, 'love/login.html', locals())


# 视图—脱单秘籍
def lovebookView(request):
    is_login = request.session.get('login', False)
    if is_login:
        id = request.session['id']
        gender = User.objects.get(id=id).gender
        if gender == '1':
            boyllist = Lovebook.objects.filter(suitgender=1).order_by('index')
        else:
            girllist = Lovebook.objects.filter(suitgender=2).order_by('index')

        alllist = Lovebook.objects.filter(suitgender=3)
        return render(request, 'love/lovebook.html', locals())
    else:
        return redirect('/love')


# 视图—动态
def logView(request):
    is_login = request.session.get('login', False)
    if is_login:
        action = request.GET.get('action', '')
        if action == 'pass':
            checkid = request.GET.get('checkid')
            User.objects.filter(id=checkid).update(vip=1)
            return redirect('/love/log')

        tochecklist = Info.objects.filter(U_id__vip=0).order_by("-jointime")

        oklist = Info.objects.filter(U_id__vip__gt=0).order_by("-jointime")
        return render(request, 'love/log.html', locals())
    else:
        return redirect('/love')


# 视图—修改密码
def changepsdView(request):
    # is_login = request.session.get('login', False)
    # if is_login:
    if request.method == 'POST':
        accounts = request.POST.get('accounts')
        newpassword = request.POST.get('newpassword')
        User.objects.filter(accounts=accounts).update(password=make_password(newpassword))
        msg = '修改成功！'

    return render(request, 'love/changepsd.html', locals())
    # else:
    #     return redirect('/love')


# 视图—审核页
def checkView(request):
    return render(request, 'love/check.html', locals())


# 视图—关系
def relationView(request):
    is_login = request.session.get('login', False)
    if is_login:
        id = request.session['id']
        # mygender = User.objects.get(id=id).gender
        myid = id
        # 倘若我没关系，创建关系
        if Relationship.objects.filter(U_id_id=myid).exists():
            pass
        else:
            newRelationship = Relationship(
                U_id_id=myid,
            )
            newRelationship.save()

        relation = request.GET.get("relation", 'love')
        if relation == 'love':
            keyword = '喜欢'
            Relationship.objects.filter(U_id_id=id).update(addlovedlist='')

            lovelist = Relationship.objects.get(U_id_id=id).lovelist.split("，")
            lovedlist = Relationship.objects.get(U_id_id=id).lovedlist.split("，")

            inlovelist = []
            fallinlovelist = []

            for i in lovelist:
                if i in lovedlist:
                    inlovelist.append(i)

            for i in inlovelist:
                try:
                    avatar = User.objects.get(id=i).avatar
                    nickname = Info.objects.get(U_id_id=i).nickname
                    gender = User.objects.get(id=i).gender
                    fallinlovelist.append({'id': i, 'gender': gender, 'avatar': avatar, 'nickname': nickname})
                except:
                    pass

            mylovelist = []
            for i in lovelist:
                try:
                    avatar = User.objects.get(id=i).avatar
                    nickname = Info.objects.get(U_id_id=i).nickname
                    gender = User.objects.get(id=i).gender
                    mylovelist.append({'id': i, 'gender': gender, 'avatar': avatar, 'nickname': nickname})
                except:
                    pass

            mylovedlist = []

            for i in lovedlist:
                try:
                    avatar = User.objects.get(id=i).avatar
                    nickname = Info.objects.get(U_id_id=i).nickname
                    gender = User.objects.get(id=i).gender
                    mylovedlist.append({'id': i, 'gender': gender, 'avatar': avatar, 'nickname': nickname})
                except:
                    pass

        elif relation == 'look':
            keyword = '看过'
            Relationship.objects.filter(U_id_id=id).update(addlookedlist='')

            looklist = Relationship.objects.get(U_id_id=id).looklist.split("，")
            lookedlist = Relationship.objects.get(U_id_id=id).lookedlist.split("，")

            inlooklist = []
            fallinlooklist = []

            for i in looklist:
                if i in lookedlist:
                    inlooklist.append(i)

            for i in inlooklist:
                try:
                    avatar = User.objects.get(id=i).avatar
                    nickname = Info.objects.get(U_id_id=i).nickname
                    gender = User.objects.get(id=i).gender
                    fallinlooklist.append({'id': i, 'gender': gender, 'avatar': avatar, 'nickname': nickname})
                except:
                    pass

            fallinlovelist = fallinlooklist

            mylooklist = []
            for i in looklist:
                try:
                    avatar = User.objects.get(id=i).avatar
                    nickname = Info.objects.get(U_id_id=i).nickname
                    gender = User.objects.get(id=i).gender
                    mylooklist.append({'id': i, 'gender': gender, 'avatar': avatar, 'nickname': nickname})
                except:
                    pass

            mylovelist = mylooklist

            mylookdlist = []

            for i in lookedlist:
                try:
                    avatar = User.objects.get(id=i).avatar
                    nickname = Info.objects.get(U_id_id=i).nickname
                    gender = User.objects.get(id=i).gender
                    mylookdlist.append({'id': i, 'gender': gender, 'avatar': avatar, 'nickname': nickname})
                except:
                    pass

            mylovedlist = mylookdlist

        return render(request, 'love/relation.html', locals())
    else:
        return redirect('/love')


# 视图—信箱
def msgView(request):
    is_login = request.session.get('login', False)
    if is_login:
        id = request.session['id']
        Relationship.objects.filter(U_id_id=id).update(newmsgnum=0)

        allmsglist = Chat.objects.filter(receiver_id=id).order_by('-time')

        sender_set = set()

        for i in allmsglist:
            sender_set.add(i.sender_id)

        msglist = []
        for j in sender_set:
            avatar = User.objects.get(id=j).avatar
            nickname = Info.objects.get(U_id_id=j).nickname
            last = allmsglist.filter(sender=j).order_by('-time')[0]
            lastmsg = last.content
            lasttime = last.time

            msglist.append({'id': j, 'nickname': nickname, 'avatar': avatar, 'lastmsg': lastmsg, 'lasttime': lasttime})

        def takeSecond(elem):
            return elem['lasttime']

        msglist.sort(key=takeSecond, reverse=True)

        return render(request, 'love/msg.html', locals())
    else:
        return redirect('/love')


from django.db.models import Q


# 视图—聊天
def chatView(request):
    is_login = request.session.get('login', False)
    if is_login:
        backpath2 = request.GET.get('backpath2', "/love/me")
        backpath = request.GET.get('backpath', "/love/me")
        scrollTop = request.GET.get('scrollTop', 0)
        relation = request.GET.get('relation', 'love')

        showtips = request.GET.get("showtips", False)

        yourid = int(request.GET.get("myid"))
        yourgender = User.objects.get(id=yourid).gender
        yourname = Info.objects.get(U_id_id=yourid).nickname
        youravatar = User.objects.get(id=yourid).avatar

        myid = request.session['id']
        mygender = User.objects.get(id=myid).gender
        # myname = Info.objects.get(U_id_id=myid).nickname
        myavatar = User.objects.get(id=myid).avatar
        myinfopsd = User.objects.get(id=myid).infopassword

        if yourid:
            if request.method == 'POST':
                content = request.POST.get('msg')
                newmsg = Chat(
                    sender_id=myid,
                    receiver_id=yourid,
                    content=content,
                )
                newmsg.save()

                oldnum = Relationship.objects.get(U_id_id=yourid).newmsgnum
                Relationship.objects.filter(U_id_id=yourid).update(newmsgnum=oldnum + 1)

                return redirect('/love/chat?myid=' + str(yourid) + "&backpath=" + backpath)

        msgtotallist = Chat.objects.filter(
            Q(sender_id=myid, receiver_id=yourid) | Q(sender_id=yourid, receiver_id=myid)).order_by('time')

        paginator = Paginator(msgtotallist, 5, 3)  # 每页5条数据
        page = request.GET.get('page', paginator.num_pages)
        msglist = paginator.page(page)  # 根据索引page，返回该page数据，如果不存在，引起 InvalidPage异常

        return render(request, 'love/chat.html', locals())
    else:
        return redirect('/love')


# 视图—获取资料
def getinfoView(request):
    try:
        id = request.session['id']
        photopath = User.objects.get(id=id).avatar
        gender = User.objects.get(id=id).gender

        action = request.GET.get('action', '')

        birthyear = 1989
        constellation = '白羊座'
        education = '本科'
        hometown = "四川成都"

        lovenum = 2
        agemin = 26
        agemax = 30
        lovenummin = 0
        lovenummax = 3
        heightmin = 1.5
        heightmax = 1.75
        yourstature = '标准'
        salarymin = 0
        youreducation = '不限'
        marrymax = 3

        # 测试数据
        # nickname = '知否'
        # phone = 13908056224
        # wechat = 13908056224
        # job = '销售'
        # salary = 8
        # truename = '知否'
        # height = 1.6
        # weight = 55

        if action == 'update':

            # 倘若我没关系，创建关系
            if Info.objects.filter(U_id_id=id).exists():
                info = Info.objects.get(U_id_id=id)
                truename = info.truename
                birthyear = info.birthyear
                nickname = info.nickname
                constellation = info.constellation
                education = info.education

                if education == 0:
                    education = '其他'
                elif education == 1:
                    education = '专科'
                elif education == 2:
                    education = '本科'
                elif education == 3:
                    education = '硕士'
                else:
                    education = '博士'

                hometown = info.hometown
                height = info.height
                weight = info.weight
                job = info.job
                salary = info.salary
                house = info.house
                car = info.car
                smoke = info.smoke
                beer = info.beer

                hobbies = info.hobbies
                hobbieslist = hobbies.split("，")
                hobbiesother = ''
                for i in hobbieslist:
                    if i not in hobbiesstring:
                        hobbiesother = hobbiesother + i

                if '读书' in hobbies: h1 = 1
                if '做饭' in hobbies: h2 = 1
                if '美食' in hobbies: h3 = 1
                if '追剧' in hobbies: h4 = 1
                if '旅游' in hobbies: h5 = 1
                if '登山' in hobbies: h6 = 1
                if '徒步' in hobbies: h7 = 1
                if '摄影' in hobbies: h8 = 1
                if '演讲' in hobbies: h9 = 1
                if '写作' in hobbies: h10 = 1
                if '英语' in hobbies: h11 = 1
                if '编程' in hobbies: h12 = 1
                if '吉他' in hobbies: h13 = 1
                if '古琴' in hobbies: h14 = 1
                if '古筝' in hobbies: h15 = 1
                if '钢琴' in hobbies: h16 = 1
                if '动漫' in hobbies: h17 = 1
                if '唱歌' in hobbies: h18 = 1
                if '跳舞' in hobbies: h19 = 1
                if '花艺' in hobbies: h20 = 1
                if '茶艺' in hobbies: h21 = 1
                if '瑜伽' in hobbies: h22 = 1
                if '游泳' in hobbies: h23 = 1
                if '网球' in hobbies: h24 = 1
                if '桌球' in hobbies: h25 = 1
                if '宠物' in hobbies: h26 = 1
                if '购物' in hobbies: h27 = 1
                if '电竞' in hobbies: h28 = 1
                if '乒乓' in hobbies: h29 = 1
                if '羽球' in hobbies: h30 = 1

                soliloquy = info.soliloquy
                lovenum = info.lovenum
                thinklove = info.thinklove

                agemin = info.agemin
                agemax = info.agemax
                lovenummin = info.lovenummin
                lovenummax = info.lovenummax
                heightmin = info.heightmin
                heightmax = info.heightmax
                yourstature = info.yourstature
                salarymin = info.salarymin
                ifhouse = info.ifhouse
                ifcar = info.ifcar
                ifsmoke = info.ifsmoke
                ifbeer = info.ifbeer
                youreducation = info.youreducation

                if youreducation == 0:
                    youreducation = '不限'
                elif youreducation == 1:
                    youreducation = '专科'
                elif youreducation == 2:
                    youreducation = '本科'
                elif youreducation == 3:
                    youreducation = '硕士'
                else:
                    youreducation = '博士'

                yourhometown = info.yourhometown

                yourhobbies = info.yourhobbies

                yourhobbieslist = yourhobbies.split("，")
                yourhobbiesother = ''
                for i in yourhobbieslist:
                    if i not in hobbiesstring:
                        yourhobbiesother = yourhobbiesother + i

                if '读书' in yourhobbies: yh1 = 1
                if '做饭' in yourhobbies: yh2 = 1
                if '美食' in yourhobbies: yh3 = 1
                if '追剧' in yourhobbies: yh4 = 1
                if '旅游' in yourhobbies: yh5 = 1
                if '登山' in yourhobbies: yh6 = 1
                if '徒步' in yourhobbies: yh7 = 1
                if '摄影' in yourhobbies: yh8 = 1
                if '演讲' in yourhobbies: yh9 = 1
                if '写作' in yourhobbies: yh10 = 1
                if '英语' in yourhobbies: yh11 = 1
                if '编程' in yourhobbies: yh12 = 1
                if '吉他' in yourhobbies: yh13 = 1
                if '古琴' in yourhobbies: yh14 = 1
                if '古筝' in yourhobbies: yh15 = 1
                if '钢琴' in yourhobbies: yh16 = 1
                if '动漫' in yourhobbies: yh17 = 1
                if '唱歌' in yourhobbies: yh18 = 1
                if '跳舞' in yourhobbies: yh19 = 1
                if '花艺' in yourhobbies: yh20 = 1
                if '茶艺' in yourhobbies: yh21 = 1
                if '瑜伽' in yourhobbies: yh22 = 1
                if '游泳' in yourhobbies: yh23 = 1
                if '网球' in yourhobbies: yh24 = 1
                if '桌球' in yourhobbies: yh25 = 1
                if '宠物' in yourhobbies: yh26 = 1
                if '购物' in yourhobbies: yh27 = 1
                if '电竞' in yourhobbies: yh28 = 1
                if '乒乓' in yourhobbies: yh29 = 1
                if '羽球' in yourhobbies: yh30 = 1

                more = info.more
                marrymax = info.marrymax
                loveslogan = info.loveslogan
                phone = info.phone
                wechat = info.wechat

                tags = info.tags

                tagsstr = '聪明好学，成熟稳重，风趣幽默，豪放不羁，淡泊名利，热心助人，责任感强，喜欢挑战，不拘小节，温柔体贴，活泼可爱，聪明伶俐，善解人意，心地善良，有同理心，自信优雅，性感迷人，内向文静'
                tagslist = tags.split("，")
                tagsother = ''
                for i in tagslist:
                    if i not in tagsstr:
                        tagsother = tagsother + i + "，"

                if '聪明好学' in tags: t1 = 1
                if '成熟稳重' in tags: t2 = 1
                if '风趣幽默' in tags: t3 = 1
                if '豪放不羁' in tags: t4 = 1
                if '淡泊名利' in tags: t5 = 1
                if '热心助人' in tags: t6 = 1
                if '责任感强' in tags: t7 = 1
                if '喜欢挑战' in tags: t8 = 1
                if '不拘小节' in tags: t9 = 1
                if '温柔体贴' in tags: t10 = 1
                if '活泼可爱' in tags: t11 = 1
                if '聪明伶俐' in tags: t12 = 1
                if '善解人意' in tags: t13 = 1
                if '心地善良' in tags: t14 = 1
                if '有同理心' in tags: t15 = 1
                if '自信优雅' in tags: t16 = 1
                if '性感迷人' in tags: t17 = 1
                if '内向文静' in tags: t18 = 1

            else:
                return redirect('/love/getinfo')

        return render(request, 'love/getinfo.html', locals())
    except:
        return redirect('/love')


# 视图—男士资料详情
def showManView(request):
    is_login = request.session.get('login', False)
    if is_login:
        action = request.GET.get('action', "")

        backpath = request.GET.get('backpath', "/love/me")
        scrollTop = request.GET.get('scrollTop', 0)
        relation = request.GET.get('relation', 'love')

        userid = request.session['id']
        id = int(request.GET.get("myid", userid))
        yourid = str(id) + '，'

        matchdegree = ifmatch(userid,id)

        if User.objects.get(id=userid).vip == 6:
            showmore = True

        # 第一次看，添加到看过列表
        look(userid, id)
        # 获取是否喜欢
        mylovelist = Relationship.objects.get(U_id_id=userid).lovelist
        if yourid in mylovelist:
            love = True
        else:
            love = False

        if action:
            # 更新喜欢状态
            if action == 'changelove':
                if love:
                    notlove(userid, id)
                    love = False
                else:
                    fallinlove(userid, id)
                    love = True
                return redirect('/love/show/man?myid=' + str(id) + '&backpath=' + backpath + '&scrollTop=' + str(
                    scrollTop) + '&relation=' + relation)

        if request.method == 'POST':
            infopassword = request.POST.get('infopassword')
            if infopassword == User.objects.get(id=id).infopassword:
                showmore = True
                tobottom = True
            else:
                showtips = True
                return redirect('/love/chat?myid=' + str(
                    id) + '&backpath2=/love/show/man&backpath=' + backpath + '&scrollTop=' + scrollTop + '&relation=' + relation + "&showtips=" + str(
                    showtips))

        if Info.objects.filter(U_id_id=id).exists():

            info = Info.objects.get(U_id_id=id)
            photopath = User.objects.get(id=id).avatar

            tags = info.tags.split('，')

            hobbies = info.hobbies
            hobbieslist = hobbies.split("，")
            hobbiesother = ''
            imghobbieslist = []
            for i in hobbieslist:
                if i:
                    if i not in hobbiesstring:
                        hobbiesother = hobbiesother + i
                    else:
                        imghobbieslist.append(i)

            age = datetime.datetime.now().year - info.birthyear

            education = NSeducation(info.education,'me')
            youreducation = NSeducation(info.education,'you')

            yourhobbies = info.yourhobbies.replace("，", ' ')

            ifhouse = info.ifhouse
            ifcar = info.ifcar
            ifsmoke = info.ifsmoke
            ifbeer = info.ifbeer

            if ifhouse:
                if ifcar:
                    yourproperty = '有车有房'
                else:
                    yourproperty = '有房'
            else:
                if ifcar:
                    yourproperty = '有车'
                else:
                    yourproperty = ''

            if ifsmoke:
                if ifbeer:
                    yourhabit = '抽烟喝酒'
                else:
                    yourhabit = '抽烟无酒'
            else:
                if ifbeer:
                    yourhabit = '无烟喝酒'
                else:
                    yourhabit = '无烟无酒'

            return render(request, 'love/showMan.html', locals())
        else:
            return redirect('/love')
    else:
        return redirect('/love')


# 视图—女士资料详情
def showWomanView(request):
    is_login = request.session.get('login', False)
    if is_login:
        action = request.GET.get('action', "")

        backpath = request.GET.get('backpath', "/love/me")
        scrollTop = request.GET.get('scrollTop', 0)
        relation = request.GET.get('relation', 'love')

        userid = request.session['id']
        id = int(request.GET.get("myid", userid))
        yourid = str(id) + '，'

        matchdegree = ifmatch(userid,id)

        if User.objects.get(id=userid).vip == 6:
            showmore = True

        # 第一次看，添加到看过列表
        look(userid, id)

        # 获取是否喜欢
        mylovelist = Relationship.objects.get(U_id_id=userid).lovelist
        if yourid in mylovelist:
            love = True
        else:
            love = False

        if action:
            # 更新喜欢状态
            if action == 'changelove':
                if love:
                    notlove(userid, id)
                    love = False
                else:
                    fallinlove(userid, id)
                    love = True
                return redirect('/love/show/woman?myid=' + str(
                    id) + '&backpath=' + backpath + '&scrollTop=' + scrollTop + '&relation=' + relation)

        if request.method == 'POST':
            infopassword = request.POST.get('infopassword')
            if infopassword == User.objects.get(id=id).infopassword:
                showmore = True
                tobottom = True
            else:
                showtips = True
                return redirect('/love/chat?myid=' + str(
                    id) + '&backpath2=/love/show/woman&backpath=' + backpath + '&scrollTop=' + scrollTop + '&relation=' + relation + "&showtips=" + str(
                    showtips))

        if Info.objects.filter(U_id_id=id).exists():

            info = Info.objects.get(U_id_id=id)
            photopath = User.objects.get(id=id).avatar

            education = NSeducation(info.education,'me')
            youreducation = NSeducation(info.education,'you')

            tags = info.tags.split('，')

            hobbies = info.hobbies
            hobbieslist = hobbies.split("，")
            hobbiesother = ''
            imghobbieslist = []
            for i in hobbieslist:
                if i:
                    if i not in hobbiesstring:
                        hobbiesother = hobbiesother + i
                    else:
                        imghobbieslist.append(i)

            age = datetime.datetime.now().year - info.birthyear

            yourhobbies = info.yourhobbies.replace("，", ' ')

            ifhouse = info.ifhouse
            ifcar = info.ifcar
            ifsmoke = info.ifsmoke
            ifbeer = info.ifbeer

            if ifhouse:
                if ifcar:
                    yourproperty = '有车有房'
                else:
                    yourproperty = '有房'
            else:
                if ifcar:
                    yourproperty = '有车'
                else:
                    yourproperty = ''

            if ifsmoke:
                if ifbeer:
                    yourhabit = '抽烟喝酒'
                else:
                    yourhabit = '抽烟无酒'
            else:
                if ifbeer:
                    yourhabit = '无烟喝酒'
                else:
                    yourhabit = '无烟无酒'

            return render(request, 'love/showWoman.html', locals())
        else:
            return redirect('/love')
    else:
        return redirect('/love')

def NSeducation(enum,who):
    if enum == 0:
        if who == 'me':
            education = '其他'
        else:
            education = '不限'
    elif enum == 1:
        education = '专科'
    elif enum == 2:
        education = '本科'
    elif enum == 3:
        education = '硕士'
    else:
        education = '博士'
    return education

def SNeducation(estr,who):
    if who == 'me':
        checkstr = '其他'
    else:
        checkstr = '不限'

    if estr == checkstr:
        education = 0
    elif estr ==  '专科':
        education = 1
    elif estr == '本科':
        education =2
    elif estr == '硕士':
        education = 3
    else:
        education = 4
    return education

# 视图—寻觅(匹配)
def matchloveView(request):
    is_login = request.session.get('login', False)
    if is_login:
        # try:
        myid = request.session['id']
        # except Exception as e:
        #     request.session.flush
        #     return redirect('/love/matchlove')

        scrollTop = request.GET.get('scrollTop', 0)

        vip = User.objects.get(id=myid).vip

        if User.objects.get(id=myid).vip == 0:
            request.session['login'] = False
            return redirect('/love/check')
        mygender = User.objects.get(id=myid).gender
        info = Info.objects.get(U_id_id=myid)

        agemin = info.agemin
        agemax = info.agemax
        heightmin = info.heightmin
        heightmax = info.heightmax
        yourstature = info.yourstature
        youreducation = info.youreducation
        youreducationstr = NSeducation(youreducation,'you')

        ifhouse = info.ifhouse
        ifcar = info.ifcar
        ifsmoke = info.ifsmoke
        ifbeer = info.ifbeer

        if request.method == 'POST':
            agemin = int(request.POST.get("agemin"))
            agemax = int(request.POST.get("agemax"))
            heightmin = float(request.POST.get("heightmin"))
            heightmax = float(request.POST.get("heightmax"))
            yourstature = request.POST.get("yourstature")
            youreducation = request.POST.get("youreducation")
            youreducationstr = youreducation
            youreducation = SNeducation(youreducation,'you')

            ifhouse = int(request.POST.get("ifhouse", 0))
            ifcar = int(request.POST.get("ifcar", 0))
            ifsmoke = int(request.POST.get("ifsmoke", 0))
            ifbeer = int(request.POST.get("ifbeer", 0))

        if ifhouse:
            if ifcar:
                yourproperty = '有车有房'
            else:
                yourproperty = '有房无车'
        else:
            if ifcar:
                yourproperty = '无房有车'
            else:
                yourproperty = '无房无车'

        if ifsmoke:
            if ifbeer:
                yourhabit = '抽烟喝酒'
            else:
                yourhabit = '抽烟无酒'
        else:
            if ifbeer:
                yourhabit = '无烟喝酒'
            else:
                yourhabit = '无烟无酒'

        todayyear = datetime.datetime.now().year
        yearmin = todayyear - agemax
        yearmax = todayyear - agemin

        if mygender == '1':
            yourgender = '2'
        else:
            yourgender = '1'


        list = Info.objects.filter(gender=yourgender, birthyear__gte=yearmin, birthyear__lte=yearmax,
                                   height__gte=heightmin, height__lte=heightmax, stature=yourstature, youreducation__gte= youreducation,
                                   house=ifhouse, car=ifcar, smoke=ifsmoke, beer=ifbeer, U_id__vip__gt=0).order_by(
            '-jointime')

    return render(request, 'love/match.html', locals())


# 视图—活动
def activityView(request):
    return render(request, 'love/activity.html', locals())


# 视图—知否运营贡献
def zflogView(request):
    return render(request, 'love/zflog.html', locals())


# 视图—邂逅
def encounterView(request):
    is_login = request.session.get('login', False)
    if is_login:
        myid = request.session['id']

        vip = User.objects.get(id=myid).vip
        if User.objects.get(id=myid).vip == 0:
            request.session['login'] = False
            return redirect('/love/check')
        action = request.GET.get('action', '')

        if Relationship.objects.filter(U_id_id=myid).exists():
            pass
        else:
            newRelationship = Relationship(
                U_id_id=myid,
            )
            newRelationship.save()

        if action:
            lastid = request.GET.get('lastid', '')

            if action == 'notlove':
                notlove(myid, lastid)
            elif action == 'love':
                fallinlove(myid, lastid)

            return redirect('/love/encounter')

        mygender = User.objects.get(id=myid).gender
        if mygender == '1':
            yourgender = '2'
        else:
            yourgender = '1'

        myRelationship = Relationship.objects.get(U_id_id=myid)
        mylovelist = myRelationship.lovelist.split('，')
        mynotlovelist = myRelationship.notlovelist.split('，')
        encounterlist = []
        allyou = Info.objects.filter(gender=yourgender, U_id__vip__gt=0)

        for i in allyou:
            if str(i.U_id_id) not in mylovelist:
                if str(i.U_id_id) not in mynotlovelist:
                    encounterlist.append(str(i.U_id_id))

        if encounterlist:
            import random
            yourid = int(request.GET.get("myid", random.choice(encounterlist)))
            yourphotopath = User.objects.get(id=yourid).avatar
        else:
            nobody = True

    return render(request, 'love/encounter.html', locals())


# 函数模块—我看你的资料了
def look(myid, yourid):
    checkmyid = str(myid) + "，"
    checkyourid = str(yourid) + "，"

    # 倘若我没关系，创建关系
    if Relationship.objects.filter(U_id_id=myid).exists():
        pass
    else:
        newRelationship = Relationship(
            U_id_id=myid,
        )
        newRelationship.save()

    # 倘若你没关系，创建关系
    if Relationship.objects.filter(U_id_id=yourid).exists():
        pass
    else:
        newRelationship = Relationship(
            U_id_id=yourid,
        )
        newRelationship.save()

    myRelationship = Relationship.objects.get(U_id_id=myid)
    yourRelationship = Relationship.objects.get(U_id_id=yourid)

    # 将yourid添加到mylooklist里,
    mylooklist = myRelationship.looklist
    if checkyourid not in mylooklist:
        newmylooklist = mylooklist + checkyourid
        Relationship.objects.filter(U_id_id=myid).update(looklist=newmylooklist)

    # 将myid添加到yourlookedlist里
    yourlookedlist = yourRelationship.lookedlist
    if checkmyid not in yourlookedlist:
        newyourlookedlist = yourlookedlist + checkmyid
        Relationship.objects.filter(U_id_id=yourid).update(lookedlist=newyourlookedlist)

    # 将myid添加到你的addlookedlist里
    youraddlookedlist = yourRelationship.addlookedlist
    if checkmyid not in youraddlookedlist:
        newyouraddlookedlist = youraddlookedlist + checkmyid
        Relationship.objects.filter(U_id_id=yourid).update(addlookedlist=newyouraddlookedlist)


# 函数模块—我喜欢你
def fallinlove(myid, yourid):
    checkmyid = str(myid) + "，"
    checkyourid = str(yourid) + "，"

    # 倘若我没关系，创建关系
    if Relationship.objects.filter(U_id_id=myid).exists():
        pass
    else:
        newRelationship = Relationship(
            U_id_id=myid,
        )
        newRelationship.save()

    # 倘若你没关系，创建关系
    if Relationship.objects.filter(U_id_id=yourid).exists():
        pass
    else:
        newRelationship = Relationship(
            U_id_id=yourid,
        )
        newRelationship.save()

    myRelationship = Relationship.objects.get(U_id_id=myid)
    yourRelationship = Relationship.objects.get(U_id_id=yourid)

    # 将yourid添加到mylovelist里,
    mylovelist = myRelationship.lovelist
    if checkyourid not in mylovelist:
        newmylovelist = mylovelist + checkyourid
        Relationship.objects.filter(U_id_id=myid).update(lovelist=newmylovelist)

    # 将yourid从mynotlovelist里移除
    mynotlovelist = myRelationship.notlovelist
    if checkyourid in mynotlovelist:
        newmynotlovelist = mynotlovelist.replace(checkyourid, '')
        Relationship.objects.filter(U_id_id=myid).update(notlovelist=newmynotlovelist)

    # 将myid添加到yourlovedlist里
    yourlovedlist = yourRelationship.lovedlist
    if checkmyid not in yourlovedlist:
        newyourlovedlist = yourlovedlist + checkmyid
        Relationship.objects.filter(U_id_id=yourid).update(lovedlist=newyourlovedlist)

    # 将myid添加到你的addlovedlist里
    youraddlovedlist = yourRelationship.addlovedlist
    if checkmyid not in youraddlovedlist:
        newyouraddlovedlist = youraddlovedlist + checkmyid
        Relationship.objects.filter(U_id_id=yourid).update(addlovedlist=newyouraddlovedlist)

# 函数模块—我不喜欢你
def ifmatch(myid, yourid):
    matchdegree = 0
    myage = datetime.datetime.now().year - Info.objects.get(U_id_id=myid).birthyear
    myheight = Info.objects.get(U_id_id=myid).height
    myeducation = Info.objects.get(U_id_id=myid).education
    mysalary = Info.objects.get(U_id_id=myid).salary
    myhouse = Info.objects.get(U_id_id=myid).house

    agemin = Info.objects.get(U_id_id=yourid).agemin
    agemax =Info.objects.get(U_id_id=yourid).agemax
    heightmin = Info.objects.get(U_id_id=yourid).heightmin
    heightmax =Info.objects.get(U_id_id=yourid).heightmax
    educationmin =Info.objects.get(U_id_id=yourid).youreducation
    salarymin = Info.objects.get(U_id_id=yourid).salarymin
    ifhouse = Info.objects.get(U_id_id=yourid).ifhouse

    if myage >= agemin and myage <= agemax : matchdegree += 20
    if myheight >= heightmin and myheight <= heightmax :matchdegree += 20
    if myeducation >= educationmin :matchdegree += 20
    if mysalary >= salarymin :matchdegree += 20
    if myhouse >= ifhouse :matchdegree += 20

    return matchdegree

# 函数模块—我不喜欢你
def notlove(myid, yourid):
    checkmyid = str(myid) + "，"
    checkyourid = str(yourid) + "，"

    # 倘若我没关系，创建关系
    if Relationship.objects.filter(U_id_id=myid).exists():
        pass
    else:
        newRelationship = Relationship(
            U_id_id=myid,
        )
        newRelationship.save()

    # 倘若你没关系，创建关系
    if Relationship.objects.filter(U_id_id=yourid).exists():
        pass
    else:
        newRelationship = Relationship(
            U_id_id=yourid,
        )
        newRelationship.save()

    myRelationship = Relationship.objects.get(U_id_id=myid)
    yourRelationship = Relationship.objects.get(U_id_id=yourid)

    # 将yourid添加到mynotlovelist里,
    mynotlovelist = myRelationship.notlovelist
    if checkyourid not in mynotlovelist:
        newmynotlovelist = mynotlovelist + checkyourid
        Relationship.objects.filter(U_id_id=myid).update(notlovelist=newmynotlovelist)

    # 将yourid从mylovelist里移除
    mylovelist = myRelationship.lovelist
    if checkyourid in mylovelist:
        newmylovelist = mylovelist.replace(checkyourid, '')
        Relationship.objects.filter(U_id_id=myid).update(lovelist=newmylovelist)

    # 将myid从yourlovedlist里移除
    yourlovedlist = yourRelationship.lovedlist
    if checkmyid in yourlovedlist:
        newyourlovedlist = yourlovedlist.replace(checkmyid, '')
        Relationship.objects.filter(U_id_id=yourid).update(lovedlist=newyourlovedlist)

    # 将myid从你的addlovedlist里移除
    youraddlovedlist = yourRelationship.addlovedlist
    if checkmyid in youraddlovedlist:
        newyouraddlovedlist = youraddlovedlist.replace(checkmyid, '')
        Relationship.objects.filter(U_id_id=yourid).update(addlovedlist=newyouraddlovedlist)


# 视图—知否（个人中心）
def meView(request):
    is_login = request.session.get('login', False)
    if is_login:
        id = request.session['id']
        vip = User.objects.get(id=id).vip
        if User.objects.get(id=id).vip == 0:
            request.session['login'] = False
            return redirect('/love/check')

        if request.method == 'POST':
            action = request.GET.get('action', '')
            if action == 'changepassword':
                newpassword = request.POST.get('newpassword')
                User.objects.filter(id=id).update(password=make_password(newpassword))
                return redirect('/love/me')
            elif action == 'setpassword':
                infopassword = request.POST.get('infopassword')
                User.objects.filter(id=id).update(infopassword=infopassword)
                return redirect('/love/me')

        photopath = User.objects.get(id=id).avatar
        gender = User.objects.get(id=id).gender
        name = Info.objects.get(U_id_id=id).truename

        try:
            # 倘若我没关系，创建关系
            if Relationship.objects.filter(U_id_id=id).exists():
                pass
            else:
                newRelationship = Relationship(
                    U_id_id=id,
                )
                newRelationship.save()

            myRelationship = Relationship.objects.get(U_id_id=id)
            looknum = myRelationship.looklist.count('，')
            lookednum = myRelationship.lookedlist.count('，')
            lovenum = myRelationship.lovelist.count('，')
            lovednum = myRelationship.lovedlist.count('，')
            addlookednum = myRelationship.addlookedlist.count('，')
            addlovednum = myRelationship.addlovedlist.count('，')
            msgnum = Chat.objects.filter(receiver_id=id).count()
            newmsgnum = myRelationship.newmsgnum

            referrer = User.objects.get(id=id).referrer
            if User.objects.filter(id=referrer).exists():
                if User.objects.get(id=referrer).vip > 0:
                    zfnum = User.objects.filter(referrer=id, vip__gt=0).count() + 1
            else:
                zfnum = User.objects.filter(referrer=id, vip__gt=0).count()

            newzfnum = User.objects.get(id=id).newzfnum

        except:
            looknum = 0
            lookednum = 0
            lovenum = 0
            lovednum = 0
            addlookednum = 0
            addlovednum = 0
            addletternum = 0
            msgnum = 0
            newmsgnum = 0
            newzfnum = 0

        return render(request, 'love/me.html', locals())
    else:
        return redirect('/love')


# 功能—登录
def login(request):
    if request.method == 'POST':
        accounts = request.POST.get('accounts')
        password = request.POST.get('password')
        try:
            turepassword = User.objects.get(accounts=accounts).password
            if check_password(password, turepassword):
                request.session['id'] = User.objects.get(accounts=accounts).id
                id = request.session['id']
                vip = User.objects.get(id=id).vip
                request.session['vip'] = vip

                if Info.objects.filter(U_id_id=id).exists():
                    if vip > 0:
                        request.session['login'] = True
                        return redirect('/love/me')
                    else:
                        return redirect('/love/check')
                else:
                    return redirect('/love/getinfo')
            else:
                passwordmsg = '密码错误，请重新输入！'
        except:
            passwordmsg = '此帐号尚未注册，请先注册！'

        return redirect('/love?passwordmsg=' + passwordmsg + '&accounts=' + accounts + '&passwordfocus=true')
    else:
        return redirect('/love')


# 功能—登出
def logout(request):
    request.session.flush()
    return redirect('/love')


# 功能—注册
def register(request):
    if request.method == 'POST':
        accounts = request.POST.get('registeraccounts')
        if User.objects.filter(accounts=accounts).exists():
            registermsg = '此帐号已注册，请换个帐号或直接登录！'
            return redirect('/love?registermsg=' + registermsg + "&showregister=true")
        else:
            password = request.POST.get('registerpassword')
            gender = request.POST.get('sex')
            referrer = request.POST.get('referrer', 0)
            if referrer == '':
                referrer = 0
            infopassword = random.randint(1000, 6666)

            newuser = User(
                accounts=accounts,
                password=make_password(password),
                gender=gender,
                referrer=referrer,
                infopassword=infopassword,
            )
            newuser.save()

            # 登录成功，用session保持存储状态，并保存id
            request.session['id'] = User.objects.get(accounts=accounts).id
            id = request.session['id']
            request.session['vip'] = User.objects.get(id=id).vip

            return redirect('/love/getinfo')
    else:
        return redirect('/love')


# 功能—保存资料
def saveinfo(request):
    id = request.session['id']
    if request.method == 'POST':
        U_id = request.session['id']
        gender = User.objects.get(id=U_id).gender
        truename = request.POST.get('truename')
        birthyear = request.POST.get('birthyear')
        nickname = request.POST.get('nickname')
        constellation = request.POST.get('constellation')
        education = request.POST.get('education')

        if education == '其他':
            education = 0
        elif education == '专科':
            education = 1
        elif education == '本科':
            education = 2
        elif education == '硕士':
            education = 3
        else:
            education = 4

        hometown = request.POST.get('hometown')
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))

        # 体质指数BMI = 体重（公斤） ÷ 身高（米）的平方 kg / m ^ 2
        # 中国体质标准为女性18 - 22，男性20 - 24
        BMI = weight / height ** 2
        if gender == 1:
            if BMI <= 18:
                stature = '骨感'
            elif BMI > 18 and BMI <= 20:
                stature = '苗条'
            elif BMI > 20 and BMI <= 24:
                stature = '标准'
            elif BMI > 24 and BMI <= 35:
                stature = '微胖'
            else:
                stature = '丰满'
        else:
            if BMI <= 16:
                stature = '骨感'
            elif BMI > 16 and BMI <= 19:
                stature = '苗条'
            elif BMI > 19 and BMI <= 22:
                stature = '标准'
            elif BMI > 22 and BMI <= 30:
                stature = '微胖'
            else:
                stature = '丰满'

        job = request.POST.get('job')
        salary = float(request.POST.get('salary'))

        house = request.POST.get('house', False)
        car = request.POST.get('car', False)
        smoke = request.POST.get('smoke', False)
        beer = request.POST.get('beer', False)
        if house == '1': house = True
        if car == '1': car = True
        if smoke == '1': smoke = True
        if beer == '1': beer = True

        hobbies = request.POST.getlist("hobbies")
        hobbiesother = request.POST.get("hobbiesother")
        hobbies = "，".join(hobbies) + '，' + hobbiesother

        tags = request.POST.getlist("tags")
        tagsother = request.POST.get("tagsother")
        tags = "，".join(tags) + '，' + tagsother

        soliloquy = request.POST.get('soliloquy')
        lovenum = int(request.POST.get('lovenum'))
        thinklove = request.POST.get('thinklove')

        agemin = int(request.POST.get('agemin'))
        agemax = int(request.POST.get('agemax'))
        lovenummin = int(request.POST.get('lovenummin'))
        lovenummax = int(request.POST.get('lovenummax'))
        heightmin = float(request.POST.get('heightmin'))
        heightmax = float(request.POST.get('heightmax'))
        yourstature = request.POST.get('yourstature')
        salarymin = float(request.POST.get('salarymin', 0))

        ifhouse = request.POST.get('ifhouse', False)
        ifcar = request.POST.get('ifcar', False)
        ifsmoke = request.POST.get('ifsmoke', False)
        ifbeer = request.POST.get('ifbeer', False)
        if ifhouse == '1': ifhouse = True
        if ifcar == '1': ifcar = True
        if ifsmoke == '1': ifsmoke = True
        if ifbeer == '1': ifbeer = True

        youreducation = request.POST.get('youreducation')

        if youreducation == '不限':
            youreducation = 0
        elif youreducation == '专科':
            youreducation = 1
        elif youreducation == '本科':
            youreducation = 2
        elif youreducation == '硕士':
            youreducation = 3
        else:
            youreducation = 4

        yourhometown = request.POST.get('yourhometown')

        yourhobbies = request.POST.getlist('yourhobbies')
        yourhobbiesother = request.POST.get("hobbiesother")
        yourhobbies = "，".join(yourhobbies) + '，' + yourhobbiesother

        more = request.POST.get('more')

        loveslogan = request.POST.get('loveslogan')

        marrymax = int(request.POST.get('marrymax'))

        phone = request.POST.get('phone')
        wechat = request.POST.get('wechat')

        if Info.objects.filter(U_id_id=U_id).exists():
            Info.objects.filter(U_id_id=U_id).update(
                truename=truename,
                birthyear=birthyear,
                nickname=nickname,
                constellation=constellation,
                education=education,
                hometown=hometown,
                height=height,
                weight=weight,
                stature=stature,
                job=job,
                salary=salary,
                house=house,
                car=car,
                smoke=smoke,
                beer=beer,
                hobbies=hobbies,
                soliloquy=soliloquy,
                lovenum=lovenum,
                thinklove=thinklove,

                agemin=agemin,
                agemax=agemax,
                lovenummin=lovenummin,
                lovenummax=lovenummax,
                heightmin=heightmin,
                heightmax=heightmax,
                yourstature=yourstature,
                salarymin=salarymin,
                ifhouse=ifhouse,
                ifcar=ifcar,
                ifsmoke=ifsmoke,
                ifbeer=ifbeer,
                youreducation=youreducation,
                yourhometown=yourhometown,
                yourhobbies=yourhobbies,
                more=more,
                marrymax=marrymax,
                loveslogan=loveslogan,
                tags=tags,
                phone=phone,
                wechat=wechat,
            )
            if User.objects.get(id=id).vip == 0:
                return redirect('/love/check')
            else:
                return redirect('/love/me')
        else:
            newinfo = Info(
                U_id_id=U_id,
                gender=gender,
                truename=truename,
                birthyear=birthyear,
                nickname=nickname,
                constellation=constellation,
                education=education,
                hometown=hometown,
                height=height,
                weight=weight,
                stature=stature,
                job=job,
                salary=salary,
                house=house,
                car=car,
                smoke=smoke,
                beer=beer,
                hobbies=hobbies,
                soliloquy=soliloquy,
                lovenum=lovenum,
                thinklove=thinklove,

                agemin=agemin,
                agemax=agemax,
                lovenummin=lovenummin,
                lovenummax=lovenummax,
                heightmin=heightmin,
                heightmax=heightmax,
                yourstature=yourstature,
                salarymin=salarymin,
                ifhouse=ifhouse,
                ifcar=ifcar,
                ifsmoke=ifsmoke,
                ifbeer=ifbeer,
                youreducation=youreducation,
                yourhometown=yourhometown,
                yourhobbies=yourhobbies,
                more=more,
                marrymax=marrymax,
                loveslogan=loveslogan,
                tags=tags,
                phone=phone,
                wechat=wechat,
            )
            newinfo.save()

            return redirect('/love/check')

    else:
        return redirect('/love')

# 功能-裁剪保存头像，并删除之前的头像
def img_postView(request):
    user_id = request.session['id']
    action = request.GET.get('action', '')
    # 得到的imgfield需转换为str才能使用
    oldphotopath = str(User.objects.get(id=user_id).avatar)

    # 裁剪后的图片是base64编码数据，用base64.b64decode还原成图片后保存到数据库中
    strs = request.POST.get('photo', '').split(",")[1]
    imgdata = base64.b64decode(strs)

    # 将datetime转换为字符串的时间戳
    now = datetime.datetime.now()
    time_stamp = datetime.datetime.strftime(now, '%Y_%m_%d_%H_%M_%S_')

    imgname = time_stamp + str(random.randint(0, 100))

    with open('upload/love/avatar/' + imgname + '.jpg', 'wb') as f:
        f.write(imgdata)

    avatar = 'love/avatar/' + imgname + '.jpg'
    User.objects.filter(id=user_id).update(avatar=avatar)

    # 避免删除默认头像
    if '知否.jpg' not in oldphotopath:
        # 物理删除图片
        import os
        from django.conf import settings
        # d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tu_jpg = os.path.join(settings.MEDIA_ROOT, oldphotopath)
        if os.path.isfile(tu_jpg):
            os.remove(tu_jpg)

    return redirect('/love/getinfo?action=' + action)
