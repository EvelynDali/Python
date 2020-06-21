import time
for i in range(4):
    print(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(time.time()))))[-2:])
    time.sleep(1)
