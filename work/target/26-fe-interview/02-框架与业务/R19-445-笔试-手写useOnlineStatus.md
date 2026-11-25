---
title: [R19-445] 笔试：手写 useOnlineStatus 与 useNetworkQuality
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## R19-445：笔试：手写 useNetworkQuality

**答**：实现：① `useOnlineStatus()`：online/offline 事件 + navigator.onLine 初值；② `useNetworkQuality()`：Network Information API（effectiveType/rtt/saveData）→ 映射档位 good/normal/poor/offline；③ 联合状态机：offline 优先；④ 网络恢复事件（offline→online）回调 onReconnect；⑤ SSR 安全与 change 监听清理。写出实现。

```javascript
export function useOnlineStatus() {
  const [online, setOnline] = useState(() =>
    typeof navigator !== 'undefined' ? navigator.onLine : true);
  useEffect(() => {
    const on = () => setOnline(true), off = () => setOnline(false);
    window.addEventListener('online', on);
    window.addEventListener('offline', off);
    return () => { window.removeEventListener('online', on); window.removeEventListener('offline', off); };
  }, []);
  return online;
}

export function useNetworkQuality({ onReconnect } = {}) {
  const online = useOnlineStatus();
  const conn = typeof navigator !== 'undefined' ? navigator.connection : null;
  const [info, setInfo] = useState(() => ({
    effectiveType: conn?.effectiveType ?? '4g',
    rtt: conn?.rtt ?? 0,
    saveData: conn?.saveData ?? false,
  }));
  useEffect(() => {
    if (!conn) return;
    const fn = () => setInfo({
      effectiveType: conn.effectiveType, rtt: conn.rtt, saveData: conn.saveData,
    });
    conn.addEventListener('change', fn);
    return () => conn.removeEventListener('change', fn);
  }, []);

  const wasOffline = useRef(false);
  useEffect(() => {
    if (!online) wasOffline.current = true;
    else if (wasOffline.current) { wasOffline.current = false; onReconnect?.(); }  // 恢复回调
  }, [online]);

  const level = !online ? 'offline'
    : info.saveData || info.effectiveType === '2g' || info.rtt > 800 ? 'poor'
    : info.effectiveType === '3g' || info.rtt > 400 ? 'normal' : 'good';
  return { online, level, ...info };
}
// 用法: 弱网降级
const { level, online } = useNetworkQuality({ onReconnect: () => syncQueue.replay() });
const showImages = level === 'good' || level === 'normal';
```

**评分点**：
- online 初值 SSR 安全 + 事件监听清理
- 档位映射三输入（effectiveType/rtt/saveData）
- offline→online 的恢复回调（驱动离线队列重放）
- saveData 优先级（poor 强制）
