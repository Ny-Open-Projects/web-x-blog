---
title: [H5-197] 设计一个 emoji 选择器（分类/搜索/最近使用）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-197：设计一个 emoji 选择器（分类/搜索/最近使用）
**答**：
- 数据：emoji 按 CLDR 分组（笑脸/手势/动物…），**关键词索引构建期生成**（emoji-data/CLDR 短名），不要运行时全量正则。
- 最近使用：localStorage 存频次 Top16，使用时置顶并去重。
- 搜索：关键词表匹配（中英文）+ Unicode 短名；皮肤色用 modifier 序列（基础 emoji + U+1F3FB~1F3FF）长按弹出。
- 工程：几千个 emoji 的渲染用分区懒渲染/content-visibility；插入操作 textarea 的 value + selectionStart 保持光标；不同平台字形不同，可指定字体栈统一风格。

```javascript
// emoji 选择器：数据分组 + 搜索 + 最近使用
const DATA = [
  { group: '笑脸', emojis: ['😀','😃','😄','😁','😆','😅','😂','🤣'] },
  { group: '手势', emojis: ['👍','👎','👌','✌️','🤞','👏','🙏'] },
  { group: '动物', emojis: ['🐶','🐱','🦊','🐻','🐼','🐨'] },
];
// 关键词索引：构建期由 emoji-data / CLDR 短名生成，别运行时全量正则
const KEYWORDS = {
  '😀': ['笑脸', '开心', 'grinning'],
  '👍': ['赞', ' thumbs up'],
  '🐶': ['狗', 'dog'],
};

// 1) 最近使用：localStorage 存 Top16，使用时置顶去重
const recent = () => JSON.parse(localStorage.getItem('emoji-recent') ?? '[]');
function use(emoji) {
  const r = [emoji, ...recent().filter((e) => e !== emoji)].slice(0, 16);
  localStorage.setItem('emoji-recent', JSON.stringify(r));
  render();
  return emoji;                  // 插入由调用方决定（输入框/聊天框）
}

// 2) 搜索：关键词表匹配（中英文 + Unicode 短名）
function search(q) {
  q = q.trim().toLowerCase();
  if (!q) return DATA.flatMap((g) => g.emojis);
  return Object.entries(KEYWORDS)
    .filter(([, ks]) => ks.some((k) => k.toLowerCase().includes(q)))
    .map(([e]) => e);
}

// 3) 渲染：几千个 emoji 分区懒渲染（每组的容器 content-visibility: auto）
const grid = document.getElementById('grid');
function render(list = search(searchInput.value)) {
  grid.replaceChildren(...list.map((e) => {
    const b = document.createElement('button');
    b.className = 'emoji';
    b.textContent = e;
    b.setAttribute('aria-label', KEYWORDS[e]?.[0] ?? e);   // 可访问性
    b.onclick = () => insertToInput(use(e));
    return b;
  }));
}
render();

// 4) 插入保持光标：操作 textarea 的 value + selectionStart
function insertToInput(emoji) {
  const ta = document.querySelector('textarea');
  const s = ta.selectionStart;
  ta.value = ta.value.slice(0, s) + emoji + ta.value.slice(ta.selectionEnd);
  ta.setSelectionRange(s + emoji.length, s + emoji.length);
  ta.focus();
}
// 5) 工程点：
// - 皮肤色：modifier 序列（基础 emoji + U+1F3FB~1F3FF）长按弹出
// - 平台字形差异：字体栈 Apple Color Emoji → Noto Color Emoji 统一风格
// - 分区懒渲染 / content-visibility: auto 扛几千个节点的首屏
```
