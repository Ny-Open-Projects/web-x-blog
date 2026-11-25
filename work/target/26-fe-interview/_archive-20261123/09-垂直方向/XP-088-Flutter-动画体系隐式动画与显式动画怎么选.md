---
title: [XP-088] Flutter 动画体系？隐式动画与显式动画怎么选？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-088：Flutter 动画体系？隐式动画与显式动画怎么选？
**答**：
- 隐式动画（`AnimatedContainer` 等 ImplicitlyAnimatedWidget）：给目标值自动补间，适合状态切换类简单效果，代码量小、不可控过程。
- 显式动画（`AnimationController` + `Tween`/`Curve`）：完全掌控时长、曲线、循环、交错（Interval 编排），适合开场动画、序列编排、手势驱动；必须手动 `dispose` 防泄漏。
- 进阶件：`Hero` 转场共享元素、`TweenAnimationBuilder`（声明式显式）、`AnimatedSwitcher`（子树切换过渡）、`flutter_animate`/Rive/Lottie 承载复杂资产。
- 性能纪律：只动 `Transform`/`Opacity` 类合成属性可走 raster 之外的最优路径；动画区域包 `RepaintBoundary` 限制重绘范围；页面不可见时 controller 停止（配合 XP-091 生命周期）。
- 与平台一致性：同参数的弹簧/缓动在 iOS/Android 表现一致（自绘），但高频跟手动画注意 isolate 与 raster 负载，低端机降级策略同 XP-110。

```dart
// 显式动画：序列编排 + 手势联动；隐式动画：状态切换
class StaggerCard extends StatefulWidget { /* ... */ }
class _StaggerCardState extends State<StaggerCard>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
  // 交错编排：同一 controller 上用 Interval 切分时间轴
  late final Animation<double> _slide = CurvedAnimation(
      parent: _c, curve: const Interval(0, 0.6, curve: Curves.easeOutCubic));
  late final Animation<double> _fade = CurvedAnimation(
      parent: _c, curve: const Interval(0.4, 1, curve: Curves.easeOut));

  @override
  void initState() { super.initState(); _c.forward(); }   // 入场
  @override
  void dispose() { _c.dispose(); super.dispose(); }        // 必须 dispose，防泄漏

  @override
  Widget build(BuildContext context) => GestureDetector(
    onTapDown: (_) => _c.reverse(),                        // 手势驱动显式动画
    onTapUp: (_) => _c.forward(),
    child: RepaintBoundary(                                 // 限制重绘范围
      child: FadeTransition(
        opacity: _fade,
        child: SlideTransition(
          position: Tween(begin: const Offset(0, 0.2), end: Offset.zero).animate(_slide),
          child: const CardBody(),
        ),
      ),
    ),
  );
}
// 简单状态切换用隐式：AnimatedContainer(duration: 200ms, color/size 变化自动补间)
```
