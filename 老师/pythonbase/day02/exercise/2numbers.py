#   1. 输入两个整数,分别用变量x, y来绑定
#     1) 计算这两个数的和
#     2) 计算这两个数的积

x = input("请输入第一个整数: ")
x = int(x)  # 转为整数
y = int(input("请输入第二个整数: "))

print(x, "+", y, '=', x + y)
print(x, "*", y, '=', x * y)