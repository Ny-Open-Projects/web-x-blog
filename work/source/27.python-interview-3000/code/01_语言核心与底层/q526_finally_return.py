def trap():
    try:
        return "from try"
    finally:
        return "from finally"         # 覆盖 try 的返回值

def swallow():
    try:
        raise ValueError("boom")
    finally:
        return "exception eaten"      # 异常被 return 静默终结

def rethrow_with_finally():
    try:
        raise ValueError("real")
    finally:
        print("finally runs during unwind")   # 清理:finally 的正职

if __name__ == "__main__":
    print(trap())
    print(swallow())
    try:
        rethrow_with_finally()
    except ValueError as e:
        print("propagated:", e)
