# file_open.py


# 此示例示意在文件操作过程中,用with来代替
# try-finally 句来关闭文件
try:
    # fr = open('myfile.txt', 'rt')
    with open('myfile.txt', 'rt') as fr:
        s = fr.readline()
        print("第一行的长度是:", len(s))
        int(input("请输入整数: "))  # 可能发生异常
except OSError:
    print("文件打开失败")

