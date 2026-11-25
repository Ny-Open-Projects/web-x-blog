---
title: [TST-926] 微前端里子应用怎么拿到主应用传的 props？如何用契约测试防止「改了 props 名全站崩」？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-926：微前端里子应用怎么拿到主应用传的 props？如何用契约测试防止「改了 props 名全站崩」？
**答**：
- 结论：把主→子的 props 当作「公开接口」——用 JSON Schema 或 TS 类型定义契约，双方 CI 都跑校验，改字段必须向后兼容。
- 落地：主应用在挂载子应用前用 ajv 校验 props 符合 schema；子应用仓库的测试用同一份 schema 校验示例入参。
- 兼容规则：只增不改——新增可选字段 OK，删除/改类型需走 major 版本 + 灰度并存。
- 追问钩子：主应用把 userId 改成了 uid，5 个子应用只有 4 个改了，契约测试怎么在合入前拦住第 5 个？

```javascript
import Ajv from 'ajv';
const propsSchema = {
  type: 'object',
  required: ['userId', 'token'],
  properties: {
    userId: { type: 'string' },
    token: { type: 'string' },
    theme: { type: 'string', enum: ['light', 'dark'] }, // 新增可选字段
  },
  additionalProperties: false,
};
const ajv = new Ajv();
const validate = ajv.compile(propsSchema);
export function mountSubApp(props) {
  if (!validate(props)) throw new Error(`props 契约违约: ${ajv.errorsText(validate.errors)}`);
  return qiankunMount(props);
}
// 子应用测试：用同一 schema 验证典型入参
test('子应用入参符合 props 契约', () => {
  expect(validate({ userId: 'u1', token: 't1', theme: 'dark' })).toBe(true);
});
```
