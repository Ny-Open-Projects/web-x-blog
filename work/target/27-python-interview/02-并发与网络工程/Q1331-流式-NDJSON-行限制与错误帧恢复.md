---
title: [Q1331] 流式 NDJSON:行限制与错误帧恢复
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1331 · 流式 NDJSON:行限制与错误帧恢复

> 难度:★★☆☆ | 标签:NDJSON, 流式解析, 错误恢复

**问**:NDJSON(每行一个 JSON)是最简单的流协议,解析器还有哪些必须设防的点?

**答**:三个。一,行缓冲上限:恶意对端只发不换行的字节,不设上限的解析器会无限攒内存——超过 max_line 就断连,这是"半包等待"必须配的护栏;二,坏行隔离:某一行 JSON 非法,应该记下错误、跳过这一行继续解析后面的,而不是让整个流报废——NDJSON 的行天然就是恢复边界,这是它优于自研二进制协议的地方;三,空白与截断:空行要跳过,行内截断的 JSON(解析失败)不能被当成"等待更多数据",因为换行符已经明确它是完整一行。下面的演示把合法流按任意碎片喂入,混入坏行与超长行,验证合法数据无损、坏行被隔离计数。

```python
# file: code/02_并发与网络工程/q1331_ndjson_stream.py
import json


class LineTooLong(Exception):
    pass


class NDJSONReader:
    def __init__(self, max_line: int = 64) -> None:
        self._buf = bytearray()
        self._max = max_line
        self.bad_lines = 0

    def feed(self, data: bytes) -> list:
        self._buf.extend(data)
        out = []
        while True:
            nl = self._buf.find(b"\n")
            if nl < 0:
                if len(self._buf) > self._max:
                    raise LineTooLong(f"未换行字节 {len(self._buf)} 超过上限 {self._max}")
                break                      # 半行: 继续等
            line = bytes(self._buf[:nl])
            del self._buf[:nl + 1]         # 每轮必消费
            if not line.strip():
                continue                   # 空行跳过
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                self.bad_lines += 1        # 坏行隔离: 记账继续
                out.append({"__bad__": line.decode(errors="replace")[:32]})
        return out


def main() -> None:
    good = [{"i": i, "v": i * 2} for i in range(6)]
    stream = b""
    stream += b'{"i":0,"v":0}\n{"i":1,"v":2}\n'      # 两行合法
    stream += b'{"i":2,"v":\n{"i":3,"v":6}\n'         # 一行坏 JSON + 一行合法
    stream += b'\n{"i":4,"v":8}\n'                    # 空行 + 合法
    stream += b'{"i":5,"v":10'                        # 结尾半行等待

    reader = NDJSONReader(max_line=64)
    parsed = []
    pos = 0
    while pos < len(stream):                          # 任意碎片喂入
        step = (pos * 7 + 3) % 9 + 1
        parsed.extend(reader.feed(stream[pos:pos + step]))
        pos += step

    bad = [p for p in parsed if "__bad__" in p]
    good_parsed = [p for p in parsed if "__bad__" not in p]
    print(f"解析出 {len(parsed)} 个结果, 其中坏行 {len(bad)} 个被隔离")
    print("坏行样本:", bad[0] if bad else None)
    assert len(bad) == 1 and reader.bad_lines == 1
    assert good_parsed == [good[0], good[1], good[3], good[4]], \
        "坏行前后的合法行必须无损(坏行本身不产出数据)"

    tail = reader.feed(b'}\n')                        # 半行补齐
    good_parsed.extend([p for p in tail if "__bad__" not in p])
    assert good_parsed == good[:2] + good[3:], \
        "半行补齐后最后一行也要解析出来(坏行 i=2 永久缺失属预期)"
    print("全部合法行最终完整解析, 顺序不变")

    # 无限不换行必须被上限拦截
    r2 = NDJSONReader(max_line=16)
    try:
        r2.feed(b"x" * 100)
        print("超长行漏过!")
    except LineTooLong as exc:
        print(f"超长行被拦截: {exc}")


if __name__ == "__main__":
    main()
```

**追问**:1) 坏行该静默跳过还是断连?——取决于协议契约:日志类单向流可以跳过+告警;交易类双向流必须断连重同步,因为"带病继续"会让双方对状态的理解慢慢分叉。2) NDJSON 的行为什么天然是恢复边界?——换行符定界让「坏行」的范围确定,跳过即可继续;二进制协议(长度前缀/定界符)坏一帧后边界可能全错,只能断连重同步——「恢复能力」是选文本流协议的核心理由之一。3) 断连重同步的完整动作?——清理半包状态(Q1322 的 reset)→记错误与字节量→重连(带退避抖动 Q1335)→重放未确认请求(若协议支持);「带病继续」在交易类流里让双方状态分叉,越走越远。4) 生产陷阱?——行缓冲无上限(只发不换行的对端撑爆内存);把截断 JSON 当「等更多数据」(换行已确认是完整一行,解析失败就是坏行);空行被当 JSON 解析炸出异常;坏行计数没告警,错误率悄悄上涨没人发现。

---
