---
title: "[Q5094] xml.etree.iterparse 流式原理与全树 OOM 容量账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5094 · xml.etree.iterparse 流式原理与全树 OOM 容量账

难度：P6 | 标签：原理深挖 | xml.etree | 容量规划

**问**：导入一个 2GB 的 XML 数据文件，`ET.parse` 直接把容器打到 OOM。为什么 ElementTree 会吃这么多内存？`iterparse` 的流式原理是什么，为什么很多人用了 iterparse 还是 OOM？

**答**：
结论：ElementTree 的 C 实现会把整个文档物化成一棵持久树——每个 Element 是独立 Python 对象（dict 存属性、list 存子节点），2GB 文档树化后内存轻松翻 5-10 倍，且构建完成前无法释放。`iterparse` 的原理是**边解析边回调**：底层 expat 逐块喂字节，每次 `end` 事件把完成的 Element 交给 Python；但根节点仍持有所有子元素的引用——所以只迭代不清理，内存照样线性涨。正确姿势是在拿到每个顶层记录后 `root.clear()`（或 `elem.clear()` 并从 root 中 pop），把引用断掉让 GC 回收。
取舍：iterparse+clear 得到恒定内存，代价是只能前向遍历、不能回溯父级（clear 后引用失效），且对"记录在深层嵌套"的文档要精确订阅正确 tag。
实战：大 XML 导入的标准模板是 `for event, elem in ET.iterparse(f, events=("end",)): if elem.tag == RECORD: process; elem.clear()`，并在外层定期 `root.clear()` 兜底；容量指标是"峰值内存与文档大小解耦"。

```python
import os, sys, tempfile
import xml.etree.ElementTree as ET

def make_xml(path, n):
    with open(path, "w", encoding="utf-8") as f:
        f.write("<records>")
        for i in range(n):
            f.write(f'<record id="{i}"><name>n{i}</name><val>{i%997}</val></record>')
        f.write("</records>")
    return path

path = make_xml(tempfile.mktemp(suffix=".xml"), 20_000)

# 错误姿势演示（小规模模拟内存线性涨）：iterparse 不清理，root 持有全部引用
def naive_iterparse(path):
    count = 0
    for _, elem in ET.iterparse(path, events=("end",)):
        if elem.tag == "record":
            count += 1          # elem 引用交给局部变量即丢，但 root 仍持有！
    return count

# 正确姿势：处理完即 clear + 从 root 摘除，内存恒定
def streaming_iterparse(path, tag="record"):
    count, total = 0, 0
    for event, elem in ET.iterparse(path, events=("end",)):
        if elem.tag == tag:
            total += int(elem.findtext("val", "0"))
            elem.clear()                     # 清空子节点与属性，断开子树
            count += 1
    return count, total

print(naive_iterparse(path), streaming_iterparse(path))

# 树化 vs 流式的内存差：同一文档 parse 全树的大小
tree = ET.parse(path)
root = tree.getroot()
import itertools
def tree_size(el):
    return sys.getsizeof(el.tag) + sys.getsizeof(el.attrib) + \
           sys.getsizeof(el) + sum(tree_size(c) for c in el)
print(f"全树对象账估算 ≈ {tree_size(root)/1e3:.0f} KB（20k 记录，随文档线性涨）")
os.unlink(path)

# 单条记录的树化开销：约 (dict+list+每 Element 对象) 数百字节起步
rec = ET.fromstring('<record id="1"><name>n</name><val>1</val></record>')
print("单 record 元素链 getsizeof ≈", sum(sys.getsizeof(x) for x in (rec, rec[0], rec[1], rec.attrib)))
```

**追问 1**：为什么 `elem.clear()` 后还要动 root？
- 追问 2 层：clear 只清空该元素自身内容，root 的 children list 仍持有它的引用；顶层记录需要在处理后从 root 里 pop，否则引用链仍在。
- 追问 3 层：iterparse 返回的 root 可以通过 `it = iter(...); next(it)` 先拿 root 再迭代事件的方式获取，`events=("start","end")` 配合可以精确知道何时摘除。

**追问 2**：除了 ElementTree，还有哪些流式方案？
- 追问 2 层：`xml.sax` 是真正的 pull 前身（push 回调），内存最省但代码最丑；`lxml.etree` 兼容 iterparse 且有 `tag` 过滤与 cleanup 参数（`lxml` 4.x+ `iterparse(..., tag=..., strip_cdata=False)`）。
- 追问 3 层：XXE/实体扩展炸弹在流式解析同样存在，expat 默认禁外部实体但内部 entity 放大仍需限制，导入端要加 `defusedxml`（第三方，3.x 全版本可用）。

## 背诵要点
1. ET.parse 全树物化，内存约为文档 5-10 倍且构建期不可释放。
2. iterparse 不等于流式省内存：root 仍持引用，必须处理完 clear + 摘除。
3. 流式代价是单向遍历，深层嵌套要精确订阅 tag；防御 XXE 用 defusedxml。

## 复盘追问
1. 为什么大 XML 比同样内容的 JSON/JSONL 更容易 OOM？——XML 必须整文档平衡后才能确认结构，JSONL 天然逐行。
2. 如果业务需要按 id 回溯已处理的记录怎么办？——把需要的字段抽成标量存外部结构（数据库/列数组），不要保留 Element 引用。
