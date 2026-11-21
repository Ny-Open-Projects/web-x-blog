ns = {}
exec("factor = 2\nplain = factor * 10\n", ns)      # 类体式执行:直接读类变量 OK
print("class body direct read:", ns["plain"])

try:
    exec("factor = 2\nvalues = [factor * n for n in range(3)]\n", ns)
except NameError as e:
    print("comprehension skips class scope:", e)

class Table:
    factor = 2
    plain = factor * 10                    # 类体直接读:OK

    @classmethod
    def scaled(cls, n):
        return n * cls.factor              # 方法经 cls 访问类属性

if __name__ == "__main__":
    print("Table.plain:", Table.plain)
    print("scaled:", Table.scaled(5))
