"""try 的最小化范围:只包裹会失败的那一句,else 走成功路径。"""
import json


def process(data):
    return data["count"] * 2


def parse_bad(raw):
    """反例:大段逻辑在 try 里,内部 bug 被吞。"""
    try:
        data = json.loads(raw.decode("utf-8"))
        return process(data)
    except Exception:
        return None


def parse_good(raw):
    """正例:try 只包解析,else 放成功逻辑。"""
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        print("    格式问题:", exc)
        return None
    else:
        return process(data)      # 内部异常正常外抛,不背锅


if __name__ == "__main__":
    print("好版本-正常输入:", parse_good(b'{"count": 21}'))
    print("好版本-坏输入:", parse_good(b'{"count": }'))
    try:
        parse_good(b'{"cnt": 21}')
    except KeyError as exc:
        print("内部 bug 正常暴露:", exc)
    print("坏版本-内部 bug 被吞:", parse_bad(b'{"cnt": 21}'))
