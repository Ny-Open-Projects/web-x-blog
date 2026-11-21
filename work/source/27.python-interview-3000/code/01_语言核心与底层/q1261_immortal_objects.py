import sys

if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    print("getrefcount(None) :", sys.getrefcount(None))
    print("getrefcount(True) :", sys.getrefcount(True))
    print("getrefcount(2**60):", sys.getrefcount(2 ** 60))
    x = object()
    print("plain object      :", sys.getrefcount(x), "传入即临时 +1")
    if sys.version_info >= (3, 12):
        print("3.12+ PEP 683:内置单例是不朽对象,计数恒为巨大常量")
    else:
        print("当前版本:以上是真实计数,会随全局引用增减")
