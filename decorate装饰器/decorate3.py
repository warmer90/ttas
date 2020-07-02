"""
装饰器何时执行
"""
regitry=[]
def register(func):
    print("register is ",func)
    regitry.append(func)
    return func
@register
def f1():
    print("f1")
@register
def f2():
    print("f2")

def f3():
    print("f3")

if __name__ == '__main__':
    print("running main()")
    print("regitry->",regitry)
    f1()
    f2()
    f3()




