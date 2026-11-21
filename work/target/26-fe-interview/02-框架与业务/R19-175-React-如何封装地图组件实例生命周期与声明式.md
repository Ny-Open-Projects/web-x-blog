---
title: [R19-175] React 如何封装地图组件？实例生命周期与声明式标记怎么设计？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-175：React 如何封装地图组件？实例生命周期与声明式标记怎么设计？
**答**：
- 地图与 Canvas 模板一致，多出两类子资源：**覆盖物（marker/polygon）**与**视口（center/zoom）**，各自需要同步策略。
- 标记做成声明式 `<MapMarker>` 子组件：内部 useEffect 按"创建 -> 更新 -> 移除"管理 marker 实例，父级只通过 context 提供 map 实例。
- 视口同步防回环：用户拖动地图 -> onCenterChange 上抛给受控 state -> 若直接回写 center 会打断拖拽；需要"拖动中不回写，结束后同步"的分寸。
- 加载即异步：SDK 按需注入 script，ready 后才渲染 children（用 state 驱动），避免拿到 undefined 的 AMap/BMap。

```tsx
// map.tsx —— 地图 SDK 的 React 封装（以高德为例的思想）
import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from 'react';

const MapCtx = createContext<any>(null);

// 1. 异步加载 SDK
function loadSdk(key: string): Promise<void> {
  return new Promise(resolve => {
    if ((window as any).AMap) return resolve();
    const s = document.createElement('script');
    s.src = `https://webapi.amap.com/maps?v=2.0&key=${key}`;
    s.onload = resolve;
    document.head.appendChild(s);
  });
}

export function MapContainer({ apiKey, center, zoom, children }: {
  apiKey: string; center: [number, number]; zoom: number; children?: ReactNode;
}) {
  const elRef = useRef<HTMLDivElement>(null);
  const [map, setMap] = useState<any>(null);
  const centerRef = useRef(center);
  centerRef.current = center;

  useEffect(() => {
    let destroyed = false;
    loadSdk(apiKey).then(() => {
      if (destroyed) return;
      const m = new (window as any).AMap.Map(elRef.current, {
        center: centerRef.current, zoom,
      });
      m.on('moveend', () => {
        // 地图结束拖动后，把新视口交给受控方（避免拖拽中回写打断用户）
        const c = m.getCenter();
        window.dispatchEvent(new CustomEvent('map:moveend', { detail: [c.lng, c.lat] }));
      });
      setMap(m);
    });
    return () => { destroyed = true; map?.destroy?.(); };
    // SDK 实例只在挂载时创建一次，center/zoom 变化走增量同步
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [apiKey]);

  // 视口增量同步：受控 center 变化 -> map.setCenter（跳过初始化那一次）
  const initialized = useRef(false);
  useEffect(() => {
    if (!map) return;
    if (!initialized.current) { initialized.current = true; return; }
    map.setCenter(center);
  }, [center, map]);

  return (
    <div ref={elRef} style={{ width: '100%', height: 400 }}>
      {map && <MapCtx.Provider value={map}>{children}</MapCtx.Provider>}
    </div>
  );
}

// 2. 声明式标记：每个 marker 一个组件，实例随组件生灭
export function MapMarker({ position, label, onClick }: {
  position: [number, number]; label: string; onClick?: () => void;
}) {
  const map = useContext(MapCtx);
  const markerRef = useRef<any>(null);
  const onClickRef = useRef(onClick);
  onClickRef.current = onClick;

  useEffect(() => {
    const AMap = (window as any).AMap;
    markerRef.current = new AMap.Marker({
      position,
      map,
      content: `<div class="map-pin">${label}</div>`,
    });
    markerRef.current.on('click', () => onClickRef.current?.());
    return () => { markerRef.current?.setMap(null); }; // 卸载即摘除标记
    // position 变化不重建 marker，走增量
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [map]);

  useEffect(() => {
    markerRef.current?.setPosition(position);
  }, [position]);

  return null;
}

// 使用：
// <MapContainer apiKey="..." center={[116.4, 39.9]} zoom={12}>
//   {stores.map(s => <MapMarker key={s.id} position={s.lnglat} label={s.name} onClick={() => open(s)} />)}
// </MapContainer>
```
