from array import array
from collections import deque

if __name__ == "__main__":
    dq = deque(range(5), maxlen=5)
    dq.append(99)                         # 右进:左端自动挤出
    print(dq)
    dq.appendleft(0)                      # 左进:右端挤出
    print(dq)
    dq.rotate(2)                          # 旋转:环形缓冲语义
    print(dq)

    arr = array("i", [1, 2, 3])
    arr.append(4)
    print(arr, "itemsize:", arr.itemsize)
    try:
        arr.append(2.5)
    except TypeError as e:
        print("typed container:", e)
