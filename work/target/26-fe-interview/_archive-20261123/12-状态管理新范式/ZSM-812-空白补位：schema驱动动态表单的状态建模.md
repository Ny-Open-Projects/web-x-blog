---
title: [ZSM-812] 空白补位：低代码/schema 驱动动态表单的状态建模
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-812：空白补位：低代码/schema 驱动动态表单的状态建模

**答**：
- 低代码表单（运营配置字段、字段动态增删）的状态三层：**schema 层**（字段定义：类型/规则/联动 deps——服务端下发，版本化）、**值层**（用户输入，ZSM-682 依赖图引擎消费 schema 的 deps/compute）、**元状态层**（字段实例的 error/touched/visible——与 schema 分离，按 `schemaVersion:fieldKey` 键控）。
- schema 版本切换的关键问题：运营改了字段定义（删字段/改规则），已填的值怎么办——**值层不做迁移**（用户输入是易失的），但元状态要清理孤儿（无 schema 对应的字段的 error/touched 清除）；硬要保留的草稿走「值层快照 + 回填校验」（值对新 schema 重跑规则，不合法标记 stale 提示）。
- 动态字段的依赖图：schema 下发时构建一次（`createFormGraph(schema)`，ZSM-682）——字段增删是「图的增量更新」，环检测在新 schema 上重跑；**schema 变更=重建引擎**，值层迁移成本远小于增量 patch 的正确性风险。
- 渲染性能：schema 驱动的表单字段组件按 `fieldKey` 订阅自己的值+元状态（ZSM-753 行级订阅同构），schema 变更只重渲受影响子树。
- 追问钩子：schema 驱动的「双源风险」——前端 schema 缓存与服务端 schema 漂移（运营改了配置，用户旧会话还在旧 schema 上填）——会话级 schema 带版本号，提交时服务端校验 schemaVersion 不符返回 409（同 ZSM-588 冲突语义）。

```javascript
// schema 驱动表单的状态三层
const formState = {
  schema: { version: 3, fields: [
    { key: 'name', type: 'string', rules: ['required'], deps: [] },
    { key: 'plan', type: 'enum', options: ['free', 'pro'], deps: ['name'] },
    { key: 'payment', type: 'payment', deps: ['plan'], visibleWhen: (v) => v.plan === 'pro' },
  ] },
  values: { name: '张三', plan: 'free' },                    // 值层（用户输入）
  meta: { 'v3:name': { touched: true, error: null }, ... },  // 元状态按 schemaVersion 键控
}

// schema 变更处理（服务端下发 v4：删除 plan 字段）
function applyNewSchema(nextSchema, prevSchema, meta, values) {
  // 1) 引擎重建（增量 patch 风险 > 重建成本）
  const engine = createFormGraph(nextSchema.fields)
  engine.detectCycle()   // 新 schema 环检测
  // 2) 值层清理孤儿 + 回填校验
  const validKeys = new Set(nextSchema.fields.map((f) => f.key))
  const nextValues = {}
  for (const [k, v] of Object.entries(values)) {
    if (validKeys.has(k)) nextValues[k] = v
    // 孤儿字段值丢弃（用户输入易失）
  }
  // 3) 元状态清理：无 schema 对应的字段元信息清除
  const nextMeta = Object.fromEntries(
    Object.entries(meta).filter(([key]) => key.startsWith(`v${nextSchema.version}:`))
  )
  return { engine, values: nextValues, meta: nextMeta }
}

// 提交时的 schema 漂移防御
async function submit(values, schemaVersion) {
  const res = await api.submit({ values, schemaVersion })
  if (res.status === 409) {
    // schema 已被运营更新：拉新 schema 重新渲染 + 提示
    toast.warn('表单配置已更新，请确认后重新提交')
  }
}
```
