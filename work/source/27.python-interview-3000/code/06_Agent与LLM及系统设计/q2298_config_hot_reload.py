"""Agent 配置热更新:版本号单调递增 原子替换快照 在途请求绑定旧快照跑完。"""


class ConfigCenter:
    def __init__(self, initial):
        self._snap = {"ver": 1, "cfg": dict(initial)}

    def snapshot(self):
        return self._snap

    def update(self, patch, required=()):
        missing = [k for k in required if k not in patch and k not in self._snap["cfg"]]
        blank = [k for k, v in patch.items() if isinstance(v, str) and not v.strip()]
        if missing or blank:
            raise ValueError("非法配置 缺失=%s 空值=%s" % (missing, blank))
        new_cfg = dict(self._snap["cfg"])
        new_cfg.update(patch)
        self._snap = {"ver": self._snap["ver"] + 1, "cfg": new_cfg}
        return self._snap["ver"]


if __name__ == "__main__":
    cc = ConfigCenter({"model": "m1", "top_k": 5, "timeout_s": 30})
    snap1 = cc.snapshot()
    assert snap1["ver"] == 1
    v2 = cc.update({"top_k": 9})
    assert v2 == 2
    assert snap1["cfg"]["top_k"] == 5, "在途请求持有旧快照 不受热更影响"
    assert cc.snapshot()["cfg"]["top_k"] == 9, "新请求即刻看到新配置"
    try:
        cc.update({"model": "   "}, required=("model",))
        raise SystemExit("空值配置应被拒")
    except ValueError:
        pass
    v3 = cc.update({"top_k": 5})
    assert v3 == 3 and cc.snapshot()["cfg"]["top_k"] == 5, "回滚也是一次前滚更新 版本只增不减"
    try:
        cc.update({"missing_key": 1}, required=("model", "temperature"))
        raise SystemExit("缺失必填应被拒")
    except ValueError as e:
        assert "temperature" in str(e)
    print("配置热更新通过:版本快照 原子替换 在途隔离 校验拒非法")
