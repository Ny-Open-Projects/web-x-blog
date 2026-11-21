"""cmp_to_key:比较器排序与「多次稳定排序」替代方案的对照。"""
import functools

rows = [("dev", "10"), ("qa", "9"), ("dev", "2"), ("ops", "100")]


def by_dept_then_num(a, b):
    """部门升序;同部门内按数值降序(字符串没法取负,必须比较器)。"""
    if a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    return int(b[1]) - int(a[1])


if __name__ == "__main__":
    print("cmp_to_key:", sorted(rows, key=functools.cmp_to_key(by_dept_then_num)))

    # 替代方案:利用 sorted 稳定性,从次要键到主要键排两遍
    staged = sorted(rows, key=lambda r: -int(r[1]))
    staged = sorted(staged, key=lambda r: r[0])
    print("稳定排序:", staged)

    # 数值序排字符串,key 一层就够,不必上比较器
    nums = ["10", "9", "2"]
    print("数值序:", sorted(nums, key=int))
