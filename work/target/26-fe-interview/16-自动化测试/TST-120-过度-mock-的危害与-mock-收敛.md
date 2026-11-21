---
title: [TST-120] 过度 mock 有什么危害？mock 的收敛边界怎么定？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-120：过度 mock 有什么危害？mock 的收敛边界怎么定？
**答**：
- 危害四连：① 测试与实现耦合——mock 了 `userService.fetch` 后改内部架构，测试全红但行为没变；② 假阳性——mock 返回的数据和真实接口结构漂移，测试全绿上线崩（契约失真）；③ 掩盖设计问题——到处 mock 说明模块边界不清、依赖注入缺失；④ 维护成本——mock 定义比被测代码还长。
- 收敛原则：只 mock「不可控的边界」——网络（MSW/page.route）、时间（vi.useFakeTimers）、随机数、浏览器 API 缺失（jsdom 里的 matchMedia/IntersectionObserver）、三方 SDK。**不 mock 自己写的模块、不 mock 被测对象内部的依赖链**。
- 判别口诀：「这段依赖是否稳定可复现？」稳定（工具函数、store）就真跑；不可控（网络、时间、三方）才 mock。能用 MSW 就别 vi.mock axios 模块——网络层 mock 语义最真。
- mock 数据质量：固定在 fixture 文件里、类型与真实接口对齐（`satisfies` 接口类型）、必要时用契约测试（schema 校验）防漂移。
- 追问钩子：怎么发现「mock 泛滥」？——grep `vi.mock` 数量/文件行数超过真实代码 = 信号；重构方向通常是抽出防腐层（repo 层）让业务依赖接口而非实现。

```javascript
// ❌ 过度 mock：把被测逻辑本身 mock 掉了
vi.mock('./useCartLogic');            // 被测组件的核心逻辑！
vi.mock('./formatPrice');             // 自己写的纯函数
vi.mock('./UserAvatar');              // 自己的子组件
test('购物车', () => expect(screen.getByTestId('total')).toHaveText('0'));

// ✅ 收敛：只 mock 网络，其余真跑
import { server } from '@/mocks/server';
server.use(
  http.get('/api/cart', () => HttpResponse.json({
    items: [{ skuId: 'SKU-001', count: 2, price: 19900 }],
  })),
);
render(<Cart />);                     // 内部逻辑/格式化/子组件全真实
await expect(screen.findByText('¥ 398.00')).resolves.toBeInTheDocument();
```
