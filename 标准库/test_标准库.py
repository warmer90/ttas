import os
print(os.path)
print(os.path.exists("b"))
#判断是否存在文件
if not os.path.exists("b"):
    os.mkdir("b")

if not os.path.exists("b/test.txt"):
    #创建文件
    f = open("b/test.txt","w")
    f.write("hello ,os using")
    f.close()
#删除文件    
os.remove("b/test.txt")
print(os.path)