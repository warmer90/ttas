"""
定义一个函数，专门处理日志，日志处理完成之后再执行真正的业务代码
"""
def foo():
    print("this is a func ,foo")

def foo2():
    print("this is a func ,foo2")

#传入函数对象func
def log(func):
    print("{} is running".format(func))
    func()

log(foo)
log(foo2)

#装饰器  用闭包函数
def log2(func):
    def log(a,b):
        print("{} is running".format(func))
        func(a,b)
    return log
@log2
def foo3(a,b):
    print("this is a func ,foo3")
    print(a+b)

foo3(1,2)