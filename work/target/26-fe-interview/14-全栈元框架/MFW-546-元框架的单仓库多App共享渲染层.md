---
title: [MFW-546] 单仓多 App 的共享渲染层：layout 级复用与跨 App 导航
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-546：单仓多 App：共享渲染层与跨 App 导航

**答**:
- 单仓多 Next App（shop/web/admin 三个 App）的共享层：1) **共享组件包**（@org/ui——source 直引 RBL-521）；2) **共享 layout 片段**（导航/页脚组件跨 App 复用——但 layout 是 App 内文件约定——共享的是组件不是 layout 文件）；3) **跨 App 导航**（shop.web.com → admin.web.com——硬导航或 shared runtime（无）——跨 App = MPA 边界（View Transitions API 的跨文档过渡 RBL-537））。
- 部署矩阵：每 App 独立构建独立部署（构建隔离 RBL-902 生命周期）vs 统一构建（大 monorepo 单产物——构建时长爆炸）；「共享包变更 → 三 App 全部重建」的受影响面（RBL-702 新鲜度传播——shared 包改 = 全 App 失效：发布影响面大）。
- 共享层变更的爆炸半径控制：shared 包 semver 化（App 锁版本——升级自主）vs 浮动（workspace:* 全跟随——一致但爆炸半径大）；「锁版本 + 升级日」（RBL-821）vs 浮动的权衡。
- 追问钩子：为什么「共享组件包改一行 → 所有 App 重建」是浮动的必然代价？——workspace:* = App 构建的输入闭包含 shared 源码（RBL-582 键完整性：输入变 → 缓存失效）；缓存失效是「正确性」不是 bug（产物必须重建才能含变更）；治理手段是「变更频率分层」：稳定的 shared（design tokens）vs 频繁的业务组件——包的变更频率设计决定爆炸半径（RBL-596 的缓存粒度思想在包级）。

```javascript
// monorepo 结构
// apps/shop / apps/web / apps/admin
// packages/ui (shared) / packages/config (共享 preset)
// packages/ui 的变更频率分层
// packages/ui/tokens.ts       —— 稳定：季度级变更（升级日统一）
// packages/ui/components      —— 高频：业务组件（锁定版本？）
// app 内引用策略
import { Button } from '@org/ui';                        // 浮动：workspace:*（跟随）
// package.json: "@org/ui": "workspace:*"                  // 锁定: "1.2.3"（升级日推进）
// 跨 App 导航（MPA 边界）
<a href="https://admin.web.com/orders">管理后台</a>       // 硬导航
// 跨文档 View Transition（现代浏览器）
document.addEventListener('click', async (e) => {
  if (!e.target.closest('a[data-cross-app]')) return;
  e.preventDefault();
  document.startViewTransition(() => { location.href = e.target.href; });
});
```
