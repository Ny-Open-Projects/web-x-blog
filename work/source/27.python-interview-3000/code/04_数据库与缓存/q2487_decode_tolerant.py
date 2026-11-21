"""缓存值解码容错: 旧格式 损坏值都要有出路"""
import json

STORE = {
    "u:1": json.dumps({"v": 2, "name": "新版", "settings": {"lang": "zh"}}),
    "u:2": json.dumps({"name": "没有版本字段的远古值"}),
    "u:3": json.dumps({"v": 1, "name": "旧版值"}),
    "u:4": "{oops 损坏的半截 JSON",
}
rebuilds = []

def migrate_v1_to_v2(d):                              # 迁移函数链: v1 -> v2
    d = dict(d)
    d["settings"] = d.get("settings") or {"lang": "zh"}
    d["v"] = 2
    return d

def decode(key, raw):                                 # 解码容错三部曲
    try:
        d = json.loads(raw)
    except (ValueError, TypeError):
        return None                                   # 信号: 上层当作未命中重建
    version = d.get("v", 1)                           # 没写版本字段的按最老格式处理
    if version < 2:
        d = migrate_v1_to_v2(d)
    return d

def get(key, loader):
    raw = STORE.get(key)
    if raw is not None:
        d = decode(key, raw)
        if d is not None:
            return d, "命中"
        STORE.pop(key, None)                          # 坏值: 当即删除, 别让毒值常驻
        rebuilds.append(key)
    return loader(key), "回源重建"

def loader(key):
    return {"v": 2, "name": "重建值 %s" % key, "settings": {"lang": "zh"}}

for k in sorted(STORE):
    d, how = get(k, loader)
    print("%s -> %-6s name=%-12s settings=%s" % (k, how, d["name"], d["settings"]))
print("本次回源重建的键: %s" % rebuilds)
print("结论: value 里自带版本字段加迁移函数链, 旧值滚动升级; 解码失败一律当未命中删键重建,")
print("      宁可多一次回源也别让一条坏值把读路径打成 500")
