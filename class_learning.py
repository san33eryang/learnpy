# -*- coding: utf-8 -*

class Student(object):
    def __init__(self,name,score):
        self.__name=name       #内部变量访问
        self.__score=score     #内部变量访问
    def get_scoretype(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <=score<=100:
            self.__score=score
        else:
            print('error')

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('dog is running')
class Cat(Animal):
    def run(self):
        print('cat is running')
def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):   # 多态的好处，可以直接继承
    def run(self):
        print('tortoise is running slowly')

class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x

if __name__ == '__main__':
    bar=Student('Bart',99)
    lisa=Student('Lisa',66)
    zip=Student('Zipp',50)

    print(bar.get_name(),bar.get_score(),bar.get_scoretype())
    # update bar's score
    bar.set_score(5)
    print(bar.get_name(),bar.get_score(),bar.get_scoretype())

    #如果内部并没有设置任何访问数据的方法，可用_Student__name来访问
    print(bar._Student__name)


run_twice(Dog())
run_twice(Animal())
run_twice(Tortoise())

obj=Myobject()
print(hasattr(obj,'x')) # if including the x
print(getattr(obj,'x'))
print(setattr(obj,'y',19)) # setup a type for obj
print(getattr(obj,'y'))

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count +=1

# 测试:
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
