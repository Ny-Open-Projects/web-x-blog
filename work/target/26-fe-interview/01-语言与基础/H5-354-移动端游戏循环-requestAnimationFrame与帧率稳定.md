---
title: [H5-354] 移动端游戏循环：rAF、帧率稳定与降级
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## H5-354：移动端游戏循环：rAF、帧率稳定与降级

**答**：
- rAF 是唯一节拍器：与屏幕刷新对齐（60/90/120Hz），hidden 自动暂停天然省电；游戏循环 = rAF + 固定步长逻辑（fixed timestep）+ 插值渲染
- 帧时间补偿：dt = min(now - last, 50ms) 防切后台回来跳帧爆冲；物理逻辑用固定步长（1/60s 累积器）保证不同刷新率行为一致
- 帧率监控与降级：滑动窗口统计帧间隔，连续低于目标（如 24fps）触发降级链——降 dpr → 减粒子/特效 → 关阴影 → 提示切换低画质
- 长任务切分：单帧逻辑 > 8ms 的（寻路/AI）分帧处理或挪 Worker（物理/AI 可 Worker + SAB）
- 输入与渲染分离：触摸采样在事件循环，渲染在 rAF，两者间用输入缓冲；高刷屏输入延迟优化用 desynchronized 上下文

```javascript
let last = performance.now(), acc = 0;
const STEP = 1000 / 60;
function loop(now) {
  let dt = Math.min(now - last, 50);
  last = now; acc += dt;
  while (acc >= STEP) { update(STEP); acc -= STEP; }   // 固定步长
  render(acc / STEP);                                   // 插值渲染
  fpsMonitor(now);                                      // 帧率监控触发降级
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```
