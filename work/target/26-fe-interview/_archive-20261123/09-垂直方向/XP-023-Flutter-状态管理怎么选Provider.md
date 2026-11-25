---
title: [XP-023] Flutter 状态管理怎么选？Provider/Bloc/Riverpod 的差异？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-023：Flutter 状态管理怎么选？Provider/Bloc/Riverpod 的差异？
**答**：
- **Provider**：InheritedWidget 的封装，简单直接，适合中小项目；缺点是依赖 BuildContext、组合复杂状态吃力。
- **Bloc**：事件驱动的单向数据流（Event→Bloc→State），强约束可测试，适合大型强流程业务；样板代码多。
- **Riverpod**：Provider 的进化版——编译期安全、不依赖 BuildContext、Provider 组合与缓存（autoDispose/family）能力强，社区当前主流推荐。
- 选型经验：团队结构简单选 Riverpod；有严格流程/审计诉求（金融、工单流）选 Bloc；勿混用多套。
- 无论哪套，核心心法相同：**UI = f(state)，状态放哪、范围多大，比选哪个库更重要**。

```dart
// Riverpod 2.x：组合、缓存与异步状态
final cartRepoProvider = Provider((ref) => CartRepo(dio));
final cartProvider = NotifierProvider<CartNotifier, CartState>(CartNotifier.new);
final totalPriceProvider = Provider<int>((ref) =>           // 派生状态：自动依赖追踪
    ref.watch(cartProvider).items.fold(0, (s, i) => s + i.priceFen * i.count));

class CartNotifier extends Notifier<CartState> {
  @override
  CartState build() => const CartState.loading();
  Future<void> load() async {
    state = const CartState.loading();
    state = CartState.data(await ref.read(cartRepoProvider).fetch());
  }
  void add(Item i) => state = state.copyWith(items: [...state.items ?? [], i]);
}

class CartPage extends ConsumerWidget {                     // 只重建依赖变化的子树
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final price = ref.watch(totalPriceProvider);            // 细粒度订阅
    return Text('合计 ${(price / 100).toStringAsFixed(2)} 元');
  }
}
// Bloc 同场景：CartBloc.add(CartItemAdded(i)) → emit(CartState(...))，事件可审计可回放
```
