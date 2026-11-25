---
title: [V3-361] Suspense 相关组件的测试策略是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-361：Suspense 相关组件的测试策略是什么？
**答**：
- 渲染测试要处理「挂起状态」：@vue/test-utils 中异步依赖未 resolve 时断言 fallback 存在；用 `flushPromises()` 推进微任务再断言真实内容。
- 覆盖三类时序：快速成功（不闪 fallback 逻辑）、慢成功（fallback → 内容）、失败（fallback → 错误边界 UI）。
- 用假计时器（vi.useFakeTimers）控制超时/minDelay 类逻辑，避免真实等待。
- 断言「重试」：mock fetch 首次 reject、第二次 resolve，验证退避与次数。
- e2e 层用路由拦截（慢速网络 profile）验证骨架屏可见性，单元层不易覆盖「闪烁」这类视觉时序。
```javascript
it('shows fallback then content', async () => {
  const wrapper = mount(SuspenseWrapper)
  expect(wrapper.find('[data-testid=sk]').exists()).toBe(true)
  await flushPromises()
  expect(wrapper.text()).toContain('商品列表')
})
```
