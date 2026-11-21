---
title: [AGT-088] AI 建议的三种 UI 模式（inline ghost text / side panel / chat）如何选型与实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-088：AI 建议的三种 UI 模式（inline ghost text / side panel / chat）如何选型与实现？
**答**：
- 三模式适配不同任务形态：ghost text 行内补全（低延迟、Tab 采纳）、side panel（解释/改写等中等任务、不打断编辑）、chat（开放式多轮任务）。
- 选型原则：短且高频 → inline；需要展示推理或多个候选 → panel；需要澄清对话 → chat；三者共享同一后端与上下文收集器。
- ghost text 技术要点：300ms 防抖 + 竞态取消（新请求 abort 旧请求）+ 输入即作废旧建议 + Tab 接受/Esc 拒绝。
- 埋点：建议展示与接受都要打点，接受率是补全质量的核心指标（AGT-114）。

```typescript
import { z } from 'zod';

// ghost text：防抖 + 竞态取消 + Tab 采纳
function useGhostText(editor: EditorLike) {
  const [ghost, setGhost] = useState('');
  const ctrlRef = useRef<AbortController | null>(null);
  const timerRef = useRef<number | undefined>(undefined);

  const request = async (prefix: string, suffix: string) => {
    ctrlRef.current?.abort();                      // 关键：新请求取消旧请求，防旧建议晚到覆盖
    const ctrl = new AbortController();
    ctrlRef.current = ctrl;
    try {
      const res = await fetch('/api/complete', {
        method: 'POST', signal: ctrl.signal,
        body: JSON.stringify({ prefix, suffix, max_tokens: 48 }),
      });
      const { text } = await res.json();
      if (!ctrl.signal.aborted) setGhost(text);
    } catch { /* aborted：忽略 */ }
  };

  useEffect(() => editor.onChange(() => {
    setGhost('');                                  // 输入即作废旧建议
    clearTimeout(timerRef.current);
    timerRef.current = window.setTimeout(
      () => request(editor.getPrefix(), editor.getSuffix()), 300,
    );
  }), []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (ghost && e.key === 'Tab') { e.preventDefault(); editor.insertAtCursor(ghost); setGhost(''); }
      if (e.key === 'Escape') setGhost('');
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [ghost]);
}
```
