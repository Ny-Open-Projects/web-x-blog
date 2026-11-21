"""doctest:把文档示例变成可执行测试。"""
import doctest


def slugify(text):
    """把标题转成 slug。

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("  A  B  ")
    'a-b'
    >>> slugify("")
    Traceback (most recent call last):
        ...
    ValueError: 空文本无法生成 slug
    """
    cleaned = "-".join(text.lower().split())
    if not cleaned:
        raise ValueError("空文本无法生成 slug")
    return cleaned


if __name__ == "__main__":
    fails, total = doctest.testmod(verbose=False)
    print(f"doctest 用例 {total} 个,失败 {fails} 个")
    print("文档即测试:示例与实现一起腐烂或一起存活")
