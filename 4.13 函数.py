"""
#1.输出六行星号
def printstart():
    for i in range(1,7):
        print("*"*i,end="\n")
printstart()
"""

"""
#2.100以内奇数和
def sum():
    a=0
    for i in range(1,101):
       if i%2==1:
           a+=i
    print("100以内奇数的和",a)
sum()
"""

"""
#3.定义有参无返回值，计算两数相加
def sum(a,b):
    print(f"{a}+{b}的和为{a+b}")
sum(1,2)
num1=int(input("请输入第一个数"))
num2=int(input("请输入第二个数"))
sum(num1,num2)
"""


"""
#4.计算长方形的面积和周长，有参无返回值
def add_chang(a,b):
    mian=float(a*b)
    zhou=float(a*2+b*2)
    print(f"长方形的面积为:{mian},长方形的周长为:{zhou}")
    print("长方形的面积为:%.2f,长方形的周长为:%.2f"%(mian,zhou))
chang = int(input("请输入长方形的长"))
kuan = int(input("请输入长方形的宽"))
add_chang(chang,kuan)
"""

"""
#5.定义有参有返回值，计算两数相加
def sum(a,b):
    print(f"{a}+{b}的和为{a+b}")
    return(sum)
num1=int(input("请输入第一个数"))
num2=int(input("请输入第二个数"))
print(sum)
"""

"""
#6.编写函数实现+-*/运算功能，有参数有返回值函数
def jisuan(a,b,c):
    sum=0
    if c=="+":
        sum=a+b
    elif c=="-":
        sum=a-b
    elif c=="*":
        sum=a*b
    elif c=="/":
        if num2==0:
            print("除数不能为0")
        else:
            sum=float(a/b)
    return sum
num1=int(input("请输入第一个数:"))
op=input("请输入运算符:")
num2=int(input("请输入第二个数:"))
result=jisuan(num1,num2,op)
print("计算结果为:%d%c%d=%d"%(num1,op,num2,result))
"""

"""
#7.判断账号密码是否正确
def gel(x,y):
    if x=="zhangsan" and y=="abc":
        print("恭喜你，登陆成功")
        return 1
    elif x!="zhangsan" or y!="abc": #也可以直接else:
        print("对不起您的账号和密码错误")
        return 0
hao=input("请输入账号")
mima=input("请输入密码")
gel(hao,mima)
"""


"""
#9.打印指定字符串功能
def str(a,b):
    for i in range(1,b+1):
        print(a)
st=input("请输入要打印的字符串:")
num=int(input("请输入打印字符串的个数"))
str(st,num)
"""

"""
#10.计算圆柱体的体积
def yuan(a,b,PI=3.14):
    tiji=float(a*PI*a*b)
    biao=float(2*PI*a*a+2*PI*a*b)
    return(tiji,biao)
r=float(input("请输入圆柱体的底面半径"))
h=float(input("请输入圆柱体的高"))
print("圆柱体的体积和表面积为:",yuan(r,h))
"""

"""
#11.用打包求多个值的最大值
def demo(*p):
    return max(p)
m=demo(3,2,4,5,6)
print("最大值为:",m)
"""
"""
#12.杨辉三角
def yanghui(k):
    print([1])  #第一行
    line=[1,1]  #第二行
    print(line)
    for i in range(2,k):                            #i=2,3,4,5,6
        r=[]                                         #每一行除去第一个数和最后一个数的列表
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])           #i=2 r=[2]  i=3  r[3,3] i=4 r[4,6,4]
        line=[1]+r+[1]                             #i=2,line[1,2,1] i=3  line[1,3,3,1]
        print(line)
num=int(input("请输入一个行数"))
yanghui(num)                                       #调用函数
"""

"""
#13.定义带参数，带返回值的函数，实现输入字符串把字符串中“山寨“替换成”**“的算法
def words(a):
    new_words=a.replace("山寨","**")
    return new_words
result=words("这个手机是山寨版的吧")
a=input("请输入字符串")
print(result)
"""
"""
#14.输入的圆柱体的底面半径和高，计算圆柱体的表面积和体积
def yuan(r,h,pi=3.14):
    biao=float(2*pi*r*r+2*pi*r*h)
    ti=float(pi*r*r)
    return biao,ti
x = float(input("请输入圆柱体的底面半径"))
y = float(input("请输入圆柱体的高"))
result=yuan(x,y)
print(f"圆柱体体积为{result[0]:.2f},圆柱体表面积为{result[1]:.2f}")
"""


"""
#15.可以接收任意多个数，返回的是一个元组
def cacluate(*args):
    ave=sum(*args)/len(*args)
    up_num=[]
    for i in args:
        if i>ave:
            up_num.append(i)
    return ave,up_num
print(cacluate(1,2,3,4,5))
"""

"""
#16.输入字符串统计大小写数量    
def fun(string):
    da=0
    xiao=0
    for i in string:
        if i.isupper():     #islower判断小写
            da+=1
        else:
            xiao+=1
    return da,xiao
da,xiao=fun("FHKJkhfksjdhkhJFSHK")
print(f"大写字母有{da}个，小写字母有{xiao}个")
"""


"""
#17.使用递归函数，实现计算任何一个数的阶乘
def fun(num):
    if num==1:
        return 1
    else:
        return num*fun(num-1)
x=int(input("请输入一个整数"))
result=fun(x)
print(f"{x}的阶乘为:{result}")
"""

"""
#18.使用递归函数，输出斐波那契序列的第n项
def feb(x):
    if x<2:
        return 1
    else:
        return feb(x-1)+feb(x-2)
num=int(input("请输入求斐波那契数列的第几项？"))
result=feb(num)
print(f"第{num}项的值为:{result}")
"""

"""
#19.售货
def all_goods():    #饮品信息
    goods={"可口可乐":2.5,"百事可乐":2.5,"冰红茶":3,"脉动":3.5,"果缤纷":3,"绿茶":3,"茉莉花茶":3,"尖叫":2.5}
    return goods
def show_goods():   #展示饮品信息
    for x,y in all_goods().items():
        print(f"{x}:{y}元")
def total(good_dict):
    count=0
    for name,num in good_dict.items():
        total_money=all_goods()[name]*num
    #总金额
        count+=total_money
    print("需要支付金额:",count,"元")
def main():
    goods_dict={}
    print("饮品自动售货机")
    show_goods()
    #循环选购商品
    print("输入q完成购买")
    while True:
        goods_name=input("请输入购物的商品:")
        if goods_name=='q':
            break
        if goods_name in [g for g in all_goods().keys()]:
            gnum=input("请输入购买数量:")
            if gnum.isdigit():#判断输入数据是不是数字
                goods_dict[goods_name]=int(gnum)
            else:
                print("商品数量不合法")
        else:
            print("请输入本店含有的商品名")
        calutotal(goods_dict)#调用计算总价的函数   传递购买的商品字典
def calutotal(gc): #传递购买的商品字典
    sum=0#统计商品的总价
    for x,y in gc.items():  #遍历购买的商品字典，x是商品名称，y是商品价格
        total=all_goods()[x]*y      #返回商品的单价 单个商品的总价=单价*数量
        sum+=total
        print(f"需要支付的金额为:{sum}元")
if __name__=="__main__":
    main()
"""


#学生管理系统
student=[]  #新建列表保存所有学生信息，每个信息存储在字典变量中
def print_menu():
    print("="*30)
    print("学生管理系统 v10.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询所有学生信息")
    print("0.退出系统")
    print("="*30)
def main():
    while True:
        print("调用功能菜单")
        key=input("请输入功能对应的数字") #获取用户输入的数字
        if key=='1':                  #获取用户输入的序号
            print("添加学生信息")
            add()                     #调用添加函数
        elif key=='2':
            print("删除学生信息")
        elif key=='3':
            print("修改学生信息")
        elif key=='4':
            print("查询所有学生信息")
            search()
        elif key=='0':
            quit_confirm=input("真的要退出吗?y/n").lower()    #lower()能强制转换为小写
            if quit_confirm=='y':
                print("谢谢使用")
                break
            elif quit_confirm=='n':
                continue
        else:
            print("输入错误")

def add():          #添加学生信息的函数
    name=input("请输入学生姓名")
    sex=input("请输入学生性别")
    tel=input("请输入联系方式")
    studic={"姓名":name,"性别":sex,"电话":tel}
    student.append(studic)
    print("添加成功")
def search():       #查询所有学生记录函数
    print("学生的信息如下:")
    print("="*40)
    print("学号\t姓名\t性别\t联系方式")
    num=0
    for i in student:       #i代表每个学生的各种信息
        num+=1
        print(f"{num}\t{i['姓名']}\t{i['性别']}\t{i['电话']}")
def delstudent():
    name=input("请输入你要删除的学生姓名")
    flag=False
    for stu in student:
        if name==stu['姓名']:
            student.remove(stu) #删除学生记录
            flag=True
            print(f"恭喜你，成功删除{name}学生")
            break
    if flag==False:
        print("你输入的学生姓名不存在")
def change():
    name=input("请输入要修改的学生姓名")
    for a in student:
        if name==a:
            newname=input("请输入要修改的学生姓名:")
            flag = False    #代表不存在这个人的记录
            for stu in student:
                if name == stu['姓名']:
                    newname=input("请输入新的姓名")
                    newsex=input("请输入新的性别")
                    newtel=input("请输入新的电话")
                    stu.update(姓名=newname,性别=newsex,电话=newtel)
                    flag=True
                    print("修改信息成功")
                    break
            if flag==False:
                print("对不起，没有你要修改的名字")

main()
























