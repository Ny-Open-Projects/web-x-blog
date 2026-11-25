---
title: [ZSM-026] 笔试：手写 Zustand 中间件组合器 compose 并保证顺序正确
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-026：手写 Zustand 中间件组合器 compose 并保证顺序正确

**答**：
- 实现 `compose(...mws)` 返回高阶 creator：`create(compose(logger, persist)(baseConfig))` 等价于嵌套调用 `logger(persist(baseConfig))`。
- 保证**最左中间件最外层**（先拿到最终 set，最后执行包装）。
- 附带实现 `apply(mws)` 语义清晰版：从内到外依次包裹。

**边界说明**：中间件签名统一为 `(config) => (set, get, api) => config(...)`。

```javascript
export const compose = (...mws) => (config) =>
  mws.reduceRight((acc, mw) => mw(acc), config)

// 等价验证：
// compose(A, B)(C) === A(B(C))
// reduceRight 从右往左包：acc=C → B(C) → A(B(C))

export const apply = (mws, config) => mws.reduce((acc, mw) => mw(acc), config)
// apply([A, B], C) === B(A(C))  注意与 compose 的方向差异

// 用法
const useStore = create(
  compose(logger, persist)((set) => ({ n: 0, add: () => set(s => ({ n: s.n + 1 })) }), null),
  // persist 作为内层：logger 能记录到 persist 恢复后的合并写入
)
```

**评分点**：
- reduceRight 方向正确：左中间件在最外层。
- 返回值是 `(set, get, api) => state` 形态的合法 creator，可直接传给 create。
- 能口述顺序差异：compose 与 reduce 方向相反，面试最常踩的坑。
