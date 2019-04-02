#   5. 修改原<<学生信息管理程序>> 将程序的整体功能封装为两个函数
#      1) 编写函数input_student() 获取学生信息,以学生姓名为
#         空输入结束,返回学生信息的字典的列表,列表同之前列表
#         如:
#           L = input_student()
#           print(L) #[{'name': 'xiaozhang', ...},{...}]
#      2) 编写函数output_student(L) 以表格的形式打印L列表中的
#        学生信息
#         如:
#           output_student(L)  # 打印表格


def input_student():
    '''此函数录入学生信息,最后返回学生信息的字典的列表'''
    L = []  # 先创建一个列表容器,准备存放字典
    while True:
        n = input("请输入姓名: ")
        if not n:  # 如果n绑定空字符串,则退出录入信息
            break
        a = int(input("请输入年龄: "))
        s = int(input("请输入成绩: "))
        d = {}  # 创建字典,准备存放学生信息
        d['name'] = n
        d['age'] = a
        d['score'] = s
        L.append(d)
    return L

def output_student(L):
    '''以表格形式打印学生信息'''
    print("+--------------+----------+----------+")
    print("|    姓 名     |  年 龄   |  成  绩  |")
    print("+--------------+----------+----------+")
    for d in L:
        sn = d['name']  # sn绑定姓名的字符串
        sa = str(d['age'])  # sa 绑定年龄的字符串
        ss = str(d['score'])  # ss 绑定成绩的字符串
        s = "|%s|%s|%s|" % (sn.center(14),
                            sa.center(10),
                            ss.center(10))
        print(s)
    print("+--------------+----------+----------+")

L = input_student()
print(L)
output_student(L)  # 打印表格
