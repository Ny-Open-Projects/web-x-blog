---
title: [MFW-201] RSC 数据流边界案例：Server Action 后的客户端状态失效链
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-201：Server Action 后的客户端状态失效链

**答**:
- 边界现象：Action 成功但客户端组件数据没更新——根因是「三层数据源」失效链没打通（RSC 树 revalidate / Router Cache / 第三方 Query 缓存）
- 打通三步：Action 内 revalidateTag → Router Cache 失效（该 tag 的 fetch 缓存被标记）→ 客户端组件若用 TanStack Query 还需 `qc.invalidateQueries`——三层各自为政必然出现「部分更新」
- 判定法则：数据消费方在哪层就失效哪层；跨层共享数据（如用户信息 RSC 与客户端都读）必须双失效
- 诊断顺序：先确认 RSC Payload 是否更新（Network 看 flight 响应），再查 Router Cache（客户端导航是否拿到新树），最后查客户端缓存

```javascript
// Server Action 三层失效
'use server'
export async function updateProfile(formData) {
  await db.updateProfile(formData)
  revalidateTag('profile')                                   // Data Cache + RSC 树
}
// 客户端组件（TanStack Query 消费方）
const { mutate } = useMutation({
  mutationFn: updateProfile,
  onSuccess: () => qc.invalidateQueries({ queryKey: ['profile'] }),   // 第三层
})
```
