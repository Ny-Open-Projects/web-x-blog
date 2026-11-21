import sys

data = [1, 2, 3]
alias = data
del data                                  # 只删名字
print("object alive via alias:", alias)

holder = {"k": [1, 2, 3]}
ref = holder["k"]
del holder["k"]                           # 删条目,对象由 ref 继续持有
print("value survives:", ref, "refcount > 1:", sys.getrefcount(ref) > 1)

nums = [0, 1, 2, 3, 4]
del nums[1:3]                             # 删切片
print("slice deleted:", nums)

def scope_demo():
    x = 1
    del x
    try:
        print(x)
    except NameError as e:
        print("unbound inside function:", e)

if __name__ == "__main__":
    scope_demo()
