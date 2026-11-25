---
title: [ZSM-714] 状态库的版本迁移：zustand v4→v5 / RTK Query 迁移的落地步骤
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-714：状态库的版本迁移：zustand v4→v5 / TanStack v4→v5 的落地步骤

**答**：
- 状态库大版本升级五步法：1) **API diff 盘点**（官方 migration guide + 项目内 grep 现有用法统计——zustand v5 移除默认 export/useStore 的第三个参数 equalityFn 改 useShallow）；2) **codemod 批量改**（官方 codemod 或自写 jscodeshift：`useStore(selector, shallow)` → `useStore(useShallow(selector))`）；3) **灰度迁移**（per-directory 迁移 + CI 双版本共存期，用 alias 让新目录用 v5）；4) **类型先行**（TS strict 下新 API 先过，旧 API 标 deprecated）；5) **行为回归**（快照测试 + 视觉回归，重点防「默认值变化」——staleTime 语义、gcTime 重命名这类静默行为差异）。
- RTK Query ↔ TanStack Query 迁移（跨库）：endpoint → queryKey 映射表、tag 失效 → invalidate 调用点清单、订阅数统计（哪些 endpoint 真被用了）——先做「用量审计」再排迁移批次，按页面路由灰度。
- 迁移期兼容技巧：过渡层 hook——`useQueryCompat` 内部判断用新 API 包装旧签名，调用方零改动；全部迁完删除 compat 层。
- 数据兼容：persist 缓存的 migrate 链（v4 数据 → v5 结构）与 ZSM-515/561 的版本迁移同构，必须先写再升。
- 追问钩子：升级 ROI 判断——v4→v5 多为内部优化（React 18 适配、体积），收益要量化（bundle 减多少、并发 bug 修掉多少）；没有实际收益的大版本升级不追新，跟随 LTS 节奏。

```javascript
// zustand v4 → v5 codemod 示例（jscodeshift 简化）
// before: useStore(selector, shallow)
// after:  useStore(useShallow(selector))
module.exports = (file, api) => {
  const j = api.jscodeshift
  const root = j(file.source)
  root.find(j.CallExpression, {
    callee: { name: 'useStore' },
  }).forEach((p) => {
    const [sel, eq] = p.node.arguments
    if (eq && eq.name === 'shallow') {
      p.node.arguments = [
        j.callExpression(j.identifier('useShallow'), [sel]),
      ]
      // 确保导入 useShallow
      addImport(root, j, 'zustand/react/shallow', 'useShallow')
    }
  })
  return root.toSource()
}

// TanStack v4 → v5 关键 diff 清单
// cacheTime → gcTime
// useInfiniteQuery: getNextPageParam 保留，initialPageParam 必填
// status: 'loading' → 'pending'（isLoading = isPending && isFetching）
// onError/onSuccess 从 hook 层移除 → useMutation 专属

// 迁移批次的灰度控制
// package.json
// {
//   "resolutions": { "zustand": "npm:zustand@5" },
//   // 或 monorepo 按目录 alias
// }
```
