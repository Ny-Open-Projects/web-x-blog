---
title: "[Q6781] 数据库存进去变成问号：连接字符集与列字符集的双重编码乱码事故"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6781 · 数据库存进去变成问号：连接字符集与列字符集的双重编码乱码事故

难度：P6 ｜ 标签：MySQL字符集、latin1连接、双重编码、乱码、charset链路

基线：Python 3.12；用纯 Python 模拟"连接字符集 × 列字符集"的编码链路，复现 latin1 连接写 utf8mb4 列的三种症状（问号、双重编码、查询期乱码）与修复矩阵，全标准库实跑。

**问**：新环境上线后用户昵称全变成 `???`，另一部分变成 `æ–‡` 这种天书，换台机器读又正常——同一个库两种乱码形态。MySQL 的字符集链路有哪几层？为什么会出现"问号"和"双重编码"两种不同的病？怎么定位断点在哪一层？

**答**：
- **结论**：字符集链路是四段：客户端把 str 编成 bytes 的编码（驱动层 charset）→ 连接字符集（`character_set_client/connection/results` 三个变量，由连接参数决定）→ 列字符集（表结构决定）→ 读回时反向走一遍。**问号**的病理：连接字符集声明 latin1，客户端按 latin1 无法表示的字节流进来，MySQL 在 latin1→utf8mb4 转码时遇到非法序列，替换成 `?`——**信息已经物理丢失**，任何配置修复都救不回来。**双重编码**（`æ–‡`）的病理：客户端实际发的是 utf-8 字节，但连接声明 latin1，MySQL 把 utf-8 字节**逐字节当作 latin1 字符**存进 utf8mb4 列——存的时候"看起来"是 mojibake，读回时如果读端连接也声明 latin1，会原样还原成正确的中文（所以"换台机器读又正常"）；但正常声明的连接读出来就是天书。诊断口诀：**先看 `SHOW VARIABLES LIKE 'character%'` 与连接参数，再确认数据列里存的是"丢了的 ?"还是"错标的双编码"**——前者要恢复备份，后者可以用 `CONVERT(BINARY CONVERT(col USING latin1) USING utf8mb4)` 一条 UPDATE 修复。
- **取舍**：① 统一的全 utf8mb4 链路（连接串 `charset=utf8mb4` + 库表列默认 utf8mb4）是唯一免维护态，任何"靠某层声明错来互相抵消"的方案都是定时炸弹；② 双编码修复必须在**只读窗口**先做 `SELECT` 验证转换结果，因为一次 UPDATE 不可逆；③ 驱动层的坑：老版 pymysql/mysqlclient 对 `charset` 参数与 `SET NAMES` 的优先级不一致，用连接串声明而非手动 `SET NAMES`，避免连接池里的状态漂移（Q6592 连接归还复位的同族问题）；④ JSON/JSONB 类二进制安全字段不受此害，但 utf8mb3 迁 utf8mb4 期间的四字节截断是另一类事故（Q6537/Q6692）。
- **实战**：① 上线清单加一条"连接字符集自检"：启动时执行 `SHOW VARIABLES` 断言三变量全 utf8mb4，不对就 fail-fast；② 乱码定位三板斧：`HEX(col)` 看原始字节（utf-8 中文首字节必是 E4-E9 段）、对照连接变量、用二进制转换在只读副本试修复；③ 事故复盘台账里记录"哪个环节的默认值被谁改过"——这类事故的根因几乎总是某个新环境的默认配置与旧环境不同；④ 双编码数据的批量修复用分批 + 抽样 HEX 比对，一次全表 UPDATE 在大表上等于一次全表重建（Q6620 同族锁账）。

```python
"""Q6781 MySQL 字符集链路: latin1 连接写 utf8mb4 列的三种症状与修复矩阵模拟。"""
# 用 bytes 精确模拟 MySQL 的转码行为: 连接 charset 决定"怎么解释收到的字节"
UTF8_TEXT = "中文"                      # 真实数据
utf8_bytes = UTF8_TEXT.encode("utf-8")   # 客户端应发出的字节
LATIN1_MAP = {i: bytes([i]) for i in range(256)}


def decode_as_latin1(data: bytes) -> str:
    return data.decode("latin-1")        # MySQL 把每字节当一个 latin1 字符


def to_column(value: str, col_charset: str) -> str:
    """列存储: utf8mb4 列接受任何 latin1 可解释的字符串; 非法序列变 '?'."""
    if col_charset == "utf8mb4":
        return value                     # latin1 字符集是 utf8 的子集, 总能存
    return value.encode(col_charset, errors="replace").decode(col_charset)


def read_back(col_value: str, conn_charset: str) -> str:
    """读回: latin1 连接时客户端把收到的字节按 latin1 还原成文本."""
    if conn_charset == "utf8mb4":
        return col_value                 # 声明一致, 原样送达 -> 双编码天书
    data = col_value.encode("latin-1")   # 服务端把内容转回 latin1 字节
    return data.decode("utf-8")          # 老客户端按 utf-8 解释 -> 假正常还原


if __name__ == "__main__":
    # 场景A: 客户端老实按 latin1 编码 -> 中文无法表示, 变 '?' (信息物理丢失)
    a_in = UTF8_TEXT.encode("latin-1", errors="replace")
    a_col = to_column(a_in.decode("latin-1"), "utf8mb4")
    # 场景B: 客户端发 utf-8 字节但连接声明 latin1 -> 逐字节被当 latin1 字符
    b_wire = decode_as_latin1(utf8_bytes)          # "æ–‡" 形态
    b_col = to_column(b_wire, "utf8mb4")
    b_read_wrong = read_back(b_col, "utf8mb4")     # 正常声明连接读到天书
    b_read_old = read_back(b_col, "latin1")        # 旧 latin1 读法反而还原
    # 修复: BINARY 打回 latin1 再按 utf8mb4 解释
    b_fixed = b_col.encode("latin-1").decode("utf-8")
    print(f"A: '?' 形态={a_col!r}  (数据已丢失, 只能恢复备份)")
    print(f"B: 存库形态={b_col!r}")
    print(f"B: utf8 连接读到 {b_read_wrong!r}, 旧 latin1 读到 {b_read_old!r} (假正常)")
    print(f"B: CONVERT(BINARY...) 修复 = {b_fixed!r}")
    ok = (a_col == "??" and b_fixed == UTF8_TEXT
          and b_read_old == UTF8_TEXT and b_read_wrong != UTF8_TEXT)
    print(f"校验: 问号丢失 + 双编码还原 + 修复成功 -> {'通过' if ok else '异常'}")
    print("结论：问号=信息已丢只能回滚; 双编码=存的是错标字节, BINARY 往返可修;")
    print("      全链路统一 utf8mb4 并在启动时断言连接变量, 是唯一免维护态")
```

**追问一**：为什么"双重编码"环境能跑好几年没人发现？它的自愈假象是怎么形成的？

→ 解析：双编码是**对称错误**——写端把 utf-8 字节当 latin1 存，读端如果同样按 latin1 解读，字节原样往返，用户看到的完全正确。老系统里"连接声明 latin1"往往是全局统一的（老驱动的默认值），于是写读两错的抵消让系统看起来健康，中文/emoji 混排、全文搜索（LIKE 中文可能命中也可能不命中，取决于字节形态）、字符长度统计（一个汉字算 3 个字符）这些边缘场景才会零星暴露。危险在于**它不能单独修一端**：只把读端改成 utf8mb4，天书立刻出现；正确顺序是先把存量数据用 BINARY 往返洗成真 utf-8，再同步切换两端声明，且期间写入要冻结或双写校验。这类"对称错误"的通用教训：依赖错误抵消的系统，任何单侧修复都会先变坏——切换前必须先盘点所有读写路径的配置矩阵。

**追问二**：`SHOW VARIABLES` 显示连接是 utf8mb4，但数据还是乱码，还剩哪些可能？

→ 解析：① **变量是会话级快照**：你查的是当前诊断连接的变量，不是业务连接的——连接池里的老连接可能带着旧声明（PgBouncer/连接池串味 Q6708 的 MySQL 版），要在业务连接里执行 `SELECT @@character_set_connection` 才算数；② **驱动绕过了声明**：某些 ORM/驱动默认用自己的 charset 建连，连接串参数名不匹配时静默回退默认值，需要抓包或开 general log 看真实握手；③ **列的字符集不是你以为的**：表 default utf8mb4 不代表每列都是，`SHOW CREATE TABLE` 逐列确认，历史上 ALTER 过的列可能残留 utf8mb3；④ **代理层转码**：中间件（ProxySQL、老版本 ShardingSphere）会在协议层改写 charset 字段；⑤ 最后兜底 `HEX()` 对字节——字节对了是读端问题，字节错了是写端问题，把链路二分。定位字符集问题的总原则：**一切以 HEX 后的原始字节为事实，变量声明只是嫌疑人供述。**
