"""pathlib 的解析陷阱:斜杠拼接、后缀、点点与相对化。"""
import pathlib


if __name__ == "__main__":
    base = pathlib.PurePosixPath("/var/log")
    print("绝对路径右操作数整体替换:", base / "/etc/conf")
    print("想追加必须用相对片段:", base / "app" / "app.log")

    arch = pathlib.PurePosixPath("backup.tar.gz")
    print("suffix 只取最后一段:", arch.suffix, "| stem 是:", arch.stem)
    print("完整后缀链:", arch.suffixes)

    weird = pathlib.PurePosixPath("a/../b")
    print(".. 不被词法消解:", list(weird.parts), "| resolve 会连同 cwd 消解:",
          pathlib.Path("a/../b").resolve())

    try:
        pathlib.PurePosixPath("a/b").relative_to("c")
    except ValueError as e:
        print("relative_to 严格前缀:", str(e)[:44], "...")
    print("正确用法:", pathlib.PurePosixPath("/var/log/app.log").relative_to("/var"))
