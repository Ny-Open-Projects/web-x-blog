"""is 的缓存边界:常量折叠、驻留时机与跨编译单元失配。"""


def same_unit_folding():
    a = "a b" + "c"      # 同一编译单元:常量表达式编译期折叠成 "a bc"
    b = "a bc"
    return a is b        # 折叠后指向同一常量,True(实现细节,勿依赖)


def cross_unit():
    # 模拟两个编译单元:各自 exec 编译一次
    unit_a, unit_b = {}, {}
    exec("v = 'a b' + 'c'", unit_a)
    exec("v = 'a bc'", unit_b)
    return unit_a["v"] == unit_b["v"], unit_a["v"] is unit_b["v"]


def runtime_values():
    parts = ["a b", "c"]
    a = "".join(parts)   # 运行时拼接,结果不一定命中驻留
    return a == "a bc"   # 相等性判断永远安全


def small_int_cache():
    a, b = 256, 128 + 128
    c, d = 257, 128 + 129
    return a is b, c is d    # -5..256 是实现缓存区间;同单元常量也会折叠


def big_int():
    base = 1000
    a, b = base * 10, base * 10   # 运行时乘法,各自新建大整数对象
    return a == b, a is b


if __name__ == "__main__":
    print("同单元常量折叠 a is b:", same_unit_folding())
    eq, ident = cross_unit()
    print("跨编译单元:== 为", eq, "| is 为", ident)
    print("运行时拼接只谈相等:", runtime_values())
    si = small_int_cache()
    print("256 命中缓存:", si[0], "| 257 同单元折叠:", si[1])
    bi = big_int()
    print("运行时大整数 == 为", bi[0], "| is 为", bi[1])
