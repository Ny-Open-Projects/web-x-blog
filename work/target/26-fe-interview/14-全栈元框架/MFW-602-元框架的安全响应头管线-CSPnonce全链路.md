---
title: [MFW-602] 安全响应头管线：CSP nonce 全链路
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-602：CSP nonce 全链路

**答**:
- CSP nonce 的生成链：middleware 生成 nonce → 请求上下文传递（header → RSC 渲染读 → 注入 script/style 标签 + CSP 头同 nonce）——「一个请求一个 nonce」的全链路传递（RBL-791 的元框架实现版：Next 的 nonce 机制）。
- nonce 的传递机制：middleware `NextResponse.next({ headers: { 'x-nonce': nonce } })` → RSC 渲染读 header → `headers().get('x-nonce')` → 组件注入 `<script nonce={nonce}>`；CSP 头同 nonce（middleware 设置响应头）。
- static 与 CSP 的冲突：静态产物（CDN 缓存）无法带 per-request nonce → 静态页的 CSP 用 hash 或 strict-dynamic（CDN 缓存友好）；「nonce 页 = 必须动态渲染」（nonce 每请求变——缓存破坏 RBL-510 权衡）。
- strict-dynamic 的传播：`script-src 'nonce-x' 'strict-dynamic'`——nonce 脚本加载的脚本自动信任（第三方加载器 RBL-882 的兼容）；旧浏览器不认 strict-dynamic → fallback 白名单。
- 追问钩子：为什么「nonce 与静态缓存的冲突」决定了 CSP 架构？——per-request nonce = 每个响应不同 → 不可 CDN 缓存（缓存 nonce 过期 = 脚本全拦）；全站动态 = 成本爆炸；解法：静态页 hash CSP（构建期已知脚本 → hash 白名单稳定）+ 动态页 nonce——「CSP 策略按缓存性分层」与产物缓存策略（RBL-582）一致：nonce 的安全收益换缓存能力——按页面角色选择（RBL-618 角色分类）。

```typescript
// middleware：生成 nonce + 设置 CSP
export function middleware(req) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64');
  const csp = `script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
    style-src 'self' 'nonce-${nonce}'; object-src 'none'; base-uri 'self'`;
  const res = NextResponse.next({ headers: { 'x-nonce': nonce } });
  res.headers.set('content-security-policy', csp.replaceAll('\n', ' '));
  return res;
}
// RSC 侧读 nonce
export default function RootLayout({ children }) {
  const nonce = headers().get('x-nonce');                // 请求上下文传递
  return (
    <html>
      <body>{children}
        <script nonce={nonce} dangerouslySetInnerHTML={{ __html: bootstrap }} />
      </body>
    </html>
  );
}
// 静态页：hash CSP（CDN 缓存友好）
// CSP: script-src 'self' 'sha256-<构建期产物 hash>' —— RBL-894 清单生成
```
