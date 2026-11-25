---
title: [TST-204] 多分片的测试报告、trace、video 如何聚合出一份总报告？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-204：多分片的测试报告、trace、video 如何聚合出一份总报告？
**答**：
- 各分片用 blob reporter 输出二进制报告到共享存储（artifact），最后 merge-reports 合成 HTML。
- trace/video 随 blob 一起聚合，失败用例可回放完整轨迹。
- 合并报告要保留分片来源标记（哪个 shard 跑的），排查环境问题必需。
- CI artifact 上传时注意路径唯一（blob-report/shard-1/），防止分片互相覆盖。

```javascript
# GitHub Actions 每分片上传 blob，最后 job 合并
- uses: actions/upload-artifact@v4
  with: { name: blob-report-${{ matrix.shard }}, path: blob-report }
# 汇总 job：download 全部 → npx playwright merge-reports --reporter=html
r
```
