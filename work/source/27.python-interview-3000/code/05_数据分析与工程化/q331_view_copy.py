try:
    import numpy as np
except ImportError:
    print("该题演示需要第三方库 numpy:pip install numpy,原理见正文")
    raise SystemExit(0)

def main():
    a = np.arange(6)
    v = a[2:5]              # 切片 -> 视图
    c = a[2:5].copy()       # 显式副本
    v[0] = 99
    print(a)                # a 被改:视图共享内存
    c[0] = -1
    print(a)                # a 未变
    print("view base is a:", v.base is a, "| copy base:", c.base is not None)
    # fancy 索引返回副本,不是视图
    f = a[[0, 1]]
    f[0] = 777
    print(a[0])             # 仍为 99 -> fancy 索引是副本

if __name__ == "__main__":
    main()
