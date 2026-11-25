---
title: [MFW-668] 主题切换的 SSR 一致性
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-668：主题切换的 SSR 一致性

**答**:
- 主题切换的 SSR 陷阱：1) **FOUC**（SSR 渲染默认主题 → client 切换到用户主题（localStorage）——闪烁）；2) **水合 mismatch**（SSR 的 theme 属性 ≠ client 水合时读取的 localStorage 主题——RBL-914）；3) SSR 读 cookie 主题（服务端知道主题——HTML 直接带正确主题：无 FOUC）；「主题的来源层次」：cookie（SSR 可读）> localStorage（client only）> prefers-color-scheme（client media query）。
- cookie 主题的写入：切换主题时写 cookie（client JS set-cookie 或 action——SSR 下次渲染读 cookie = 服务端渲染正确主题）。
- prefers-color-scheme 的 SSR 处理：cookie 不存在时——inline script 读 matchMedia（CSS 加载前执行——RBL-777 theme boot）；「inline script + CSS 变量」的双保险（RBL-777）。
- 追问钩子：为什么「主题用 cookie 而非 localStorage」是 SSR 一致性的关键？——cookie 随请求发送（SSR 可读 → 服务端渲染用户主题——HTML 即正确）；localStorage client only（SSR 读不到 → 渲染默认主题 → client 切换 = FOUC + mismatch）；「SSR 可读的状态进 cookie」原则（RBL-936 状态序列化的 cookie 维度）：任何影响渲染的用户状态（主题/locale/实验组）都应进 cookie——SSR 一致性的通用解。

```tsx
// cookie 主题（SSR 可读）
// middleware：读 cookie 主题 → 注入 data-theme 属性
export function middleware(req) {
  const theme = req.cookies.get('theme')?.value ?? 'auto';
  const res = NextResponse.next({ headers: { 'x-theme': theme } });
  return res;
}
// RSC：读主题渲染
export default function RootLayout({ children }) {
  const theme = headers().get('x-theme') ?? 'light';
  return (
    <html data-theme={theme}>
      <body>
        {children}
        {/* 切换主题：action 写 cookie（SSR 下次渲染即新主题） */}
        <ThemeToggle />
      </body>
    </html>
  );
}
'use server';
export async function setThemeCookie(theme: string) {
  (await cookies()).set('theme', theme, { maxAge: 31536000, path: '/' });
}
// prefers-color-scheme 兜底（cookie=auto 时）
// inline script（CSS 加载前）：matchMedia('(prefers-color-scheme: dark)') → data-theme
```
