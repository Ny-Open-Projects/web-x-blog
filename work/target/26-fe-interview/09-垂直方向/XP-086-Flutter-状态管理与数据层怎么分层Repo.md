---
title: [XP-086] Flutter 状态管理与数据层怎么分层？Repository 模式如何落地？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-086：Flutter 状态管理与数据层怎么分层？Repository 模式如何落地？
**答**：
- 分层：**UI（Widget）→ 状态层（Riverpod/Bloc）→ Repository（数据门面）→ DataSource（remote/local）**，UI 不直连网络与 DB，状态层只编排不实现。
- 选型经验：Riverpod（编译期安全、易测试）适合中大型；Bloc（强约束事件流）适合复杂交互与团队强规范；Provider 只做依赖注入基础件。
- Repository 职责：聚合 remote/local 双源、DTO→Domain 映射、缓存与过期策略、分页游标管理；对外暴露 `Stream`/`Future`，屏蔽来源细节。
- 数据一致性：写操作走 Repository 单入口（本地乐观更新 + 服务端对账），多页面订阅同一 provider 自动同步；错误统一转 Domain 层异常类型。
- 测试：Repository 依赖注入 mock DataSource 单测；状态层用 fake Repository 测试编排；UI golden test 只验展示（与 XP-106 视觉回归衔接）。

```dart
// data/repository/article_repository.dart —— 数据门面：双源聚合 + 缓存 + 映射
class ArticleRepository {
  ArticleRepository(this._remote, this._local);
  final ArticleApi _remote;          // remote datasource：retrofit/dio
  final ArticleDao _local;           // local datasource：drift/sqlite

  Future<List<Article>> fetchFeed({String? cursor}) async {
    final cached = await _local.queryFeed(cursor: cursor);
    if (_isFresh(cached)) return cached.map(_toDomain).toList();   // 本地新鲜直接用
    try {
      final dto = await _remote.feed(cursor: cursor);
      await _local.upsertFeed(dto);                                 // 回写缓存
      return dto.items.map(_toDomain).toList();
    } on SocketException {
      if (cached.isNotEmpty) return cached.map(_toDomain).toList(); // 弱网降级缓存
      rethrow;
    }
  }
}

// 状态层 Riverpod：只编排，不碰实现细节
final articleRepoProvider = Provider((ref) =>
    ArticleRepository(ref.watch(articleApiProvider), ref.watch(articleDaoProvider)));

final feedProvider = AsyncNotifierProvider<FeedNotifier, List<Article>>(FeedNotifier.new);

class FeedNotifier extends AsyncNotifier<List<Article>> {
  @override
  Future<List<Article>> build() =>
      ref.watch(articleRepoProvider).fetchFeed();     // UI 只 watch 此 provider
}
```
