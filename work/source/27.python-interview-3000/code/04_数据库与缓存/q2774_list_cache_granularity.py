"""列表页缓存的粒度: 整页缓存省读费写, id 集合省写费读"""
PAGE, CATS, PAGES_PER_CAT = 20, 10, 50

page_keys = CATS * PAGES_PER_CAT
print("整页缓存: %d 个页键; 一次商品改价保守失效该分类全部 %d 个页"
      % (page_keys, PAGES_PER_CAT))
print("id 集合: 一次改价只失效 1 个对象键; 但每次读列表要取 %d 个键 (1 集合 + %d 对象)"
      % (1 + PAGE, PAGE))

print("折中: 整页缓存 + 短 TTL")
for ttl, inv in [(5, PAGES_PER_CAT), (60, 0)]:
    stale = 0 if inv else ttl
    print("  TTL %2ds: 同步失效动作 %d 个, 最坏陈旧窗口 %ds" % (ttl, inv, stale))
print("选型口诀: 变更频繁选对象粒度, 列表稳定选整页, 中间态用短 TTL 页缓存")
