"""检查点增量存储与完整性校验:只存相对前一点的 delta,哈希链串联,篡改可检出。"""
import copy
import hashlib
import json


def digest(obj):
    raw = json.dumps(obj, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


class CheckpointStore:
    def __init__(self):
        self.chain = []
        self.last_state = {}

    def save(self, label, full_state):
        prev = self.chain[-1]["hash"] if self.chain else "genesis"
        delta = {}
        for k, v in full_state.items():
            if not self.chain or self.last_state.get(k) != v:
                delta[k] = copy.deepcopy(v)
        for k in set(self.last_state) - set(full_state):
            delta[k] = None                      # 删除键记墓碑
        entry = {"label": label, "delta": delta, "prev": prev,
                 "hash": digest({"prev": prev, "delta": delta, "label": label})}
        self.chain.append(entry)
        self.last_state = copy.deepcopy(full_state)
        return entry["hash"]

    def verify(self):
        prev = "genesis"
        for e in self.chain:
            expect = digest({"prev": prev, "delta": e["delta"], "label": e["label"]})
            if expect != e["hash"]:
                raise ValueError("哈希链断裂于 %s,检查点被篡改" % e["label"])
            prev = e["hash"]

    def restore(self, target_label=None):
        self.verify()
        state = {}
        for e in self.chain:
            for k, v in e["delta"].items():
                if v is None:
                    state.pop(k, None)
                else:
                    state[k] = copy.deepcopy(v)
            if target_label and e["label"] == target_label:
                break
        return state


if __name__ == "__main__":
    store = CheckpointStore()
    h1 = store.save("ck1", {"a": 1, "b": 2})
    h2 = store.save("ck2", {"a": 1, "b": 3, "c": 4})
    assert h1 != h2
    assert len(store.chain[1]["delta"]) == 2, "第二检查点只应存 b 和 c 的增量"
    assert store.restore() == {"a": 1, "b": 3, "c": 4}
    assert store.restore("ck1") == {"a": 1, "b": 2}, "可恢复到任意历史点"

    h3 = store.save("ck3", {"a": 9, "b": 3})
    assert store.chain[2]["delta"] == {"a": 9, "c": None}, "改值与删除墓碑都进增量"
    assert store.restore() == {"a": 9, "b": 3}, "墓碑恢复时删除该键"
    assert h3

    # 篡改演练:改历史 delta,校验必须报错
    store.chain[0]["delta"]["a"] = 999
    try:
        store.restore()
        raise AssertionError("篡改必须被哈希链发现")
    except ValueError as e:
        assert "篡改" in str(e)
    print("检查点链通过:增量存储省体积,任意点可恢复,篡改被哈希链拦截")
