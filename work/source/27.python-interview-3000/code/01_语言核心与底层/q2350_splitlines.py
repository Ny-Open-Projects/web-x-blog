"""splitlines 的边界:识别哪些换行、行尾空行与 split 的差异。"""

if __name__ == "__main__":
    text = "a\nb\r\nc\rd\x85e\u2028f"
    print("转义视图:", text.encode("unicode_escape"))
    print("splitlines:", text.splitlines())
    print("split('\\n'):", text.split("\n"))
    print("keepends:", text.splitlines(keepends=True))

    nl = "a\nb\n"
    print("splitlines 无空尾行:", nl.splitlines())
    print("split 有空尾行:", nl.split("\n"))

    body = "姓名,年龄\n张三,20\n李四,30\n"
    rows = [line.split(",") for line in body.splitlines() if line]
    print("解析结果:", rows)
