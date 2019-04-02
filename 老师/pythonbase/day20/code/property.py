# property.py

class Student:
    def __init__(self, score=0):
        self.__score = score

    def set_score(self, v):
        '''setter'''
        assert 0 <= v <= 100, "成绩超出范围"
        self.__score = v

    def get_score(self):
        '''getter'''
        return self.__score

s = Student()
print(s.get_score())
s.set_score(99)
# s.set_score(1000)  # 报错
print(s.get_score())

# print(s.score)  # 取值
# s.score = 99    # 正确赋值
# s.score = 10000  # 赋值报错
# print(s.score)
