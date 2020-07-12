
list_w=[1,5,4,6,8]
#list_w.append(0) #在最后一位追加
#list_w.insert(0, 4) #在给定位置添加元素
#list_w.remove(4)
#删除列表里面给定位置的元素并返回他，如果没有给定位置，list_w（）将会删除并返回列表中的最后一个元素
#list_w.pop(0)
#list_w.sort(reverse=True) #排序 加 reverse=True 从大到小  不加从小到大
#倒序排列
list_w.reverse()

print(list_w)

a={} #{}里面是空则是字典
b=set()
c={1} ##{}里面不是空则是集合
d=()
e=[]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#集合
f={1,2,3,6}
e={1,4,5,8}
#两个集合的并集
print(f.union(e))
#两个集合的交集
print(f.intersection(e))
#两个集合的差集
print(f.difference(e))
#集合添加
f.add("v")
print(f)

#列表推导式,会去重
print({i for i in "asdgdfwwersdfgergdsfg"})


#字典  可以两种写法
hogwarts_dict = {"a":1,"b":2}
hogwarts_dict2=dict(a=1,b=2)
print("hogwarts_dict",hogwarts_dict)
print(type(hogwarts_dict))
print("hogwarts_dict2",hogwarts_dict2)
print(type(hogwarts_dict2))

print(hogwarts_dict.keys())
print(hogwarts_dict.values())

#pop会删除key=a 的键值对，并返回a的值1
print(hogwarts_dict.pop("a"))
print(hogwarts_dict)
#返回被删除的键值对
print(hogwarts_dict2.popitem())
#删除上边执行的键值对后，还剩的元素
print(hogwarts_dict2)
