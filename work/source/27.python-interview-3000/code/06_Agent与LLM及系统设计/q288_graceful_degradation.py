import time


class RecommendationService:
    def fetch(self, uid: str) -> list[str]:
        raise ConnectionError("service down")


class CachedRecommendation:
    """读旧缓存兜底,缓存里保存最近一次成功结果。"""
    def __init__(self, svc: RecommendationService):
        self.svc = svc
        self.cache: dict[str, tuple[float, list]] = {}

    def get(self, uid: str) -> list[str]:
        try:
            data = self.svc.fetch(uid)
            self.cache[uid] = (time.time(), data)
            return data
        except ConnectionError:
            cached = self.cache.get(uid)
            if cached:
                print("[degrade] serve stale cache")
                return cached[1]
            return []  # 默认空推荐,页面隐藏模块


if __name__ == "__main__":
    svc = CachedRecommendation(RecommendationService())
    svc.cache["u1"] = (time.time(), ["item1", "item2"])
    print(svc.get("u1"))
    print(svc.get("u2"))  # 无缓存,返回默认
