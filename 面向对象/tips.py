#类型提示
# 1 提前给变量一个数据类型，然后可以直接调用此数据类型的方法
# 2 没有实际改变数据类型
def excute_data(a:list)->list:
    a.sort()
    print(a)
excute_data([3,2,1])



#列表推导式
#得到数组中是偶数位数的个数

nums=[12,345,2,6,7896,65,88,66878,1125796]
list1=[]
#1，先新建一个空列表
#2。把判断循环语句按顺序放进去
#3.把append里面的内容放到最前面

list2=[i for i in nums if len(str(i))%2==0]
# for i in nums:
#     if len(str(i))%2==0:
#         list1.append(i)

print(len(list1))

print(list2)
print(len(list2))


