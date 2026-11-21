---
title: [H5-034] Geolocation API 如何使用？精度与权限怎么处理？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-034：Geolocation API 如何使用？精度与权限怎么处理？
**答**：
- `navigator.geolocation.getCurrentPosition(success, error, options)`，options 可设 `enableHighAccuracy`、`timeout`、`maximumAge`（缓存时长）。
- 必须在安全上下文（HTTPS），首次调用浏览器弹权限申请；用户拒绝后 error 回调 `PERMISSION_DENIED`。
- 持续追踪用 `watchPosition`，返回 id 用 `clearWatch` 停止。
- 注意只取粗略位置时别开高精度（费电、慢）；业务要容错——定位失败必须给降级体验。

```javascript
// 封装一个带超时与错误分类的定位工具
function getLocation(options = { enableHighAccuracy: true, timeout: 8000, maximumAge: 60000 }) {
  return new Promise((resolve, reject) => {
    if (!('geolocation' in navigator)) {
      return reject(new Error('browser not supported'));
    }
    navigator.geolocation.getCurrentPosition(
      (pos) => resolve({
        lat: pos.coords.latitude,
        lng: pos.coords.longitude,
        accuracy: pos.coords.accuracy, // 精度半径（米）
      }),
      (err) => {
        switch (err.code) {
          case err.PERMISSION_DENIED: reject(new Error('用户拒绝了定位授权')); break;
          case err.POSITION_UNAVAILABLE: reject(new Error('位置信息不可用')); break;
          case err.TIMEOUT: reject(new Error('定位超时')); break;
          default: reject(err);
        }
      },
      options
    );
  });
}

// 使用：失败时降级为手动选择城市
getLocation()
  .then(({ lat, lng }) => renderNearbyStores(lat, lng))
  .catch((e) => {
    console.warn(e.message);
    showCityPicker(); // 降级方案
  });

// 持续追踪（骑行轨迹类需求）
const watchId = navigator.geolocation.watchPosition((pos) => track.push(pos.coords));
// navigator.geolocation.clearWatch(watchId); // 停止
```
