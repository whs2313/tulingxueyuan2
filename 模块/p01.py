
# 包含一个学生类
# 一个sayhello语句
# 一个打印语句
class Student():
    def __init__ (self,name="Noname",age=18):
        self.name = name
        self.age = age
    def sayHello(self):
        print("Hello,{0}!".format(self.name))
def say ():
    print("Hi,欢迎来到铜陵学院！")

# 此判断语句建议一直作为程序的入口
if __name__ =='__main__':

    print("我是模块01呀，你特么导入我干毛")