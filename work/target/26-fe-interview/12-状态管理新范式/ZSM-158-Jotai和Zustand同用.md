---
title: [ZSM-158] 一个项目里同时用 Jotai 和 Zustand 会不会精神分裂？两库混用的边界怎么划？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-158：一个项目里同时用 Jotai 和 Zustand 会不会精神分裂？两库混用的边界怎么划？
**答**：
- 技术上没冲突：两库都是独立订阅模型，数据互不感知，混用不会互相引发渲染；真正的问题在团队心智——两套 API、两套 devtools、两套测试方式。
- 合理的混用边界：Jotai 管「组件级共享的细粒度派生」（表单联动、图层显隐这类 atom 森林），Zustand 管「应用级少而稳的领域状态」（会话、偏好、购物车）。
- 判断口令：「状态的形状」决定工具——多而小的原子值、复杂派生链用 Jotai；少而大的领域对象、需要组件外读写用 Zustand。
- 面试风险提示：主动说「理想情况是收敛到一个，混用要有 ADR 说明边界」，否则 onboarding 成本会翻倍——展示治理意识比展示会两个库更值钱。

```javascript
// Zustand：少而稳的应用级领域状态
const useSessionStore = create((set) => ({
  user: null, cart: [], setUser: (user) => set({ user }),
  addCart: (item) => set(s => ({ cart: [...s.cart, item] })),
}))

// Jotai：多而细的组件级派生森林
const layersAtom = atom([{ id: 'bg', on: true }, { id: 'grid', on: false }])
const visibleLayersAtom = atom((get) =>
  get(layersAtom).filter(l => l.on))
const layerCountAtom = atom((get) => get(visibleLayersAtom).length)

// 组件各取所需，互不越界
function StatusBar() {
  const user = useSessionStore(s => s.user)       // 领域状态：Zustand
  const count = useAtomValue(layerCountAtom)      // 图层派生：Jotai
  return <span>{user?.name} · {count} 层可见</span>
}
```
