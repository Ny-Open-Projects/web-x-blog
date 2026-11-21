def find_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(n, "divisible by", i)
            break
    else:                                     # 没被 break:是素数
        print(n, "is prime")

def find_first_even(nums):
    for x in nums:
        if x % 2 == 0:
            return x
    else:
        return None                           # 等价于函数尾 None

if __name__ == "__main__":
    find_prime(13)
    find_prime(15)
    print("first even:", find_first_even([1, 3, 4, 6]))
    for _ in range(0):                        # 空序列:直接 else
        pass
    else:
        print("empty loop still reaches else")
