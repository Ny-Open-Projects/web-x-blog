import sys

data = [1, -2, 3, -4, 5]
squares = [x * x for x in data if x > 0]        # 立即求值
sq_iter = (x * x for x in data if x > 0)        # 惰性

matrix = [[1, 2], [3, 4]]
flat = [cell for row in matrix for cell in row] # 等价双重循环

if __name__ == "__main__":
    print(squares, flat)
    print(sys.getsizeof(squares), "bytes for list")
    print(sys.getsizeof(sq_iter), "bytes for genexp,与元素个数无关")
    print(sum(sq_iter))    # 消费一次
    print(list(sq_iter))   # 已耗尽,空列表

    pairs = {s: s.upper() for s in ["a", "b"]}  # dict 推导
    print(pairs)
