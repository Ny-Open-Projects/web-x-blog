---
title: [TS-125] 大厂 TS 规范如何落地？strict 全家桶逐项解释？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-125：大厂 TS 规范如何落地？strict 全家桶逐项解释？
**答**：
- `strict: true` 是总开关，含 strictNullChecks（null/undefined 不能赋给其他类型，最大收益）、noImplicitAny（禁止隐式 any）、strictFunctionTypes（函数参数逆变检查）、strictBindCallApply、strictPropertyInitialization（类属性必须初始化）、noImplicitThis、alwaysStrict、useUnknownInCatchVariables（catch 变量为 unknown）。
- 辅助开关：noImplicitReturns、noFallthroughCasesInSwitch、noUnusedLocals/noUnusedParameters。
- 落地策略：存量仓库用 `tsc --noEmit` 摸底存量错误，按目录豁免渐进收紧，CI 设为门禁。

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "useUnknownInCatchVariables": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "skipLibCheck": true
  }
}
```

```typescript
// strict 打开后的典型报错变化
function fetchUser(id: string | null) {
  // strictNullChecks：id 可能为 null，使用前必须收窄
  if (id === null) return Promise.reject("no id");
  return Promise.resolve({ id });
}

try {
  JSON.parse("{}");
} catch (e) {
  // useUnknownInCatchVariables：e 是 unknown，不能直接 e.message
  if (e instanceof Error) e.message;
}

class Store {
  state: { count: number };
  constructor() {
    // strictPropertyInitialization：必须初始化或声明为可选/ definite assignment
    this.state = { count: 0 };
  }
}
```
