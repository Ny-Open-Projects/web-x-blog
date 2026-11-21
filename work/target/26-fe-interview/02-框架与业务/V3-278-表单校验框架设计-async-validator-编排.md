---
title: [V3-278] 表单校验框架（async-validator）的编排设计是怎样的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-278：表单校验框架（async-validator）的编排设计是怎样的？
**答**：
- 规则分层：字段级（required/format/range）、跨字段（自定义 validator 拿整个 model）、服务端级（唯一性检查，异步 + 防抖）。
- Schema 转换：动态表单的 rules 声明编译为 async-validator 的 descriptor；服务端规则挂 `asyncValidator`。
- 触发编排：blur 校验单字段、change 防抖校验（300ms）、提交时全量并行校验后统一收集（`Promise.all` + errors 聚合），聚焦首个错误字段。
- 异步校验注意：竞态——新值校验结果必须覆盖旧值（比对请求序号），防抖 + 取消上次请求。
- 错误呈现：errors 存 `Map<fieldPath, msg>`，渲染层就近读取；提交失败滚动定位 + aria-invalid 无障碍标注。

```typescript
import Schema from 'async-validator';
const descriptor = {
  name: [{ required: true, message: '请输入名称' }, { max: 20, message: '最长 20 字' }],
  endTime: [{
    validator: (_r, value, cb) => value > model.startTime ? cb() : cb(new Error('结束时间需晚于开始时间')),
  }],
  inviteCode: [{
    asyncValidator: async (_r, value) => {         // 服务端唯一性
      const ok = await checkCode(value);           // 内部已防抖+竞态保护
      if (!ok) throw new Error('邀请码已被占用');
    },
  }],
};
const validator = new Schema(descriptor);
async function validateAll(model) {
  try { await validator.validate(model); return null; }
  catch ({ errors }) {
    const map = new Map(errors.map((e) => [e.field, e.message]));
    focusFirstError(map); return map;
  }
}
```
