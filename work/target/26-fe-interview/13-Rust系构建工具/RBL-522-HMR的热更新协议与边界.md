---
title: [RBL-522] HMR 的热更新协议：从文件变更到模块替换的完整链路
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-522：HMR 的热更新协议：从文件变更到模块替换的完整链路

**答**:
- HMR 完整链路六步：1) **watch 触发**（文件变更事件，防抖合并）；2) **增量编译**（失效传播 ZSM-514 → 受影响模块重转换）；3) **更新清单生成**（changed modules + accepted 边界判定）；4) **推送**（WS 消息：update hash + 模块列表）；5) **客户端执行**：runtime 按依赖方向「从叶子到根」执行模块替换，每步检查 `module.hot.accept` 是否声明可热替换；6) **边界处理**：无 accept 覆盖的变更 → 整页 reload（fallback）。
- accept 语义的精确含义：`module.hot.accept(deps, callback)` 声明「当 deps 更新时我可以处理」——**accept 是自底向上的责任声明**：入口 accept 了所有下游 → 热替换成功；中间某层没 accept → 从该层向上全部失效 → reload。
- 状态保留的边界：热替换只保留「未变更模块」的状态——被替换模块的内部状态丢失（除非模块自己实现 dispose 保存/restore 恢复，`module.hot.dispose`）。React Fast Refresh 在此之上加了组件级恢复（保存 hooks 状态），这就是 Fast Refresh 的核心增量。
- HMR 与 sourcemap：替换后的模块代码必须带正确 sourcemap，否则报错栈错位——增量编译的 sourcemap 增量更新是 HMR 正确性的隐藏难点。
- 追问钩子：HMR 失效的常见业务原因——「顶层副作用」（模块加载时注册事件/启动定时器）没有 dispose 清理 → 重复注册——「HMR 事故的 90% 是副作用未清理」。

```javascript
// HMR 完整链路
const HMR_PIPELINE = {
  六步: ['watch 触发（防抖合并）', '增量编译（失效传播）', '更新清单+accept 边界判定', 'WS 推送（update hash+模块列表）', '客户端叶子→根执行替换（检查 accept）', '无 accept 覆盖→整页 reload'],
  accept语义: {
    meaning: '自底向上的责任声明：accept(deps, cb) = 我能处理 deps 的更新',
    fallback: '中间层未 accept → 该层向上全失效 → reload',
  },
  状态保留: {
    default: '被替换模块状态丢失',
    dispose: 'module.hot.dispose 保存 + restore 恢复',
    fastRefresh: '组件级 hooks 状态保留（React Fast Refresh 的核心增量）',
  },
  隐藏难点: '替换模块的 sourcemap 增量更新——报错栈正确性',
  事故主因: '顶层副作用无 dispose 清理 → 重复注册（HMR 事故 90%）',
}
```
