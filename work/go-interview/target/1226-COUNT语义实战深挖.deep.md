# 1226 COUNT 语义实战深挖

> 分类：数据库 / MySQL | 难度：L4 | 题型：体系化深挖 | 频率：中 | 关键词：**COUNT 语义** / **EXPLAIN 验证** / **常见误区**

## 思路与架构
`COUNT` 题的答题架构是"**语义 → 机制 → 排序 → 引擎差异**"四层递进：
- **语义层**：`COUNT(expr)` 计 `expr` 非 NULL 行；`COUNT(*)` 计所有行（ANSI 计行语法）。
- **机制层**：Server 层维护计数变量，循环读 InnoDB 记录；索引选择决定扫哪棵树。
- **排序层**：由"是否读列值 + 是否判 NULL + 索引 IO 大小"推导性能排序。
- **引擎层**：MyISAM 无事务→O(1)；InnoDB 有 MVCC→必须扫索引或靠应用层计数。

## 方案取舍
| 写法 | 语义 | 索引选择 | 相对速度 |
|---|---|---|---|
| `COUNT(*)` | 计全部行 | 最小二级索引 | 最快 |
| `COUNT(1)` | 计全部行 | 最小二级索引（与 * 同路径） | 最快 |
| `COUNT(主键)` | 计全部行 | 聚簇索引（全字段） | 较慢 |
| `COUNT(索引字段)` | 计非 NULL | 二级索引 + 判 NULL | 中 |
| `COUNT(非索引字段)` | 计非 NULL | 全表扫描 | 最慢 |

**工程取舍**：要准确总数又高频 → 应用层维护计数表/缓存（见 1246 的缓存思路）；只要近似值 → `information_schema`/`SHOW TABLE STATUS`。

## 答题技巧
1. **先破误区**：开口就点"网上说 COUNT(*) 最慢是错的"，立刻建立专业感。
2. **一句话锁语义**："`COUNT` 永远计参数非 NULL 的行"——所有差异从这里推。
3. **用 EXPLAIN 收口**：说"有二级索引时 `COUNT(*)` 走最小 key_len 的二级索引"，比空谈"快"更有说服力。
4. **锚定引擎差异**：MyISAM O(1) vs InnoDB MVCC，是区分"懂原理"和"只会背"的分水岭。
5. **边界不漏**：`COUNT(0)`/`COUNT(4)` 都计全部行（0/4 非 NULL）；`COUNT(NULL)` 恒 0——这两个边界常被追问。

## 细节与核心 API

**语义**：`COUNT(expr)` 计 expr 非 NULL 行；`COUNT(*)` 计全部行（ANSI 计行语法）：

```sql
SELECT COUNT(*), COUNT(1), COUNT(id), COUNT(name), COUNT(NULL) FROM t;
-- COUNT(*) / COUNT(1)       走最小二级索引（最快）
-- COUNT(主键)              走聚簇索引（全字段，较慢）
-- COUNT(索引字段)          二级索引 + 判 NULL（中）
-- COUNT(非索引字段)        全表扫描（最慢）
-- COUNT(0)/COUNT(4) 都计全部行（非 NULL）；COUNT(NULL) 恒 0
EXPLAIN SELECT COUNT(*) FROM t;   -- 看 key 选最小 key_len 的二级索引
```

**引擎差异**：MyISAM 无事务 → O(1) 维护总行数；InnoDB 有 MVCC → 必须扫索引或靠应用层计数。

```text
高频准确总数 → 应用层计数表/缓存；近似总数 → information_schema / SHOW TABLE STATUS
```

> 边界：索引选择与 key_len 见 1245；覆盖索引见 1246；本卡只讲 COUNT 语义实战。
