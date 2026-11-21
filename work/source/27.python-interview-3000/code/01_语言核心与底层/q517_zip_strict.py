import sys

names = ["a.txt", "b.txt"]
sizes = [100, 200, 300]                       # 长度不齐的脏数据

if __name__ == "__main__":
    for name, size in zip(names, sizes):      # 默认:静默丢掉 300
        print("truncating:", name, size)

    if sys.version_info >= (3, 10):
        try:
            for name, size in zip(names, sizes, strict=True):
                print("strict:", name, size)
        except ValueError as e:
            print("strict caught:", e)
    else:
        print(f"该特性需要 Python 3.10+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")

    from itertools import zip_longest
    for name, size in zip_longest(names, sizes, fillvalue=0):
        print("longest:", name, size)
