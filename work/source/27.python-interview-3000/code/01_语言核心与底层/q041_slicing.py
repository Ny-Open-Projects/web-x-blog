if __name__ == "__main__":
    data = list(range(10))
    print(data[::-1])            # 反转
    print(data[::2])             # 步长取样
    print(data[-3:])             # 末尾三个

    HEAD = slice(0, 3)
    print(data[HEAD])            # 可命名复用的切片对象

    nums = [1, 2, 3, 4, 5]
    nums[1:3] = ["a", "b", "c"]  # 不等长替换
    print(nums)
    nums[2:2] = ["X"]            # 插入
    print(nums)
    del nums[::2]                # 按步删除
    print(nums)

    class Grid:
        def __getitem__(self, key):
            if isinstance(key, slice):
                return f"slice {key.start}:{key.stop}:{key.step}"
            return f"item {key}"
    print(Grid()[1:7:2], Grid()[5])
