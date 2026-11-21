"""代理键生成:自然键到代理键用映射表或确定性哈希,入库前按自然键去重"""

import hashlib

NATURAL_KEYS = [
    ("手机号", "13800000001"),
    ("手机号", "13800000001"),   # 重复
    ("身份证", "110101199001011234"),
    ("邮箱", "a@b.com"),
]

SEQUENCE = {}   # 已分配映射: 自然键 -> 代理键


def next_id(mapping, natural):
    if natural not in mapping:
        mapping[natural] = len(mapping) + 1
    return mapping[natural]


def hash_id(natural, salt="s1"):
    """确定性哈希键:无需查表可并行生成;敏感自然键必须加盐防撞库"""
    return int(hashlib.md5((salt + "|".join(natural)).encode()).hexdigest()[:12], 16)


if __name__ == "__main__":
    seen = set()
    for kind, value in NATURAL_KEYS:
        natural = (kind, value)
        if natural in seen:
            print(f"跳过重复自然键: {natural}")
            continue
        seen.add(natural)
        print(f"{natural} -> 序列键 {next_id(SEQUENCE, natural)}, 哈希键 {hash_id(natural)}")
    print("要点:序列键连续可读但分配点是单例瓶颈;哈希键无状态可并行但要防碰撞加盐;两种方式都要先按自然键去重")
