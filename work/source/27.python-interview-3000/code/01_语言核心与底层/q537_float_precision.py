import math

if __name__ == "__main__":
    print("0.1 + 0.2 =", 0.1 + 0.2)
    print("equals 0.3:", (0.1 + 0.2) == 0.3)
    print(f"0.1 in binary-ish: {0.1:.20f}")
    print("isclose:", math.isclose(0.1 + 0.2, 0.3))

    nums = [0.1] * 10
    print("naive sum == 1.0:", sum(nums) == 1.0)
    print("fsum == 1.0   :", math.fsum(nums) == 1.0)

    print("big eats small:", 1e16 + 1.0 - 1e16)
    print("fsum resists  :", math.fsum([1e16, 1.0, -1e16]))
