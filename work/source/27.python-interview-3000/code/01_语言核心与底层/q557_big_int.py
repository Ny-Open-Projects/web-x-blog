import sys

if __name__ == "__main__":
    print("platform word:", sys.maxsize)
    big = 2 ** 200
    print("bits:", big.bit_length())
    print("sizeof 2**30 :", sys.getsizeof(2 ** 30))
    print("sizeof 2**200:", sys.getsizeof(big), "(digit array grows)")

    print("to bytes:", (2 ** 64).to_bytes(9, "big").hex())
    print("hash is small:", hash(big))
    if sys.version_info >= (3, 11):
        print("int max str digits limit:", sys.get_int_max_str_digits())
    else:
        print(f"该特性需要 Python 3.11+,当前 {sys.version_info.major}.{sys.version_info.minor},演示跳过")
