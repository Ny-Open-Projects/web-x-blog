"""动态构建格式说明符:嵌套替换字段让 spec 也能参数化。"""


def render_table(rows, headers, widths, aligns):
    """width 与 align 由参数决定,先拼出行模板再逐行 format。"""
    fmt = " ".join("{:" + a + str(w) + "}" for a, w in zip(aligns, widths))
    print(fmt.format(*headers))
    print("-" * len(fmt.format(*headers)))
    for row in rows:
        print(fmt.format(*row))


if __name__ == "__main__":
    # 方式一:嵌套替换字段,spec 内部引用参数(fill 必须在 align 之前)
    print("{:{fill}>{width}.{prec}f}".format(3.14159, fill="*", width=10, prec=2))

    # 方式二:format_map 让 spec 引用上下文字典
    spec = "{price:>{w}.{p}f} 元"
    print(spec.format_map({"price": 12.5, "w": 8, "p": 1}))

    # 方式三:程序化拼 spec 渲染整表
    render_table(
        rows=[["cpu", 0.75], ["mem", 0.42]],
        headers=["指标", "占用"],
        widths=[6, 8],
        aligns=["<", ">"],
    )
