"""字段类型收紧迁移: 收紧不对称与安全步骤"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, phone TEXT)")
conn.executemany("INSERT INTO users(phone) VALUES(?)",
                 [("138%08d" % i,) for i in range(800)]
                 + [("+86-138-00000001",), ("unknown",), ("",)])

# 放宽随时可做 收紧必须先审计存量: 找出不满足新格式的行
bad = conn.execute("SELECT COUNT(*) FROM users WHERE length(phone) <> 11").fetchone()[0]
print("长度不是 11 位的存量行:", bad, " 收紧前必须清洗或人工处置")

# sqlite 宽松类型不拦超长字符串 MySQL 严格模式才拦截 所以审计不能依赖数据库
conn.execute("INSERT INTO users(phone) VALUES(?)", ("13800000000000000000",))
print("超长字符串插入 -> 成功 sqlite 不拦 靠应用层与迁移前的存量审计兜底")

# 收紧三步: 加新列 回填校验 原子换名 旧列保留一个发布周期
conn.executescript("""
ALTER TABLE users ADD COLUMN phone_new TEXT;
UPDATE users SET phone_new = CASE WHEN length(phone) = 11 THEN phone ELSE NULL END;
ALTER TABLE users RENAME COLUMN phone TO phone_legacy;
ALTER TABLE users RENAME COLUMN phone_new TO phone;
""")
n_null = conn.execute("SELECT COUNT(*) FROM users WHERE phone IS NULL").fetchone()[0]
n_legacy = conn.execute("SELECT COUNT(*) FROM users WHERE phone_legacy IS NOT NULL").fetchone()[0]
n_clean = conn.execute("SELECT COUNT(*) FROM users WHERE phone IS NOT NULL").fetchone()[0]
print(f"回填成功 {n_clean} 行 无法转换 {n_null} 行 legacy 列保留 {n_legacy} 行可追溯可回滚")
print("结论: 放宽是加法随时可做 收紧是减法必须先审计存量 走加列 回填 原子切换 旧列留一个发布周期")
