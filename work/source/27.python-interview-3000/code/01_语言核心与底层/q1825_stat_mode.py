"""stat 模块:st_mode 位掩码与类型判断。"""
import os
import stat as st
import tempfile


def describe(path):
    s = os.stat(path)
    kinds = [(st.S_ISDIR, "目录"), (st.S_ISREG, "普通文件"),
             (st.S_ISLNK, "符号链接")]
    kind = next(label for test, label in kinds if test(s.st_mode))
    return kind, st.filemode(s.st_mode), s.st_size


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as root:
        f = os.path.join(root, "a.txt")
        d = os.path.join(root, "sub")
        os.mkdir(d)
        with open(f, "w") as fh:
            fh.write("hello")
        os.chmod(f, 0o640)
        print("文件:", describe(f))
        print("目录:", describe(d))
        print("权限位:", oct(os.stat(f).st_mode & 0o777), "| 类型位:",
              oct(os.stat(f).st_mode & 0o170000))
