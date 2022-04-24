#用户登陆需求
"""
count=3
for i in range(1,4):
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "aaa" and password == "123":
        print("输入正确")
        break
    else:
        count-=1
        print("登陆失败\n还有%d次机会"%count)
if count<=0:
        print("登陆次数超过三次，系统被锁定")
"""

#字符串对齐
"""
str ="学生管理系统"
print(f"{str.center(20, )}")
print(str.center(20,'*'))
print("{0}".format(str.ljust(30,"*")))
print("%s"%(str.rjust(30,"*")))
print("%s"%(str.rjust(30,"@")))
"""


#练习10以内加法
"""
import random
#导入随机数模块
count=0
#答题次数
dui=0
#答对次数
print("温馨提示:退出请输入exit")
while True:
    num1 = random.randint(0,10)
    num2 = random.randint(0, 10)
    print(f"{num1}+{num2}=?")
    result = input("请输入你的答案:")
    if result =="exit":
        break
    else:
        count+=1
        if int(result) == num1+num2:
           print("恭喜你答对了")
           dui+=1
        else:
          print("答错了")
print("一共答了{0}个题，答对{0}个题，正确率为:{2:.2f}".format(count,dui,dui/count*100))
"""

#一正一负累加
"""
f=0
a=0
for i in range(1,21):
    if i%2==1:
        f-=i
    if i%2==0:
        a+=i
print("累加和为:%d"%(f+a))
"""

#字符串函数的作用
"""
hz,xx,dx,sz,qt=0,0,0,0,0
string="通知：ZJ20220201花园宝宝项目和SZ20191008皮卡丘\n"\
       "工程由张经理负责，电话为：18609892341,将在明天晚8：00\n"\
       "在Tencent腾讯视频中进行预算会议。"
for i in string:
       if string>="\u4e00" and string<="\u9fa5":
              hz+=1
       elif i.issuper():
              dx+=1
       elif i.islover():
              xx+=1
       elif i.isdigit():
              sz+=1
       else:
              qt+=1
print("通知如下:\n"+string)
print("汉字%d个，小写字母%d个，大写字母%d个,数字%d个，其他字符%d个"%hz,xx,dx,sz,qt)
"""


#列表练习
"""
import math
lx =[34,65,87,98,12,57,79,37,86,89,93,91,75]
print(type(lx))
#1.输出数据类型
# for i in lx:
#        print(lx)
#2.循环输出列表数据
print(lx[::1])
#3.切片方式输出列表中数据
print(lx[::-1])
#4.切片方式逆序输出列表中数据
print("偶数",lx[::2])
#5.切片方式输出偶数位置的元素数据
print(lx[1::2])
#6.切片方式输出奇数位置的元素数据
print(lx[3:9])
#7.输出列表3-8位的数据
count=0
print(len(lx))
for i in (lx):
    count+=1
print("元素个数为:%d"%count)
#8.输出列表中元素的个数
print("最大值为:",max(lx),"最小值为:",min(lx),"所有元素之和为:",sum(lx))
#9.输出列表中最大值，最小值，以及所有元素的和
print("空列表",lx[::])
#10.切片方式返回空列表
print(lx[3:-6:1])
#11.取位置3在位置-5的左侧，正向切片的数据
print(lx[3:-16:-1])
#12.取位置3在位置-15的右侧，-1表示反向切片的数据
lx[len(lx):]=[100]
print("在尾部追加元素",lx)
lx.append(100)
print("用append追加元素",lx)
#13.在列表尾部追加元素100，并输出
lx[0:0]=[23,30]
print("头部追加元素",lx)
#14.在列表头部插入[23,30],并输出  lx[0:3]表示用[23,30]覆盖列表前三项
lx.insert(6,50)
print("在第五个位置插入50",lx)
#15.在第五个位置插入50，并输出  列表名.insert(项,插入的数据)
lx[0:5]=[5]
print("前四个元素改成5",lx)
#16.把前四个元素都改成5，并输出
del lx[0:4:]
print("删除前四个元素",lx)
#17.删除前四个元素，并输出
del lx[::2]
print("隔一个删除列表中的元素",lx)
#19.隔一个删除列表中的元素 数字名[前闭:后开:间隔数]
lx.sort()
print("排序输出",lx)
#20.把现在列表中的数据排序输出
print("倒序输出",lx[::-1])
#21.倒序输出列表中的数据      用切片倒序输出，
lx.pop()
print("删除最后一个元素",lx)
#22.删除列表的最后一个元素
"""


#列表练习
"""
ltx=["邓论","欧阳娜娜","吉克隽逸","宋祖儿","任嘉伦","宋亚轩"]
#del ltx[0:3]   #直接删除前几项，再输出后三项
print(ltx[3:6]) #用切片输出后三项
print("输出1-3项数据",ltx[1:4])
#输出1-3项数据
print("输出0-2项数据",ltx[0:3])
#输出0-2项数据
print("输出2-6项数据",ltx[2:7])
#输出2-6项数据
print("输出列表4-5位数据",ltx[4:6])
#输出列表4-5位数据
print("倒序输出所有数据",ltx[::-1])
#倒序输出所有数据
ltx.reverse()
ltx.insert(3,'杨幂')
print("在第三位后插入杨幂",ltx)
#在第三位后插入“杨幂”
ltx.reverse()       #先把列表翻转，不能直接输出翻转列表，没有返回值
print(ltx[0:7:3])   #在输出选出的几项
ltx.append("肖战")
print(ltx)
#在尾部添加“肖战”
"""

#元组练习
"""
tp=(98,43,12,65,78,90,234,65,16,65,98)
print(tp)
#1.输出元组的数据
print("元组的数据类型为:",type(tp))
#2.查看该数据的数据类型
lie=list(tp)
#3.转换列表赋值一个列表变量 元组不能修改元素
print("转换后的列表",lie)
#4.输出转换列表变量   元组转换为列表想再进行操作需要赋给一个变量
print("查看当前列表的数据类型",type(list(tp)))
#5.查看当前列表的数据类型
del lie[4:5:]
print(lie)
#6.删除列表中的第四个元素
print("列表所有数据:",lie)
#7.输出列表所有数据
print("查看元组第三个元素",lie[2])
#8.查看元组第三个元素
print("最大值:",max(tp),"最小值",min(tp))
#9.查看元组最大值和最小值并输出
print("最后一个元素的值:",tp[-1])
#10.查看元组最后一个元素的值
count=0
for i in (tp):
    if i==65:
        count+=1
print("65出现的次数为:",count)
#11.查看'65'出现的次数
suoyin=0
for j in (tp):
        if j!=234:
            suoyin+=1
        else:
            suoyin+=1
            print("234出现的索引为:",suoyin)
#12.查看元组中'234'出现的索引
jilu=-1
for k in (tp):
    jilu+=1
print("元组中有%d个记录"%jilu)
#13.查看元组中有多少个记录
print("排序后的元组为:",sorted(tp))
#14.对元组进行排序输出
lie.append(520)
print("将'520'追加到列表尾",lie)
#15.将'520'追加到列表尾部
"""

#集合练习
"""
st=set()
print("集合为:",st)
#创建空集合
print(type(st))
#输出数据类型
st=set(range(2,9))
print(st)
#使用range生成2到9之间的序列
st.add(13)
print(st)
#在集合中添加元素13
new=set([14])
st.update(new)
print("修改元素14",st)
#修改元素2,14   update()用一个旧集合和新集合做对比，共有的元素只出现一次，没有则补上
st.remove(5)
print("删除元素5",st)
#删除元素5
st.pop()
print("弹出的元素为:",st.pop())
print("弹出后的集合为:",st)
#弹出第一个元素    当集合是由列表和元组组成时、set.pop()从左边删除元素
"""

#字典练习
dl={"书名":"python 程序设计","价格":"35.6","出版社":"人民邮电出版社"}
print("输出字典所有数据",dl)
#1.输出字典所有数据
print("输出字典的数据类型",type(dl))
#2.输出字典的数据类型
print("书名：",dl["书名"],"价格",dl["价格"])
#3.输出书名，价格
print("把字典的key转换为列表输出",list(dl.keys()))
#4.把字典的key转换为列表，输出
print("把字典的所有数据以列表输出",dl.items())
#5.xxx.items()以列表方式返回可遍历的元组数据
lt=list(dl.values())
print("转换为列表后的",lt[0])
for x,y in dl.items():
    print(y)        #第二种方法，用items输出values内容
    break
#6.输出转换后列表中的"python 程序设计"   先将所有的值转换为列表给lt，再输出第一位
del dl["价格"]
print('删除"价格"信息后输出',dl)
#dl.pop("价格")            #用pop来指定删除一个键 popitem()随机删除一个键
#7.删除"价格"信息并输出
dl["出版社"]="21世纪出版社"
print('修改"出版社"后输出',dl)
#8.修改出版社后输出
dl["IBSN"]="6789392432"
print("添加版号后:",dl)
dl.update(IBSN=6789392432)  #使用update添加元素,键名不用加引号,值如果是数字可以不加，字符串需要加引号
#9.添加版号后输出
dl["序号"]="001"
print("插入序号后:",dl)
dl["出版社"]="清华出版社"
#10.添加序号后输出
del dl["出版社"]
print("弹除出版社",dl)
#11.弹出出版社



#p70课后第一题
"""
li_num1=[4,5,2,7]
li_num2=[3,6]
li_num1.extend(li_num2)
#extend()将两个列表合并为一个列表
li_num3=sorted(li_num1)
#sorted()按升序排列
i=0
temp=0
for i in li_num3:
    if li_num3[i]<li_num3[i+1]:
        temp=li_num3[i]
        li_num3[i]=li_num3[i+1]
        li_num3[i+1]=temp
print(li_num3)
"""









