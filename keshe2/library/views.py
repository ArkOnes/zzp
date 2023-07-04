from django.shortcuts import HttpResponse
from .models import *
import os
import json
from keshe2 import settings
from django.forms.models import model_to_dict

# Create your views here.

# 用户注册  post方法
def user_register(request):
    account = request.POST.get("account")
    password = request.POST.get("password")
    sex = request.POST.get("sex")
    f = request.FILES['avatar']
    filePath = os.path.join(settings.MEDIA_ROOT,f.name)
    with open(filePath,'wb') as fp:
        for info in f.chunks():
            fp.write(info)
    file_absolute_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'+filePath   # 获取图片绝对路径
    print("account:",account,",password:",password,"filePath:",file_absolute_path)   
    # 使用os.path.abspath(__file__)获取当前文件的绝对路径。
    # 使用os.path.dirname()获取当前文件的所在目录    directory_path = os.path.dirname(os.path.abspath(__file__))
    # 使用多个os.path.dirname()嵌套以获取当前文件的所在目录的上一级目录。
    #                           parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # f:图片文件名； filePath：图片相对路径(/static/upfile); file_absolute_path=图片绝对路径
    user.objects.create(account=account,password=password,sex=sex,avatar=filePath) 
    return HttpResponse("注册成功,请登录")

# 用户登录   post方法
def user_login(request):
    account=request.POST.get("account")
    password=request.POST.get("password")
    try:
        User = user.objects.get(account=account)
        if User.password == password:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("用户名或密码错误，请重试")
    except:
        return HttpResponse("没有这个用户，请注册")

# 用户信息查询   GET方法
def user_select(request):
    account = request.GET.get("account")
    User = user.objects.get(account=account)
    json_list = []
    json_list.append(model_to_dict(User))
    return HttpResponse(json.dumps(json_list), content_type="application/json")

# 用户信息 修改
def user_update(request):    # 更新数据
    account = int(request.POST.get("account"))
    # name = request.POST.get("name")
    sex = request.POST.get("sex")
    f = request.FILES['avatar']
    filePath = os.path.join(settings.MEDIA_ROOT,f.name)
    with open(filePath,'wb') as fp:
        for info in f.chunks():
            fp.write(info)
    # # file_absolute_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'+filePath   # 获取图片绝对路径
    # # print("account:",account,"sex:",sex,"filePath:",file_absolute_path)   
    # # 使用os.path.abspath(__file__)获取当前文件的绝对路径。
    # # 使用os.path.dirname()获取当前文件的所在目录    directory_path = os.path.dirname(os.path.abspath(__file__))
    # # 使用多个os.path.dirname()嵌套以获取当前文件的所在目录的上一级目录。
    # #                           parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # # f:图片文件名； filePath：图片相对路径(/static/upfile); file_absolute_path=图片绝对路径
    obj = user.objects.get(account=account)
    # obj.name = name
    obj.sex = sex
    obj.avatar = filePath
    obj.save()
    return HttpResponse("数据已更新成功")

# 通过ID删除一条记录   用户信息 删除
def user_delete(request):
    account = int(request.GET.get("account"))
    user.objects.filter(account=account).delete()
    return HttpResponse("删除成功")

# 预约信息 增加   post方法
def reservation_insert(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    place = request.POST.get("place")
    time = request.POST.get("time")
    reservation.objects.create(id=id,name=name,place=place,time=time)
    return HttpResponse("数据已成功添加到数据库!")

# 预约信息 查询  get方法
def reservation_select(request):
    json_list = []
    data = reservation.objects.all()
    print(data)
    # 生成一个列表，列表中的每一个元素都是字典
    for i in data:
        print(model_to_dict(i))
        json_list.append(model_to_dict(i))
    return HttpResponse(json.dumps(json_list), content_type="application/json")

# 通过id 查询 预约信息   get方法
def reservation_select_by_id(request):
    id = int(request.GET.get("id"))
    article = reservation.objects.filter(id=id).first()
    json_list = []
    json_list.append(model_to_dict(article))
    return HttpResponse(json.dumps(json_list),content_type="application/json")

# 预约信息 修改
def reservation_update(request):    # 更新数据
    id = int(request.POST.get("id"))
    name = request.POST.get("name")
    place = request.POST.get("place")
    time = request.POST.get("time")
    obj = reservation.objects.get(id=id)
    obj.name = name
    obj.place = place
    obj.time = time
    obj.save()
    return HttpResponse("数据已更新成功")

# 文章表更新数据
# def article_update(request):
#     id = int(request.POST.get("id"))
#     articleTitle = request.POST.get("articleTitle")
#     articleContent = request.POST.get("articleContent")
#     articleTime = request.POST.get("articleTime")
#     f = request.FILES['picture']
#     filePath = os.path.join(settings.MEDIA_ROOT,f.name)
#     with open(filePath,'wb') as fp:
#         for info in f.chunks():
#             fp.write(info)
#     print(filePath)
#     obj = Article.objects.get(id=id)
#     obj.articleTitle = articleTitle
#     obj.articleContent = articleContent
#     obj.articleTime = articleTime
#     obj.articleImagePath = filePath
#     obj.save()
#     return HttpResponse("update success")

# 通过ID删除一条记录   预约信息 删除
def reservation_delete(request):
    id = int(request.GET.get("id"))
    reservation.objects.filter(id=id).delete()
    return HttpResponse("删除成功")

# 座位表添加数据
def classroom_init(request):
    # 一楼  **********************************************
    place_id1=1
    place1="一楼101室1排1号"
    busy1="空闲中"
    classroom.objects.create(place_id=place_id1,place_number=place1,busy=busy1)
    place_id2=2
    place2="一楼102室2排3号"
    busy2="空闲中"
    classroom.objects.create(place_id=place_id2,place_number=place2,busy=busy2)
    place_id3=3
    place3="一楼103室4排2号"
    busy3="空闲中"
    classroom.objects.create(place_id=place_id3,place_number=place3,busy=busy3)
    # 二楼  **********************************************
    place_id4=4
    place4="二楼201室4排2号"
    busy4="空闲中"
    classroom.objects.create(place_id=place_id4,place_number=place4,busy=busy4)
    place_id5=5
    place5="二楼202室1排3号"
    busy5="空闲中"
    classroom.objects.create(place_id=place_id5,place_number=place5,busy=busy5)
    place_id6=6
    place6="二楼203室3排2号"
    busy6="空闲中"
    classroom.objects.create(place_id=place_id6,place_number=place6,busy=busy6)# 
    # 三楼  **********************************************
    place_id7=7
    place7="三楼302室4排4号"
    busy7="空闲中"
    classroom.objects.create(place_id=place_id7,place_number=place7,busy=busy7)
    place_id8=8
    place8="三楼303室2排1号"
    busy8="空闲中"
    classroom.objects.create(place_id=place_id8,place_number=place8,busy=busy8)
    place_id9=9
    place9="三楼303室1排2号"
    busy9="空闲中"
    classroom.objects.create(place_id=place_id9,place_number=place9,busy=busy9)
    # 四楼  **********************************************
    place_id10=10
    place10="四楼401室2排2号"
    busy10="空闲中"
    classroom.objects.create(place_id=place_id10,place_number=place10,busy=busy10)
    place_id11=11
    place11="四楼402室1排3号"
    busy11="空闲中"
    classroom.objects.create(place_id=place_id11,place_number=place11,busy=busy11)
    place_id12=12
    place12="四楼403室2排4号"
    busy12="空闲中"
    classroom.objects.create(place_id=place_id12,place_number=place12,busy=busy12)
    return HttpResponse("座位表初始化成功")

    # place1="一楼101室1排1号"
    # freeTime1=''
    # userId1=''
    # busy1="空闲中"
    # classroom.objects.create(place_number=place1,freeTime=freeTime1,userId=userId1,busy=busy1) 
    # place2="一楼102室2排2号"
    # freeTime2=''
    # userId2=''
    # busy2="空闲中"
    # classroom.objects.create(place_number=place2,freeTime=freeTime2,userId=userId2,busy=busy2) 
    # place3="二楼201室3排2号"
    # freeTime3=''
    # userId3=''
    # busy3="空闲中"
    # classroom.objects.create(place_number=place3,freeTime=freeTime3,userId=userId3,busy=busy3) 
    # place4="二楼203室4排3号"
    # freeTime4=''
    # userId4=''
    # busy4="空闲中"
    # classroom.objects.create(place_number=place4,freeTime=freeTime4,userId=userId4,busy=busy4) 
    # place5="三楼301室5排6号"
    # freeTime5=''
    # userId5=''
    # busy5="空闲中"
    # classroom.objects.create(place_number=place5,freeTime=freeTime5,userId=userId5,busy=busy5) 
    # place6="三楼302室6排4号"
    # freeTime6=''
    # userId6=''
    # busy6="空闲中"
    # classroom.objects.create(place_number=place6,freeTime=freeTime6,userId=userId6,busy=busy6) 
    # place7="四楼401室6排4号"
    # freeTime7=''
    # userId7=''
    # busy7="空闲中"
    # classroom.objects.create(place_number=place7,freeTime=freeTime7,userId=userId7,busy=busy7) 
    # place8="四楼403室4排1号"
    # freeTime8=''
    # userId8=''
    # busy8="空闲中"
    # classroom.objects.create(place_number=place8,freeTime=freeTime8,userId=userId8,busy=busy8)
    # return HttpResponse("座位表初始化成功!")

# 座位表 查询  get方法
def classroom_select(request):
    json_list = []
    data = classroom.objects.all()
    print(data)
    # 生成一个列表，列表中的每一个元素都是字典
    for i in data:
        print(model_to_dict(i))
        json_list.append(model_to_dict(i))
    return HttpResponse(json.dumps(json_list), content_type="application/json")