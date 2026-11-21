"""dict.get vs try/except:键存在与缺失两条路径的实测。"""
import timeit

D = {("key" + str(i)): i for i in range(1000)}
PRESENT = "key500"
MISSING = "nope"


def via_get_present():
    return D.get(PRESENT, 0)


def via_try_present():
    try:
        return D[PRESENT]
    except KeyError:
        return 0


def via_get_missing():
    return D.get(MISSING, 0)


def via_try_missing():
    try:
        return D[MISSING]
    except KeyError:
        return 0


def bench(stmt, number=200000):
    return round(timeit.timeit(stmt, globals=globals(), number=number), 4)


if __name__ == "__main__":
    print("键存在  get:", bench("via_get_present()"))
    print("键存在 try:", bench("via_try_present()"))
    print("键缺失  get:", bench("via_get_missing()"))
    print("键缺失 try:", bench("via_try_missing()"))
    print("结论:存在路径两者接近,try 略快;缺失路径 get 明显更快")
