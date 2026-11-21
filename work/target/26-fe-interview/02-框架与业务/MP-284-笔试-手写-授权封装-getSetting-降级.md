---
title: [MP-284] 笔试：手写授权封装（检查/请求/拒绝降级三段式）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-284：笔试：手写授权封装
**题**：实现 ensureAuth(scope, { degradate })：getSetting 已授权直接过；未请求过调 wx.authorize；已拒绝则弹「去设置」引导 wx.openSetting，仍拒绝执行 degradate 降级回调；返回 Promise<boolean>；记录拒绝状态防重复打扰。

```javascript
async function ensureAuth(scope, { degradate } = {}) {
  const { authSetting } = await wx.getSetting()
  const st = authSetting[scope]
  if (st === true) return true
  if (st === false) {
    // 曾经拒绝：引导去设置页（不再弹原生框）
    const { confirm } = await wx.showModal({ title: '需要授权', content: '请在设置中开启相关权限' })
    if (!confirm) return degradate?.(), false
    const res = await wx.openSetting()
    if (res.authSetting[scope]) return true
    return degradate?.(), false
  }
  // undefined：从未请求
  try {
    await wx.authorize({ scope })
    return true
  } catch {
    return degradate?.(), false // 用户当场拒绝 → 降级（如手动选地址）
  }
}
// 用法：
// const ok = await ensureAuth('scope.userLocation', { degradate: () => showManualCityPicker() })
// if (ok) locate()
```
**评分点**：
- authSetting 三态判定（true/false/undefined）。
- 拒绝后走 openSetting 而非重复 authorize（原生框不再弹）。
- degradate 降级回调与布尔返回双出口。
- 首次拒绝的「场景延迟触发」理念（说出即可）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-c398f6e5-5c53-44e5-94ee-6f85d455162b-cwd'; fi
exit "$__zcode_status"
