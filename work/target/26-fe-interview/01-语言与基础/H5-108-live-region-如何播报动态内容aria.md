---
title: [H5-108] live region 如何播报动态内容？aria-live 三档与 busy 怎么用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-108：live region 如何播报动态内容？aria-live 三档与 busy 怎么用？
**答**：
- live region 让"非焦点移动的 DOM 更新"被读屏自动播报：`aria-live="polite"`（等空闲再说）、`assertive`（打断，慎用）、`off`。
- 支撑属性：`aria-atomic="true"` 整体播报（改一个字播全部）；`aria-relevant` 控制增删文本哪类变化触发；`role="status/alert/log/timer"` 自带 live 语义（alert=assertive，status=polite）。
- 播报条件：区域**必须先存在于 DOM**，后改内容——动态创建节点再塞文本经常不播；推荐页面常驻一个隐藏播报器。
- `aria-busy="true"`：批量更新时先置忙，全部就绪后改 false，避免读屏逐条打断式播报。
- 典型场景：搜索结果条数、表单提交结果、购物车数量、倒计时进度、聊天新消息（log）。

```html
<!-- 常驻播报器：视觉隐藏但对读屏可见 -->
<div id="announcer" class="sr-only"
     aria-live="polite" aria-atomic="true"></div>
<div id="alert-zone" role="alert"></div>   <!-- role=alert 隐含 aria-live=assertive -->

<style>
  .sr-only {
    position: absolute; width: 1px; height: 1px;
    margin: -1px; padding: 0; overflow: hidden;
    clip: rect(0 0 0 0); white-space: nowrap; border: 0;
  }
</style>

<script>
  const announcer = document.getElementById('announcer');

  // 统一播报入口：先清空再改写，确保相同文案也重新播报
  let announceTimer;
  function announce(text) {
    clearTimeout(announceTimer);
    announcer.textContent = '';
    announceTimer = setTimeout(() => { announcer.textContent = text; }, 50);
  }

  // 场景 1：搜索结果
  searchForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const { total } = await search(searchForm.q.value);
    announce(`搜索完成，共 ${total} 条结果`);
  });

  // 场景 2：批量更新用 busy 包裹
  list.setAttribute('aria-busy', 'true');
  const items = await loadItems();
  list.replaceChildren(...items.map(renderItem));
  list.setAttribute('aria-busy', 'false');      // 就绪后一次性播报

  // 场景 3：错误走 alert 区（assertive，立即打断）
  function showError(msg) {
    const zone = document.getElementById('alert-zone');
    zone.textContent = '';                       // 重置以重播
    zone.textContent = msg;
  }
</script>
```
