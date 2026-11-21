"""pyc 失效判定:解析 16 字节头部,对照源文件 stat。"""
import importlib.util
import os
import py_compile
import struct
import tempfile


def read_pyc_header(pyc_path):
    raw = open(pyc_path, "rb").read(16)
    magic, flags, src_mtime, src_size = struct.unpack("<IIII", raw)
    return magic, flags, src_mtime, src_size


if __name__ == "__main__":
    tmp = tempfile.mkdtemp()
    src = os.path.join(tmp, "m.py")
    with open(src, "w") as f:
        f.write("VALUE = 1\n")

    pyc = py_compile.compile(src)
    magic, flags, src_mtime, src_size = read_pyc_header(pyc)
    st = os.stat(src)

    print("缓存路径:", pyc)
    print("magic 匹配解释器:",
          magic == struct.unpack("<I", importlib.util.MAGIC_NUMBER)[0])
    print("flags(0 即时间戳校验):", flags)
    print("mtime 一致:", src_mtime == int(st.st_mtime))
    print("size 一致:", src_size == st.st_size)

    # 模拟源文件变更:mtime 后移,头部立刻过期
    old = st.st_mtime
    os.utime(src, (old - 1000, old - 1000))
    _, _, src_mtime, _ = read_pyc_header(pyc)
    print("源文件回拨后 mtime 一致:",
          src_mtime == int(os.stat(src).st_mtime), "-> 触发重编译")
