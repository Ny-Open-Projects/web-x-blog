"""原子写文件:tempfile + fsync + os.replace。"""
import json
import os
import tempfile


def atomic_write(path, data: str, encoding="utf-8"):
    dir_ = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(dir=dir_, prefix=".tmp_")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())  # 强制落盘,防断电丢数据
        os.replace(tmp, path)     # 原子替换,读者不会看到半成品
    except BaseException:
        os.unlink(tmp)            # 失败清理临时文件
        raise


if __name__ == "__main__":
    path = "/tmp/app_config.json"
    atomic_write(path, json.dumps({"version": 1, "host": "db-1"}))
    with open(path) as f:
        print("read back:", f.read())
    # 重复原子写,模拟更新
    atomic_write(path, json.dumps({"version": 2, "host": "db-2"}))
    with open(path) as f:
        print("updated  :", f.read())
