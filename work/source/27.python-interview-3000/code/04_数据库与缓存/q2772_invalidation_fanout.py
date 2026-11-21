"""失效扇出核算: 一次商品写波及多少派生键, 三种策略各摊多少"""
CATS, PAGES_PER_CAT, SEARCH_HITS = 1, 50, 200

def naive_fanout():
    """全部逐键删除: 详情 1 + 该商品所在分类全部列表页 + 命中它的搜索页 + 推荐位"""
    return 1 + PAGES_PER_CAT + SEARCH_HITS + 1

def strategy_fanout():
    """详情逐键删 1, 列表翻版本号 1, 搜索靠 TTL 0, 推荐 TTL 0"""
    return 2

print("商品改价一次, 派生键: 列表页 %d + 搜索页 %d + 详情与推荐 %d"
      % (PAGES_PER_CAT, SEARCH_HITS, 2))
print("全部逐键删除: %d 个失效动作 (写路径的隐性放大系数)" % naive_fanout())
print("按类型分派策略后: %d 个同步动作, 其余交给版本号与 TTL 异步收敛" % strategy_fanout())
assert strategy_fanout() < naive_fanout()
print("设计评审必答题: 一次写的失效扇出是多少? 答不出来等于没设计")
