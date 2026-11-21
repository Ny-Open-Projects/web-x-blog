"""Q2867 请求指纹的归一化:空白 角色与易变字段不进哈希。

给请求做精确缓存,指纹必须「语义相同则指纹相同」:多一个空格 角色名
大小写 换了 request_id,都不该改变指纹;但正文差一个字必须不同。
归一化规则要明确到每个字段,否则缓存命中率永远是个谜。
"""

import hashlib
import json
import re

VOLATILE = {"request_id", "timestamp", "user_id"}


def norm_messages(messages):
    out = []
    for m in messages:
        role = m.get("role", "user").strip().lower()
        content = re.sub(r"\s+", " ", m.get("content", "")).strip()
        out.append([role, content])
    return out


def fingerprint(messages, extra=None):
    clean_extra = {k: v for k, v in (extra or {}).items()
                   if k not in VOLATILE}
    payload = json.dumps({"m": norm_messages(messages), "x": clean_extra},
                         ensure_ascii=False, separators=(",", ":"),
                         sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def main():
    base = [
        {"role": "System", "content": "你是  客服助手 "},
        {"role": "user", "content": "退货政策  是什么"},
    ]
    variant = [
        {"role": "system", "content": "你是 客服助手"},
        {"role": "user", "content": "退货政策 是什么"},
    ]
    fp1 = fingerprint(base, extra={"request_id": "aaa", "timestamp": 1})
    fp2 = fingerprint(variant, extra={"request_id": "bbb", "timestamp": 2})
    assert fp1 == fp2, (fp1, fp2)   # 空白 大小写 易变字段都不影响
    diff = [{"role": "user", "content": "退货政策是什么?"}]  # 多个问号
    assert fingerprint(diff) != fp1
    # 易变字段白名单外的字段参与指纹:温度不同就是不同请求
    assert fingerprint(base, extra={"temperature": 0.2}) != \
        fingerprint(base, extra={"temperature": 0.7})
    print("语义相同的两个请求指纹:", fp1, fp2, "相同:", fp1 == fp2)
    print("正文有差异的指纹不同,采样参数不同也区分")


if __name__ == "__main__":
    main()
