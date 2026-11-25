---
title: [MP-370] 笔试：手写埋点 Behavior（PV/停留时长/曝光）
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 笔试题, 可观测]
type: 笔试题
---

## MP-370：笔试：手写埋点 Behavior

**答**：实现页面埋点 Behavior：① PV：onShow 记录（route/scene/来源参数）+ 去重（热启动重复 onShow——同一页面连续 onShow 不重复计）；② 停留时长：onShow→onHide 时间差，离开时上报（onUnload 兜底未上报的）；③ 曝光：组件级 IO observer 声明式触发；④ 停留时长的「后台时间剔除」（切后台不计——onHide 分段计算）；⑤ 批量上报（队列 + onHide flush）。写出实现。

```javascript
export const trackBehavior = Behavior({
  lifetimes: {
    attached() { this._showAt = null; this._activeMs = 0; },
  },
  pageLifetimes: {
    show() {
      const now = Date.now();
      if (!this._showAt) {                            // 去重: 连续 show 不重复 PV
        this._showAt = now;
        track('pv', { route: this.route, scene: getScene(), query: this.options });
      }
    },
    hide() {
      if (this._showAt) {
        this._activeMs += Date.now() - this._showAt;  // 后台时间剔除: 分段累加
        this._showAt = null;
        track('stay', { route: this.route, ms: this._activeMs });   // 每段上报
        this._activeMs = 0;
      }
      flushTrack();                                   // 切后台 flush
    },
    unload() {
      // 兜底: 直接退出小程序(onUnload 触发但 hide 未计)
      if (this._showAt) track('stay', { route: this.route, ms: Date.now() - this._showAt + this._activeMs });
    },
  },
  methods: {
    trackExpose(slotId) {
      this._io ??= this.createIntersectionObserver().relativeToViewport({ bottom: 0 });
      this._io.observe(`#exp-${slotId}`, (res) => {
        if (res.intersectionRatio > 0.5) track('expose', { slot: slotId });
      });
    },
  },
});
```

**评分点**：
- 连续 onShow 去重（热启动重复触发）
- 后台时间剔除（分段累加 activeMs）
- onUnload 兜底（直接退出的停留时长）
- IO 曝光与 visibility 声明式接入
