import sys
import threading

counter = 0

def worker(n):
    global counter
    for _ in range(n):
        counter += 1   # 字节码层面是 读-加-写 三步,并不原子

if __name__ == "__main__":
    print(sys.getswitchinterval())  # 默认 0.005 秒
    threads = [threading.Thread(target=worker, args=(100_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(counter, "!= 400000 时说明竞态存在")
