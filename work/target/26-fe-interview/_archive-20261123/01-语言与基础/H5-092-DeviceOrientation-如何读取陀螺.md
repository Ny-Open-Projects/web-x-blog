---
title: [H5-092] DeviceOrientation 如何读取陀螺仪？iOS 13+ 的权限问题怎么处理？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-092：DeviceOrientation 如何读取陀螺仪？iOS 13+ 的权限问题怎么处理？
**答**：
- 数据三轴：`alpha`（罗盘 0-360）、`beta`（前后倾）、`gamma`（左右倾）；`DeviceMotionEvent` 提供加速度与转速，两者常配合使用。
- **iOS 13+ 必须**先调 `DeviceOrientationEvent.requestPermission()`（返回 granted/denied），且**只能在用户手势里调用**；Android 直接 `addEventListener` 即可。
- 权限拒绝后无法再申请，只能引导用户去设置开启"动作与方向访问"；HTTPS 是所有传感器 API 的前提。
- 数据噪声大：要做低通滤波（`cur = cur * a + raw * (1 - a)`）和节流，否则界面抖动。
- 事件频率约 60Hz，处理函数里避免 DOM 写入，用 rAF 合帧。

```html
<button id="enable-tilt">开启倾斜检测</button>
<p id="tilt-out">等待数据…</p>

<script>
  const out = document.getElementById('tilt-out');
  let smoothed = { beta: 0, gamma: 0 };

  async function startTilt() {
    // iOS 13+：必须在手势里先要权限
    if (typeof DeviceOrientationEvent?.requestPermission === 'function') {
      const state = await DeviceOrientationEvent.requestPermission();
      if (state !== 'granted') return alert('请在 设置-隐私-动作与方向 中允许访问');
    }

    window.addEventListener('deviceorientation', (e) => {
      // 低通滤波抗抖：a 越小越平滑
      const a = 0.15;
      smoothed.beta = smoothed.beta * (1 - a) + (e.beta ?? 0) * a;
      smoothed.gamma = smoothed.gamma * (1 - a) + (e.gamma ?? 0) * a;

      requestAnimationFrame(() => {
        out.textContent =
          `beta（前后倾）${smoothed.beta.toFixed(1)}°，` +
          `gamma（左右倾）${smoothed.gamma.toFixed(1)}°，` +
          `alpha（朝向）${Math.round(e.alpha ?? 0)}°`;
      });
    });
  }

  document.getElementById('enable-tilt').addEventListener('click', startTilt);
</script>

<script>
  // parallax 应用：根据倾斜角移动背景层
  window.addEventListener('deviceorientation', (e) => {
    const bg = document.querySelector('.parallax-bg');
    if (!bg || e.gamma == null) return;
    bg.style.transform =
      `translate(${(e.gamma / 45) * -10}px, ${(e.beta / 45) * -10}px)`;
  });
</script>
```
