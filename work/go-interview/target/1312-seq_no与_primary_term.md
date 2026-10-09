# 1312 _seq_no 与 _primary_term：ES 高版本默认并发控制

> 分类：Elasticsearch / 并发控制 | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**_seq_no** / **_primary_term** / **if_seq_no** / **if_primary_term** / **6.6 引入 7.0 默认**
> 原文锚点：第 25~52 段「6.6 起用 _seq_no(序列号,每文档递增)与 _primary_term(主分片代次)；7.0 默认；GET 取二者，更新时 if_seq_no/if_primary_term 匹配才成功；主分片重分配时 primary_term 递增用于恢复去重」

## 一句话总述
ES 6.6 起引入 **`_seq_no`（序列号，每文档单调递增，步长不固定为 1）** 与 **`_primary_term`（主分片代次，主分片重分配/重启选举时递增）** 作为并发控制依据；**7.0 起默认采用此方式**。更新时通过 `if_seq_no` + `if_primary_term` 指定预期值，二者全匹配才成功，否则 409 冲突。

## 面试官视角
- 意图：是否理解 `_seq_no`/`_primary_term` 的语义及为何要两者配合。
- P5 知 7.0 默认用 seq_no 控制；P6 知二者须同时匹配；P7 知 `primary_term` 用于主分片切换后识别"同一 seq_no 的不同代"、避免恢复时取错数据。
- 红旗：以为只靠 `_seq_no` 即可；忽略 `primary_term` 在主分片重分配场景的作用。
- 惊艳点：点出"seq_no 只保证单文档内顺序，主分片换代会复用 seq_no，故需 primary_term 区分代次" `[经验]`。

## 主问答
**Q（面试官原话）：** ES 高版本用 _seq_no 和 _primary_term 怎么做并发控制？
**A：**
1. **语义**：`_seq_no` 是每文档的全局递增序列号（每次写操作分配新值，步长不一定为 1）；`_primary_term` 是主分片代次，主分片因宕机/重分配/重启选举而变更时递增。
2. **用法**：先 GET 取文档的 `_seq_no` 与 `_primary_term`，更新时带 `if_seq_no` + `if_primary_term`；仅当两者与当前文档**同时匹配**才成功，否则返回版本冲突。
3. **为何两者配合**：主分片切换后 seq_no 可能"回绕复用"，单靠 seq_no 无法区分新旧；`primary_term` 标记代次，二者组合才能唯一确定操作顺序，保证恢复/并发时数据一致。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|---|---|---|---|---|
| L1 | 何时引入/默认 | 概念 | 6.6 引入/7.0 默认 | 换题 |
| L2 | 二者含义 | 机制 | seq_no 顺序/primary_term 代次 | 判 P5 |
| L3 | 更新怎么用 | 用法 | if_seq_no+if_primary_term | 判 P6 |
| L4 | 为何要两个 | 设计 | 主分片换代会复用 seq_no | 判 P6+ |
| L5 | 恢复场景 | 进阶 | primary_term 去重取最新 | 判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 6.6 起支持 | 7.0 起默认采用 | 新项目直接用 if_seq_no/if_primary_term；老 internal/external 仍可用但非默认 |

## 关键代码
```go
// 示意：_seq_no + _primary_term 乐观并发（elasticsearch-go），未做端到端验证
got, _ := es.Get("user", "1")
seqNo := got.SeqNo        // 文档当前序列号
pTerm := got.PrimaryTerm  // 文档当前主分片代次

req := esapi.UpdateRequest{
    Index:        "user",
    DocumentID:   "1",
    IfSeqNo:      &seqNo,      // 预期 seq_no
    IfPrimaryTerm: &pTerm,     // 预期 primary_term
}
res, _ := req.Do(ctx, es)
if res.StatusCode == http.StatusConflict {
    // 409：文档已被他人更新（seq_no 或 primary_term 不匹配），重取最新后重试
}
```

## 总结与追问预判
- `_seq_no`+`_primary_term` 是 7.0 默认并发控制；两者同时匹配才更新成功。
- 预判：与 internal/external 对比 → 见 1312；实战重试模式 → 见 1312。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词（英文专有名词被错读为近似音、部分中文术语写错字），本卡统一为规范术语 `[经验]`。事实核校：6.6 引入、7.0 默认、`_seq_no` 单调递增、`_primary_term` 主分片代次、二者匹配才更新——均正确，未做更正。
