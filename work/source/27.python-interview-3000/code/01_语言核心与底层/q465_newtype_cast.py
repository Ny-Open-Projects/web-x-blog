from typing import NewType, cast

UserId = NewType("UserId", int)
OrderNo = NewType("OrderNo", int)
IdList = list[int]                        # 类型别名

def get_name(uid: UserId) -> str:
    return f"user-{uid}"

def first(items: IdList) -> int:
    return items[0]

if __name__ == "__main__":
    raw = 42
    print(get_name(UserId(raw)))          # 显式构造:语义转换点清晰
    print(get_name(OrderNo(raw)))         # mypy 报错:OrderNo 不是 UserId
    print(first([1, 2, 3]))

    payload = {"id": 7}
    uid = UserId(cast(int, payload["id"]))   # 外部数据:cast 声明假设
    print(get_name(uid))
