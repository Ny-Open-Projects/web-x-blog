"""分片合并: 连续性校验、哈希完整性、原子落盘(纯标准库)。"""
import hashlib
import os
import tempfile


def merge_chunks(parts, total, expected_digest):
    """parts: [(start, data)]; 校验连续性与总量后合并, 返回合并字节与 sha256。"""
    parts = sorted(parts)
    cursor, buf = 0, []
    for start, data in parts:
        if start != cursor:
            raise ValueError(f"分片不连续: 期望从 {cursor} 开始, 实际 {start}")
        buf.append(data)
        cursor += len(data)
    blob = b"".join(buf)
    if len(blob) != total:
        raise ValueError(f"总长度不符: 期望 {total}, 实际 {len(blob)}")
    digest = hashlib.sha256(blob).hexdigest()
    if digest != expected_digest:
        raise ValueError("sha256 与客户端声明不符, 拒绝合并")
    return blob, digest


def atomic_write(path, blob):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(blob)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)                    # 原子改名, 半成品不会被读到


payload = b"A" * 400 + b"B" * 200 + b"C" * 400
chunks = [(0, payload[:400]), (400, payload[400:600]), (600, payload[600:])]
expected = hashlib.sha256(payload).hexdigest()

blob, digest = merge_chunks(chunks, len(payload), expected)
print("合并成功, sha256 前缀:", digest[:16], "长度:", len(blob))

target = os.path.join(tempfile.mkdtemp(), "upload.bin")
atomic_write(target, blob)
print("原子落盘:", os.path.exists(target), os.path.getsize(target))

corrupt = [(0, payload[:400]), (400, b"X" * 200), (600, payload[600:])]
try:
    merge_chunks(corrupt, len(payload), expected)
except ValueError as e:
    print("损坏分片被拒:", e)

try:
    merge_chunks([(0, payload[:400]), (600, payload[600:])], len(payload), expected)
except ValueError as e:
    print("缺口被拒:", e)
