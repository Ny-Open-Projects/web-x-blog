"""RFC 7386 JSON Merge Patch: 递归合并与 null 删除语义(纯标准库)。"""


def merge_patch(target, patch):
    """Merge Patch 核心算法。
    patch 是 dict: 逐键合并, 值为 None 表示删除该键, 值为 dict 递归, 其他值整体替换。
    patch 不是 dict: 直接替换整个目标文档。
    """
    if not isinstance(patch, dict):
        return patch
    result = dict(target) if isinstance(target, dict) else {}
    for key, value in patch.items():
        if value is None:
            result.pop(key, None)                       # null 的唯一语义: 删除成员
        elif isinstance(value, dict):
            result[key] = merge_patch(result.get(key), value)
        else:
            result[key] = value
    return result


doc = {"title": "旧标题", "tags": ["a"], "meta": {"color": "red", "size": "L"},
       "obsolete": True}
patch = {"title": "新标题", "meta": {"color": "blue"}, "obsolete": None, "extra": 1}
merged = merge_patch(doc, patch)
print("原文档:", doc)
print("补丁  :", patch)
print("结果  :", merged)
assert merged == {"title": "新标题", "tags": ["a"],
                  "meta": {"color": "blue", "size": "L"}, "extra": 1}
assert merge_patch({"tags": [1, 2]}, {"tags": [3]}) == {"tags": [3]}   # 数组整体替换
assert merge_patch({"a": 1}, "flat") == "flat"                          # 非对象补丁整体替换
assert "obsolete" not in merged                                         # null 即删除
print("要点: 对象递归合并、null 即删除、数组与标量整体替换, 三条规则就是 RFC 7386 的全部")
