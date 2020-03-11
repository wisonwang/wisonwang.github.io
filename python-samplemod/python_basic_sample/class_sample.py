# -*- coding: utf-8 -*-

class Student(object):
    # 这里定义的定义 会同事定义class和object属性
    fname = "??"
    sname = "????"
    age = 12
    addr = "......"
    phone = "1000000"

    def __init__(self, fname: str, sname: str, age: int, **kw):
        """初始化方法"""
        self.fname = fname
        self.sname = sname
        # class 属性可以作为默认值
        self.age = kw.get("age", self.age)
        self.phone = kw.get("phone", self.phone)
        self.addr = kw.get("addr", self.addr)
        # sex只是对象的属性，不是class的属性
        self.sex = kw.get("sex", 0)

    def echo(self):
        print(str(self))

    @classmethod
    def echo_class(cls):
        print(cls, cls.fname, cls.sname, cls.age, cls.addr, cls.phone)

    def __str__(self):
        """当对象转化成字符串时回调用对象的__str__方法"""
        return str({
            "fname": self.fname,
            "sname": self.sname,
            "age": self.age,
            "addr": self.addr,
            "phone": self.phone,
            "sex": self.sex
        })


Student.echo_class()

s1 = Student("vincent", "wang", 32, sex=1)

s1.echo()

Student.addr = "??????xxxx"
Student.echo_class()

s2 = Student("vincent", "wang", 32, sex=1)

# 可以看到s2和s1的addr属性是不一致的，原因是对象在初始化前，首先拷贝的类的属性和值
s2.echo()
