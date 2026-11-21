"""Q2857 请求日志的键值双模式脱敏:递归遍历与命中统计。

LLM 请求体里既有密钥字段又有用户随手贴的身份证 手机号,只按字段名
脱敏会漏自由文本,只按正则会漏结构化字段。双模式:键名命中直接打码,
字符串值再做模式匹配,全部递归,命中数进统计便于审计。
"""

import copy
import re

SENSITIVE_KEYS = {"api_key", "password", "authorization", "token", "secret"}
PHONE_RE = re.compile(r"1[3-9]\d{9}")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def mask_node(node, stats):
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k.lower() in SENSITIVE_KEYS:
                out[k] = "***"
                stats["by_key"] += 1
            else:
                out[k] = mask_node(v, stats)
        return out
    if isinstance(node, list):
        return [mask_node(x, stats) for x in node]
    if isinstance(node, str):
        s = PHONE_RE.sub("<phone>", node)
        s = EMAIL_RE.sub("<email>", s)
        if s != node:
            stats["by_value"] += 1
        return s
    return node


def mask_request(req):
    stats = {"by_key": 0, "by_value": 0}
    return mask_node(copy.deepcopy(req), stats), stats


def main():
    req = {
        "api_key": "sk-abcdef123456",
        "tenant": "t_acme",
        "messages": [
            {"role": "user",
             "content": "帮我联系 张三 13812345678, 邮箱 zs@corp.com 处理"},
        ],
        "meta": {"token": "tk_9", "nested": {"password": "p@ss"}},
    }
    masked, stats = mask_request(req)
    assert masked["api_key"] == "***", masked
    assert masked["meta"]["token"] == "***" and masked["meta"]["nested"]["password"] == "***"
    body = masked["messages"][0]["content"]
    assert "13812345678" not in body and "<phone>" in body, body
    assert "zs@corp.com" not in body and "<email>" in body, body
    assert masked["tenant"] == "t_acme"   # 正常字段不动
    assert req["api_key"] == "sk-abcdef123456"  # 原对象未被污染
    assert stats == {"by_key": 3, "by_value": 1}, stats
    print("脱敏后正文:", body)
    print("命中统计:", stats)


if __name__ == "__main__":
    main()
