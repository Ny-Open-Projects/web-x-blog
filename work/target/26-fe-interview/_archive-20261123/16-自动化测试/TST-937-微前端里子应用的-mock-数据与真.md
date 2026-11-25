---
title: [TST-937] 微前端里子应用的 mock 数据与真实主应用契约脱节，怎么根治「本地绿、集成炸」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-937：微前端里子应用的 mock 数据与真实主应用契约脱节，怎么根治「本地绿、集成炸」？
**答**：
- 结论：mock 必须从「真实契约」生成，而非手写——用 OpenAPI/JSON Schema 产出 mock server，子应用测试与主应用集成跑同一份契约。
- 做法：契约文件作为 single source of truth，mock server 与校验器共用；契约变更时 mock 自动更新，子应用测试立刻暴露不兼容。
- 补充：定期用录制的主应用真实流量回放，校验 mock 覆盖度。
- 追问钩子：子应用 mock 里 token 字段是可选的，但主应用实际必传，本地全绿集成后 401，你怎么让 mock 不再骗人？

```javascript
// 契约文件 = 唯一真相，mock 与校验共用
import schema from './contracts/props.schema.json';
import { buildMock } from 'json-schema-faker';
const mockProps = buildMock(schema); // mock 从 schema 生成，不手写

test('子应用在契约 mock 下正常工作', () => {
  const props = validateWithSchema(schema, mockProps);
  expect(render(props)).toContain('订单');
});
// 契约更新：token 改为必填 → mock 自动包含 token → 子应用若假设 token 可选会失败
function validateWithSchema(s, data) {
  if (!s.required.every(k => k in data)) throw new Error('mock 不满足契约');
  return data;
}
```
