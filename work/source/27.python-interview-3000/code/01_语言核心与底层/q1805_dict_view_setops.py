"""dict 视图的集合运算:keys/items 视图的交并差。"""


def diff_views(old, new):
    ko, kn = old.keys(), new.keys()
    return {
        "added": sorted(kn - ko),
        "removed": sorted(ko - kn),
        "kept": sorted(ko & kn),
    }


def changed_values(old, new):
    return sorted(k for k in old.keys() & new.keys() if old[k] != new[k])


def values_not_setlike():
    return hasattr({"a": 1}.values(), "__sub__")


def items_setlike():
    a = {"x": 1, "y": 2}
    b = {"x": 1, "z": 3}
    return sorted(a.items() & b.items())     # 键值对元组的集合交集


if __name__ == "__main__":
    old = {"a": 1, "b": 2, "c": 3}
    new = {"b": 20, "c": 3, "d": 4}
    print("视图差集与交集:", diff_views(old, new))
    print("值变化的键:", changed_values(old, new))
    print("values 视图支持集合运算:", values_not_setlike())
    print("items 视图交集:", items_setlike())
