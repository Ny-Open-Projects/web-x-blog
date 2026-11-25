---
title: "[Q7721] 流式输出把 emoji 切成两半：UTF-8 跨 chunk 解码"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7721 · 流式输出把 emoji 切成两半：UTF-8 跨 chunk 解码

难度：P6 ｜ 标签：流式输出、UTF-8、增量解码、SSE

基线：Python 3.12；`codecs.getincrementaldecoder('utf-8')`；SSE / httpx stream。

**问**：流式输出中文和 emoji 时，线上偶发 `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf0 in position 0: unexpected end of data`，日志里还出现 "�" 乱码。同一段文本短的时候完全正常，只有长回复、移动端弱网时炸。文本是按字符流传输的，为什么按 chunk 解码会坏？

**答**：
- **结论**：HTTP chunk / SSE 的边界是**字节边界**，不是字符边界。UTF-8 的一个字符占 1-4 字节，emoji（如 😀）是 4 字节；网络层完全可能在**第 2 个字节处切断**。对每个 chunk 独立 `decode('utf-8')`，遇到不完整的多字节序列就抛 `UnicodeDecodeError`；用 `errors='ignore'` 则会静默丢字符，变成乱码/缺字。正确做法是**增量解码器**：把上一次未完成的字节缓存到下一次，凑齐一个完整字符再输出。
- **取舍**：增量解码（`codecs.getincrementaldecoder` / `TextDecoder(stream=True)`）零丢失、零额外拷贝，是标准解；`errors='replace'` 能避免崩溃但会产出 "�"，不能用于要展示/入库的文本；按"行"读取（`readline`/SSE 的 `\n\n` 分帧）能降低概率，但**不能保证**——一行内部仍可能被 TCP 分段，且大模型输出不一定按行 flush。
- **实战**：① 服务端统一用增量解码器，`final=True` 时 flush 残余字节；② SSE 解析要按 `\n\n` 分帧、按 `data:` 取载荷，不能按 chunk 直接当消息；③ 客户端（浏览器 `TextDecoder`、Go `bufio`）同样要开流式模式；④ 入库前校验替换字符 `\ufffd` 的比例，异常升高说明链路上有错误解码。

```python
"""按字节切流：直接 decode 会炸，增量解码器能跨 chunk 拼回字符。"""
import codecs

TEXT = "你好😀世界🚀end"


def naive_decode(chunks: list[bytes]) -> list[str]:
    out = []
    for c in chunks:
        try:
            out.append(c.decode("utf-8"))
        except UnicodeDecodeError as e:
            out.append(f"<ERROR:{e.reason}>")
    return out


def incremental_decode(chunks: list[bytes]) -> str:
    decoder = codecs.getincrementaldecoder("utf-8")()
    return "".join(decoder.decode(c) for c in chunks) + decoder.decode(b"", final=True)


if __name__ == "__main__":
    raw = TEXT.encode("utf-8")
    # 故意在 emoji 的中间切：每 5 字节一刀
    chunks = [raw[i:i + 5] for i in range(0, len(raw), 5)]
    print("chunk 数:", len(chunks), "首块:", chunks[0])

    print("逐块 decode:", naive_decode(chunks))
    print("增量 decode:", incremental_decode(chunks))
    print("是否还原:", incremental_decode(chunks) == TEXT)

    bad = b"".join(chunks).decode("utf-8", errors="replace")
    print("errors=replace 的替换符数量:", bad.count("\ufffd"))
    print("结论：流式文本必须用增量解码器，不能按 chunk 独立 decode")
```

**追问一**：SSE 是按字节分帧还是按行分帧？为什么"按行读"仍可能出错？
→ 解析：SSE 规范用空行（`\n\n`）分隔事件，载荷是 `data:` 行，逻辑上是**文本行**；但传输层仍是字节流，TCP/代理可以在任意字节处切分，读取方必须先做增量解码再按行切。若直接对每个网络 chunk 调 `split("\n\n")`，既可能切坏多字节字符，也可能把一行拆到两个 chunk 导致事件解析失败。

**追问二**：为什么 `errors='ignore'` 比崩溃更危险？
→ 解析：它把非法字节**静默丢弃**，长度、内容、引用编号都可能错位，且不会触发告警；对 RAG 引用、代码块、金额等场景是数据正确性问题。崩溃至少能被监控发现，静默丢字往往到用户投诉才暴露。生产应使用增量解码 + 对 `\ufffd` 计数告警。
