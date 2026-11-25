---
title: [SCN-268] H5 唤起地图 App——URL Scheme 与兜底策略？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-268：H5 页面点导航要唤起手机高德/百度地图 App，怎么实现与兜底？

**答**:
- 唤起机制：URL Scheme（高德 androidamap/iosamap、百度 bdapp://）或 Universal Link/App Link（更可靠但需域名配置）、web 兜底（唤不起→打开地图 web 版导航页）。
- 唤起检测：尝试 scheme 后检测是否成功（visibilitychange/页面隐藏=唤起成功；timeout 未隐藏=未安装→跳 web 版）， iOS 与 Android 检测时机差异（Android 用 intent URL 更可靠：intent://...#Intent;scheme=...;package=...;end）。
- 选择器交互：多地图选择（用户装了高德和百度——选择面板列出可用项+记住选择），参数标准化（起点/终点/坐标坐标系转换：GCJ-02 vs WGS-84 的坑——国内地图用 GCJ-02，混用偏移 500 米）。
- 边界：微信/浏览器内 scheme 被屏蔽（微信内需引导右上角浏览器打开或使用微信内地图能力）、坐标系的统一转换层（业务统一 WGS-84，唤起时按目标 App 转换）。

```javascript
function openNav(target, { lat, lng }) {
  const schemes = [
    { name: '高德', url: isIOS()
      ? `iosamap://navi?sourceApplication=app&poiname=${target}&lat=${gcj(lat)}&lon=${gcj(lng)}&dev=0`
      : `androidamap://navi?sourceApplication=app&poiname=${target}&lat=${gcj(lat)}&lon=${gcj(lng)}&dev=0` },
    { name: '百度', url: `bdapp://map/direction?destination=${target}` },
  ];
  showPicker(schemes, (s) => {
    const t0 = Date.now();
    location.href = s.url;
    setTimeout(() => {                        // 2.5s 未离开=未安装
      if (document.visibilityState === 'visible' &&
          Date.now() - t0 > 2400)
        location.href = webNavUrl(target);    // web 版兜底
    }, 2500);
  });
}
// 坐标系：业务 WGS-84 → GCJ-02 转换层（国内 App 用 GCJ-02）。
```

**追问**：

1. 用 `visibilityState === 'visible'` 判未安装，但 iOS 从 scheme 返回时也是 visible，怎么区分？ → 记录发起时刻，返回后若 elapsed 明显小于超时且期间曾隐藏过则视为成功，单看最终状态会误判。
2. 微信内 scheme 被拦，只能引导浏览器打开吗？ → 优先用微信内置地图能力或跳 H5 导航页，引导文案要给「右上角」的具体操作。
3. 坐标系只转 lat/lng 就够了吗？ → GCJ-02 转换要成对转且不可重复转，二次转换会再偏几百米，转换层要加幂等标记。
