"""textwrap:帮助文本的换行、缩进与截断。"""
import textwrap

BRIEF = ("本工具将大 CSV 文件按行数拆分为多个分片,"
         "支持自定义分隔符与编码,用于把大文件切成可并行处理的小块。")


def wrap_help(width=40):
    return textwrap.fill(BRIEF, width=width,
                         initial_indent="  ", subsequent_indent="  ")


def dedent_compare():
    raw = """\
        用三引号写的文档
        带着源码缩进粘进来。
    """
    return textwrap.dedent(raw)


def short_usage(width=30):
    return textwrap.shorten(BRIEF, width=width, placeholder="……")


if __name__ == "__main__":
    print(wrap_help())
    print("--- dedent ---")
    print(dedent_compare())
    print("--- shorten ---")
    print(short_usage())
