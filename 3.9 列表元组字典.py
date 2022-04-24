#[]列表
"""
mylist = [False,89,"love","school",90,78.3]
print ("集合数据为:",mylist)
print ("mylist数据类型为:",type(mylist))
mylist[2] = "sanshine"
print ("此时集合数据为:",mylist)
"""


#()元组内元素不能修改
"""
mytp = (True,"Kate","Myname",90.5,78+9j)
print ("mytp中的数据为:",mytp)
print ("mytp中的类型为:",type(mytp))
#mytp[1] = "Tom"
print (mytp)
"""

#{}集合内元素不能修改
"""
myset = {291,"mone","i am student",False,291,"mome",291,"i am student"}
print ("mytp中的数据为:",myset)
print ("mytp中的类型为i:",type(myset))
"""

#{}也能创建字典 键(key):值(value)
"""
mydic = {"学号":"001","姓名":"王小龙","性别":"男","国家":"中国","爱好":"篮球"}
print ("mydic的数据为:",mydic)
print ("mydic的类型为:",type(mydic))
mydic ["爱好"] = "高山滑雪"
mydic ["姓名"] = "谷爱凌"
print ("mydic的数据为:",mydic)
"""


#输入三角形三边求面积
"""
a = int(input("请输入三角形的边"))
#input()输入函数默认字符类型，需要强制转换
b = int(input("请输入三角形的边"))
c = int(input("请输入三角形的边"))
p = float((a+b+c)/2)
#p为周长
import math
S = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print ("三角形的面积为：",S)
"""

#求平均成绩
"""
input("请输入您的姓名:")
Chi = int(input("输入语文成绩:"))
Math = int(input("输入数学成绩:"))
Eng = int(input("输入英语成绩:"))
Avg = float(Chi+Math+Eng)/2
print ("平均成绩为:",Avg)
percent = float(Chi/(Chi+Math+Eng)*100)
print("语文成绩占比:",percent,"%")
"""


#打印购物账单
"""
water = int(input("水的数量为:"))
dan = int(input("蛋的数量为:"))
milk = int(input("牛奶的数量为:"))
print("-"*30)
print("商品名      数量      单价      总价")
print("矿泉水",water,"2.5",float(water*2.5),sep="        ")
print("蛋黄派",dan,"3.9",float(dan*3.9),sep="         ")
print("牛奶",dan,"3.9",float(milk*22.5),sep="        ")
print("-"*30)
"""




#输入成绩判断是否为学霸
"""
python = int(input("请输入您的python成绩:"))
html = int(input("请输入您的html成绩:"))
if python>90:
    if html>90:
        print("原来你是学霸")
else:
    print("还需要努力")
"""
"""
#用and
python = int(input("请输入您的python成绩:"))
html = int(input("请输入您的html成绩:"))
if python>90 and html>90:
    print("原来你是学霸")
else:
    print("还需要努力")
"""




#输入用户名密码判断正误
"""
Ruser = "zhangsan"
    #正确的用户名
Rpass = "python123"
    #正确的密码
user = input("用户名为:")
password = input("密码为:")
if user ==Ruser and password==Rpass:
    print("欢迎您")
elif user!=Ruser and password!=Rpass:
    print("全部错误")
elif user!=Ruser:
    print("用户名错误")
elif password!=Rpass:
    print("密码错误")
"""



#输入一个数，判断奇偶性
"""
num = int(input("请输入一个数:"))
if num%2==0:
    print(num,"为偶数")
elif num%2!=0:
    print(num,"为奇数")
"""



#身体健康指数
"""
weight = float(input("请输入你的体重"))
height = float(input("请输入你的身高"))
BMI = float(weight/(height*height))
print("BMI的值为:",BMI)
if BMI<18.5:
    print("偏轻")
elif BMI>18.5 and BMI<=24.9:
    print("正常")
elif BMI>=25 and BMI<=29.9:
    print("超重")
elif BMI>=30 and BMI<=34.9:
    print("肥胖")
elif BMI >=35:
    print("过度肥胖")
"""



#超市管理系统
"""
print("-"*10,"欢迎访问超市管理系统","-"*10)
print(" "*11,"1.登陆\n"," "*10,"2.注册\n"," "*10,"3.退出")
num1 = int(input("请选择您的操作:"))
Ruser ="z"
#正确用户名"z"
Rpass ="123"
#正确密码"123"
if num1 ==1:
    print("-"*30,"\n")
    user = input("请输入您的用户名:")
    password = input("请输入您的密码:")
    if user == Ruser and password == Rpass:
        print("登陆成功")
        print("-"*30,"\n")
        print(" "*11,"1.查看所有会员信息\n"," "*10,"2.删除指定的会员\n"," "*10
              ,"3.添加会员\n"," "*10,"4.退出系统\n"," "*30)
        num2 = input("请选择要执行的操作:\n")
elif num1!=1:
    print("对不起，您目前不能进行其他操作，请重新登陆")
"""













