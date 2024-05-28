class Person:

    # sex:int范形
    def __init__(self,sex: int,age: int):
        self.sex = sex
        self.age = age

    def say(self,word):
        print('say ->{}'.format(word))


#     继承
class Man(Person):
    def __init__(self,sex: int,age: int,name='no'):
        super(Man,self).__init__(sex,age)
        # __私有属性
        self.__name = name

    # 更改name属性 get
    @property
    def name(self):
        return self.__name

    # set
    @name.setter
    def name(self,name):
        self.__name = name

    @classmethod
    def create_empty(cls,age,sex):
        return cls(age = age,sex = sex)


man = Man(sex = 1,age = 13,name = 'harder')
Man.create_empty(age = 1,sex = 1).pr
man.name = 'james'
man.say('hello')
print(man.sex)
print(man.name)

from abc import ABCMeta,abstractmethod


# 抽象类定义
class AbsFoo(metaclass = ABCMeta):
    @abstractmethod
    def foo(self):
        pass


class Foo(AbsFoo):
    def foo(self):
        print("foo")
