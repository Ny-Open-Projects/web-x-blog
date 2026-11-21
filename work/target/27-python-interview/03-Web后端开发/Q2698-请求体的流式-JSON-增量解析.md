---
title: [Q2698] 请求体的流式 JSON 增量解析
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2698 · 请求体的流式 JSON 增量解析

> 难度:★★★★ | 标签:流式解析, JSON, 性能

**问**:客户端一次 POST 十万条记录的大 JSON 数组,不想等全部收完再处理,怎么边收边解析?

**答**:核心是"缓冲 + raw_decode"循环:chunk 追加进缓冲,用 `JSONDecoder.raw_decode` 尝试解码,成功就吐出一个完整对象并前移偏移;抛 JSONDecodeError 说明半个对象没到齐,静默等下一块。两种形态:JSON 数组流式解析要自己消费元素间的逗号与收尾的右括号;NDJSON(每行一个对象)实现最简单也最抗错,坏行只影响自己。收益两条:内存峰值从全量字符串降到单块大小,首条处理时间提前到第一个对象就绪。框架层对应 FastAPI 的流式请求体与生成器消费,语义一致;字符串里的逗号右括号不会误判,因为只有处于值之间的位置才检查分隔符。

```python
# file: code/03_Web后端开发/q2698_stream_json_incremental.py
"""请求体的流式 JSON 增量解析: 边收边出, 不必等整个报文(纯标准库)。"""
import json


class ArrayStreamParser:
    """流式解析一个 JSON 数组: 每喂一段 chunk, 返回本轮凑齐的完整元素。

    关键点: 用 raw_decode 在缓冲区上尝试解码, 解不动说明数据还没到齐,
    静默等下一块; 元素间的逗号与收尾的右括号在值之间消费。
    """

    def __init__(self):
        self.buf = ""
        self.started = False
        self.finished = False
        self.dec = json.JSONDecoder()

    def feed(self, chunk):
        self.buf += chunk if isinstance(chunk, str) else chunk.decode("utf-8")
        out = []
        while not self.finished:
            self.buf = self.buf.lstrip()
            if not self.buf:
                break
            if not self.started:
                if self.buf[0] != "[":
                    raise ValueError("顶层必须是 JSON 数组")
                self.started = True
                self.buf = self.buf[1:].lstrip()
                continue
            if self.buf[0] == "]":
                self.finished = True
                self.buf = self.buf[1:]
                break
            if self.buf[0] == ",":
                self.buf = self.buf[1:]
                continue
            try:
                obj, end = self.dec.raw_decode(self.buf)
            except json.JSONDecodeError:
                break  # 半个对象, 等下一块
            out.append(obj)
            self.buf = self.buf[end:]
        return out


def ndjson_feed(lines_iter):
    """NDJSON 形态: 每行一个独立 JSON 对象, 增量语义最简单也最抗错。"""
    for line in lines_iter:
        line = line.strip()
        if line:
            yield json.loads(line)


payload = json.dumps(
    [{"id": i, "name": "item%d" % i, "note": "],配,"} for i in range(50)],
    ensure_ascii=False,
)
parser = ArrayStreamParser()
got = []
for i in range(0, len(payload), 17):  # 故意按 17 字节硬切, 跨对象边界
    got.extend(parser.feed(payload[i:i + 17]))
assert parser.finished and got == json.loads(payload), (len(got), parser.finished)
print("数组增量解析: %d 个对象, 与整体解码结果一致" % len(got))

nd = '{"a":1}\n{"b":2}\n\n{"c":3}\n'
assert list(ndjson_feed(nd.splitlines(keepends=True))) == [{"a": 1}, {"b": 2}, {"c": 3}]
bad = ArrayStreamParser()
try:
    bad.feed('{"x":1')
except ValueError as e:
    print("NDJSON 跳过空行通过; 顶层数组约束生效:", e)
```

**追问**:
- 为什么不直接对缓冲反复 json.loads?——整缓冲 loads 要等全量且失败后无法定位已完成部分;raw_decode 恰好返回消费偏移,这是流式语义的关键。
- 解析到非法 JSON 怎么终止?——顶层数组约束在第一个字节就拒绝,元素级错误在 raw_decode 持续失败且连接结束时以 400 收尾。
