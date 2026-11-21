"""静态检查 SQL 中的常见索引失效写法"""
import re

RULES = [
    ("函数作用于索引列", re.compile(r"(WHERE|AND|OR)\s+\w+\s*\(", re.I)),
    ("对索引列做算术运算", re.compile(r"(WHERE|AND)\s+\w+\s*[+\-*/]\s*\d", re.I)),
    ("前导模糊 LIKE", re.compile(r"LIKE\s+'%", re.I)),
    ("隐式类型转换风险", re.compile(r"(WHERE|AND)\s+\w*(name|code|phone)\w*\s*=\s*\d+", re.I)),
]


def find_failures(sql: str) -> list:
    return [name for name, pat in RULES if pat.search(sql)]


if __name__ == "__main__":
    samples = [
        "SELECT * FROM t WHERE create_time = '2024-01-01'",          # 正常
        "SELECT * FROM t WHERE DATE(create_time) = '2024-01-01'",     # 函数
        "SELECT * FROM t WHERE id + 1 = 10",                          # 运算
        "SELECT * FROM t WHERE name LIKE '%abc'",                     # 前导模糊
        "SELECT * FROM t WHERE user_name = 12345",                    # 数字比字符串
    ]
    for sql in samples:
        issues = find_failures(sql)
        print("有风险" if issues else "OK", issues, "<-", sql)
    # 改写思路: DATE(col)=d 改成 col 范围比较; LIKE '%abc' 改倒排/全文索引
