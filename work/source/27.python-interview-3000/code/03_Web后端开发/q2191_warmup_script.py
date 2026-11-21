"""冷启动预热脚本: 连接、缓存与路由三类预热加就绪门禁(纯标准库)。"""
import time


class App:
    def __init__(self):
        self.db_ready = False
        self.cache = {}
        self.route_cache = set()
        self.cold_cost = {}

    def query_db(self, key):
        t0 = time.time()
        time.sleep(0.01)                            # 模拟建连加查询
        self.cold_cost.setdefault(key, round((time.time() - t0) * 1000, 1))
        return "data-" + key

    def warm(self, hot_keys, routes):
        """预热三件事: 连接池、热点缓存、代表性路由的完整处理路径。"""
        self.db_ready = True                        # 预建连接(以标志模拟)
        for key in hot_keys:
            self.cache[key] = self.query_db(key)
        for route in routes:
            self.route_cache.add(route)

    def ready(self, hot_keys, routes):
        return (self.db_ready
                and all(k in self.cache for k in hot_keys)
                and all(r in self.route_cache for r in routes))


hot, routes = ["hot1", "hot2"], ["GET /orders", "GET /goods"]
app = App()
t0 = time.time()
app.warm(hot, routes)
print("预热耗时: {}ms, 就绪判定: {}".format(round((time.time() - t0) * 1000, 1),
                                            app.ready(hot, routes)))
cold = App()
print("未预热实例就绪判定:", cold.ready(hot, routes), "-> 不该接流量")
assert app.ready(hot, routes) and not cold.ready(hot, routes)
print("要点: 预热交的是首请求的税——建连、热点数据、完整处理路径; readiness 以预热完成为门禁")
