import time
def bar():
    scale = 50
    print("\033[32m打开进程中...\033[0m".center(65, " "))
#    start = time.perf_counter() 开始时间
    for i in range(scale+1):
        a = '*' * i
        b = '.' * (scale - i)
        c = i/scale*100
#        dur = time.perf_counter() - start  开始时间减去现在时间 = 已用时间
        print("\r[{}->{}]{:^3.0f}%".format(a,b,c),end="")  #去掉dur变量引用

        time.sleep(0.01)
