base = {"a": 1, "b": 2, "c": 3}
override = {"b": 20, "d": 4}

if __name__ == "__main__":
    print(base | override)                # 右侧赢,新字典
    print({**base, **override})           # 等价,可混入更多字典
    print(override | base)                # 方向反了结果不同

    m = base.copy()
    result = m.update(override)           # 原地:返回 None
    print(result, m)
    print("base unchanged:", base)

    print(list((base | override).keys())) # 冲突键保持 base 的位置
    print(list((override | base).keys()))
