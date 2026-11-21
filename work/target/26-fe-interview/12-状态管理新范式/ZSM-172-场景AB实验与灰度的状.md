---
title: [ZSM-172] 场景：AB 实验和灰度开关的状态怎么管理？实验分组数据要不要进客户端 store？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-172：场景：AB 实验和灰度开关的状态怎么管理？实验分组数据要不要进客户端 store？
**答**:
- 实验配置（有哪些实验、分流规则）是服务端数据：进入应用时一次性拉取（SDK 内部缓存），生命周期与会话等长；分组结果（我是 A 还是 B）是「服务端计算的派生值」，以只读形式注入客户端。
- 归层建议：分组结果放独立轻量 store/atom（只读 + 可被调试工具覆盖），不要和业务 store 混放；UI 变体渲染用 `useExperiment('new-checkout')` 的 Hook 派生。
- 两个坑：① SSR 与客户端分组不一致导致闪烁——分组要在服务端定死并随 HTML 下发；② 实验状态污染缓存 key——实验变量影响数据时进 queryKey（`['list', { variant }]`），否则两个变体共用一份缓存看到相同数据，实验就白做了。
- 面试要点：说出「实验分组是只读派生态 + 调试覆盖入口」的设计，体现工程完整度。

```javascript
// 实验 SDK：会话级只读态 + 调试覆盖
const useExperiments = create((set) => ({
  groups: window.__INITIAL_EXPERIMENTS__ ?? {},   // SSR 下发的分组，只读
  overrides: {},                                   // 本地调试覆盖
  setOverride: (k, v) => set(s => ({ overrides: { ...s.overrides, [k]: v } })),
}))

export function useExperiment(name) {
  const { groups, overrides } = useExperiments()
  return overrides[name] ?? groups[name] ?? 'control'
}

// 变体影响数据时：必须进 queryKey
function ProductList() {
  const variant = useExperiment('plp-rank-v2')
  const { data } = useQuery({
    queryKey: ['goods', { variant }],              // 不同变体不同缓存
    queryFn: () => api.goods({ variant }),
  })
  return variant === 'b' ? <NewList data={data}/> : <OldList data={data}/>
}
```
