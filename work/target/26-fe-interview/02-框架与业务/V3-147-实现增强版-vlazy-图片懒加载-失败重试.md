---
title: [V3-147] 实现增强版 v-lazy 图片懒加载（失败重试 + webp 降级）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-147：实现增强版 v-lazy 图片懒加载（失败重试 + webp 降级）？
**答**：
- IntersectionObserver 监听进入视口（rootMargin 提前 200px 预加载），进入后 disconnect 再加载，比 scroll 监听性能好。
- webp 能力一次性探测并缓存：支持时把 .jpg/.png URL 替换成 CDN 的 .webp（七牛/OSS 常见规则），不支持时退回原格式。
- 失败重试链：webp 失败先退回原格式，再失败按指数退避（500ms * 2^n）重试，超过上限兜底占位图。
- 加载成功淡入（opacity 过渡），卸载时 disconnect observer 防泄漏。

```vue
<!-- directives/lazy.ts + 使用示例 -->
<script setup lang="ts">
import { type Directive } from "vue";

const RETRY_LIMIT = 3;

// webp 能力探测：一次性缓存结果
let webpSupported: boolean | null = null;
function detectWebp(): boolean {
  if (webpSupported !== null) return webpSupported;
  const canvas = document.createElement("canvas");
  canvas.width = canvas.height = 1;
  webpSupported = canvas.toDataURL("image/webp").startsWith("data:image/webp");
  return webpSupported;
}

function load(el: HTMLImageElement, src: string, retry: number) {
  const finalSrc = detectWebp()
    ? src.replace(/\.(png|jpe?g)(\?|$)/, ".webp$2") // CDN webp 参数规则
    : src;
  const img = new Image();
  img.onload = () => {
    el.src = finalSrc;
    el.style.opacity = "1"; // 淡入
  };
  img.onerror = () => {
    if (retry === 0 && finalSrc !== src) return load(el, src, 1); // webp 失败退回原格式
    if (retry < RETRY_LIMIT) {
      return setTimeout(() => load(el, src, retry + 1), 500 * 2 ** retry); // 指数退避
    }
    el.src = "data:image/svg+xml;base64,PHN2Zy8+"; // 兜底占位图
    el.style.opacity = "1";
  };
  img.src = finalSrc;
}

const vLazy: Directive<HTMLImageElement, string> = {
  mounted(el, binding) {
    el.style.opacity = "0";
    el.style.transition = "opacity .3s";
    const io = new IntersectionObserver(
      (entries) => {
        if (!entries[0].isIntersecting) return;
        io.disconnect();
        load(el, binding.value, 0);
      },
      { rootMargin: "200px 0px" } // 提前 200px 预加载
    );
    io.observe(el);
    (el as any)._lazyIO = io;
  },
  unmounted(el) {
    (el as any)._lazyIO?.disconnect(); // 防泄漏
  },
};

const goods = Array.from({ length: 30 }, (_, i) => ({ id: i + 1, img: `/img/item-${i + 1}.jpg` }));
</script>

<template>
  <ul class="list">
    <li v-for="g in goods" :key="g.id">
      <img v-lazy="g.img" width="200" height="150" loading="decoding-async" />
    </li>
  </ul>
</template>
```
