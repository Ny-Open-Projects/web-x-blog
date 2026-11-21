"""按大小切割的日志写入器: 轮转移位与上限保留(纯标准库)。"""
import os
import tempfile


class SizedRotatingWriter:
    """超过 max_bytes 就轮转: 当前 -> .1 -> .2, 超过 backups 份即丢弃最旧。"""

    def __init__(self, path, max_bytes, backups=3):
        self.path, self.max_bytes, self.backups = path, max_bytes, backups
        self.fh = open(self.path, "a", encoding="utf-8")

    def _rotate(self):
        self.fh.close()
        for i in range(self.backups - 1, 0, -1):  # 从最旧开始右移
            src = "{}.{}".format(self.path, i)
            dst = "{}.{}".format(self.path, i + 1)
            if os.path.exists(src):
                os.replace(src, dst)
        os.replace(self.path, self.path + ".1")   # 原子改名, 不丢行
        self.fh = open(self.path, "a", encoding="utf-8")

    def write(self, line):
        data = line if line.endswith("\n") else line + "\n"
        if self.fh.tell() + len(data.encode("utf-8")) > self.max_bytes:
            self._rotate()
        self.fh.write(data)
        self.fh.flush()

    def close(self):
        self.fh.close()


tmpdir = tempfile.mkdtemp()
path = os.path.join(tmpdir, "app.log")
writer = SizedRotatingWriter(path, max_bytes=60, backups=3)
for i in range(1, 13):
    writer.write("log-line-{:02d} padding".format(i))
writer.close()

files = sorted(f for f in os.listdir(tmpdir) if f.startswith("app.log"))
print("产生的文件:", files)
for name in files:
    with open(os.path.join(tmpdir, name), "rb") as fh:
        first = fh.readline().decode().strip()
    print("  {} 首行: {}".format(name, first))

assert "app.log" in files and "app.log.1" in files
assert "app.log.4" not in files, "最多保留 backups 份历史"
assert os.path.getsize(path) <= 60 + 21, "当前文件不超过一个上限行"
with open(path + ".1", encoding="utf-8") as fh:
    assert fh.readline().startswith("log-line-")
print("要点: 轮转三步 右移历史 原子改名当前 重开新文件; "
      "保留份数封顶磁盘占用, tell 加行宽判断让单行也不会撑破预算")
