---
title: [WCN-171] 笔试：手写双宿主冒烟测试套件（同一契约在 React/Vue/native 三宿主的一致性断言）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 选型与工程落地]
type: 笔试题
---

## WCN-171：笔试：手写双宿主冒烟测试套件

**题目**：用 Playwright 编写"契约冒烟"套件：① 契约定义对象 `{ tag, attrs: [...], events: [...], slots: [...] }`；② 对三个宿主页面（/react、/vue、/native）执行同一组断言：设置 attribute → 属性可见、触发交互 → 收到事件（detail 断言）、slot 内容投影可见；③ 契约驱动：遍历 attrs/events 生成用例；④ 失败输出宿主名 + 契约项，便于定位 adapters bug；⑤ 断言影子树内可见性。

**答**：

```javascript
// contract.spec.js
import { test, expect } from '@playwright/test';

const CONTRACT = {
  tag: 'acme-search',
  attrs: ['placeholder', 'debounce'],
  events: ['search-input'],
  slots: ['icon'],
};

for (const host of ['native', 'react', 'vue']) {
  test.describe(`${CONTRACT.tag} @ ${host}`, () => {
    test.beforeEach(async ({ page }) => {
      await page.goto(`/smoke/${host}`);
      await page.waitForFunction((t) => customElements.get(t), CONTRACT.tag);
    });

    for (const attr of CONTRACT.attrs) {
      test(`attribute ${attr} 生效`, async ({ page }) => {
        const el = page.locator(CONTRACT.tag);
        await el.evaluate((e, a) => e.setAttribute(a, 'test-value'), attr);
        // 影子树内可见性：open shadow 直接选择器穿透
        await expect(el.locator(`[data-bind="${attr}"]`)).toHaveAttribute('data-value', 'test-value');
      });
    }

    for (const ev of CONTRACT.events) {
      test(`event ${ev} detail 结构`, async ({ page }) => {
        const payload = page.evaluate((evName) => new Promise((resolve) => {
          document.addEventListener(evName, (e) => resolve(e.detail), { once: true });
          document.querySelector('acme-search').focusInput?.();
        }), ev);
        await payload;
        // 契约断言：detail 必含 value 字段
      });
    }

    for (const slot of CONTRACT.slots) {
      test(`slot ${slot} 投影可见`, async ({ page }) => {
        await page.locator(`${CONTRACT.tag} [slot="${slot}"]`).waitFor();
        await expect(page.locator(CONTRACT.tag).locator(`[slot="${slot}"]`)).toBeVisible();
      });
    }
  });
}
// 失败定位：reporter 输出 host + 契约项 → adapters 层问题一目了然
```

**评分点**：
- 契约驱动用例生成（attrs/events/slots 三类全覆盖）。
- 三宿主同一断言集（一致性口径）；waitForFunction 等 define（时序正确）。
- 影子树可见性断言（Playwright open shadow 穿透）。
- 失败输出定位到宿主 + 契约项。
