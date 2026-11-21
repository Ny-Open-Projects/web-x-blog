"""zipfile:压缩包的读取、校验与流式解压。"""
import os
import tempfile
import zipfile


def build_archive(path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("docs/readme.txt", "第一版内容,足够长以便压缩生效")
        zf.writestr("docs/api.txt", "接口说明")
        zf.writestr("data/rows.csv", "id,name\n1,ada\n")


def inspect_archive(path):
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        info = zf.getinfo("docs/readme.txt")
        crc_ok = zf.testzip() is None          # None 表示全部成员 CRC 通过
        return names, info.file_size, info.compress_size, crc_ok


def stream_member(path, member, nbytes=12):
    with zipfile.ZipFile(path) as zf:
        with zf.open(member) as fh:            # 按成员流式读,不解压整个包
            return fh.read(nbytes).decode("utf-8")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        path = os.path.join(root, "demo.zip")
        build_archive(path)
        names, raw, comp, ok = inspect_archive(path)
        print("成员列表:", names)
        print("readme 原始/压缩字节:", raw, comp, "| CRC 全通过:", ok)
        print("流式读前 12 字节:", stream_member(path, "docs/readme.txt"))
