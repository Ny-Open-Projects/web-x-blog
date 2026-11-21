"""and/or 的短路字节码与操作数返回语义。"""
import dis


def pick(a, b):
    return a or b


if __name__ == "__main__":
    dis.dis(pick)                      # 看 JUMP_IF_TRUE_OR_POP

    print("0 and 1/0 =", 0 and 1 / 0)          # 0,右侧不求值
    print("[] or 'default' =", [] or "default")  # 返回操作数本身
    print("0 or '' =", repr(0 or ""))          # 空串,假值陷阱
    print("None or 0 =", repr(None or 0))      # 0

    x = None
    print("x is None 判缺失:", "default" if x is None else x)
