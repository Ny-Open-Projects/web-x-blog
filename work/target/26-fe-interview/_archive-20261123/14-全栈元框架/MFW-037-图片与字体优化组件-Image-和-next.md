---
title: [MFW-037] next/image 与 next/font 在元框架层面解决了什么问题？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-037：next/image 与 next/font 在元框架层面解决了什么问题？
**答**：
- `next/image` 四件事：**自动按视口生成多尺寸 srcset**（按需缩放）、**转 WebP/AVIF**、**懒加载 + 首屏 preload**（priority）、**强制 width/height 防止 CLS**——把图片优化清单从人工变成框架默认。
- `next/font` 构建期自托管字体：内联 woff2 到构建产物（无第三方请求）、自动 `font-display: swap`、消除 FOIT/FOUT、配合 CSS 变量供 Tailwind 使用。
- 两者的共同思想：**元框架把「性能最佳实践」做成默认行为**——这是与纯 Vite/CRA 项目的本质差距。
- Image 配置：`remotePatterns` 白名单外部图源；`sizes` 属性让 srcset 选择更准（视口内实际宽度）。
- 代价要知道：图片处理占服务 CPU（可换 loader 走 CDN 端处理），字体自托管要求构建产物携带字体文件。

```jsx
import Image from 'next/image';
import { Inter, Noto_Sans_SC } from 'next/font/google';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter', display: 'swap' });
const sans = Noto_Sans_SC({ weight: '400', subsets: ['latin'], variable: '--font-sans' });

export default function Product({ p }) {
  return (
    <div className={`${inter.variable} ${sans.variable}`}>
      <Image
        src={p.cover}          // 可为本地或 remotePatterns 白名单域名
        alt={p.title}
        width={800} height={600} // 防布局抖动
        priority               // LCP 图：preload，不懒加载
        sizes="(max-width: 768px) 100vw, 50vw" // 帮浏览器选最合适的 srcset
      />
      <h1 className="font-[var(--font-sans)]">{p.title}</h1>
    </div>
  );
}
```
