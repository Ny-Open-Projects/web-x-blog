---
title: [SCN-048] 团队 Code Review 流于形式，如何建立有效的 CR 机制与清单？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-048：团队 Code Review 流于形式，如何建立有效的 CR 机制与清单？
**答**：
- 机器先审：ESLint、TypeScript、单测、体积预算全部进 CI，把格式与低级错误挡在人工 CR 之前，人只审设计与逻辑。
- 人审聚焦四类：正确性（边界、竞态、错误处理、内存泄漏）、可维护性（命名、职责、重复代码）、安全（XSS、敏感信息硬编码、越权）、性能（无效渲染、N+1 请求）。
- 流程约定：PR 控制在 400 行以内、24 小时内响应、阻塞项必须改完再合，建议项可下迭代处理。

```typescript
// CR 高频问题样本：一个 composable 藏着三类典型缺陷与对应修法
export function useSearch() {
  let timer: number;                                  // 缺陷1：定时器未随组件卸载清理
  const kw = ref('');
  watch(kw, () => {
    timer = window.setTimeout(() => doSearch(kw.value), 300);
    // 缺陷2：竞态 —— 未取消上一次请求，慢响应可能覆盖新结果
  });
  onUnmounted(() => clearTimeout(timer));             // 修复1：卸载时清理定时器

  async function doSearch(q: string) {
    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
    if (!res.ok) throw new Error(`搜索失败 ${res.status}`); // 修复3：显式错误处理，禁止静默失败
    return res.json();
    // 缺陷3（原始写法）：fetch 失败直接抛未捕获 Promise，界面无任何反馈
  }
  return { kw };
}
```

## 追问（补充）

**追问**：

1. PR 确实超 400 行但业务要求一次改完，怎么拆？ → 按「可独立回滚的行为变更」拆成 stacked PR，用 feature flag 串起来，禁止按目录机械切分。
2. 24 小时响应靠自觉守不住，机制上怎么保证？ → 设轮值 CR owner 与 SLA 看板，超时自动指派 backup，并把 CR 工时写进排期而非「有空再看」。
3. 格式已被机器挡住，人审还是漏了竞态和内存泄漏怎么办？ → 在清单里加「异步生命周期」专项（定时器、订阅、请求取消），用卸载与并发用例兜底，不靠肉眼。
