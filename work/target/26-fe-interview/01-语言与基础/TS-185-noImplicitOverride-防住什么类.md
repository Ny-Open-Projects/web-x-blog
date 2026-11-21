---
title: [TS-185] noImplicitOverride 防住什么类继承事故？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-185：noImplicitOverride 防住什么类继承事故？
**答**：
- 子类覆盖父类方法必须显式写 override，否则报错。
- 最大收益：父类删除/改名方法时，子类的"覆盖"立刻报错（父类已无该方法），防止静默腐化成孤儿方法。
- 大型类继承体系（组件基类、抽象 service）的标配选项。

```typescript
class BaseComponent {
  render(): string { return "base"; }
}

class Button extends BaseComponent {
  // ❌ noImplicitOverride 报错：必须写 override
  // render(): string { return "button"; }

  override render(): string { return "button"; } // ✅
}

// 事故回放：父类把 render 改名为 renderV2，
// 没有该选项时 Button.render 变成"子类新方法"，调用处静默拿到父类实现；
// 开启后 Button 的 override render 直接报错，问题在编译期暴露
```
