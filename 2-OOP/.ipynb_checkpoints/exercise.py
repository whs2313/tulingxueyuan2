'''
输入一个三位数与程序随机数比较大小
1如果大于程序随机数，则分别出这个三位数个位\十位\百位
2如果等于程序随机数，则提示中奖，记100分
3如果小于程序随机数，则将120个字符输入到文本文件中
（规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字）
'''
import random
import math

def line():
    # 定义一个空字符串用于拼接字符
    str_num = ""
    # 循环前四个随机字母（用ascii码对应的值来随机再转换位字母）
    for i in range(4):
        #随机小写字母ascii值
        num1 = random.randrange(97,123)
        #将ascii值转换位字母
        str_s = chr(num1)
        #一次拼接得到的随机字母
        str_num = str_num + str_s

    for i in range(8):
        num = random.randrange(0,10)
        str_num = str_num +str(num)
    return str_num
#输入函数
num = input("请输入一个三位数：")
#程序随机数
random_num = random.randrange(100,1000)
if num.isdigit() and 100 < int(num) <= 999: # 输入的函数返回的是字符串，需要强制类型转换
    num = int(num)
    random_num = int(random_num)
    #判断随机数与输入的大小
    if num > random_num:
        #求百位数字方法：地板除100或用数学模块floor()函数
        bai = num//100
        #求十位数字方法：先把三位数字取100余数，再地板除
        shi = (num%100)//10
        #求个位数的方法：直接取10的余数
        ge = num%10
        print("你输入的数比随机数大，程序随机数是",random_num)
        print("你输入的数的百位是{0}，十位是{1}，个位是{2}".format(bai,shi,ge))
    if num == random_num:
        print("你中奖了",random_num)
    if num < random_num:
        #由于120个字符，每行12个可知只需存入10行就可以
        for i in range(10):
            str_line=line()
            #print(str_line)
            #执行文件存入操作
            with open('str_num.txt',"a") as f:
                f.write(str_line+"\n")
else:
    print("请按规定输入")


