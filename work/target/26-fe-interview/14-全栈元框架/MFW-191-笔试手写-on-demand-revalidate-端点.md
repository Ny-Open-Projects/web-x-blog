---
title: [MFW-191] 笔试：手写 on-demand revalidate 端点（secret 校验 + 分派）
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-191：笔试：手写 on-demand revalidate 端点（secret 校验 + tag/path 分派）
**答**：实现一个 `/api/revalidate` 端点（Route Handler）供 CMS webhook 调用：① 必须带 `?secret=`，与 `process.env.REVALIDATE_SECRET` 比较（用恒时比较防时序攻击）；② 按 body 分派：`{ type: 'tag', tag }` 走 revalidateTag，`{ type: 'path', path }` 走 revalidatePath；③ path 必须是站内路径（防「cache 欺骗」：外部输入不能清除任意路径）；④ 支持 tag 批量（数组）；⑤ 记录审计日志（谁在何时失效了什么）；⑥ webhook 重试会重复调用——端点必须幂等安全。

```ts
import { revalidatePath, revalidateTag } from 'next/cache';
import { timingSafeEqual } from 'node:crypto';
import { NextRequest } from 'next/server';

const SITE_PREFIX = '/'; // ③ 允许清单前缀

function safeEqual(a: string, b: string) {
  const ab = Buffer.from(a), bb = Buffer.from(b);
  return ab.length === bb.length && timingSafeEqual(ab, bb);
}

export async function POST(req: NextRequest) {
  const secret = req.nextUrl.searchParams.get('secret') ?? '';
  if (!safeEqual(secret, process.env.REVALIDATE_SECRET ?? '')) {
    return Response.json({ error: 'forbidden' }, { status: 403 });
  }
  const body = await req.json();
  const tags: string[] = [];
  try {
    if (body.type === 'tag') {
      for (const tag of [].concat(body.tag)) { // ④ 批量
        if (typeof tag !== 'string' || !tag) continue;
        revalidateTag(tag); tags.push(tag);
      }
    } else if (body.type === 'path') {
      const path: string = body.path;
      // ③ 只允许站内路径：拒绝协议/域名与越界路径
      if (typeof path === 'string' && path.startsWith(SITE_PREFIX) && !path.includes('..')) {
        revalidatePath(path); tags.push(`path:${path}`);
      } else {
        return Response.json({ error: 'invalid path' }, { status: 400 });
      }
    } else {
      return Response.json({ error: 'unknown type' }, { status: 400 });
    }
    console.info('[revalidate] by webhook', { tags, at: new Date().toISOString() }); // ⑤ 审计
    return Response.json({ revalidated: tags, now: Date.now() }); // ⑥ 重复调用无副作用
  } catch {
    return Response.json({ error: 'failed' }, { status: 500 }); // 让 webhook 重试
  }
}
```

**评分点**：
1. secret 用恒时比较（timingSafeEqual），普通 === 会泄漏前缀匹配信息。
2. path 白名单校验防 cache 欺骗（外部输入可清除任意路径是真实漏洞）。
3. tag 批量处理 + 未知 type 返回 400 而不是静默成功。
4. 幂等性：revalidate 重复调用无副作用，webhook 重试安全；失败时返回 5xx 触发上游重试。
5. 审计日志包含失效对象与时间——缓存失效是高危操作，必须可追溯。
