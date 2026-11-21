---
title: [DP-236] 源码识别：Zod 源码中的组合模式与解释器？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-236：源码识别：Zod 源码中的组合模式与解释器？
**答**：
- 组合模式：z.object({ a: z.string(), b: z.array(z.number()) }) 是 schema 树——每个 ZodType 有 parse/safeParse 同接口，父子组合递归求值。
- 解释器：parse 是对 schema 树的解释执行（遍历 + 校验 + 收集 issues）；链式 API（.min(5).optional()）返回新 schema（不可变组合，命令带修饰）。
- 策略/备忘录：transform/refine 挂自定义策略；superRefine 收集多条错误；schema 可 freeze 复用（模块级单例）。
- 识别要点：能解释"safeParse 返回 { success, data | issues } 而不是 throw"——错误收集型解释器 vs 异常控制流（throw 型）的差异与选择。

```typescript
// Zod 源码级简化
abstract class ZodType<T> {
  _checks: Checker[] = [];                      // 修饰命令收集
  parse(input: unknown): T {
    const r = this.safeParse(input);
    if (!r.success) throw new ZodError(r.issues);
    return r.data;                              // throw 型入口
  }
  safeParse(input) {                            // 解释器：递归求值
    const parsed = this._parse(input);
    if (!parsed.success) return parsed;
    for (const c of this._checks) {             // 修饰按注册顺序执行
      const ok = c(parsed.data);
      if (!ok) parsed.issues.push({ code: c.code, path: [], message: c.message });
    }
    return parsed;
  }
  min(n: number, msg = 'too short') { const s = this.clone(); s._checks.push({ code: 'min', n, message: msg }); return s; }  // 不可变组合
}
class ZodString extends ZodType<string> { _parse(i) { return typeof i === 'string' ? { success: true, data: i } : { success: false }; } }
class ZodObject extends ZodType<object> { constructor(public shape) { super(); }
  _parse(o) {                                   // 组合：递归子 schema
    const data = {}; const issues = [];
    for (const [k, v] of Object.entries(this.shape)) {
      const r = v.safeParse(o[k]);
      r.success ? data[k] = r.data : issues.push(...r.issues.map(i => ({ ...i, path: [k, ...i.path] })));
    }
    return issues.length ? { success: false, issues } : { success: true, data };
  } }
```
