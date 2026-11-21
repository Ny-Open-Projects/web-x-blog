---
title: [H5-142] WebAudio 音效播放池怎么做？移动端为什么要"解锁"音频上下文？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-142：WebAudio 音效播放池怎么做？移动端为什么要"解锁"音频上下文？
**答**：
- iOS/部分安卓要求 `AudioContext` 必须在**用户手势内** `resume()`，否则处于 suspended 状态播放静音——所以首次点击要做"解锁"。
- `AudioBuffer` 解码一次后复用；`AudioBufferSourceNode` 是一次性对象（播完即弃），所谓"播放池"实际是**并发上限控制 + 活跃 source 集合管理**。
- 多音效重叠：直接创建多个 source，用 `GainNode` 独立控音量；`playbackRate` 可做随机变调避免重复感。
- 对比 `<audio>`：WebAudio 延迟低、可精控混音/变速/空间化，但必须有解锁流程；`<audio>` 简单但延迟与调度粗。

```html
<button id="fire">播放音效（可叠加）</button>
<script>
class SoundPool {
  #ctx; #buffers = new Map(); #active = new Set(); #maxVoices = 5;
  async unlock() {                 // 必须在用户手势内调用一次
    this.#ctx ??= new (window.AudioContext || window.webkitAudioContext)();
    if (this.#ctx.state === 'suspended') await this.#ctx.resume();  // iOS 关键
  }
  async load(name, url) {
    const res = await fetch(url);
    // decodeAudioData 一次解码，之后播放零解码开销
    this.#buffers.set(name, await this.#ctx.decodeAudioData(await res.arrayBuffer()));
  }
  play(name, { volume = 1, rate = 1 } = {}) {
    const buf = this.#buffers.get(name);
    if (!buf || this.#active.size >= this.#maxVoices) return;   // 并发上限
    const src = this.#ctx.createBufferSource();   // source 是一次性对象，播完即弃
    src.buffer = buf;
    src.playbackRate.value = rate;
    const gain = this.#ctx.createGain();
    gain.gain.value = volume;
    src.connect(gain).connect(this.#ctx.destination);
    this.#active.add(src);
    src.onended = () => { this.#active.delete(src); src.disconnect(); };
    src.start();
  }
}
const pool = new SoundPool();
document.getElementById('fire').onclick = async () => {
  await pool.unlock();             // 第一次点击：解锁 + 预加载
  await pool.load('hit', '/sfx/hit.mp3').catch(() => {});
  pool.play('hit', { volume: 0.6, rate: 0.95 + Math.random() * 0.1 });  // 变调去重复感
};
</script>
```
