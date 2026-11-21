"""Q2834 列表结果的头尾采样裁剪:省略计数与可回捞标记。

工具返回上千条记录直接进上下文是灾难。裁剪策略:保头尾、中间折叠成
一个带计数的省略标记,标记本身是结构化数据,下游既知道被截了多少,
也知道怎么回捞,而不是拿到一份看不出被动过手脚的列表。
"""


def trim_list(items, keep_head, keep_tail):
    """头尾保留,中间折叠为省略标记,返回裁剪后列表与标记。"""
    n = len(items)
    if n <= keep_head + keep_tail:
        return list(items), None
    omitted = n - keep_head - keep_tail
    marker = {
        "omitted": omitted,
        "hint": "中间结果已省略,可用 cursor 分页回捞",
        "cursor": str(keep_head) + "-" + str(n - keep_tail),
    }
    head = items[:keep_head]
    tail = items[-keep_tail:] if keep_tail > 0 else []
    return head + [marker] + tail, marker


def main():
    items = ["row_%02d" % i for i in range(1, 13)]
    trimmed, marker = trim_list(items, keep_head=2, keep_tail=2)
    assert marker == {"omitted": 8,
                      "hint": "中间结果已省略,可用 cursor 分页回捞",
                      "cursor": "2-10"}, marker
    assert trimmed[0] == "row_01" and trimmed[1] == "row_02", trimmed
    assert trimmed[-1] == "row_12" and trimmed[-2] == "row_11", trimmed
    assert trimmed[2]["omitted"] == 8, trimmed[2]
    # 列表本身不长时不裁剪,保持原样
    same, no_marker = trim_list(items[:3], 2, 2)
    assert no_marker is None and same == items[:3], same
    # 不保尾部:标记仍然准确
    head_only, marker2 = trim_list(items, 3, 0)
    assert marker2["omitted"] == 9, marker2
    assert head_only[-1] == marker2, head_only
    print("裁剪后:", trimmed)
    print("短列表不裁:", same)
    print("省略计数随策略变化:", marker2["omitted"])


if __name__ == "__main__":
    main()
