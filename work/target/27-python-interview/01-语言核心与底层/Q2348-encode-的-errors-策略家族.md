---
title: [Q2348] encode 的 errors 策略家族
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2348 · encode 的 errors 策略家族

> 难度:★★★☆☆ | 标签:encode, errors, codecs

**问**:encode 遇到编码不了的字符,除了报错还能怎么办?各策略分别适合什么场景?

**答**:encode 的 errors 参数是一组策略:strict 默认抛 UnicodeEncodeError;ignore 静默丢字符(审计场景禁用,信息无声消失);replace 用 ? 顶替(适合日志预览);xmlcharrefreplace 把字符转成 `&#NNNN;` 实体(HTML/XML 输出专用,encode 独有);backslashreplace 转成 \xNN 转义(适合错误消息与日志,能原样还原);namereplace 转成 \N{名称}。策略还可以自定义:`codecs.register_error` 注册一个处理器,函数收到异常、返回「替换串与消费终点」二元组,就能实现星号顶替、拼音转写等业务策略。注意 encode 与 decode 的策略集不对称:xmlcharrefreplace 只属于 encode,而 decode 有自己的 surrogateescape 等选项。选型原则是「信息是否有价值」:宁可显式 replace 也不要 ignore,转义类策略保留可逆性最好。

```python
# file: code/01_语言核心与底层/q2348_encode_errors.py
"""encode 的 errors 策略对比:strict、ignore、replace 与转写家族。"""
import codecs

if __name__ == "__main__":
    text = "价格 ¥100,café"
    for policy in ["strict", "ignore", "replace",
                   "xmlcharrefreplace", "backslashreplace", "namereplace"]:
        try:
            out = text.encode("ascii", errors=policy)
        except UnicodeEncodeError as exc:
            out = f"报错: {exc.reason}"
        print(f"{policy:>18}: {out}")

    def star_replace(exc):
        """自定义策略:编码不了的字符换成星号。"""
        return ("*", exc.end)

    codecs.register_error("star", star_replace)
    print("自定义 star:", text.encode("ascii", errors="star"))

    dirty = b"caf\xe9"
    print("decode replace:", dirty.decode("ascii", errors="replace"))
    print("decode backslashreplace:", dirty.decode("ascii", errors="backslashreplace"))
```

**追问**:1) surrogateescape 是干什么的?——decode/encode 共用的「字节保真」策略:解不开的字节暂存为代理区码点,再 encode 时原样吐回字节,常用于按 ASCII 处理未知编码文件而不破坏原始数据。2) errors 家族的完整分工?——strict(默认,数据安全)、ignore/replace(展示容错)、backslashreplace(转义展示)、xmlcharrefreplace(HTML)、surrogateescape(字节保真往返)——选型按「数据 vs 展示」(Q1541)。3) 编解码的边界治理?——入口确定编码(或 chardet 启发),出口统一;两侧 errors 策略必须配对;surrogate 字符不能进 JSON/DB。4) 生产陷阱?——ignore 静默丢字节;往返用不同 errors 丢数据;把 surrogate 码点写进结构化存储崩。
