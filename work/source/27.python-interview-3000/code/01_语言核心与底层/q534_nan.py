import math

nan = float("nan")

if __name__ == "__main__":
    print("nan == nan:", nan == nan)      # False:IEEE 754 规定
    print("nan != nan:", nan != nan)      # True:唯一自我不等的数
    print("math.isnan:", math.isnan(nan))

    print("list.count finds same object:", [1, nan].count(nan))   # 同一性短路

    d = {nan: "a"}
    print("dict lookup by identity:", d[nan])

    print("sorted with nan:", sorted([1.0, nan, 2.0]))            # 顺序不可靠
    print("module-level nan is a singleton:", math.nan is math.nan)
