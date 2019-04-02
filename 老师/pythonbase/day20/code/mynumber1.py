# mynumber1.py


# 此示例示意让自定义的类使用运算符进行操作
class MyNumber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return "MyNumber(%d)" % self.data
    
    def __add__(self, other):
        print('__add__方法被调用')
        v = self.data + other.data
        return MyNumber(v)  # 创建一个新对象并返回

    def __sub__(self, rhs):
        return MyNumber(self.data - rhs.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)
n3 = n1 + n2  # 等同于 n3 = n1.__add__(n2)
print(n1, '+', n2, '=', n3)

print(n1, '-', n2, '=', n1 - n2)





