"""Range 分片上传协议: Content-Range 登记、缺口计算与断点续传(纯标准库)。"""


class ChunkUpload:
    """服务端上传会话: 记录已落盘的闭区间列表。"""

    def __init__(self, total):
        self.total = total
        self.received = []                      # [(start, end)] 闭区间

    def put_chunk(self, content_range):
        """PUT 分片: Content-Range: bytes start-end/total。"""
        unit, rng = content_range.split()
        if unit != "bytes":
            return 400, "仅支持 bytes 单位"
        part, total = rng.split("/")
        if total != str(self.total):
            return 400, "total 与会话不符"
        start, end = (int(x) for x in part.split("-"))
        if start > end or end >= self.total:
            return 416, "区间越界"
        self.received.append((start, end))
        return 201, {"received": sorted(self.received)}

    def missing_ranges(self):
        """HEAD 查询: 已收区间之外就是缺口, 客户端按缺口补发。"""
        missing, cursor = [], 0
        for start, end in sorted(self.received):
            if start > cursor:
                missing.append((cursor, start - 1))
            cursor = max(cursor, end + 1)
        if cursor < self.total:
            missing.append((cursor, self.total - 1))
        return missing


up = ChunkUpload(1000)
print("发 0-399:", up.put_chunk("bytes 0-399/1000"))
print("乱序发 600-999:", up.put_chunk("bytes 600-999/1000"))
print("发越界片:", up.put_chunk("bytes 900-1200/1000"))
print("HEAD 查缺口:", up.missing_ranges())
print("按缺口补发 400-599:", up.put_chunk("bytes 400-599/1000")[0])
print("缺口清零:", up.missing_ranges(), "-> 可以调用合并")
