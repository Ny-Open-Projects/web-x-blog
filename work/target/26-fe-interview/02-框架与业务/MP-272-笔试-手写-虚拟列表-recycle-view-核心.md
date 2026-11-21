---
title: [MP-272] 笔试：手写小程序虚拟列表核心（scroll-view + 窗口渲染）
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-272：笔试：手写小程序虚拟列表核心
**题**：实现页面逻辑：定高行高 ROW_H=80；scroll-view onScroll 计算可视窗口（含上下各 5 条缓冲），setData 只更新 visible 数据与 padding（上下占位高度）；滚动节流（rAF 语义用 16ms）；支持 scrollToIndex。

```javascript
const ROW_H = 80
Page({
  data: { visible: [], paddingTop: 0, paddingBottom: 0, scrollTop: 0 },
  list: [], // 全量数据（逻辑层内存）
  _timer: null,
  onScroll(e) {
    if (this._timer) return
    this._timer = setTimeout(() => {
      this._timer = null
      const st = e.detail.scrollTop
      const viewH = e.detail.scrollHeight // 或取窗口高度缓存
      const start = Math.max(0, Math.floor(st / ROW_H) - 5)
      const count = Math.ceil(viewH / ROW_H) + 10
      const visible = this.list.slice(start, start + count).map((item, i) => ({ ...item, index: start + i }))
      this.setData({ visible, paddingTop: start * ROW_H, paddingBottom: Math.max(0, (this.list.length - start - count) * ROW_H) })
    }, 16)
  },
  scrollToIndex(i) {
    this.setData({ scrollTop: i * ROW_H })
  },
  onUnload() { clearTimeout(this._timer) }
})
```
**评分点**：
- 窗口计算（可视 + 缓冲）。
- 上下占位 padding 撑住滚动高度（核心技巧）。
- 滚动节流 + 卸载清理。
- 说明不定高版本需实测行高校正（说出思路即可）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-45125328-054c-42df-b9f7-d745a3782d49-cwd'; fi
exit "$__zcode_status"
