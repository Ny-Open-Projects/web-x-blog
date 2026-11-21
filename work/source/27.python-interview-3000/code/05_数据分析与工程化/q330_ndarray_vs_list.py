try:
    import numpy as np
except ImportError:
    print("该题演示需要第三方库 numpy:pip install numpy,原理见正文")
    raise SystemExit(0)

def main():
    py_list = [1, 2, 3, 4]
    arr = np.array([1, 2, 3, 4])
    print(type(py_list), type(arr), arr.dtype)
    print(arr * 2)                # 向量化:逐元素
    print(py_list * 2)            # list:重复拼接,语义完全不同
    print(arr + 1)                # ndarray 支持
    try:
        py_list + 1
    except TypeError as e:
        print("expected error:", e)
    print(arr.sum(), arr.mean(), arr.max())   # 内置聚合方法

if __name__ == "__main__":
    main()
