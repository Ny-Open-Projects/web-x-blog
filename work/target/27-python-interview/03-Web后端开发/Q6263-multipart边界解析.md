---
title: "[Q6263] multipart/form-data 的边界解析：CRLF 归属与文件名清洗"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6263 · multipart/form-data 的边界解析：CRLF 归属与文件名清洗

难度：P7 ｜ 标签：multipart、文件上传、boundary、流式解析、文件名清洗、CRLF

基线：CPython 3.12.2，纯标准库；手写一个按行边界扫描的 multipart 解析器，验证内容里出现 `--boundary` 前缀、尾部 CRLF 与文件名路径穿越。

**问**：上传接口收到一个 2MB 的二进制文件，解析后 SHA-256 总是和客户端算的不一致，差 2 字节；另一个请求的文件内容里恰好有一行以 `--boundary` 开头，`body.split(b"--" + boundary)` 把文件切成两半，后半个 part 被当成新字段。还有安全扫描报了"路径穿越"：`filename="../../etc/passwd"` 被直接拼到上传目录。multipart 的 delimiter 到底包含哪些 CRLF？内容里的 `--boundary` 为什么不能简单 split？文件名应该怎么处理？

**答**：

- **结论**：`multipart/form-data` 的分隔符不是裸的 `--boundary`，而是**行首的 `CRLF + "--" + boundary`**；第一个 part 之前可以没有前导 CRLF（body 直接以 `--boundary` 开头），之后的每个 delimiter 都带前导 CRLF。紧跟在 boundary 后面的必须是 `CRLF`（还有下一个 part）或 `--`（结束），否则它只是内容里恰好出现的字符串，不是分隔符。每个 part 的内容**不包含**结尾那个 CRLF——那个 CRLF 属于 delimiter，解析时要去掉；如果保留，文件就会多 2 字节，校验必然失败。文件名只是客户端提供的**元数据**，可能包含 `../`、绝对路径、引号、CRLF、控制字符，服务端必须 basename + 白名单清洗，并自己生成存储名。
- **取舍**：`body.split()` 最简单，但会把"内容里恰好出现的 boundary"当成分隔符，二进制文件几乎必然踩雷；正确做法是**按行扫描 delimiter**（或用一个真正的流式状态机），只在行首且后接 `CRLF`/`--` 时才切分。另一个取舍是一次性读入内存还是流式：小表单可以整块解析，大文件必须流式（边读边找 delimiter），并限制 `max_part_size`、`max_parts`，否则一个 10GB 的 part 会直接 OOM。`email` 标准库能解析 MIME，但它偏向"整块读入 + 宽松解析"，不适合不可信大文件；生产上多用框架的 streaming parser，并显式设上限。
- **实战**：事故解析器用 `split`，且保留了 part 尾部的 `\r\n`，导致①二进制内容含 boundary 前缀时被切碎；②每个文件多 2 字节。修复：① 改成"扫描 `\r\n--boundary`，校验后接 `\r\n` 或 `--`"；② 内容区间取 `[data_start, delim_index)`，不含 CRLF；③ 文件名 `os.path.basename(name.replace("\\", "/"))`，拒绝含 `\x00`/控制字符的名字，存储名用 UUID；④ 限制单 part 64MB、总 part 32 个。上线后校验失败归零，路径穿越告警归零。

下面构造两个 part（其中一个内容含 `--Xnot-a-boundary` 与尾部 CRLF），验证边界识别、内容不含尾部 CRLF、文件名清洗。

```python
# multipart 解析: delimiter = 行首 CRLF + "--" + boundary, 后接 CRLF 或 "--"
import os

BOUNDARY = b"----X"
DELIM = b"--" + BOUNDARY


def parse_headers(raw: bytes) -> dict:
    headers = {}
    for line in raw.split(b"\r\n"):
        if not line:
            continue
        name, _, value = line.partition(b":")
        headers[name.strip().lower().decode("latin-1")] = value.strip().decode("latin-1")
    return headers


def find_delimiter(body: bytes, start: int) -> int:
    """找行首的 CRLF--boundary, 且后面必须是 CRLF 或 '--'."""
    needle = b"\r\n" + DELIM
    idx = body.find(needle, start)
    while idx != -1:
        after = idx + len(needle)
        if body[after:after + 2] in (b"\r\n", b"--"):
            return idx
        idx = body.find(needle, idx + 1)
    return -1


def parse_multipart(body: bytes):
    if not body.startswith(DELIM):
        raise ValueError("body must start with --boundary")
    pos = len(DELIM)
    if body[pos:pos + 2] == b"\r\n":
        pos += 2
    parts = []
    while True:
        header_end = body.find(b"\r\n\r\n", pos)
        if header_end == -1:
            raise ValueError("unterminated part headers")
        headers = parse_headers(body[pos:header_end])
        data_start = header_end + 4
        delim_at = find_delimiter(body, data_start)
        if delim_at == -1:
            raise ValueError("unterminated part body")
        parts.append((headers, body[data_start:delim_at]))
        after = delim_at + 2 + len(DELIM)
        if body[after:after + 2] == b"--":
            break
        pos = after + 2                     # 跳过 delimiter 后的 CRLF
    return parts


def safe_filename(name: str) -> str:
    name = name.replace("\\", "/")
    name = os.path.basename(name)
    if not name or any(ord(ch) < 32 for ch in name):
        raise ValueError("invalid filename")
    return name


body = (
    b"--" + BOUNDARY + b"\r\n"
    b'Content-Disposition: form-data; name="note"\r\n'
    b"\r\n"
    b"hello\r\n--Xnot-a-boundary\r\n"
    b"--" + BOUNDARY + b"\r\n"
    b'Content-Disposition: form-data; name="file"; filename="../../etc/passwd"\r\n'
    b"Content-Type: application/octet-stream\r\n"
    b"\r\n"
    b"BINARY\x00DATA\r\n"
    b"--" + BOUNDARY + b"--\r\n"
)

parts = parse_multipart(body)
print("[1] part 数:", len(parts))
assert len(parts) == 2

note_headers, note_data = parts[0]
print("[2] note 内容:", note_data)
assert note_data == b"hello\r\n--Xnot-a-boundary", "不能把内容里的 --X 当分隔符, 也不能保留尾部 CRLF"
assert note_headers["content-disposition"].endswith('name="note"')

file_headers, file_data = parts[1]
print("[3] file 内容:", file_data)
assert file_data == b"BINARY\x00DATA"

raw_name = 'filename="../../etc/passwd"'
filename = raw_name.split("filename=", 1)[1].strip('"')
cleaned = safe_filename(filename)
print("[4] 原始文件名:", filename, "-> 清洗后:", cleaned)
assert cleaned == "passwd"

try:
    safe_filename("bad\r\nname")
    raise AssertionError("控制字符文件名应被拒绝")
except ValueError as exc:
    print("[5] 控制字符文件名 ->", exc)

print("[6] 结论: 行首 delimiter + 校验后缀 + 去尾部 CRLF + basename 清洗")
```

**追问一**：为什么 `Content-Disposition` 里的 `name` 也不能直接信？—— `name` 决定这个 part 对应哪个表单字段，攻击者可以伪造一个 `name="role"` 的 part 覆盖服务端字段，或者用重复 `name` 制造歧义（有的框架取第一个、有的取最后一个）。服务端应该按白名单接受字段名、拒绝重复、对未知字段直接丢弃；`filename` 同理，不能用来拼路径，也不能用来决定 `Content-Type` 的信任级别。

**追问二**：流式解析怎么处理"boundary 跨读缓冲"？—— 需要一个滑动窗口：保留 `len(delimiter)+4` 字节的尾部，在新数据到达时拼接后再找 delimiter；找到后只消费到 delimiter 之前，剩余字节留到下一轮。难点是"内容里的 boundary 前缀"要等后续字节到了才能判断是不是真分隔符，不能一看到 `\r\n--X` 就切。工程上更稳的是用成熟库（如 `python-multipart`），但也要设 `max_part_size`、`max_file_size`、`max_fields`，否则解析器本身就是 DoS 面。

## 背诵要点

- delimiter = 行首 `CRLF + "--" + boundary`，后接 `CRLF`（继续）或 `--`（结束）；内容里的裸 `--boundary` 不是分隔符。
- part 内容**不含**结尾 CRLF，它属于 delimiter；保留会多 2 字节、校验失败。
- `filename` 只当元数据：basename + 控制字符校验 + 服务端生成存储名；流式解析要限制 part 大小/数量。

## 复盘追问

- 为什么 `body.split(b"--" + boundary)` 对二进制上传几乎必坏？（内容里任意位置出现该字节序列都会被切开，且不校验行首/后缀）
- 如果 boundary 出现在文件内容且恰好是行首 `--boundary\r\n`，解析器该怎么办？（按协议它就是分隔符，客户端必须选一个内容中不出现的 boundary；服务端无法区分，只能按协议切）
