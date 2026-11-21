---
title: [XP-018] Widget 的不可变性与重建优化？const 和 Key 的正确用法？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-018：Widget 的不可变性与重建优化？const 和 Key 的正确用法？
**答**：
- Widget 是 `@immutable` 的：重建成本只是" new 一个小对象 + Element diff"，但重建太深太广仍会烧 CPU。
- **const 构造**：编译期常量 Widget 指向同一实例，build 时被 Element 直接跳过（identical 短路），是最便宜的优化。
- **Key**：无状态 diff 用默认即可；列表重排/有状态子项必须用 ValueKey/ObjectKey，否则 State 会错位复用；GlobalKey 用于跨树移动且保留 State（慎用，代价高）。
- 优化顺序：const → 缩小 rebuild 范围（拆 Consumer/Selector）→ RepaintBoundary → 慎用深比较 shouldRebuild。
- 反模式：在 build 里 new 大闭包/匿名 List 导致 const 失效；用 index 当 key。

```dart
class CartPage extends StatelessWidget {
  const CartPage({super.key, required this.items});
  final List<Item> items;

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      const HeaderBar(),                    // const：实例复用，Element diff 直接 identical 跳过
      Expanded(
        child: ListView.builder(
          itemCount: items.length,
          // 正确：以业务 id 作 key，删除/重排时 State 不错位
          // 错误示例：key: ValueKey(index) —— 删除中间项后复选框状态会错位
          itemBuilder: (_, i) => CartRow(
            key: ValueKey(items[i].id),
            item: items[i],
          ),
        ),
      ),
    ]);
  }
}
// 反例：CartRow(trailing: Checkbox(value: x)) 每次 build new Checkbox → 无 const、重建成本高
// 改法：Checkbox 加 const 或下沉到内部 StatefulWidget 管理，缩小 rebuild 范围
```
