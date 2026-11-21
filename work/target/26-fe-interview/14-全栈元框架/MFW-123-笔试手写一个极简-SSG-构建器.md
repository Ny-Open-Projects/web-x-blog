---
title: [MFW-123] 笔试：手写一个极简 SSG 构建器（路由 + 渲染 + 输出）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-123：笔试：手写一个极简 SSG 构建器（路由 + 渲染 + 输出）
**题目**：实现 `build(config)`：① 遍历静态路由与带 `getStaticPaths` 的动态路由；② 用模板函数渲染 HTML；③ 输出到 dist 目录（含 index.html 与嵌套目录）；④ 渲染失败收集错误最后统一报告，失败的页面不产文件；⑤ 并发渲染（Promise pool，限制 8）。

```ts
import { mkdir, writeFile } from 'fs/promises';
import { join } from 'path';

type PageModule = {
  path?: string;                              // 静态路由
  getStaticPaths?: () => Promise<Array<{ params: Record<string, string>; props?: unknown }>>;
  template: (props: { params?: Record<string, string>; data?: unknown }) => string;
};

function fillPath(pattern: string, params: Record<string, string>): string {
  return pattern.replace(/:([\w]+)/g, (_, k) => params[k]);
}

async function pool<T>(tasks: Array<() => Promise<T>>, limit: number): Promise<void> {
  let i = 0;
  await Promise.all(Array.from({ length: Math.min(limit, tasks.length) }, async () => {
    while (i < tasks.length) await tasks[i++]();
  }));
}

async function build(config: { pages: PageModule[]; outDir: string }): Promise<void> {
  const jobs: Array<() => Promise<void>> = [];
  const errors: Array<{ path: string; err: unknown }> = [];

  await mkdir(config.outDir, { recursive: true });

  for (const page of config.pages) {
    if (page.getStaticPaths) {
      const paths = await page.getStaticPaths();
      for (const { params, props } of paths) {
        const url = fillPath(page.path ?? '', params);
        jobs.push(async () => {
          try {
            const html = page.template({ params, data: props });
            const file = join(config.outDir, url === '/' ? 'index.html' : url + '/index.html');
            await mkdir(join(file, '..'), { recursive: true });
            await writeFile(file, html);
          } catch (err) {
            errors.push({ path: url, err }); // 收集，不中断
          }
        });
      }
    } else {
      jobs.push(async () => {
        try {
          const html = page.template({ data: null });
          await writeFile(join(config.outDir, 'index.html'), html);
        } catch (err) { errors.push({ path: page.path ?? '/', err }); }
      });
    }
  }

  await pool(jobs, 8); // 并发渲染限 8

  if (errors.length) {
    // 统一报告：构建失败，指出具体页面
    throw new Error(`SSG 构建失败 ${errors.length} 页:\n` +
      errors.map((e) => `  - ${e.path}: ${(e.err as Error)?.message}`).join('\n'));
  }
  console.log(`构建完成：${jobs.length} 页`);
}

export { build };
```

**评分点**：
1. 动态路由参数展开正确（`:id` 替换），静态页输出 `index.html`、动态页输出嵌套目录 `products/p1/index.html`（干净 URL）。
2. 并发池限制 8 而不是全量 Promise.all（防内存/句柄打爆）。
3. 错误聚合：收集所有失败页最后统一抛出，且失败页不写文件。
4. mkdir recursive 处理嵌套目录；出口路径拼接用 path.join 防 Windows 分隔符问题。
5. 能说出真实 SSG 还需要：资源指纹、sitemap 生成、链接爬取发现隐藏路由。
