---
title: [BAS-060] 原生 dialog 元素怎么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-060：原生 dialog 元素怎么用？
**答**：
- `showModal()` 打开模态态：自动居中、自带 ::backdrop 遮罩、焦点管理、Esc 可关、进入 top layer 不受 z-index 影响。
- `show()` 是非模态展示；`close(returnValue)` 关闭，`form method="dialog"` 提交即关闭并把按钮 value 带回 returnValue。
- 相比手写弹窗，天然解决焦点圈闭和层叠层级问题。

```html
<dialog id="dlg">
  <form method="dialog">
    <p>确认删除？</p>
    <button value="yes">确定</button>
    <button value="no">取消</button>
  </form>
</dialog>
<script>
  const dlg = document.getElementById('dlg');
  dlg.showModal();
  dlg.addEventListener('close', () => console.log(dlg.returnValue)); // yes 或 no
</script>
```
