"""Prompt 注册表:版本管理 + stable/canary 别名 + 变量 schema 校验。"""


class PromptRegistry:
    def __init__(self):
        self.store = {}       # name -> {version: (template, required_vars)}
        self.alias = {}       # name -> {"stable": ver, "canary": ver}

    def register(self, name, version, template, required_vars, set_stable=False):
        self.store.setdefault(name, {})[version] = (template, required_vars)
        if set_stable or version not in self.alias.get(name, {}).values() and not self.alias.get(name):
            self.alias.setdefault(name, {})["stable"] = version

    def set_canary(self, name, version):
        assert version in self.store[name], "canary 必须先注册"
        self.alias[name]["canary"] = version

    def render(self, name, variables, channel="stable", version=None):
        version = version or self.alias[name][channel]
        template, required = self.store[name][version]
        missing = [v for v in required if v not in variables]
        assert not missing, f"变量缺失 {missing},拒绝渲染"
        return template.format(**variables), version


if __name__ == "__main__":
    reg = PromptRegistry()
    reg.register("qa", "v1", "你是客服。问题:{question}", ["question"], set_stable=True)
    reg.register("qa", "v2", "你是资深客服,先复述问题再回答:{question} (语言:{lang})", ["question", "lang"])
    reg.set_canary("qa", "v2")

    for ch in ["stable", "canary"]:
        text, ver = reg.render("qa", {"question": "怎么退款", "lang": "中文"}, channel=ch)
        print(f"[{ch}] v={ver}: {text}")

    try:
        reg.render("qa", {}, channel="canary")
    except AssertionError as e:
        print("变量缺失被拦截:", e)
    # 灰度回滚 = 把别名切回
    reg.alias["qa"]["canary"] = reg.alias["qa"]["stable"]
    _, rolled = reg.render("qa", {"question": "hi"}, channel="canary")
    assert rolled == "v1"
    print("回滚生效,canary 现指向", rolled)
