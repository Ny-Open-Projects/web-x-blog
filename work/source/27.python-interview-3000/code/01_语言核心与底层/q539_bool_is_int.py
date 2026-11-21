if __name__ == "__main__":
    print("issubclass:", issubclass(bool, int), "| isinstance:", isinstance(True, int))
    print("True + True:", True + True, "| True * 3:", True * 3)
    print("as index:", ["a", "b", "c"][True])

    print("count via sum:", sum(x > 2 for x in range(5)))

    d = {True: "yes", 1: "no"}
    print("True and 1 are the same key:", d)
    print(True == 1, True is 1)           # True False:== 相等推不出身份相同

    print(type(False).__name__, False == 0)
