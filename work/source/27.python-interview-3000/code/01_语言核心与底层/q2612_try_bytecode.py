"""3.9 的异常处理块栈:SETUP_FINALLY 到 RERAISE 的完整链路。"""
import dis


def tri(x):
    try:
        v = int(x)
    except ValueError:
        v = 0
    finally:
        print("done")
    return v


if __name__ == "__main__":
    tri("42")
    tri("x")
    dis.dis(tri)
