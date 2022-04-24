"""
print("你好：我是软件工程师\n"
      "姓名：爱编程\n"
      "年龄：20岁\n"
      "爱好：打篮球\n")
"""
#第六题
""""
print("未来原理科技股份有限公司\n"
      "张先生      主管\n"
      "--------------------\n"
      "手机：1868888888\n"
      "地址：北京昌平区建材城西路金燕路办公楼\n")
"""


""""
import keyword
print(keyword.kwlist)
from keyword import kwlist
print(kwlist)
"""


"""
import math
print (math.sqrt(81))
from math import sqrt
print (sqrt(81))
"""

"""
print ("          欢迎来到我行我素购物管理系统\n"
       "*************************************\n"
       "          1.客户信息管理\n"
       "          2.购物结算\n"
       "          3.真情回馈\n"
       "          4.注销\n"
       "*************************************")
"""


'''
phone = input ("请输入手机号码:")
money = input ("请输入充值金额:")
print ("您充值的手机号码是:",phone)
print
'''

''''
chang = int(input ("请输入长:"))
kuan  = int(input ("请输入宽:"))
print ("长为:",chang)
print ("宽为:",kuan)
print ("周长为:",(chang+kuan)*2)
'''#输入长方形的长和宽输出周长


'''
r =float(input("圆的半径为:"))
p =float(3.14)
print ("圆的面积为:",p*r*r)
'''#输入半径输出圆的面积

"""
print ("还需要运",int((29.5-4*3)/2.5)"次")
"""

#摄氏温度转换为开尔文温度
"""
c = float(input ("请输入摄氏度:"))
print (c,"对应的开氏温度为:",float(c+273.15))
"""


#工资计算问题
"""
money = float(input ("请输入基本工资:"))
#输入基本工资
print ("该员工的工资明细为:\n"
"*******************************")
print ("基本工资为:",money)
#输出基本工资
wu = float(money*0.4)
print ("物价津贴为:",wu)
#计算并输出物价津贴
fang = (money*0.25)
print ("房租津贴为:",fang)
#计算并输出房租津贴
print ("*******************************\n"
       "实领工资为:",(money+wu+fang))
#输出实领工资(基本工资+物价津贴+房租津贴)
"""

#输入圆柱体的半径和高求体积
"""
p = float(3.14)
#将π赋值为3.14
r = int(input("圆柱体的半径为:"))
#输入圆柱体的半径
g = int(input("圆柱体的高为:"))
#输入圆柱体的高
print ("此圆柱体的体积为:",float(p*r*r*g))
#计算圆柱体的体积(底面积×高)
"""

#输入两个值计算后输出算式
"""
a = int(input("请输入第一个数:"))
#为变量a赋值
b = int(input("请输入第二个数:"))
#为变量b赋值
print ("a 等于 ",a,"b 等于"  ,b,",a+b 的结果: ","a+b=",float(a+b))
#输出a,b,a+b的值
print ("a 等于 ",a,"b 等于"  ,b,",a-b 的结果: ","a-b=",float(a-b))
print ("a 等于 ",a,"b 等于"  ,b,",a*b 的结果: ","a*b=",float(a*b))
print ("a 等于 ",a,"b 等于"  ,b,",a/b 的结果: ","a/b=",float(a/b))
"""


#输入一个整数n,求1-n之和
"""
n = int (input ("请输入一个整数"))
sum = 0
for i in (range(n+1)):
    sum +=i
    print ("1~%d的求和结果为:%d"%(n,sum))
"""


"""
ming = "阿莫西林胶囊"
eng = "amoxicillin"
per = "白色至黄色粉末状"
print (ming,eng,per,sep="\n")   
"""
#sep用法:sep=" "默认为空格，用于设定间隔符


dan = "单号:10120014"
time = "2022-3-8"
print ("*************")
print ("名称    数量   单价    金额\n"
"金士顿U盘 1   40.00   40.00")










