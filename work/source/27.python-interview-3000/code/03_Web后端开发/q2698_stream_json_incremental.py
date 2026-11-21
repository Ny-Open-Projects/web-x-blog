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
