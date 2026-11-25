---
title: [MFW-776] 笔试：手写 Flight 流解析合并器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-776：笔试：手写 Flight 流解析合并

**答**：实现 `createMergedStreamParser()`。输入：HTML 与 Flight chunk 交织的流（RBL-775 形态）。方法：`push(htmlOrChunk)`。规则：1) **区分 HTML 与 Flight**：Flight chunk 的标志 = `<script>(self.__next_f.push(...)` 或以行格式 `数字:` 开头——HTML = 其他；2) HTML → DOM 渲染（mock：onHtml 回调）；Flight → 解析（RBL-503 的行格式——onFlight 回调）；3) **顺序保持**：HTML 与 Flight 的交织顺序 = 到达顺序（不做排序——流式语义 RBL-714）；4) `stats()` 返回 `{ htmlChunks, flightChunks, totalBytes }`。边界：纯 HTML（无 Flight）；纯 Flight（SSR prefetch——无 HTML）；空 push。

```javascript
function createMergedStreamParser({ onHtml, onFlight } = {}) {
  let htmlChunks = 0, flightChunks = 0, totalBytes = 0;
  return {
    push(content) {
      if (!content) return;
      totalBytes += content.length;
      // Flight 检测：inline script push 或行格式
      const isFlight = /self\.__next_f\.push\(/.test(content) ||
        /^\d+:\[/.test(content.trim());
      if (isFlight) {
        flightChunks++;
        // 提取 Flight 数据
        const match = content.match(/push\(\[("[^"]+"),\s*("(?:[^"\\]|\\.)*")\]\)/);
        const flightData = match ? JSON.parse(match[2]) : content;
        onFlight?.(flightData);
      } else {
        htmlChunks++;
        onHtml?.(content);
      }
    },
    stats: () => ({ htmlChunks, flightChunks, totalBytes }),
  };
}

// 自测
const htmlParts = [], flightParts = [];
const parser = createMergedStreamParser({
  onHtml: (h) => htmlParts.push(h),
  onFlight: (f) => flightParts.push(f),
});
// 交织流
parser.push('<div>content</div>');                       // HTML
parser.push('<script>(self.__next_f.push(["0","[\\\"$\\\",\\\"div\\\"]"]))</script>');   // Flight
parser.push('<div>more</div>');                          // HTML
parser.push('<script>(self.__next_f.push(["1","[\\\"$\\\",\\\"p\\\"]"]))</script>');     // Flight
console.log(parser.stats().htmlChunks === 2);
console.log(parser.stats().flightChunks === 2);
console.log(htmlParts.join('') === '<div>content</div><div>more</div>');
console.log(flightParts.length === 2);

// 纯 HTML
const p2 = createMergedStreamParser({ onHtml: (h) => htmlParts.push(h) });
p2.push('<html><body>static</body></html>');
console.log(p2.stats().htmlChunks === 1 && p2.stats().flightChunks === 0);

// 纯 Flight（SSR prefetch）
const p3 = createMergedStreamParser({ onFlight: (f) => flightParts.push(f) });
p3.push('0:["$","div",null,{"children":"data"}]');
console.log(p3.stats().flightChunks === 1 && p3.stats().htmlChunks === 0);

// 空 push
p3.push('');
console.log(p3.stats().totalBytes === '0:["$","div",null,{"children":"data"}]'.length);
```

**评分点**：
- 双流区分（Flight 的 inline script 标志 + 行格式检测）；顺序保持（到达序）
- onHtml/onFlight 分离回调（消费方分别处理——HTML 渲染 vs Flight 解析 RBL-503）
- 边界（纯 HTML/纯 Flight/空 push）；stats 统计
- 能说清「Flight 嵌入 HTML 的 inline script 模式：同流到达无额外 RTT——合并流的原子性优于分流」属于加分
