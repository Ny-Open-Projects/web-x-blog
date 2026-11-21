---
title: [H5-095] 屏幕方向如何监听与锁定？screen.orientation 的能力边界。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-095：屏幕方向如何监听与锁定？screen.orientation 的能力边界。
**答**：
- 监听变化：`screen.orientation.addEventListener('change')`，读 `type`（landscape-primary 等）与 `angle`；`resize` 也随方向触发但语义弱。
- 锁定：`screen.orientation.lock('landscape')` 需 **Fullscreen API 激活状态**（全屏内才允许锁方向），失败抛 NotSupportedError。
- 解锁用 `screen.orientation.unlock()`；退出全屏后锁定自动失效。
- CSS 侧兜底：`@media (orientation: portrait/landscape)` 排版适配永远比 JS 锁定优先考虑——锁不住的环境（iOS Safari 不支持 lock）必须能正常竖屏。
- 游戏场景组合拳：全屏 → 锁横屏 → 提示"请横屏游玩"；按 try/catch 降级为竖屏可玩布局。

```html
<style>
  /* CSS 先行：竖屏时给横屏游戏的遮罩提示 */
  @media (orientation: portrait) {
    .rotate-tip { display: flex; }
  }
  .rotate-tip {
    display: none;
    position: fixed; inset: 0;
    background: #000c; color: #fff;
    align-items: center; justify-content: center;
    z-index: 99;
  }
</style>

<p class="rotate-tip">请将设备横过来以获得最佳体验</p>
<button id="enter-game">全屏进入游戏</button>

<script>
  document.getElementById('enter-game').addEventListener('click', async () => {
    const el = document.documentElement;
    try {
      await el.requestFullscreen();                       // 1) 必须先全屏
      await screen.orientation.lock('landscape');         // 2) 再锁横屏
    } catch (err) {
      // iOS Safari 不支持 lock：降级为竖屏布局 + 提示
      console.warn('方向锁定失败：', err.name);
    }
  });

  // 3) 监听方向变化：双保险
  screen.orientation?.addEventListener?.('change', () => {
    console.log('方向：', screen.orientation.type, screen.orientation.angle);
  });

  // 4) 退出游戏时恢复
  function exitGame() {
    screen.orientation?.unlock();
    if (document.fullscreenElement) document.exitFullscreen();
  }
</script>
```
