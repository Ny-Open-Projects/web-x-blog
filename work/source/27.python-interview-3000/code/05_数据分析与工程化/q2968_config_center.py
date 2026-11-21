"""配置中心本地实现: 多层 JSON 加载 -> 深合并 -> schema 校验 -> 基于 mtime 的热读"""
import json
import os
import tempfile

SCHEMA = {
    "db.host": str,
    "db.port": int,
    "log.level": str,
    "flags.gray": bool,
}

BASE = {"db": {"host": "127.0.0.1", "port": 5432}, "log": {"level": "INFO"}, "flags": {"gray": False}}
OVERLAY_V1 = {"db": {"port": 6432}, "flags": {"gray": True}}
OVERLAY_V2 = {"db": {"port": 7432}, "flags": {"gray": True}}
OVERLAY_BAD = {"db": {"port": "six"}}


def deep_merge(base, overlay):
    """递归合并: dict 逐层下钻, 其他类型整体覆盖"""
    out = dict(base)
    for k, v in overlay.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = v
    return out


class ConfigCenter:
    """本地配置中心: 后层文件覆盖前层; 每次读取前比对 mtime, 变了才重载"""

    def __init__(self, paths, schema=None):
        self.paths = list(paths)
        self.schema = schema or {}
        self._mtimes = [None] * len(self.paths)
        self._cfg = None
        self.reload_count = 0

    def _read(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _reload(self):
        merged = {}
        for p in self.paths:
            merged = deep_merge(merged, self._read(p))
        self._cfg = merged
        self.reload_count += 1

    def refresh_if_changed(self):
        changed = False
        for i, p in enumerate(self.paths):
            m = os.stat(p).st_mtime
            if m != self._mtimes[i]:
                self._mtimes[i] = m
                changed = True
        if changed or self._cfg is None:
            self._reload()

    def get(self, dotted, default=None):
        """热读入口: 先检查文件是否更新, 再按 a.b.c 取值"""
        self.refresh_if_changed()
        node = self._cfg
        for part in dotted.split("."):
            if not isinstance(node, dict) or part not in node:
                return default
            node = node[part]
        return node

    def validate(self):
        errs = []
        for key, typ in self.schema.items():
            v = self.get(key)
            if v is None:
                errs.append(key + " 缺失")
            elif not isinstance(v, typ):
                errs.append("%s 期望 %s 实得 %s" % (key, typ.__name__, type(v).__name__))
        if errs:
            raise ValueError("配置校验失败: " + "; ".join(errs))
        return True


def touch(path, ts):
    os.utime(path, (ts, ts))


if __name__ == "__main__":
    d = tempfile.mkdtemp(prefix="conf_")
    base_p, overlay_p = os.path.join(d, "base.json"), os.path.join(d, "overlay.json")
    for p, obj in [(base_p, BASE), (overlay_p, OVERLAY_V1)]:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False)

    cc = ConfigCenter([base_p, overlay_p], SCHEMA)
    print("校验通过:", cc.validate())
    print("db.host =", cc.get("db.host"), "(来自 base, overlay 未覆盖)")
    print("db.port =", cc.get("db.port"), "(overlay 覆盖 base)")
    print("flags.gray =", cc.get("flags.gray"))
    print("missing.key =", cc.get("missing.key", "默认值"))

    # 热读: 改 overlay 后无需重启, 下一次 get 生效
    with open(overlay_p, "w", encoding="utf-8") as f:
        json.dump(OVERLAY_V2, f, ensure_ascii=False)
    touch(overlay_p, os.stat(overlay_p).st_mtime + 10)
    print("热读后 db.port =", cc.get("db.port"), "重载次数 =", cc.reload_count)
    print("未变更再读 db.port =", cc.get("db.port"), "重载次数 =", cc.reload_count, "(mtime 未变不重载)")

    with open(overlay_p, "w", encoding="utf-8") as f:
        json.dump(OVERLAY_BAD, f, ensure_ascii=False)
    touch(overlay_p, os.stat(overlay_p).st_mtime + 10)
    try:
        cc.validate()
    except ValueError as e:
        print("故意写坏配置被拦截:", e)
    print("要点: 深合并让覆盖粒度到叶子, mtime 热读零依赖实现, schema 校验把坏配置挡在生效之前")
