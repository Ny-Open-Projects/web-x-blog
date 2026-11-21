

def show():
    try:
        raise ValueError("boom")
    except ValueError as e:
        print("inside block:", e)
    try:
        print(e)                        # 块外:名称已被隐式删除
    except NameError as err:
        print("outside block ->", type(err).__name__)

    kept = None
    try:
        raise ValueError("persist")
    except ValueError as e:
        kept = e.with_traceback(None)   # 摘掉 traceback 再保存
    print("kept message:", kept, "| traceback detached")


if __name__ == "__main__":
    show()
