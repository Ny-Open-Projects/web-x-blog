---
title: [AIC-235] AI 生成错误路径测试时常见哪些问题？怎么让它写出高质量的异常用例？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-235：AI 生成错误路径测试时常见哪些问题？怎么让它写出高质量的异常用例？
**答**：
- 常见问题：只测「抛了异常」不断言异常类型/信息；mock 掉错误源使错误根本不会发生；漏掉部分失败（批量操作 3 成功 1 失败）。
- 要求异常断言三元组：错误类型 + 关键错误信息 + 状态未污染（数据未写入一半）。
- 错误注入要在正确层级 mock（网络层/时钟层），并给出注入示例。
- 补充「部分失败」「重试后成功」「错误后重试」等复合场景清单。

```javascript
it('批量导入：第 2 条失败时返回部分结果且不污染已成功数据', async () => {
  server.use(http.post('/api/rows', async ({ request }) => {
    const body = await request.json();
    if (body.row === 2) return HttpResponse.error(); // 正确层级注入
    return HttpResponse.json({ ok: true });
  }));
  const res = await importRows([1, 2, 3]);
  expect(res.succeeded).toEqual([1, 3]);            // 部分结果
  expect(res.failed).toEqual([{ row: 2, retryable: true }]);
  expect(await db.rows.count()).toBe(2);            // 状态未污染
});
r
```
