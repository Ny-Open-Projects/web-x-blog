"""纯逻辑判断一个查询能命中联合索引的前几列"""
COMPOSITE = ("a", "b", "c")


def usable_prefix(where_cols: set) -> tuple:
    """返回可以走索引的连续最左前缀, 遇到缺口立即停止"""
    used = []
    for col in COMPOSITE:
        if col in where_cols:
            used.append(col)
        else:
            break
    return tuple(used)


CASES = [
    {"a"},
    {"a", "b"},
    {"a", "b", "c"},
    {"b", "c"},          # 缺 a, 全部失效
    {"a", "c"},          # b 缺失, c 用不上索引(排序断链)
]

if __name__ == "__main__":
    for cols in CASES:
        print(f"WHERE {sorted(cols)} -> 命中前缀: {usable_prefix(cols) or '无'}")
    # 数据佐证: 索引内部排列 (1,1,1)(1,1,2)(1,2,1)(2,1,1)...
    # b 的取值只在同一 a 内有序, 全局不有序, 所以跳过 a 无法使用 b
