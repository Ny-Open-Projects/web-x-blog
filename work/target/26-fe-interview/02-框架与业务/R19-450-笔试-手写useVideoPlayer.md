---
title: [R19-450] 笔试：手写 useVideoPlayer（播放器状态机 hook）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 多媒体]
type: 笔试题
---

## R19-450：笔试：手写 useVideoPlayer

**答**：实现 `useVideoPlayer(videoRef, { src, autoPlay })`：① 状态机：idle/loading/ready/playing/paused/buffering/error；② 事件绑定全套（canplay/playing/waiting/pause/ended/error/timeupdate）——video 事件同步到 React state；③ 控制面 API：play/pause/seek(rate)/setVolume/mute；④ 首帧耗时统计（play 请求到 playing 的时长）；⑤ 错误恢复（stalled 5s 重载保进度 + error 3 次降级源）。写出实现。

```javascript
export function useVideoPlayer(videoRef, { src, fallbackSrc, autoPlay = false } = {}) {
  const [state, setState] = useState('idle');
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState(null);
  const errCount = useRef(0);
  const playStart = useRef(null);

  useEffect(() => {
    const v = videoRef.current;
    if (!v) return;
    if (autoPlay) { playStart.current = performance.now(); v.play().catch(() => {}); }
    const on = (ev, fn) => { v.addEventListener(ev, fn); return () => v.removeEventListener(ev, fn); };
    const cleanups = [
      on('canplay', () => setState('ready')),
      on('playing', () => {
        setState('playing');
        if (playStart.current) {                       // 首起播耗时
          beacon({ fpt: performance.now() - playStart.current });
          playStart.current = null;
        }
      }),
      on('waiting', () => {
        setState('buffering');
        const t = setTimeout(() => { const ct = v.currentTime; v.load(); v.currentTime = ct; v.play().catch(() => {}); }, 5000);
        v.addEventListener('playing', () => clearTimeout(t), { once: true });
      }),
      on('pause', () => setState('paused')),
      on('ended', () => setState('ended')),
      on('timeupdate', () => setProgress(v.currentTime / (v.duration || 1))),
      on('error', () => {
        if (++errCount.current >= 3 && fallbackSrc) { const ct = v.currentTime; v.src = fallbackSrc; v.currentTime = ct; v.play().catch(() => {}); }
        else setState('error'), setError(v.error?.message);
      }),
    ];
    return () => cleanups.forEach((c) => c());
  }, [src, fallbackSrc, autoPlay]);

  const api = useMemo(() => ({
    play: () => { playStart.current ??= performance.now(); return videoRef.current?.play(); },
    pause: () => videoRef.current?.pause(),
    seek: (ratio) => { const v = videoRef.current; if (v?.duration) v.currentTime = ratio * v.duration; },
    setVolume: (n) => { const v = videoRef.current; if (v) { v.volume = n; v.muted = n === 0; } },
  }), []);
  return { state, progress, error, ...api };
}
```

**评分点**：
- 事件到 React state 的完整同步（六类事件）
- 首帧耗时统计（play 请求 → playing）
- stalled 5s 重载保进度 + error 3 次降级源
- 控制面 API 稳定引用（useMemo 空 deps）
