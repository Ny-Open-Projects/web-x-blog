import sys
import threading

# 判断运行在哪种构建:free-threading 构建下 sys._is_gil_enabled() 可为 False
print("version:", sys.version)
is_ft = getattr(sys, "_is_gil_enabled", None)
if is_ft is not None:
    print("GIL enabled:", is_ft())
else:
    print("no _is_gil_enabled -> 普通含 GIL 构建")

# 无论哪种构建,这段 check-then-act 都不是原子的
# 在 free-threading 下竞争窗口更大,正确做法是加锁
lock = threading.Lock()
seen = set()

def check_and_add(n):
    with lock:                    # 去掉锁,free-threading 下可能出现覆盖
        seen.add(n)

threads = [threading.Thread(target=check_and_add, args=(i % 50,)) for i in range(1000)]
[t.start() for t in threads]
[t.join() for t in threads]
print("unique:", len(seen))
