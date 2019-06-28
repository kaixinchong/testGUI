#字符串练习

import time

li = []
time01=time.time()
for i in range(1000000):
    li.append('abc')
a="".join(li)
time02=time.time()
print("运算时间"+ str(time02-time01))

    
