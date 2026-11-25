---
title: [AGT-108] 设计一个浏览器自动化 Agent（DOM 感知 + 操作工具 + 安全边界）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-108：设计一个浏览器自动化 Agent（DOM 感知 + 操作工具 + 安全边界）？
**答**：
- DOM 感知：不把 HTML 全塞给模型（太大且脆），而是序列化「可交互元素清单」（编号 + 角色 + 文本 + 选择器），模型只输出「点击 N 号元素」这类结构化动作。
- 感知-决策-行动循环：每步重新感知（DOM 会变，元素编号重算），动作基于编号引用而非硬编码 XPath，失败自动重新感知。
- 安全边界：域名白名单、禁支付/删除类页面动作、步数上限、全程操作日志可回放、敏感动作人工确认。
- 观察反馈：截图或 DOM 快照作为每步观察回给模型，视觉与结构双通道。

```typescript
import { z } from 'zod';

// 浏览器自动化 Agent：感知 - 决策 - 行动循环
interface PageElement { index: number; role: string; text: string; selector: string }

async function perceive(page: Page): Promise<PageElement[]> {
  return page.evaluate(() =>
    [...document.querySelectorAll('a,button,input,select,[role=button]')]
      .filter((el) => (el as HTMLElement).offsetParent !== null)     // 过滤不可见元素
      .slice(0, 100)
      .map((el, index) => ({
        index,
        role: el.tagName.toLowerCase(),
        text: ((el as HTMLElement).textContent ?? el.getAttribute('aria-label') ?? '').trim().slice(0, 80),
        selector: cssSelectorOf(el),
      })),
  );
}

export async function browseTask(page: Page, goal: string) {
  const WHITELIST = ['example.com', 'docs.example.com'];             // 安全边界：域名白名单
  for (let step = 0; step < 15; step++) {
    if (!WHITELIST.includes(new URL(page.url()).hostname)) throw new Error('越出白名单，终止');
    const elements = await perceive(page);
    const action = await structuredLLM(
      [{
        role: 'user',
        content: `目标：${goal}
当前页面可交互元素：${JSON.stringify(elements)}
输出动作 JSON：{"act":"click","index":N} 或 {"act":"type","index":N,"text":"..."} 或 {"act":"done","answer":"..."}`,
      }],
      z.union([
        z.object({ act: z.literal('click'), index: z.number() }),
        z.object({ act: z.literal('type'), index: z.number(), text: z.string() }),
        z.object({ act: z.literal('done'), answer: z.string() }),
      ]),
    );
    if (action.act === 'done') return action.answer;
    await execAction(page, action, elements);                        // 按编号执行并等待渲染
  }
  throw new Error('超过步数上限');
}
```
