try:
    import numpy as np
except ImportError:
    print("该题演示需要第三方库 numpy:pip install numpy,原理见正文")
    raise SystemExit(0)

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])          # shape (2, 3)
    b = np.array([10, 20, 30])         # shape (3,) -> (1, 3) 广播
    print(a + b)
    col = np.array([[100], [200]])     # shape (2, 1) 广播成 (2, 3)
    print(a + col)
    # 归一化:每列减去均值,广播经典用法
    print((a - a.mean(axis=0)) / a.std(axis=0))
    # 形状 (2, 3) 与 (2,) 不兼容 -> ValueError
    try:
        a + np.array([1, 2])
    except ValueError as e:
        print("expected error:", e)

if __name__ == "__main__":
    main()
