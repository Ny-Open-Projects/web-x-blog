"""slice 对象是一等公民:复用、等价与 indices 求界。"""
import operator


LAST_THREE = slice(-3, None)     # 具名切片:一处定义,处处复用


def apply_slice(seq, sl):
    return seq[sl]               # 等价于 seq[sl.start:sl.stop:sl.step]


def indices_bounding():
    # slice.indices(len) 把 None 与越界折算成合法的 start/stop/step
    return slice(2, 99).indices(5), slice(-2, None).indices(5)


def equivalence_check():
    seq = list(range(10))
    manual = seq[2:8:2]
    via_obj = seq[slice(2, 8, 2)]
    return manual, via_obj, manual == via_obj


def itemgetter_family():
    seq = [10, 20, 30, 40]
    return operator.itemgetter(slice(1, 3))(seq)   # 切片也能进 itemgetter


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    print("具名切片取最后三个:", apply_slice(data, LAST_THREE))
    print("indices 求界:", indices_bounding())
    print("手工切片与 slice 对象等价:", equivalence_check())
    print("itemgetter + slice:", itemgetter_family())
    print("slice 自身字段:", LAST_THREE.start, LAST_THREE.stop, LAST_THREE.step)
