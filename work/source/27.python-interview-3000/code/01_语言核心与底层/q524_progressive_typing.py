from typing import List, Optional

def total_v1(values):                     # 迁移前:无注解
    return sum(values)

def total_v2(values: List[int]) -> int:   # 第二步:公共函数补注解
    return sum(values)

def find_user(uid: int, cache: Optional[dict] = None) -> Optional[str]:
    """第三步:Optional 显式化,返回值可能为 None 进入签名"""
    cache = cache or {}
    return cache.get(uid)

if __name__ == "__main__":
    print(total_v1([1, 2]), total_v2([1, 2]))
    print(find_user(1, {1: "alice"}), find_user(2))
    print("annotations:", total_v2.__annotations__)
