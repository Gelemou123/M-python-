#存款买车
"""
cun =int(input("请输入您的银行存款"))
if cun>500:
    print("买凯迪拉克")
elif cun>100:
    print("买帕萨特")
elif cun > 50:
    print("买一兰托")
elif cun>10:
    print("买奥拓")
else:
    print("买捷安特")
"""

#分数
"""
percent =int(input("请输入小明考试成绩"))
if percent==100:
    print("买辆车")
elif percent>=90:
    print("买MP4")
elif percent>=60 and percent<90:
    print("买本参考书")
else:
    print("什么也不买")
"""

#名次
"""
ming =int(input("请输入名次"))
if ming==1:
    print("将参加麻省理工大学组织一个月训练营")
elif ming==2:
    print("奖励笔记本")
elif ming==3:
    print("奖励硬盘一个")
else:
    print("不给任何奖励")
"""


#百分制成绩
"""
percent =int(input("请输入百分制成绩"))
if percent>=90:
    print("A")
elif percent>=80 and percent<90:
    print("B")
elif percent>=70 and percent<80:
    print("C")
elif percent>=60 and percent<70:
    print("D")
else:
    print("E")
"""

#输入两个数字和操作符进行计算
"""
num1 = int(input("请输入第一个数字:"))
fu = input("请输入操作符")
num2 = int(input("请输入第二个数字"))
if fu=='+':
    print(num1,'+',num2,'=',num1+num2,sep="")
elif fu=='-':
    print(num1,'-',num2,'=',num1-num2,sep="")
elif fu=='*':
    print(num1,'*',num2,'=',num1*num2,sep="")
elif fu=='/':
    if num2==0:
        print("除数不能为0")
    else:
        print(num1,'/',num2,'=',num1/num2,sep="")
else:
    print("您输入的运算符违法")
"""

#输出20以内的偶数
"""
i=1
while i<20:
    if i%2==0:
        print(i,end=' ')
    i=i+1
"""



#输出100以内能被7整除不能被5整除的数
"""
#用while写的
i=1                     
while i<=100:
    if i%7==0 and i%5!=0:
        print(i,end=" ")
    i=i+1
"""
#用for写的
"""
for num in range(1,100,1):
    if num%7==0 and num%5!=0:
        print(num)
"""

#给定字符串，统计字
"""
str="Python是一种代表简单主义思想的语言。\n" \
    "阅读一个良好的Python程序就感觉像是在\n" \
    "读英语一样。它使你能够专注于解决问题而\n" \
    "不是去搞明白语言本身"
yu=0
ni=0
for k in str:
    if k=='语':
        yu=yu+1
    elif k=='你':
        ni=ni+1
print(str,'\n''这段文字中有',yu,'个语','有',ni,'个你',sep=' ')
"""


#for语句一般用于遍历循环      for 临时变量 in 目标对象    语句块
#range(x,y,z)  x+z加到y为止，但不能为y


#for循环打印指令输出次数的字符串
"""
str = input("请输入字符串")
num = int(input("请输入打印次数"))
for t in range(1,num+1):
    print(str)
"""



#打印星号
"""
for i in range(5):
    for k in range(5):
        print("#",end='')
    print("\n",end='')
"""
#range(5)相当于C语言中的for(i=0;i<5;i++) range(1,6)跟rang(5)也差不多
"""
for i in range(1,6):
    print("#"*5,end='\n')
"""


#100以内偶数和，奇数和
"""
i=1        #控制循环次数
ou=0       #偶数的和
ji=0       #奇数的和
while i<100:
    if i%2==0:
        ou=ou+i
        i=i+1
    if i%2==1:
        ji=ji+i
        i=i+1
print("所有奇数的和为:",ji)
print("所有偶数的和为:",ou)
"""



#输入五个数求平均值
"""
sum=0
for i in range(6):
    num = int(input("请输入数字"))
    sum=sum+num
    #循环执行五次
avg = sum/6
print("平均数为:%.2f"%avg)
"""



#从键盘键入一个数求其阶乘
"""
result = 1
num = int(input("请输入要计算阶乘的数"))
for i in range(1,num+1):
    result=result*i
print(i,"的阶乘为:",result)
"""



#猜数字游戏
"""
import random
ran = random.randint(1,99)
#导入函数random
count = 0
#猜的次数
print("我心里有一个1-99之间的数，你猜猜是什么")
while True:
    count+=1
    num = int(input("请输入你要猜的数"))
    if num==ran:
        print("恭喜你，猜对了!")
        break
    elif num>ran:
        print("大了点")
    elif num<ran:
        print("小了点")
    else:
        print("输入错误")
if count>10:
    print("你太笨了")
elif count>5:
    print("马马虎虎")
else:
    print("您太厉害了")
"""


#输入一个数字输出由数字组成的三角形
"""
num = int(input("请输入一个数字:"))
for i in range(1,num+1):
   for k in range(1,i+1):
       print(i,end=" ")
   print()
"""

#打印正三角
"""
num = int(input("请输入要打印*的行数:"))
for i in range(1,num+1):
    for k in range(1,i+1):
        print("*",end=" ")
    print()
"""


#打印棱形
"""
num = int(input("请输入行数"))
for k in range(1,num):      #上层三角
    print((" * "*k).center(num*4))
for f in range(num,0,-1):   #从x开始递减,下层三角
    print((" * "*f).center(num*4))
    #center()居中对齐
"""


#输入一个数求1~num的阶乘
"""
num = int(input("请输入一个自然数:"))
sum=0
for i in range(1,5):
    ji=1
    for k in range(1,i+1):
        ji*=k
        #阶乘
    sum+=ji
    #累加和
print("这个自然数的阶乘和为:",sum)
"""

#打印棋盘
"""
i=0
num=int(input("请输入行"))
num-=2
print("┏-","-┯-"*num,"-┓",sep='')
for i in range(1,num+1):
    print("┠-", "-┼-" * num, "-┨",sep='')
    i+=1
print("┗-","-┷-"*num,"-┛",sep='')
"""


#打印九九乘法表
"""
for i in range(1,10):
    for k in range(1,i+1):
        print(i,'*',k,'=',i*k,sep=' ',end=' ')
    print()
for i in range(1,10):
    for k in range(1,i+1):
        print("%d*%d=%2-d"%i%k)
"""


#判断2000到2022有几个闰年
"""
temp=0
for i in range(2000,2023):
    if i%4==0 and i%100!=0 or i%400==0 :
        print(i,"是闰年",sep='')
        temp=temp+1
print("共有",temp,'个闰年',sep='')
"""


#接收10个数并输出
"""
sum=0
for i in range(1,6):
    num= int(input(f"请输入第{i}个数:"))  #f格式化这些字符串，里面{变量名}
    sum+=num
print("这",i,"个数之和为:",sum,sep="")
"""


#输入若干成绩，回答yes输入下一个,no跳出循环，并统计输入成绩数量和平均值
"""
count=0
sum=0
while True:
    score=int(input("请输入成绩:"))
    sum+=score
    #将成绩累加
    count+=1
    #记录输入成绩个数
    op=input("是否要继续？yes/no:")
    if op!="yes":
        break
print("输入了",count,"个学生成绩,平均成绩为:",float(sum/count),sep='')
"""



#求最大小值，删除元素，求和
"""
sum=0
num=0
list=[]
for i in range(1,7):        #六个评委进行打分
    num+=1
    score = int(input(f"第{i}个评委的评分为:"))
    list.append(score)
    #append往列表追加数据
    sum += score
    #求列表中的和
print("最大值为:", max(list))
print("最小值为:", min(list))
#输出列表中的最大值和最小值
list.remove(max(list))
list.remove(min(list))
#删除最大值和最小值
print("平均分为:", sum / (num-2))
"""


#打印棋盘(没写完)
"""
size = int(input("请输入棋盘大小:"))
for i in range(size):
    for j in range(size):   #先打印四个角
        if i==0 and j==0:
            print("┏-", end='')
        elif i==0 and j==size:
            print("-┓", end='')
        elif i==size and j==0:
            print("┗-", end='')
        elif i==size and j==size:
            print("-┛", end='')
            """
"""
print("┗-", end='')
print("┠-", end='')
print("-┯-", end='')
print("-┷-", end='')
print("-┓", end='')
print("-┛", end='')
print("-┨", end='')
print("-┼-", end='')
"""





#绘制圆圈
"""
import turtle
turtle.circle(50)#画圆，圆的半径
turtle.pensize(1)#笔的宽度
turtle.pencolor("black")#笔的颜色
turtle.circle(60)
turtle.mainloop( )    #结束绘制，加结束语
    #width宽度
"""

#字符串
"""
st = 'let\'s learn python'  #可以用转义字符反斜杠\
print(st)
print(r"转义字符中前加r原样输出:\n,\r,\b")
#\n换行   \r回车    \b退格
"""


#使用格式转换符输出圆柱体的体积和表面积
"""
r = int(input("请输入底面半径:"))
h = int(input("请输入圆柱体的高:"))
s = 2*r*3.14/h
#体积
c = 2*3.14*r*r+2*3.14*r*h
#表面积
print("圆柱体的体积为:%-8.2f\n圆柱体的表面积为:%-8.2f"%(s,c))
"""


#趣味模板用{0}形式输出   .format方式格式化字符串   多种方式输出字符串
"""
name = input("请输入姓名:")
place = input("请输入地址:")
game = input("请输入游戏:")
print("可爱的{0}在{1}玩{2}".format(name,place,game))
print("可爱的{}在{}玩{}".format(name,place,game))
print(f"可爱的{name}在{place}玩{game}")
print("可爱的%s在%s玩%s"%(name,place,game))
"""


#动态进度条
"""
import time
dot = 50 #.的数量
print('='*23+'开始下载'+'='*25)
#打印最上面的开始下载
for i in range(dot+1):
    xing = '*'*i
    #*的个数逐渐增加，表示进度
    indot = '.'*(dot-i)
    #.的数量越来越少
    prep = (i/dot)*100 #进度条里的百分比
    print("\r{:.0f}%[{}{}]".format(prep,xing,indot),end='')
    time.sleep(0.1)
print("\n"+'='*23+'下载完成'+"="*25)
#打印最后的下载完成
"""



#计算器（各种输出方式）
"""
num1 = float(input("请输入第一个数字："))
fu =input("请输入操作符")
num2 = float(input("请输入第二个数字："))
if fu =='+':
    print("%.f%c%.f ="%(num1,fu,num2),"运算结果为:",num1+num2,sep='')
    #用百分号格式转换符输出
elif fu =='-':
    print("{:.f}{}{:.f}".format(num1,fu,num2),"=",num1-num2,sep='')
    #用占位符输出
elif fu =='*':
    print(f"{num1:.f}{fu}{num2:.f}=",f"{num1*num2}")
elif fu =='/':
    print("计算结果为:{0}{1}{2}={3}".format(num1,fu,num2,num1/num2))
    print("计算结果为:{a:.f}{b}{c:.}={d:.}".format(a=num1, b=fu, c=num2, d=num1 / num2))
"""



#查找和替换(新字符串名字=要修改的字符串名字.replace("要修改的字符串","改完的内容")
"""
str = "这个手机是山寨版吧！不承认也不行就是山寨版的！打个赌吧！"
new = str.replace("山寨","**")
print(new)
"""
#替换(replace),拆分(split),连接(join)
"""
fruit = "西梅、白玉樱桃、橘子、砂糖桔、橙子、柠檬、青柠、柚子、金桔、葡萄柚、香橼"
newf = fruit.replace("、",",")
print("替换之后",newf)
lt = fruit.split("、")
print("拆分之后:"lt)
string = "-".join(lt)
print("连接之后:"string)
"""


#upper()将字符串全部转换为大写,lower()小写
#capitalize()将字符串第一个字母转换为大写
#title()将字符串每个单词首字母转换为大写
#center()返回长度width的字符串，原字符居中显示

"""
count = 0
s = "AbcDeFGhIJ"
for i in s:
    if i.islower():#如果结果为True，执行下面
        count+=1
print("字符串%s,小写字母数量为:%d"%(s,count))

sk = "Life is short.I use python"
if sk.find("python")>=0:
    nsk=sk.replace("python","Python")
    print(nsk)
else:
    print("没有这个字符串")
"""























