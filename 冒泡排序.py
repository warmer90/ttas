
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#list1 = [10, 55, 336, 54, 99, 65, 48]

#总循环次数,排序次数
for i in range(len(list1)-1):
    #对比次数
    for j in range(len(list1)-i-1):
        # 每两个相邻位置对比大小，如果后一位比前一位小就交换位置
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
            print(list1)
print(list1)