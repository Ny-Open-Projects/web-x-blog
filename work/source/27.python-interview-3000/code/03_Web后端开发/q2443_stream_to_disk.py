"""大文件上传的流式落盘: 分块写入 边写边算哈希 超限熔断(纯标准库)。"""
import hashlib
import os
import tempfile

CHUNK = 64 * 1024


def stream_to_disk(chunks, max_bytes):
    """逐块写临时文件, 返回 (路径, 字节数, 摘要或原因)。"""
    digest = hashlib.sha256()
    written = 0
    fh = tempfile.NamedTemporaryFile(delete=False, suffix=".upload")
    path = fh.name
    try:
        for chunk in chunks:
            if written + len(chunk) > max_bytes:
                fh.close()
                os.unlink(path)
                return None, written, "超限熔断: 将写入 {} 字节, 超过上限 {}".format(
                    written + len(chunk), max_bytes)
            fh.write(chunk)
            digest.update(chunk)
            written += len(chunk)
        fh.close()
        return path, written, digest.hexdigest()
    except BaseException:
        fh.close()
        if os.path.exists(path):
            os.unlink(path)
        raise


def fake_upload(total_mb, seed=42):
    """确定性伪数据流, 模拟客户端逐块上传。"""
    sent = 0
    block = bytes(range(256)) * 256                # 64KB 确定性块
    while sent < total_mb * 1024 * 1024:
        n = min(CHUNK, total_mb * 1024 * 1024 - sent)
        yield block[:n]
        sent += n


# 场景一: 3MB 正常上传
path, size, digest = stream_to_disk(fake_upload(3), max_bytes=10 * 1024 * 1024)
expect = hashlib.sha256(b"".join(fake_upload(3))).hexdigest()
print("正常上传: size={} 摘要前16位={}".format(size, digest[:16]))
assert size == 3 * 1024 * 1024 and digest == expect
os.unlink(path)

# 场景二: 上限 1MB, 第 17 块触发熔断, 半成品不落盘
path2, size2, reason = stream_to_disk(fake_upload(3), max_bytes=1024 * 1024)
print("受限上传: size={} 原因={}".format(size2, reason))
assert path2 is None and size2 == 1024 * 1024
assert "超限熔断" in reason
print("要点: 上传落盘只认 内存安全 的流式三件套 定长块 边写边哈希 超限即删临时文件, "
      "永远不要 request.read() 一次吞下整个文件")
