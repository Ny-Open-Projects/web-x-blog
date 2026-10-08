## 思路与架构
"char/varchar 区别（二）"实际落点是**索引长度限制体系**：把"单索引上限 767/3072"与"行格式/文件格式/版本/字符集"四个变量串起来，再区分"行长度 65535"这一独立限制。它把 1228- 三张主卡收敛成一张版本对照 + 解除限制 checklist。

```text
索引长度限制决策矩阵
  变量            取值                → 单索引上限
  行格式          COMPACT/REDUNDANT  → 767 字节
  行格式          DYNAMIC/COMPRESSED → 3072 字节
  文件格式        Antelope           → 仅 REDUNDANT/COMPACT
  文件格式        Barracuda          → 支持 DYNAMIC/COMPRESSED
  字符集          UTF8MB4(4B)        → 放大占用(varchar(255)*4=1020)
  版本            5.6                → 默认 Antelope+OFF→767(最坑)
  版本            5.7/8.0            → 默认 Barracuda/DYNAMIC→3072
```

## 方案取舍
| 限制 | 范围 | 触发 | 解法 |
| --- | --- | --- | --- |
| 行长度 65535 | 整行 | 字段总和超 | TEXT/BLOB 只算元信息 |
| 索引 767/3072 | 单索引 | 字符集×长度超 | Barracuda+dynamic+large_prefix |

**取舍结论**：行限制看"总字节"（TEXT/BLOB 豁免），索引限制看"行格式+字符集+版本"。现代 5.7+/8.0 默认 3072，legacy 5.6 最易踩 767——迁移老库要显式切 Barracuda。

**分层边界**：行格式四种与默认演进见 1215-row-format-overview；key_len 读取见 1245-key-len；char/varchar 存储数学见 1227（只引不重述）；本卡只做索引长度限制体系 [边界]。

## 答题技巧
1. **先抛两个上限**：767（compact）/3072（dynamic），根因是行溢出阈值 768。
2. **点字符集放大**：UTF8MB4 4 字节，varchar(255) 在 utf8 下 765 勉强过、utf8mb4 下 1020 早超。
3. **讲版本演进**：5.6 Antelope+OFF 最坑，5.7/8.0 默认 3072、8.0 配置移除。
4. **区分两限制**：行 65535（TEXT/BLOB 豁免）vs 索引 767/3072，别混。
5. **避坑**：不在 8.0 找 innodb_large_prefix；不说"索引限制恒 767"；不把 TEXT/BLOB 算进行长。
