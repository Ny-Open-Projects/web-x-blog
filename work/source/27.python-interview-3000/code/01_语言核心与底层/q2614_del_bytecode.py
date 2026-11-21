"""del 的字节码家族:DELETE_FAST、DELETE_NAME、DELETE_DEREF 与容器形态。"""
import dis

module_var = 1


def del_fast():
    a = 1
    del a                       # DELETE_FAST
    return a                    # 已未绑定


def make_closure():
    x = 10

    def inner():
        nonlocal x
        del x                   # DELETE_DEREF
    return inner


def del_global():
    global module_var
    del module_var              # DELETE_GLOBAL


if __name__ == "__main__":
    print("del 局部变量:")
    dis.dis(del_fast)

    print("del 闭包变量:")
    dis.dis(make_closure())

    lst = [1, 2, 3]

    class Box:
        pass

    b = Box()
    b.v = 1

    def del_container():
        del lst[0]              # DELETE_SUBSCR
        del b.v                 # DELETE_ATTR
    dis.dis(del_container)
