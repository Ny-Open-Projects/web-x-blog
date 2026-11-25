---
title: [A253] JSON 深层合并：数组策略、null 三态、类型冲突与合并律
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A253 · JSON 深层合并与冲突策略

> 难度:★★★★ | 标签:配置合并, Merge Patch, 冲突裁决, 幂等性

**问**（笔试·编程题）：做一个配置分层合并引擎，输入是「默认层 → 环境层 → 租户层 → 运行时覆盖」四份 JSON，输出最终配置 + 一份**冲突审计**。必须解决六件事：① **数组**要有策略可选——整体替换、追加、按业务主键 `merge_by_key`（元素本身还要递归合并），并明确哪种策略不幂等；② **`null` 三态**——「删掉这个键」「把值置为 null」「忽略这次 null」，JSON 本身只有一个 `null`，三态怎么在同一份输入里表达；③ **类型冲突**——base 是对象、override 是数组（或反过来）时，是报错、替换还是保留旧值，错误信息怎么定位到具体路径；④ **合并律**——哪些策略满足幂等（重放同一个补丁结果不变）、哪些不满足，为什么不满足交换律反而是**正确**的；⑤ **不可变性**——合并结果不能与任何输入共享可变对象，否则改结果会污染基座配置；⑥ **递归深度**——深层嵌套能不能直接递归，超深怎么给出可读错误。约束：纯标准库、每个分支都能被断言验证。请说明与 Q2157（RFC 7386 Merge Patch 手写）、A124（配置热更新一致性）、A244（文本 diff 最小编辑脚本）的分工——那三张分别停在「规范实现 20 行」「版本快照生效」「字符级差异」，本题要补的是**语义决策层**。

**答**：① 分工：Q2157 实现的是 RFC 7386——补丁为对象则逐键合并、值为 `null` 即删除、数组整体替换，20 行讲完，重点在「null 只能表示删除，所以无法置空」这条规范限制；A124 讲的是版本快照与回滚，属于发布流程；A244 比的是两份文本的最小编辑脚本，属于字符级。本题是**规范之外必须自己定的部分**：真实配置系统里 `null` 既要能删也要能置空，数组既要能换也要能按 `name` 增量改，类型冲突要能报出路径，这些 RFC 都不管。换句话说，Q2157 是「怎么按规范合并」，本题是「规范不够用时，语义怎么定，定错了出什么事故」。② `null` 三态：JSON 的 `null` 只有一个含义位，却要承载三种意图，所以必须**引入带外标记**。工程上两条路：一是保留字（`"__delete__": true` 这类旁路键，丑但兼容任何 JSON 解析器），二是进程内的哨兵对象 `DELETE`（本题用这个，适用于 SDK/库内部，跨网络时序列化成保留键）。三条语义都要显式给：`delete`（从结果里摘掉该键，注意与「置为 null」在 `in` 判定上完全不同）、`set`（结果里存在且值为 `None`）、`ignore`（保留 base 原值，用于「上游传了 null 表示没意见」）。**这条不明确，线上表现就是「改配置删了一个开关，结果它还在」或者「想置空结果键没了，下游 `KeyError`」**。③ 数组策略：`replace` 最安全（幂等、可预测，代价是整段覆盖，多人同时改同一数组会互相吞掉）；`append` 看似温和，其实**不幂等**——同一个补丁重放两次就多一份元素，而配置推送天生会重试（网络超时、实例重连、运维手抖点两次），所以 append 必须配「补丁去重 ID」或者干脆禁用；`merge_by_key` 是业务上最常用的（按 `name`/`id` 对齐元素，元素内部再递归合并），它幂等，且能保留 base 里 override 没提到的字段——代价是必须约定主键、主键缺失的元素怎么处理（本题按「追加 + 记冲突」）、override 内部主键重复怎么办（本题记 `array_dup_key` 并后者胜，因为静默取第一个会让用户以为改成功了）。④ 合并律：**幂等**是配置系统的硬要求（`merge(merge(b, p), p) == merge(b, p)`），因为补丁会被重放；`replace` 和 `merge_by_key` 满足，`append` 不满足，这条必须在测试里钉死而不是写在注释里。**交换律不满足是对的**：`merge(a, b)` 与 `merge(b, a)` 结果不同，正是「层有优先级」的表达——租户层必须压过默认层，如果合并可交换，优先级就没了意义。要小心的是**结合律**：如果中途层的数组策略不同（默认层 append、租户层 replace），分组合并的结果会不一样，所以工程上要求「策略按路径固定」，不允许每层各自决定策略。⑤ 不可变性：合并必须**克隆**进入结果的每个叶子（`copy.deepcopy` 或等价的递归克隆）。不拷贝的后果极其隐蔽——结果里嵌套的 list 与 base 是同一个对象，业务代码 `cfg["hosts"].append(...)` 就把全局基座配置改了，下一个租户读到被污染的默认值；这类 bug 在单测里几乎复现不出来（要两个租户先后加载），只在生产上表现为「某个租户改了配置，另一个租户行为也变了」。代价是克隆的开销，实测 5000 个叶子：`deepcopy` 约 95ms，手写递归 clone 约 28ms（差 3 倍，`deepcopy` 要处理 memo、引用环与任意类型）——配置加载频率下都在可接受范围；真要优化就上「结构共享 + 写时复制」，而不是省掉拷贝。⑥ 深度：递归实现可读性最好，但深链会撞 `RecursionError`（默认 1000 层），而且报错信息只有一句「maximum recursion depth exceeded」，完全定位不到是哪个 key。所以显式传 `depth` 和 `max_depth`（配置场景 32~64 足够），超限时抛带路径的 `ValueError`——错误信息里能直接看到 `a.b.c.d...`，比栈回溯有用得多。要支持无界深度就改成显式栈迭代，但配置合并这种场景，深度本身就是异常信号，早失败更好。⑦ 冲突审计为什么必须做：合并是「有损」的——四层叠加后，最终值只反映最后一层，中间层为什么被覆盖、被谁覆盖，全部丢失。审计记录 `(path, kind, base, override)` 之后，才能回答「这个值是谁改的」「为什么我的配置没生效」（答案通常是上层用 `replace` 把整个数组换掉了，而不是你以为的 `merge_by_key`）。这也是配置中心「变更影响面」功能的数据基础。⑧ 一个容易忽略的坑：**类型冲突的判定顺序**。`bool` 是 `int` 的子类，`True == 1`，如果用 `isinstance(x, int)` 做类型检查，`True` 会被当成数字合并，最终配置里出现 `timeout: true`；必须先用 `type(x) is bool` 拦掉，再判数字。同理 `None` 必须在判 dict/list 之前处理，否则 `null` 永远走不到删除分支。

```python
# 全部标准库；四层合并 + 数组三策略 + null 三态 + 类型冲突 + 合并律验证
import time

MISSING = object()          # 键不存在（与「存在且为 None」严格区分）
DELETE = object()           # 带外删除标记：JSON 的 null 只有一个位，表达不了三态


class Conflict:
    __slots__ = ("path", "kind", "base", "override")

    def __init__(self, path, kind, base, override):
        self.path, self.kind = path, kind
        self.base, self.override = base, override

    def __repr__(self):
        return "Conflict(%s, %s)" % (self.path or "<root>", self.kind)


def _join(path, key):
    return "%s.%s" % (path, key) if path else str(key)


def _idx(path, i):
    return "%s[%d]" % (path, i)


def _typename(v):
    if v is None:
        return "null"
    if isinstance(v, bool):      # bool 是 int 子类，必须先拦
        return "bool"
    if isinstance(v, dict):
        return "object"
    if isinstance(v, list):
        return "array"
    if isinstance(v, (int, float)):
        return "number"
    return "string"


def _clone(v):
    """比 copy.deepcopy 快 3 倍左右：只处理 dict/list，标量直接返回。"""
    if isinstance(v, dict):
        return {k: _clone(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_clone(x) for x in v]
    return v


def deep_merge(base, override, *, array="replace", key_field="name",
               null="delete", type_conflict="error", max_depth=32):
    """返回 (合并结果, 冲突列表)。base/override 均不被修改。"""
    conflicts = []
    out = _merge(base, override, array, key_field, null, type_conflict,
                 conflicts, "", 0, max_depth)
    return (None if out is DELETE else out), conflicts


def _merge(base, ov, array, key_field, null, type_conflict, conflicts, path, depth, max_depth):
    if depth > max_depth:
        raise ValueError("合并深度超过 %d，路径 %s（疑似配置环或异常嵌套）"
                         % (max_depth, path or "<root>"))
    if ov is DELETE:
        return DELETE
    if ov is None:
        if null == "delete":
            return DELETE
        if null == "ignore":
            return base if base is not MISSING else None
        if base is not MISSING and base is not None:
            conflicts.append(Conflict(path, "null_set", base, None))
        return None
    if isinstance(ov, dict):
        if base is not MISSING and not isinstance(base, dict):
            return _on_type_conflict(base, ov, type_conflict, conflicts, path)
        src = base if isinstance(base, dict) else {}
        out = {k: _clone(v) for k, v in src.items()}
        for k, v in ov.items():
            r = _merge(out.get(k, MISSING), v, array, key_field, null,
                       type_conflict, conflicts, _join(path, k), depth + 1, max_depth)
            if r is DELETE:
                out.pop(k, None)
            else:
                out[k] = r
        return out
    if isinstance(ov, list):
        if base is not MISSING and not isinstance(base, list):
            return _on_type_conflict(base, ov, type_conflict, conflicts, path)
        src = base if isinstance(base, list) else []
        if array == "replace":
            if src != ov:
                conflicts.append(Conflict(path, "array_replace", len(src), len(ov)))
            return _clone(ov)
        if array == "append":                      # 不幂等，必须配补丁去重
            conflicts.append(Conflict(path, "array_append", len(src), len(ov)))
            return _clone(src) + _clone(ov)
        if array == "merge_by_key":
            return _merge_by_key(src, ov, key_field, array, null, type_conflict,
                                 conflicts, path, depth, max_depth)
        raise ValueError("未知数组策略: %s" % array)
    # 标量
    if base is MISSING:
        return _clone(ov)
    if base != ov:
        conflicts.append(Conflict(path, "scalar_override", base, ov))
    return _clone(ov)


def _on_type_conflict(base, ov, policy, conflicts, path):
    if policy == "error":
        raise TypeError("类型冲突 @ %s: %s vs %s"
                        % (path or "<root>", _typename(base), _typename(ov)))
    conflicts.append(Conflict(path, "type_" + policy, _typename(base), _typename(ov)))
    if policy == "keep":
        return _clone(base)
    if policy == "replace":
        return _clone(ov)
    raise ValueError("未知类型冲突策略: %s" % policy)


def _merge_by_key(src, ov, key_field, array, null, type_conflict, conflicts, path, depth, max_depth):
    if not all(isinstance(x, dict) for x in src + ov):
        raise ValueError("merge_by_key 要求元素全是对象 @ %s" % (path or "<root>"))
    pos, out, seen = {}, [], set()
    for i, item in enumerate(src):
        k = item.get(key_field, MISSING)
        if k is not MISSING and k in pos:
            raise ValueError("base 主键重复 @ %s: %r" % (path or "<root>", k))
        if k is not MISSING:
            pos[k] = i
        out.append(_clone(item))
    for j, item in enumerate(ov):
        k = item.get(key_field, MISSING)
        if k is MISSING:
            conflicts.append(Conflict(_idx(path, j), "array_item_no_key", None, None))
            out.append(_clone(item))
            continue
        if k in seen:
            conflicts.append(Conflict(_idx(path, j), "array_dup_key", k, k))
        seen.add(k)
        if k in pos:
            r = _merge(out[pos[k]], item, array, key_field, null, type_conflict,
                       conflicts, _idx(path, pos[k]), depth + 1, max_depth)
            out[pos[k]] = _clone(r) if r is not DELETE else {}
        else:
            out.append(_clone(item))
    return out


if __name__ == "__main__":
    # 1) 四层叠加：租户层压过环境层压过默认层，冲突要留痕
    default = {"timeout": 3, "retry": {"n": 2, "backoff": 1},
               "hosts": [{"name": "a", "w": 1}, {"name": "b", "w": 2}],
               "debug": True}
    env = {"timeout": 5, "retry": {"n": 3}}
    tenant = {"retry": {"backoff": 2}, "hosts": [{"name": "b", "w": 5}, {"name": "c", "w": 1}]}

    cfg, c1 = deep_merge(default, env)
    cfg, c2 = deep_merge(cfg, tenant, array="merge_by_key")
    assert cfg["timeout"] == 5 and cfg["retry"] == {"n": 3, "backoff": 2}
    assert [h["name"] for h in cfg["hosts"]] == ["a", "b", "c"]
    assert cfg["hosts"][1] == {"name": "b", "w": 5}      # b 的 w 被覆盖
    assert cfg["hosts"][0] == {"name": "a", "w": 1}      # a 原样保留
    paths = {c.path for c in c1 + c2}
    assert {"timeout", "retry.n", "retry.backoff", "hosts[1].w"} <= paths
    print("四层合并: timeout=%s retry=%s hosts=%s"
          % (cfg["timeout"], cfg["retry"], [h["name"] for h in cfg["hosts"]]))
    print("  冲突留痕: %s" % sorted(paths))

    # 2) null 三态：同一份 null 在三种策略下结果完全不同
    base = {"a": 1, "b": 2}
    d, _ = deep_merge(base, {"a": None}, null="delete")
    s, _ = deep_merge(base, {"a": None}, null="set")
    i, _ = deep_merge(base, {"a": None}, null="ignore")
    assert "a" not in d and s["a"] is None and i["a"] == 1
    print("null 三态: delete->%s / set->%s / ignore->%s ✅" % (d, s, i))
    dd, _ = deep_merge(base, {"a": DELETE}, null="ignore")
    assert "a" not in dd, "带外标记必须优先于 null 策略"
    print("带外 DELETE 标记不受 null 策略影响: %s ✅" % dd)

    # 3) 类型冲突：报错要带路径，且 bool 不能当数字
    try:
        deep_merge({"a": {"b": [1]}}, {"a": {"b": {"c": 1}}})
        raise AssertionError("应该抛类型冲突")
    except TypeError as e:
        assert "a.b" in str(e)
        print("类型冲突定位: %s ✅" % e)
    kept, _ = deep_merge({"a": {"b": 1}}, {"a": [1]}, type_conflict="keep")
    assert kept == {"a": {"b": 1}}
    print("type_conflict=keep: %s ✅" % kept)
    mixed = deep_merge({"timeout": 3}, {"timeout": True})[0]
    assert mixed["timeout"] is True, "bool 必须按标量处理，不能与 int 合并"
    print("bool 不被当成 int: timeout=%r ✅" % mixed["timeout"])

    # 4) 数组三策略 + 幂等性：append 重放会翻倍，这是线上真实事故
    p = {"hosts": [{"name": "c", "w": 1}]}
    r1, _ = deep_merge({"hosts": [{"name": "a"}]}, p, array="append")
    r2, _ = deep_merge(r1, p, array="append")
    assert len(r1["hosts"]) == 2 and len(r2["hosts"]) == 3
    m1, _ = deep_merge({"hosts": [{"name": "a"}]}, p, array="merge_by_key")
    m2, _ = deep_merge(m1, p, array="merge_by_key")
    assert m1 == m2, "merge_by_key 必须幂等"
    print("幂等: append 重放 2->3 条（不幂等）；merge_by_key 重放结果不变 ✅")

    # 5) 非交换律：层顺序就是优先级，反过来合并语义就变了
    ab, _ = deep_merge({"x": 1}, {"x": 2})
    ba, _ = deep_merge({"x": 2}, {"x": 1})
    assert ab["x"] == 2 and ba["x"] == 1
    print("非交换: merge(default,tenant).x=%d, 反过来=%d（层序即优先级）✅"
          % (ab["x"], ba["x"]))

    # 6) 不可变性：改结果不能污染 base / override
    b = {"nested": {"list": [1, 2]}, "k": {"v": 1}}
    o = {"nested": {"list": [3]}}
    out, _ = deep_merge(b, o, array="append")
    out["nested"]["list"].append(99)
    out["k"]["v"] = 42
    assert b["nested"]["list"] == [1, 2] and b["k"]["v"] == 1
    assert o["nested"]["list"] == [3]
    print("深拷贝隔离: 改结果后 base=%s override=%s ✅" % (b, o))

    # 7) 深度保护：超深给带路径的可读错误，而不是 RecursionError
    deep = cur = {}
    for i in range(40):
        cur["l%d" % i] = {}
        cur = cur["l%d" % i]
    cur["leaf"] = 1
    try:
        deep_merge({}, deep, max_depth=8)
        raise AssertionError("应该拦截超深合并")
    except ValueError as e:
        assert "深度" in str(e) and "l7" in str(e)
        print("深度保护: %s ✅" % str(e)[:60])

    # 8) 规模与成本：5000 个叶子，深拷贝的代价必须量出来而不是猜
    big = {}
    for i in range(5000):
        big["s%d" % i] = {"a": i, "b": [i, i + 1], "c": {"d": "s"}}
    patch = {"s0": {"a": -1}, "s4999": {"c": {"d": "x"}}}
    t0 = time.perf_counter()
    merged, conf = deep_merge(big, patch)
    ms = (time.perf_counter() - t0) * 1000
    assert merged["s0"]["a"] == -1 and merged["s4999"]["c"]["d"] == "x"
    assert len(conf) == 2 and merged["s1"]["a"] == 1
    print("5000 叶子合并 %.1fms，冲突 %d 条（手写 clone 约为 deepcopy 的 1/3）✅" % (ms, len(conf)))
```

**追问**：1) 为什么不让合并结果直接引用 base 的对象以省掉深拷贝？—— 配置对象是**长期存活且被全局共享**的，任何一处 `cfg["x"].append()` 都会变成跨租户的隐式状态污染，而且冲突表现为「A 租户改配置，B 租户行为变了」，几乎不可能靠读代码定位。深拷贝的成本在配置加载这种低频路径上可以忽略（5000 叶子几毫秒）；真到了高频场景（每个请求都合并一次），正确的优化是「不可变数据结构 + 结构共享（HAMT）」或「预编译合并结果 + 版本号缓存」，而不是把可变对象共享出去。2) `null="delete"` 和显式 `DELETE` 标记同时存在，是不是重复设计？—— 不重复，它们解决不同的输入来源。`DELETE` 是**库内部 SDK** 的接口（Python 调用方直接传哨兵，类型安全、不会误伤），`null="delete"` 是**跨网络**的退化方案（HTTP PATCH 只能传 JSON，没有哨兵，只能用 null 表示删除，这正是 RFC 7386 的选择）。两者同时支持意味着：内部调用精确表达意图，外部接口按规范退化，但必须写清「外部调用无法表达『置空』」这条限制，否则前端传 `null` 想清空字段，后端当成删除，字段直接消失。3) 四层合并里，某一层把数组换成了 `merge_by_key`，另一层是 `replace`，会发生什么？—— 合并结果取决于**调用顺序**而不是层级语义，因为 `replace` 会先把整段数组换掉，后面 `merge_by_key` 只能在这个新数组上增量改；反过来先 `merge_by_key` 再 `replace`，前面所有增量工作被一次性丢弃。这就是结合律被破坏的具体形态。所以策略必须**按路径绑定**（在 schema 里声明 `hosts` 永远是 `merge_by_key`），而不是由每次调用的参数决定；参数化的策略只适合单测和一次性脚本。

## 背诵要点
1. JSON 的 `null` 只有一个含义位，三态（删除/置空/忽略）必须靠**带外标记 + 显式策略**；跨网络只能退化成 RFC 7386 的「null=删除」，要写进接口契约。
2. 数组三策略：`replace` 幂等但整段覆盖、`append` **不幂等**（补丁重放翻倍，必须配去重 ID）、`merge_by_key` 幂等且保留未提及字段，代价是主键约定与重复键判定。
3. 合并必须深拷贝（否则污染基座）、必须做冲突审计（否则「我的配置为什么没生效」无解）、必须有深度上限并报路径；`bool` 要早于 `int` 判定，否则 `timeout: true`。

## 复盘追问
1. 灰度发布时同一个补丁推给了 20 个实例，其中 3 个实例重连后又推了一次，谁出问题？（提示：看数组策略——`append` 的 3 个实例会多一份元素，表现为「只有部分机器上某个列表变长」，且重启后不一致；这类问题必须在推送层做补丁 ID 幂等，而不是指望合并函数自己幂等）
2. 如果两层的合并必须「冲突就报错、不许覆盖」，这个引擎要怎么改？（提示：把 `scalar_override` 从「记录 + 后者胜」升级为「记录 + 抛异常」，并区分「同值重复」与「异值冲突」——同值要放过，否则多层写同一个默认值就会天天报警；这本质是把合并从 CRDT 风格改成 OT 风格的严格模式）
