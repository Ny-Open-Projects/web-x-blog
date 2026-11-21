"""__init_subclass__ 的声明式 kwargs:配置上浮与约束校验。"""


class Table:
    registry = {}

    def __init_subclass__(cls, table=None, strict=True, **kwargs):
        super().__init_subclass__(**kwargs)      # 其余 kwargs 沿 MRO 继续上传
        cls.table = table or cls.__name__.lower()
        cls.strict = strict
        if strict and "columns" not in cls.__dict__:
            raise TypeError(cls.__name__ + " 缺少 columns 声明")
        Table.registry[cls.table] = cls


class User(Table, table="users", strict=False):
    columns = ["id", "name"]


class Order(Table):
    columns = ["id", "amount"]


if __name__ == "__main__":
    print("注册表:", sorted(Table.registry))
    print("User 表名:", User.table, "| strict:", User.strict)
    print("Order 表名(默认推导):", Order.table)
    try:
        type("Bad", (Table,), {"table": "bad"})  # strict 且缺 columns
    except TypeError as e:
        print("约束生效:", str(e)[:44])
