---
title: [TST-272] SSR 多环境（dev/staging/prod）配置的测试保障？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-272：SSR 多环境（dev/staging/prod）配置的测试保障？
**答**：
- 配置快照：每环境关键配置（API 域名/开关）快照断言，防止 env 泄漏错位（prod key 进 dev）。
- 运行时注入测试：NEXT_PUBLIC_ 前缀与纯服务端变量边界（服务端变量不出现在客户端 bundle）。
- 缺配置行为：必需 env 缺失时启动失败（fail-fast）而非运行时 undefined 崩溃。
- secrets 扫描进 CI：bundle 中不得出现密钥模式。

```javascript
test('服务端变量不泄漏', async () => {
  const bundle = await readClientBundle();
  expect(bundle).not.toContain(process.env.DB_PASSWORD!);  // 服务端秘密不出端
});
r
```
