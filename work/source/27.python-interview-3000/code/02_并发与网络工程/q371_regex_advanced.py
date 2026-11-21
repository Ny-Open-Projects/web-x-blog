"""正则高级用法示例:命名分组 / 断言 / 懒惰匹配。"""
import re

LOG_PATTERN = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "   # 命名分组
    r"\[(?P<level>[A-Z]+)\] (?P<msg>.*)$"
)

if __name__ == "__main__":
    line = "2026-11-01 10:00:00 [ERROR] db connection lost"
    m = LOG_PATTERN.match(line)
    print(m.group("level"), "|", m.group("msg"))

    # 先行断言:取所有后跟 元 的 数字,数字本身不被消费
    print(re.findall(r"\d+(?=元)", "苹果5元 香蕉3元 榴莲20块"))

    # 懒惰 vs 贪婪:提取 markdown 链接
    text = "[a](x) and [b](y)"
    print(re.findall(r"\[(.*?)\]\((.*?)\)", text))  # 懒惰配对正确

    # 非捕获分组:只分组不保存
    print(re.findall(r"(?:http|https)://\S+", "go to https://example.com now"))
