# with2.py

# 此示例示意将自定义的类变为环境管理器,
# 让自定义的类创建的对象能用在with语句中

class A:
    def __enter__(self):
        '''此方法必须返回由 as 绑定的对象'''
        print("A类对象已进入with语句")
        return self

    def __exit__(self, e_type, e_value, e_tb):
        '''e_type绑定异常类型,没有异常时绑定None
        e_value 绑定错误对象,没有异常时绑定None
        e_tb 绑定追踪对象,没有异常时绑定None
        '''
        print("A类对象已离开with语句")
        if e_type is None:
            print("我是没有异常时退出的with语句")
        else:
            print("有离开with语句时有异常发生")
            print(e_type)
            print(e_value)
            print(e_tb)

with A() as a:
    print("这是with语句内部的一条语句")
    int(input("请输入整数: "))

print("程序正常退出")





