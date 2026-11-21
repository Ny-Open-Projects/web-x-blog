"""缓存键序列化: 参数规范化与撞键防范"""
import hashlib
import json

def canonical_key(namespace, version, params):
    """把任意参数结构规范化成稳定可复现的缓存键"""
    def norm(v):
        if isinstance(v, bool):          # bool 必须先于 int 判断 否则 True 被当成 1
            return ("b", v)
        if isinstance(v, (int, float)):
            return ("n", repr(v))        # repr 区分 1 与 1.0 防跨类型撞键
        if isinstance(v, (list, tuple)):
            return ("l", [norm(x) for x in v])
        if isinstance(v, dict):
            return ("d", sorted((k, norm(x)) for k, x in v.items()))
        return ("s", str(v))
    payload = json.dumps(norm(params), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]
    return f"{namespace}:v{version}:{digest}", payload

k1, p1 = canonical_key("search", 3, {"q": "python", "page": 1, "filters": {"tag": "db", "sort": "hot"}})
k2, _ = canonical_key("search", 3, {"sort": "hot", "page": 1, "q": "python", "filters": {"sort": "hot", "tag": "db"}})
k3, _ = canonical_key("search", 3, {"q": "python", "page": 1})
k4, _ = canonical_key("search", 3, {"q": "Python ", "page": 1, "filters": {"tag": "db", "sort": "hot"}})
print("键序不同的同参数 -> 相同键:", k1 == k2, " 键:", k1)
print("少一个参数       -> 相同键:", k1 == k3, " 键:", k3)
print("大小写与空格差异 -> 相同键:", k1 == k4, " 内容差异要保留 不能擅自清洗")
print("规范化载荷:", p1)

# 反例: 直接 str(dict) 做键 插入顺序影响结果 同参数生成两个缓存条目
bad1 = str({"q": "py", "page": 1})
bad2 = str({"page": 1, "q": "py"})
print("str(dict) 反例   -> 相同键:", bad1 == bad2, " 同一份参数裂成两个条目 命中率被稀释")

# 布尔与整数的坑: True 与 1 在 str 里同形 语义却不同
print("str 混淆示例     ->", str({"debug": True}) == str({"debug": 1}), " 规范化里用类型标记区分")
print("结论: 键序列化必须做到同参数必同键 异参数必异键 结构排序加哈希 类型要带标记 版本前缀负责整域失效")
