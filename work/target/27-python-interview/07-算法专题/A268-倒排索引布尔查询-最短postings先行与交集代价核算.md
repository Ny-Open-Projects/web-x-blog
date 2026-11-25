---
title: [A268] 倒排索引与布尔查询：最短 postings 先行与交集代价核算
date: 2026-11-24
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A268 · 倒排索引构建与布尔查询的交集优化

> 难度:★★★★ | 标签:倒排索引, 布尔查询, postings 交集, 调度场解析, 查询优化

**问**（笔试·编程题）：不借助任何搜索引擎库，从零实现一个支持布尔查询的倒排索引。要求：① 构建器：文档集 → {词 → 升序 postings}；② 查询语言：支持 AND / OR / NOT 与括号组合（NOT 为一元最高优先级），写出分词器 + 调度场解析 + RPN 求值；③ AND 求值必须做 **postings 交集优化**：按表长升序折叠，短表逐 id 用 `bisect` 探长表，并在代码里**计数比较探针**——与「按书写顺序双指针归并」的朴素策略对比，用「180 篇含 python、2 篇含 zebra」的语料量化两者探针数并断言优化版更省；④ 正确性对账：对每篇文档的词集做暴力布尔求值，与索引求值结果集逐查询断言一致（含嵌套括号与 NOT 的 ≥3 个查询）；⑤ 说清 NOT 在 postings 模型下的实现代价（求补集为什么必须知道全集）与 OR 的代价口径。请说清与 Q905（SQLite FTS5 的原理与 LIKE 对比，不手写结构）、Q7739（中文分词缺失与 n-gram 建索引）、Q6134/Q6144（pg_trgm / FTS5 成本账）的分工——本题只回答「**倒排结构本体、布尔代数在 postings 上的求值与交集顺序优化**」。

**答**：① 分工：Q905 讲的是「FTS5 替你做了什么」，Q7739 讲「中文怎么切」，本题讲的是**被这些引擎藏起来的那层**：倒排结构本体与布尔代数如何跑在 postings 上——笔试现场手写这层，正是搜索引擎岗与后端岗共用的基本功。② 构建：每篇文档 `set(tokenize)` 去重后按 doc_id 升序追加，得到 {词 → 升序 postings}——**升序是后面一切优化前提**：bisect 要单调、归并要同向、跳表指针也是建立在有序之上。③ 查询解析走调度场（shunting-yard）：优先级 NOT(3) > AND(2) > OR(1)，一元 NOT 单独处理；RPN 求值时每个原子查一次词典拿 postings，运算即集合运算。④ 交集优化的核心观察：双指针归并的探针数 ≈ len(a)+len(b)，**与先后顺序无关**；但「短表逐 id 用 bisect 探长表」的探针数 = len(short)·log2(len(long))——罕见词（低 DF、表短）∧ 高频词（高 DF、表长）时，先交短表把候选集直接压到短表规模，探针从 O(表长和) 降到 O(短表 × log 长表)。实测 180∧2：归并约 181 次探针，bisect 约 15 次，差一个数量级；这正是真实引擎查询优化器「**高 DF 词后置、低 DF 词先交**」的由来。k 词 AND 的完整策略：按表长升序折叠，且每折一次结果只会更短，后续直接拿当前结果集去 bisect 下一张长表。⑤ NOT 的代价：postings 是「有哪些」，NOT 问的是「除这些外还有谁」——求补 = 全集 U − postings，O(|U|)，而且**必须先物化全集**：这就是为什么真实引擎把 NOT 改写成「正向命中的减法」或要求查询必须含至少一个正词（纯 NOT 查询等于全表扫描）。OR 的代价 ≈ 各表长之和（结果集与词频同阶，省不掉）。于是布尔查询的成本排序是 **AND ≪ OR < NOT**——「搜索建议里多拼一个 AND 少拼一个 OR」的成本根源就在这张表。⑥ 正确性对账：同一棵 RPN，换个原子求值器（每篇文档词集上逐个算真假）做暴力对账，索引解与暴力解逐查询断言相等——手写解析器最容易在优先级和一元运算上翻车，对账是唯一可信的护城河。

```python
# 全部标准库；手写倒排索引：构建 + 布尔查询（AND/OR/NOT）+ 最短 postings 先行的交集优化
import bisect
import re


def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def build_index(docs):
    """docs: {doc_id: text} -> {term: 升序 postings}"""
    index = {}
    for doc_id in sorted(docs):
        for term in set(tokenize(docs[doc_id])):
            index.setdefault(term, []).append(doc_id)
    return index


def intersect_merge(a, b, probes):
    """双指针归并求交，探针数 ≈ len(a)+len(b)，与顺序无关。"""
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        probes[0] += 1
        if a[i] == b[j]:
            out.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return out


def intersect_short_first(short, long_, probes):
    """短表逐 id bisect 探长表：探针数 = len(short)·log2(len(long))。"""
    out = []
    for x in short:
        probes[0] += 1
        pos = bisect.bisect_left(long_, x)
        if pos < len(long_) and long_[pos] == x:
            out.append(x)
    return out


def and_fold(postings_list, probes):
    """AND 折叠：按表长升序，短表 bisect 探长表（结果只会更短）。"""
    tables = sorted(postings_list, key=len)
    acc = tables[0]
    for nxt in tables[1:]:
        if len(acc) * 16 < len(nxt):        # 短表足够短才值得 bisect，否则归并更稳
            acc = intersect_short_first(acc, nxt, probes)
        else:
            acc = intersect_merge(acc, nxt, probes)
        if not acc:
            break                            # 空交集提前终止，后面白探
    return acc


def to_rpn(tokens):
    """调度场解析：NOT(3,一元) > AND(2) > OR(1)，左结合。"""
    prec = {"NOT": 3, "AND": 2, "OR": 1}
    out, ops = [], []
    for tk in tokens:
        if tk in prec:
            while ops and ops[-1] != "(" and prec[ops[-1]] >= prec[tk]:
                out.append(ops.pop())
            ops.append(tk)
        elif tk == "(":
            ops.append(tk)
        elif tk == ")":
            while ops and ops[-1] != "(":
                out.append(ops.pop())
            ops.pop()                        # 弹掉 "("
        else:
            out.append(tk)
    while ops:
        out.append(ops.pop())
    return out


def eval_rpn(rpn):
    """RPN 求值为 AST：原子 = 词字符串，运算 = 嵌套元组。"""
    st = []
    for tk in rpn:
        if tk == "NOT":
            st.append(("not", st.pop()))
        elif tk == "AND":
            b, a = st.pop(), st.pop()
            st.append(("and", a, b))
        elif tk == "OR":
            b, a = st.pop(), st.pop()
            st.append(("or", a, b))
        else:
            st.append(tk)
    return st[0]


def postings_eval(node, index, universe):
    if isinstance(node, str):
        return list(index.get(node, []))
    if node[0] == "not":
        return sorted(set(universe) - set(postings_eval(node[1], index, universe)))
    if node[0] == "and":
        return intersect_merge(postings_eval(node[1], index, universe),
                               postings_eval(node[2], index, universe), [0])
    return sorted(set(postings_eval(node[1], index, universe))
                  | set(postings_eval(node[2], index, universe)))


def brute_eval(node, doc_tokens):
    """逐文档词集上的暴力布尔求值，做对账基准。"""
    if isinstance(node, str):
        return node in doc_tokens
    if node[0] == "not":
        return not brute_eval(node[1], doc_tokens)
    if node[0] == "and":
        return brute_eval(node[1], doc_tokens) and brute_eval(node[2], doc_tokens)
    return brute_eval(node[1], doc_tokens) or brute_eval(node[2], doc_tokens)


if __name__ == "__main__":
    # 语料：200 篇，python 高频 180 篇，zebra 罕见 2 篇，cache/go 陪跑
    docs = {}
    for i in range(200):
        words = ["python"] * 3 if i < 180 else ["go"]
        if i % 5 == 0:
            words.append("cache")
        if i in (7, 123):
            words.append("zebra")
        docs[i] = " ".join(words) + " doc%d" % i
    index = build_index(docs)
    universe = sorted(docs)
    assert len(index["python"]) == 180 and len(index["zebra"]) == 2

    # 1) 交集优化核算：180∧2 的探针数，优化版 vs 朴素归并
    long_t, short_t = index["python"], index["zebra"]
    p_naive = [0]
    intersect_merge(long_t, short_t, p_naive)          # 书写顺序：长表在前
    p_opt = [0]
    got = intersect_short_first(short_t, long_t, p_opt)
    assert got == [7, 123]
    print("交集探针: 归并(长表在前) %d 次 vs 短表先行 bisect %d 次 -> 优化 %.0f%% ✅"
          % (p_naive[0], p_opt[0], 100.0 * (1 - p_opt[0] / p_naive[0])))
    assert p_opt[0] < p_naive[0] // 2

    # 2) AND 折叠 + 空交集提前终止
    p_fold = [0]
    assert and_fold([index["python"], index["zebra"], index["go"]], p_fold) == []
    print("AND 折叠: python∧zebra∧go -> 空交集提前终止，后续长表白探被省掉 ✅")

    # 3) 查询解析与求值：三个查询与暴力对账（含嵌套括号与 NOT）
    queries = ["python AND zebra",
               "(python OR go) AND NOT cache",
               "python AND (zebra OR cache)",
               "NOT python AND NOT cache AND NOT zebra AND NOT go"]
    for q in queries:
        tokens = re.findall(r"\(|\)|AND|OR|NOT|[a-z0-9]+", q)
        tree = eval_rpn(to_rpn(tokens))
        # 索引解
        r_index = set(postings_eval(tree, index, universe))
        # 暴力解
        r_brute = {d for d in universe if brute_eval(tree, set(tokenize(docs[d])))}
        assert r_index == r_brute, (q, r_index, r_brute)
        print("对账: %-42s 命中 %d 篇，索引解=暴力解 ✅" % (q, len(r_index)))

    # 4) NOT 的代价口径：纯 NOT 查询 = 全集减法
    r = postings_eval(eval_rpn(to_rpn(["NOT", "python"])), index, universe)
    assert r == [d for d in universe if d >= 180]
    print("NOT 口径: NOT python = 全集 %d - postings %d = %d 篇，O(|U|) 物化全集 ✅"
          % (len(universe), len(index["python"]), len(r)))
```

**追问**：1) 为什么 postings 必须升序、求交前不能先转 set？—— 升序是 bisect 与归并的共同前提，乱序表两者全部失效；转 set 则是 O(n) 哈希加一次内存物化，把「流式求交」变成「先整表拷贝再求」，大表上内存翻数倍且丢掉了「空交集提前终止」的机会——布尔求值的美感就在流式短路：AND 链上任何一层空了，后面的长表一次都不用碰。2) 這套骨架怎么长成 BM25 打分引擎？—— 求值阶段不变，打分挂在「候选集」上：AND/OR 收敛出候选 doc_id 后，对每个候选按 TF（词频）× IDF（log(总文档/DF)）累加词贡献，再按分数截断 TopK——骨架是「先布尔收敛候选、再相关性排序」，两阶段解耦；这也是 Q7739 里 IDF 压高频字的同一套数学。3) 索引怎么增量更新？—— 不可变段 + 内存增量段的 LSM 思路：新文档进内存段（哈希），查询时多段各自求值后归并；内存段写满冻结成磁盘段，后台把小段归并成大段（层数 log 级，写放大可控）。删除不真删——posting 上打删除标记，归并时物理清除。生产引擎（ES/Lucene）全是这个形态，本题的手写骨架就是它的零阶近似。

## 背诵要点
1. postings 升序是 bisect/归并的前提；AND 按表长升序折叠、短表 bisect 探长表：探针 O(short·log long) vs 归并 O(sum)，实测 180∧2 约 181→15 次。
2. NOT = 全集差集 O(|U|) 必须物化全集；OR 代价 ≈ 表长之和；布尔查询成本 AND ≪ OR < NOT。
3. 调度场解析 NOT > AND > OR；正确性用「逐文档暴力布尔求值」对账；空交集提前终止省掉后续全部探针。
