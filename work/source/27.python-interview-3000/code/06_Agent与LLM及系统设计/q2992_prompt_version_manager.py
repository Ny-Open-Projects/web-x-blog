"""Q2992 提示词版本管理器:多版本+变量渲染+稳定标签+一键回滚。

提示词是 LLM 应用的「代码」,必须像代码一样管版本:同一模板可以有
多个版本,渲染时统一做变量替换并对缺失变量报错;stable 标签决定
线上默认用哪一版;新版本灰度出问题要能一键回滚——本质是把 stable
指回旧版本。渲染结果要可复现,同样的输入永远得到同样的提示词。
"""

import re

VAR_PATTERN = re.compile(r"\{\{(\w+)\}\}")


class PromptError(Exception):
    pass


class PromptManager:
    def __init__(self):
        self._templates = {}      # name -> {version: template_str}
        self._stable = {}         # name -> stable version

    def add(self, name, version, template, stable=False):
        self._templates.setdefault(name, {})[version] = template
        if stable or name not in self._stable:
            self._stable[name] = version

    def promote(self, name, version):
        if version not in self._templates.get(name, {}):
            raise PromptError("版本不存在")
        self._stable[name] = version

    def rollback(self, name, to_version):
        """回滚 = 把 stable 指回指定旧版本。"""
        self.promote(name, to_version)

    def render(self, name, variables, version=None):
        versions = self._templates.get(name)
        if not versions:
            raise PromptError("模板不存在:" + name)
        ver = version or self._stable[name]
        template = versions[ver]
        required = set(VAR_PATTERN.findall(template))
        missing = required - set(variables)
        if missing:
            raise PromptError("缺少变量:" + ",".join(sorted(missing)))
        out = VAR_PATTERN.sub(
            lambda m: str(variables[m.group(1)]), template)
        extra = set(variables) - required
        note = "" if not extra else "(多余变量已忽略:%s)" \
            % ",".join(sorted(extra))
        return out + note

    def versions(self, name):
        return sorted(self._templates.get(name, {}))


def main():
    pm = PromptManager()
    pm.add("refund_reply", "v1",
           "您好,订单 {{order_id}} 的退款 {{amount}} 元将在 {{eta}} 内到账。",
           stable=True)
    pm.add("refund_reply", "v2",
           "您好,订单 {{order_id}} 已受理退款 {{amount}} 元,"
           "预计 {{eta}} 到账,短信将发送至 {{phone}}。")

    # 渲染走 stable,缺变量报错而不是填空串
    out = pm.render("refund_reply", {"order_id": "o_9", "amount": "199",
                                     "eta": "3 个工作日"})
    assert out.startswith("您好,订单 o_9 的退款 199 元"), out
    try:
        pm.render("refund_reply", {"order_id": "o_9"})
        raise AssertionError("应当报缺变量")
    except PromptError as exc:
        assert "缺少变量" in str(exc)

    # 指定版本渲染 + 多余变量提示
    out2 = pm.render("refund_reply",
                     {"order_id": "o_1", "amount": "50", "eta": "明天",
                      "phone": "138xxx", "memo": "x"},
                     version="v2")
    assert "138xxx" in out2 and "多余变量已忽略:memo" in out2, out2

    # 灰度出问题 → 一键回滚 stable
    pm.promote("refund_reply", "v2")
    assert pm.render("refund_reply", {"order_id": "x", "amount": "1",
                                      "eta": "d", "phone": "p"}).startswith(
        "您好,订单 x 已受理")
    pm.rollback("refund_reply", "v1")
    assert pm._stable["refund_reply"] == "v1"
    assert pm.versions("refund_reply") == ["v1", "v2"]
    try:
        pm.promote("refund_reply", "v9")
        raise AssertionError("应当报版本不存在")
    except PromptError:
        pass
    print("v1 渲染:", out)
    print("回滚后 stable:", pm._stable["refund_reply"])
    print("v2 渲染:", out2[:40] + "...")


if __name__ == "__main__":
    main()
