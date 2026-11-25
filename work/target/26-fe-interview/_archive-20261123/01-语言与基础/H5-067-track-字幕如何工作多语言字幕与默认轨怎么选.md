---
title: [H5-067] track 字幕如何工作？多语言字幕与默认轨怎么选？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-067：track 字幕如何工作？多语言字幕与默认轨怎么选？
**答**：
- `<track kind="subtitles">` 给 video 挂 WebVTT 字幕，`srclang` 声明语言，`label` 是菜单显示名；**不带 kind 默认按 subtitles 处理**。
- `default` 属性标记默认开启的轨道，但注意：带 `default` 的 subtitles 在 Chrome 等浏览器**默认并不自动显示**，需要用户在菜单开启或 JS 控制 `track.mode`。
- `kind` 还有 `captions`（含音效描述的无障碍字幕）、`chapters`（章节导航）、`descriptions`、`metadata`（隐藏轨，JS 读取 cue 做联动）。
- 多语言切换本质是改 `textTrack.mode`：`showing / hidden / disabled` 三态，JS 切换即时生效无需重载视频。
- VTT 文件必须与视频**同源或带 CORS 头**，跨域字幕缺失是高频 bug；cuechange 事件可驱动弹幕、高亮歌词等衍生功能。

```html
<video id="lecture" src="/media/lecture.mp4" controls preload="metadata"
       crossorigin="anonymous">
  <track kind="subtitles" srclang="zh" label="中文" src="/vtt/zh.vtt">
  <track kind="subtitles" srclang="en" label="English" src="/vtt/en.vtt">
  <track kind="chapters" srclang="zh" label="章节" src="/vtt/chapters.vtt">
  <track kind="metadata" src="/vtt/timeline.vtt"> <!-- 隐藏轨：驱动侧边笔记联动 -->
</video>

<script>
  const v = document.getElementById('lecture');
  const zh = v.textTracks[0], en = v.textTracks[1];

  // 手动语言切换：showing 同一时间只允许一条字幕轨
  document.getElementById('lang').addEventListener('change', (e) => {
    for (const t of v.textTracks) {
      if (t.kind === 'subtitles') t.mode = 'disabled';
    }
    v.textTracks[e.target.value].mode = 'showing';
  });

  // metadata 轨 cuechange：时间轴联动笔记高亮
  const meta = [...v.textTracks].find(t => t.kind === 'metadata');
  meta.mode = 'hidden';                          // 不显示但要解析
  meta.addEventListener('cuechange', () => {
    const cue = meta.activeCues[0];
    if (cue) highlightNote(cue.value.noteId);    // cue.value 携带 JSON 数据
  });

  // 校验字幕是否真的加载成功：404 或 CORS 失败时 mode 会异常
  zh.addEventListener('load', () => console.log('中文字幕就绪'));
</script>
```
