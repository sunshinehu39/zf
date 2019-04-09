from django.db import models

# 数据表建模：用户
class User(models.Model):
    accounts = models.CharField(verbose_name='帐号',max_length=20,unique=True)
    password = models.CharField(verbose_name='密码',max_length=150)
    gender=models.CharField(verbose_name='性别',default='2',max_length=4,choices=(("1", u"男"), ("2", u"女")))
    vip = models.IntegerField(verbose_name='会员等级',default=0,choices=((1, u"注册会员"), (2, u"青铜会员"), (3, u"白银会员"), (4, u"黄金会员"),(5, u"钻石会员"),(6, u"运营团队")))
    avatar = models.ImageField(verbose_name='头像', default='love/avatar/知否.jpg', upload_to='love', max_length=200,
                               blank=True, null=True)

    infopassword = models.CharField(verbose_name='资料密码',max_length=20,default='doszf666')
    referrer = models.IntegerField(verbose_name='推荐人编号',default=0,blank=True, null=True)
    newzfnum = models.IntegerField(verbose_name='新增知否币数量',default=0)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.accounts

# 数据表建模：成员
class Info(models.Model):
    U_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='编号')
    gender=models.CharField(verbose_name='性别',default='2',max_length=4,choices=(("1", u"男"), ("2", u"女")))
    truename = models.CharField(verbose_name='真实姓名', max_length=16)
    birthyear = models.IntegerField(verbose_name='出生年份')
    nickname = models.CharField(verbose_name='昵称',max_length=16,default='知否')
    constellation = models.CharField(verbose_name='星座',max_length=8)
    education = models.IntegerField(verbose_name='学历',choices=((0, u"其他"),(1, u"专科"),(2, u"本科"),(3, u"硕士"),(4, u"博士")))
    hometown = models.CharField(verbose_name='家乡',max_length=16)
    height = models.FloatField(verbose_name='身高')
    weight = models.FloatField(verbose_name='体重')
    stature = models.CharField(verbose_name='身材', max_length=6,default='标准')
    job = models.CharField(verbose_name='工作',max_length=30)
    salary = models.FloatField(verbose_name='年薪')
    house = models.BooleanField(verbose_name='是否有房',default=False)
    car = models.BooleanField(verbose_name='是否有车',default=False)
    smoke = models.BooleanField(verbose_name='是否抽烟',default=False)
    beer = models.BooleanField(verbose_name='是否喝酒',default=False)
    hobbies = models.CharField(verbose_name='兴趣爱好',max_length=300,blank=True, null=True)
    tags = models.CharField(verbose_name='个性标签',max_length=200,blank=True, null=True)
    soliloquy = models.TextField(verbose_name='内心独白', max_length=1000,blank=True, null=True)
    lovenum = models.IntegerField(verbose_name='恋爱次数',blank=True, null=True)
    thinklove = models.TextField(verbose_name='恋爱感悟', max_length=1000,blank=True, null=True)

    agemin = models.IntegerField(verbose_name='年龄下限',blank=True, null=True)
    agemax = models.IntegerField(verbose_name='年龄上限',blank=True, null=True)
    lovenummin = models.IntegerField(verbose_name='恋爱次数下限',blank=True, null=True)
    lovenummax = models.IntegerField(verbose_name='恋爱次数上限',blank=True, null=True)
    heightmin = models.FloatField(verbose_name='身高下限',blank=True, null=True)
    heightmax = models.FloatField(verbose_name='身高上限',blank=True, null=True)
    yourstature = models.CharField(verbose_name='对方身材', max_length=6,default='标准')
    salarymin = models.FloatField(verbose_name='年薪下限',blank=True, null=True)
    ifhouse = models.BooleanField(verbose_name='是否有房',default=False)
    ifcar = models.BooleanField(verbose_name='是否有车',default=False)
    ifsmoke = models.BooleanField(verbose_name='是否抽烟',default=False)
    ifbeer = models.BooleanField(verbose_name='是否喝酒',default=False)
    youreducation = models.IntegerField(verbose_name='对方学历',choices=((0, u"不限"),(1, u"专科"),(2, u"本科"),(3, u"硕士"),(4, u"博士")))
    yourhometown = models.CharField(verbose_name='对方家乡',max_length=16,default='不限')
    yourhobbies = models.CharField(verbose_name='对方兴趣爱好',max_length=300,blank=True, null=True)
    loveslogan = models.CharField(verbose_name='交友宣言', max_length=30, blank=True, null=True)
    more = models.TextField(verbose_name='更多期望', max_length=1000,blank=True, null=True)
    marrymax = models.IntegerField(verbose_name='结婚期望',blank=True, null=True)
    phone = models.CharField(verbose_name='手机号', max_length=11)
    wechat = models.CharField(verbose_name='微信号', max_length=20)
    jointime = models.DateTimeField(auto_now_add=True, verbose_name='加入时间',blank=True, null=True)

    class Meta:
        verbose_name = '会员资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.truename

# 数据表建模：关系
class Relationship(models.Model):
    U_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='编号')
    lovelist = models.CharField(verbose_name='我喜欢的人',max_length=3000,default='')
    meetlist = models.CharField(verbose_name='我见过的人',max_length=3000,default='')
    notlovelist = models.CharField(verbose_name='我不喜欢的人',max_length=3000,default='')
    lovedlist = models.CharField(verbose_name='喜欢我的人', max_length=3000,default='')
    looklist = models.CharField(verbose_name='我看过的人', max_length=3000,default='')
    lookedlist = models.CharField(verbose_name='看过我的人', max_length=3000,default='')
    addlookedlist = models.CharField(verbose_name='新增看我的人',max_length=300,default='')
    addlovedlist = models.CharField(verbose_name='新增喜欢我的人',max_length=300,default='')
    newmsgnum = models.IntegerField(verbose_name='新增信息数',default=0)

    class Meta:
        verbose_name = '关系'
        verbose_name_plural = verbose_name

# 数据表建模：信箱
class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发信人',related_name='Chat_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='收信人',related_name='Chat_receiver')
    content = models.CharField(verbose_name='内容',max_length=100)
    time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')

    class Meta:
        verbose_name = '信箱'
        verbose_name_plural = verbose_name

# 数据表建模：脱单秘籍
class Lovebook(models.Model):
    suitgender=models.CharField(verbose_name='适合性别',default='2',max_length=4,choices=(("1", u"男"), ("2", u"女"),("3", u"男女皆可")))
    index = models.IntegerField(verbose_name='排序',blank=True, null=True)
    tags = models.CharField(verbose_name='标签',max_length=50)
    title = models.CharField(verbose_name='标题',max_length=50)
    url = models.URLField(verbose_name='链接', max_length=200,blank=True, null=True)
    source = models.CharField(verbose_name='来源',default='喜马拉雅',max_length=30,blank=True, null=True)
    note = models.TextField(verbose_name='笔记', max_length=1000,blank=True, null=True)
    pubtime = models.DateTimeField(verbose_name='发布时间',auto_now_add=True )

    class Meta:
        verbose_name = '脱单秘籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
