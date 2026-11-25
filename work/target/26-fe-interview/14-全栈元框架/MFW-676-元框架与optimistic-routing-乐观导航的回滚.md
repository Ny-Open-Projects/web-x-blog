---
title: [MFW-676] 乐观导航的回滚
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-676：乐观导航的回滚

**答**:
- 乐观导航（optimitic navigation）：点击 Link → 立即更新 URL + 骨架（不等待 payload）→ payload 到达渲染；失败（404/网络错误）→ 回滚 URL + 内容（RBL-676 主题：URL 与内容的一致性）。
- 实现的协议：1) history.pushState 乐观写（URL 先变）；2) payload fetch 失败 → history.back() 回滚 + 显示 error；3) 与 history 的交互：浏览器后退栈的状态（乐观导航的 pushState 在失败后 back = 回到原页——正确回滚语义）。
- 与 Next Router 的差异：Next 的导航 = payload 成功后才 pushState（非乐观——无回滚需求）；乐观导航 = pushState 先（UX 更快但需回滚）——两种导航语义的权衡：确定性（Next）vs 速度（乐观）。
- 追问钩子：为什么「乐观导航的回滚」比「等待后再导航」更难做对？——乐观 = URL 已变（用户看到新 URL）+ 内容未渲染（骨架）→ 失败回滚 = URL 恢复 + 内容恢复（原页面的 state/滚动位置——回滚的状态恢复）；等待式 = URL 不变 → 失败 = 原页面不动（零回滚）；「回滚的状态恢复」：原页面的 DOM/state/滚动位置需要保存与恢复（快照协议 RBL-936）——乐观的复杂度 = 回滚的完整性（原状态无损恢复）。

```typescript
// 乐观导航
async function optimisticNavigate(href: string) {
  const snapshot = { scrollY: window.scrollY, html: document.body.innerHTML };
  history.pushState({ optimistic: true }, '', href);      // URL 先变
  document.body.innerHTML = '<div class="skeleton">加载中…</div>';   // 骨架
  try {
    const payload = await fetch(href, { headers: { rsc: '1' } });
    if (!payload.ok) throw new Error(payload.status);
    const content = await payload.text();
    renderPayload(content);                               // 成功：渲染
  } catch (e) {
    // 回滚：URL + 内容 + 滚动
    history.back();
    document.body.innerHTML = snapshot.html;              // 恢复原页面
    window.scrollTo(0, snapshot.scrollY);                 // 恢复滚动
    showError(`导航失败: ${e.message}`);
  }
}
// Next Router 的非乐观语义
// router.push(href) → await payload → pushState
// 失败 = 原页面不动（无回滚需求——确定性优先）
```
