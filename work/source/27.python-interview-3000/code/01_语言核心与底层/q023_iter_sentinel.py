from io import StringIO

def read_blocks(stream):
    # 每次调用 stream.readline,读到空字符串哨兵为止
    for line in iter(stream.readline, ""):
        yield line.rstrip("\n")

if __name__ == "__main__":
    fake = StringIO("alpha\nbeta\ngamma")
    for block in read_blocks(fake):
        print("block:", block)

    import functools
    import random

    def roll():
        return random.randint(1, 7)

    rolls = iter(roll, 7)          # 掷到 7 停,本例必停
    print(list(rolls))
