---
title: [Q2349] removeprefix 与 removesuffix:3.9 的前后缀新解
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2349 · removeprefix 与 removesuffix:3.9 的前后缀新解

> 难度:★★☆☆☆ | 标签:str, 3.9 新特性, API

**问**:去掉文件名后缀或 URL 前缀,为什么要用 3.9 新增的这两个方法而不用切片或 strip?

**答**:旧写法各有暗坑:`s[len(p):]` 不判断前缀存在与否,直接切会切错;`startswith` + 切片要写两步还容易复制粘贴错;`lstrip("test_")` 最危险——它按「字符集合」从左剥离,只要字符在集合里就一直剥,会把前缀之外的字符也剥掉。3.9 的 `removeprefix`/`removesuffix` 语义精确:前缀/后缀匹配则去掉,不匹配原样返回,幂等且安全,天然适合链式处理多级后缀(如 a.tar.gz)。实现上它们等价于官方替你写好的那个 if + 切片,没有性能开销。迁移建议:代码库中出现「先 startswith 再切片」的地方都可以替换;strip 家族继续用于「去空白」,两者职责不再混淆。

```python
# file: code/01_语言核心与底层/q2349_remove_affix.py
"""3.9 的 removeprefix/removesuffix:替代裸切片与 strip 误用。"""
import sys

if __name__ == "__main__":
    print("Python 版本:", sys.version.split()[0])
    filename = "report_2024_final.pdf"
    print("removeprefix:", filename.removeprefix("report_"))
    print("removesuffix:", filename.removesuffix(".pdf"))
    print("前缀不存在原样返回:", "data.csv".removeprefix("report_"))

    old = filename[len("report_"):] if filename.startswith("report_") else filename
    print("旧写法等价但啰嗦:", old)

    print("lstrip 按字符集剥离会剥过头:", "testest_value".lstrip("test_"))
    print("removeprefix 语义精确:", "testest_value".removeprefix("test_"))

    for name in ["a.tar.gz", "b", "c.txt"]:
        print(name, "->", name.removesuffix(".gz").removesuffix(".tar"))
```

**追问**:1) 为什么没有 removemiddle 之类的对称方法?——前缀后缀是「边界语义」,切片可精确表达;中间内容的删除依赖具体业务规则,交给 replace 或正则更合适。2) 与 startswith/endswith 的配合?——removeprefix 幂等:有则删无则原样;旧写法 `if s.startswith(p): s = s[len(p):]` 的样板代码就此消失;空串安全。3) 版本与兼容?——3.9+ 才有;旧版本写条件切片;替换 strip(p) 的误用(strip 是字符集语义不是前缀语义——strip("ab") 会删两侧任意 a/b 字符)。4) 生产陷阱?——用 strip 删前缀(语义错,高频笔误);replace 误删中间多次出现;对长度为零前缀的边界假设。
