#列表练习
"""
lx=["桥边姑娘","下山","年少心事","海市蜃楼","好想抱住你","哪里都是你","她会魔法吧"]
print("变量的数据类型为:",type(lx))
#1.输出该变量的数据类型
print("用切片输出所有数据",lx[::])
#2.用切片输出所有数据
print("输出三到五位的数据",lx[3:6])
#3.输出三到五位的数据
print("倒序输出所有数据",lx[::-1])
#4.倒序输出所有数据
print("输出二到六位数据并倒序输出",lx[2:7:-1])
#5.输出二到六位数据并倒序输出
lx.insert(4,"夏天的风")
print("在第四位后插入夏天的风",lx)
#6.在第四位后插入夏天的风
lx.append("一路生花")
print("在尾部追加一路生花",lx)
#7.在尾部追加一路生花
print("输出最后一个元素",lx[-1])
#8.输出最后一个元素
del lx[2:5]
print("删除第二到第四位数据",lx)
#9.删除第二到第四位数据
print("查询列表此时有多少条数据",len(lx))
#10.查询列表此时有多少条数据
lx.clear()
print(lx)
#11.清空列表的所有数据
"""


"""
biao=[]
percent=0
for i in range(1,11):
    percent=int(input("请第%d位评委输入评分:"%i))
    biao.append(percent)
MAX=max(biao)
print("最高分为:",MAX)
MIN=min(biao)
print("最低分为:",MIN)
del MAX,MIN
sum=0
for num in biao:
    sum+=num
print("选手最终的成绩为:",float(sum/8))
"""


"""#没懂
dl={}
lt=[]
print("输入quit表示选手成绩录入完毕")
while True:
    name=input("请输入选手名称")
    if name=='quit':
        break
    score=int(input("请输入选手的票数"))
    dl[name]=score
for n in dl.items():        #item()遍历字典所有元素
    dl.append([n[1]],n[0])  #在列表尾部追加元素
print("lt:",lt)
lt.sort(reverse=True)       #降序排列
for k in range(1,len(lt)+1):
    print(f"第{k}名:{lt[k-1][1]},票数为:{lt[k-1][0]}")
"""

"""
score=[]#存储评分
for n in range(1,11):
    percent=int(input(f"请第{n}位评委输入评分"))
    score.append(percent)#列表追加数据
mx=max(score)#最高分
mn=min(score)#最低分
score.sort()   #给列表的数据排序，从小到大排序
print(f"去掉最低分",score[0])
print(f"去掉最高分",score[len(score)-1])
score.remove(mx)#删除最高分
score.remove(mn)#删除最低分
del score[0]#删除第一元素  最低分
score.pop()#弹出最后一个元素
print(f"选手最终得分：{sum(score)/8:2f}")
"""

"""
#没懂
dl=[]       #存储多个联系人的列表
print("="*20)
print("欢迎使用通讯录:"
      "1.添加联系人"
      "2.查看通讯录"
      "3.删除联系人"
      "4.修改联系人信息"
      "5.查找联系人"
      "6.退出")
print("="*20)
while True:
    pl={}       #每循环一次产生一个空字典，添加时产生一个人的记录
    gong=int(input("请输入功能序号:"))
    if gong==1:
        print("添加")
        name=input("请输入联系人的姓名")
        tl=input("请输入联系人的电话")
        email=input("请输入联系人的邮箱")
        address=input("请输入联系人的地址")
        pl.update(姓名=name,手机号=tl,邮箱=email,地址=address)
        dl.append(pl)   #把信息添加到列表中
        print("保存成功")
    elif gong==2:
        print("查看")
        if len(dl)==0:
            print("通讯录没有信息")
        else:
            for n in dl:
                print("姓名",n["姓名"])
                print("手机号码", n["手机号码"])
                print("电子邮箱", n["电子邮箱"])
                print("地址", n["地址"])
    elif gong==3:
        print("删除")
        if len(dl)==0:
            print("通讯录没有记录，不能记录")
        else:
            delname=input("请输入要删除的联系人姓名")
            flag=False
            for n in dl:
                if n["姓名"]==delname:    #代表存在这个人的记录
                    flag=True            #存在这个人，则标记修改为True
                    dl.remove(n)         #删除记录
                    print("删除记录成功")
                if flag==False:
                    print(f"delname","") #没写完
    elif gong==4:
        print("修改联系人信息")
        if len(dl)==0:
            print("通讯录中没有记录，无法进行修改")
        else:
            flag=False
            for n in dl:
                if n["姓名"]==name:
                    print(f"姓名:,{n['姓名']}\t手机号:{n['手机号']}\t邮箱:{n['邮箱']}\t{n['地址']}")
                    name=input("请输入新的姓名")
                    tl=input("请输入新的电话号")
                    email=input("请输入新的邮箱")
                    address=input("请输入新的地址")
                    n.update(姓名=name,手机号=tl,地址=address)
                    print("更新联系人信息成功，可以查看")
                    print(n)
                    flag=False
                if flag==False:
                    print("您输入的联系人姓名不存在")

    elif gong==5:
        print("查找联系人")
        if len(dl)==0:
            print("通讯录没有记录")
        else:
            flag=False
            for n in dl:
                if n["姓名"]==name:
                    flag=True
                    print(f"姓名:,{n['姓名']}\t手机号:{n['手机号']}\t邮箱:{n['邮箱']}\t{n['地址']}")
            if flag==False:
                print("没有查找到这个联系人的信息")

    elif gong==6:
        print("退出")
        break
    else:
        print("您输入了错误的序号")
"""









