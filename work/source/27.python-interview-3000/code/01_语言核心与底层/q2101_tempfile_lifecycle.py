"""tempfile:临时资源的安全生命周期与自动清理。"""
import os
import pathlib
import tempfile


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="job-", suffix=".d") as tmp:
        work = pathlib.Path(tmp) / "out.txt"
        work.write_text("hello", encoding="utf-8")
        print("目录内写入:", work.read_text())
    print("with 结束自动清理:", not pathlib.Path(tmp).exists())

    fd, path = tempfile.mkstemp(suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write("{}")
        print("mkstemp 需自管生命周期:", pathlib.Path(path).stat().st_size, "字节")
    finally:
        os.remove(path)
    print("手动删除后:", not os.path.exists(path))

    with tempfile.NamedTemporaryFile("w+", suffix=".log", delete=True) as nf:
        nf.write("log line")
        nf.flush()
        print("NamedTemporaryFile 随 with 结束删除:", nf.name)
