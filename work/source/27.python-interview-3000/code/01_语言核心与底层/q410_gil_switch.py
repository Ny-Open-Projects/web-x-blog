import sys
import threading
import time

print("switch interval:", sys.getswitchinterval())   # 默认 0.005 秒

counter = 0
N = 200_000

def busy():
    global counter
    for _ in range(N):
        counter += 1          # 字节码级非原子:LOAD/ADD/STORE 三步

t0 = time.perf_counter()
threads = [threading.Thread(target=busy) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
print("expect", 4 * N, "got", counter, "elapsed", round(time.perf_counter() - t0, 3))
# 计数大概率不等于期望值:GIL 只保证字节码间切换,不保证复合操作原子

# 收紧切换间隔:切换更频繁,上下文切换开销上升
sys.setswitchinterval(0.0001)
counter = 0
t0 = time.perf_counter()
threads = [threading.Thread(target=busy) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
print("small interval elapsed", round(time.perf_counter() - t0, 3), "got", counter)
