"""Prompt 仓库不可变:版本按内容哈希寻址,发布后禁改,引用记录可追溯到请求级。"""
import hashlib, json


def cid_of(text, meta):
    return hashlib.sha256(json.dumps({"t": text, "m": meta}, sort_keys=True,
                                     ensure_ascii=False).encode("utf-8")).hexdigest()[:12]


class PromptRepo:
    def __init__(self):
        self.objects = {}
        self.refs = {}

    def publish(self, text, meta, alias):
        cid = cid_of(text, meta)
        self.objects[cid] = {"text": text, "meta": dict(meta)}
        self.refs[alias] = cid
        return cid

    def resolve(self, alias):
        if alias not in self.refs:
            raise KeyError("未注册别名 %s" % alias)
        cid = self.refs[alias]
        return cid, self.objects[cid]

    def audit_ref(self, alias, request_id):
        cid, _ = self.resolve(alias)
        return {"request": request_id, "alias": alias, "cid": cid}

    def mutate(self, cid, new_text):
        old = self.objects[cid]
        new_cid = cid_of(new_text, old["meta"])
        if new_cid != cid:
            self.objects[new_cid] = {"text": new_text, "meta": old["meta"]}
        return new_cid


if __name__ == "__main__":
    repo = PromptRepo()
    c1 = repo.publish("你是客服,只答退货。", {"lang": "zh"}, "stable")
    c1b = repo.publish("你是客服,只答退货。", {"lang": "zh"}, "stable")
    assert c1 == c1b, "同内容幂等 内容寻址唯一"
    c2 = repo.mutate(c1, "你是客服,只答退款。")
    assert c2 != c1, "改动产出新对象"
    assert repo.objects[c1]["text"] == "你是客服,只答退货。", "旧对象原样保留 不可变"
    assert repo.resolve("stable")[0] == c1, "别名仍指旧版 切换是显式动作"
    repo.refs["stable"] = c2
    assert repo.resolve("stable")[0] == c2
    rec = repo.audit_ref("stable", "req-42")
    assert rec == {"request": "req-42", "alias": "stable", "cid": c2}, "请求级可追溯"
    try:
        repo.resolve("canary")
        raise SystemExit("未注册别名应报错")
    except KeyError:
        pass
    print("Prompt 仓库通过:内容寻址 幂等发布 不可变对象 请求级追溯")
