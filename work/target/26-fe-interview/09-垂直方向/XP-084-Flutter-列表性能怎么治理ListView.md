---
title: [XP-084] Flutter 列表性能怎么治理？ListView.builder 与 Sliver 体系？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-084：Flutter 列表性能怎么治理？ListView.builder 与 Sliver 体系？
**答**：
- 基础纪律：列表用 `ListView.builder`（懒构建）而**绝不用 `children:` 全量构造**；能定高给 `itemExtent`（跳过子项测量，滚动计算 O(1)）；`shrinkWrap: true` 会失去懒加载，谨慎使用。
- Sliver 体系：复杂页面用 `CustomScrollView` + `SliverAppBar/SliverList/SliverGrid` 组合，头部吸顶、多类型混合布局一次滚动编排；`SliverPersistentHeader` 做下沉收缩效果。
- 构建卡顿定位：DevTools Timeline 看 **build / layout / raster** 三段；build 超帧多半是 item 内重计算（下放 isolate 或缓存），raster 超帧多为阴影/模糊/大图（用 `RepaintBoundary` 隔离重绘区域）。
- 配套参数：`cacheExtent` 控制屏外预构建距离（低端机调小省内存）、`addAutomaticKeepAlives/addRepaintBoundaries` 按需关闭减开销、`findChildIndexCallback` 保持 item 状态防抖动。
- 图片与占位：item 内图片强制定宽高 + `cacheWidth` 解码降采样，防止 decode 抖 raster 线程；预加载配合 `ScrollController` 位置监听（与 XP-076 的治理指标口径统一）。

```dart
// 复杂首页：Sliver 体系编排 + 定高懒列表
CustomScrollView(
  controller: _controller,
  cacheExtent: 300,                          // 屏外预构建距离，低端机可再调小
  slivers: [
    SliverAppBar(expandedHeight: 200, pinned: true, flexibleSpace: FlexibleSpaceBar(
      title: Text('发现'),                   // 吸顶收缩头部
    )),
    SliverToBoxAdapter(child: BannerCarousel()),          // 轮播：一次性构建合理
    SliverPadding(
      padding: EdgeInsets.symmetric(horizontal: 12),
      sliver: SliverList.builder(            // Sliver 懒构建列表
        itemCount: items.length,
        // 定高：跳过 item 测量，滚动与定位计算 O(1)，治白屏关键
        itemExtent: 88,
        // 列表数据重排时按 key 找回旧 child，保持状态防跳动
        findChildIndexCallback: (key) =>
            items.indexWhere((e) => e.id == key.toString()),
        itemBuilder: (_, i) => RepaintBoundary(          // 隔离 item 重绘
          child: FeedCard(item: items[i]),               // 内部图片定宽高+cacheWidth
        ),
      ),
    ),
    // 瀑布流场景换 SliverGrid / flutter_staggered_grid_view，slivers 间共享滚动
  ],
);
// 定位口诀：build 慢→缓存与 isolate，layout 慢→布局简化，raster 慢→RepaintBoundary 与降阴影
```
