---
title: [VIZ-144] WGS84 / GCJ02 / BD09 坐标系的区别与互转？（压轴）
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-144：WGS84 / GCJ02 / BD09 坐标系的区别与互转？（压轴）
**答**：① **WGS84**——GPS 原始坐标（国际标准）；② **GCJ02**——国测局加密偏移（"火星坐标"），高德/腾讯使用，境内地图合规要求；③ **BD09**——百度在 GCJ02 基础上的二次加密。混用整体偏移 50~500 米。转换是非线性算法（公开实现），顺序 WGS84 ↔ GCJ02 ↔ BD09。工程要点：数据源声明坐标系、入库统一 WGS84、展示前转目标地图坐标系；GCJ02 只对境内偏移（境外原样返回）；用 gcoord 库而非自己抄公式。

```javascript
// WGS84 <-> GCJ02（火星坐标）核心转换
const PI = Math.PI, A = 6378245.0, EE = 0.00669342162296594326;
const outOfChina = (lng, lat) =>
  lng < 72.004 || lng > 137.8347 || lat < 0.8293 || lat > 55.8271; // 境外不偏移
function transformLat(x, y) {
  let ret = -100 + 2*x + 3*y + 0.2*y*y + 0.1*x*y + 0.2*Math.sqrt(Math.abs(x));
  ret += (20*Math.sin(6*x*PI) + 20*Math.sin(2*x*PI)) * 2/3;
  ret += (20*Math.sin(y*PI) + 40*Math.sin(y/3*PI)) * 2/3;
  ret += (160*Math.sin(y/12*PI) + 320*Math.sin(y*PI/30)) * 2/3;
  return ret;
}
function transformLng(x, y) {
  let ret = 300 + x + 2*y + 0.1*x*x + 0.1*x*y + 0.1*Math.sqrt(Math.abs(x));
  ret += (20*Math.sin(6*x*PI) + 20*Math.sin(2*x*PI)) * 2/3;
  ret += (20*Math.sin(x*PI) + 40*Math.sin(x/3*PI)) * 2/3;
  ret += (150*Math.sin(x/12*PI) + 300*Math.sin(x/30*PI)) * 2/3;
  return ret;
}
function wgs84ToGcj02(lng, lat) {
  if (outOfChina(lng, lat)) return [lng, lat];
  const radLat = lat / 180 * PI;
  let magic = Math.sin(radLat); magic = 1 - EE * magic * magic;
  const sqrtMagic = Math.sqrt(magic);
  const dLat = (transformLat(lng - 105, lat - 35) * 180) /
    ((A * (1 - EE)) / (magic * sqrtMagic) * PI);
  const dLng = (transformLng(lng - 105, lat - 35) * 180) /
    (A / sqrtMagic * Math.cos(radLat) * PI);
  return [lng + dLng, lat + dLat];
}
```
