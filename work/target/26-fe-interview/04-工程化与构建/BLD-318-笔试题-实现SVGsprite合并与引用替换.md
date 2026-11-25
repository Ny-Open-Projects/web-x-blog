---
title: [BLD-318] 笔试题——实现 SVG sprite 合并与引用替换？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-318：手写 SVG sprite

**需求与边界**：
- 需求：图标目录 → sprite 产物 + 引用替换（SCN-BLD-284）——① 扫描源码中使用的图标（只打包用到的——按需 sprite）；② sprite 生成（symbol 元素 + id）；③ 源码引用替换（<img src> → <use href>）；④ 清理（SVGO 参数化——precision/去元数据）。
- 边界：① 只含使用到的图标（全量 sprite 体积黑洞——使用分析）；② id 冲突防御（同 name 不同目录——加前缀）；③ 清理保留必要属性（viewBox/aria——可访问性不能删）。

**答**：
```javascript
async function svgSprite(srcDir, sourceFiles) {
  // 1. 使用分析（只打包用到的）
  const used = new Set();
  for (const file of sourceFiles)
    for (const m of fs.readFileSync(file, 'utf8').matchAll(/icon-([\w-]+)/g))
      used.add(m[1]);
  // 2. sprite 生成（symbol + 前缀防冲突）
  const symbols = [...used].map(name => {
    const raw = fs.readFileSync(path.join(srcDir, name + '.svg'), 'utf8');
    const cleaned = svgoOptimize(raw, { precision: 2, removeMetadata: true,
      keepViewBox: true, keepAria: true });            // 清理保留 viewBox/aria
    return `<symbol id="icon-${name}" ${extractAttrs(cleaned)}>${extractInner(cleaned)}</symbol>`;
  }).join('\n');
  const sprite = `<svg style="display:none" xmlns="...">${symbols}</svg>`;
  const spriteHash = sha256(sprite).slice(0, 8);
  fs.writeFileSync(`icons-${spriteHash}.svg`, sprite);
  // 3. 引用替换
  for (const file of sourceFiles)
    replace(file, /<img[^>]*icon-([\w-]+)[^>]*>/g,
      `<svg class="icon"><use href="/icons-${spriteHash}.svg#icon-$1"/></svg>`);   // use 引用
  return { sprite: `icons-${spriteHash}.svg`, usedCount: used.size };
}
```

**评分点**:
- 使用分析驱动（只打包用到的——非全量黑洞）。
- 清理参数化（precision/去元数据但保留 viewBox/aria——可访问性）。
- id 冲突防御 + hash 命名（缓存友好）。
- 源码引用替换（img → use——闭环）。
