"""上下文窗口用量仪表:分项计量 token 用量,水位线告警并指出最大占用段。"""
import re


def est_tokens(text):
    """粗估:中文按字计,其余按 4 字符一个 token。"""
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    other = len(text) - cjk
    return cjk + (other + 3) // 4


class ContextGauge:
    def __init__(self, window, warn_at=0.8):
        self.window = window
        self.warn_at = warn_at
        self.sections = {}

    def add(self, section, text):
        self.sections[section] = self.sections.get(section, 0) + est_tokens(text)

    def usage(self):
        total = sum(self.sections.values())
        ratio = total / float(self.window)
        alerts = []
        if ratio >= 1.0:
            alerts.append("超窗:必须裁剪后才能发起请求")
        elif ratio >= self.warn_at:
            alerts.append("高水位:接近窗口上限")
        top = max(self.sections, key=self.sections.get) if self.sections else None
        return {"sections": dict(self.sections), "total": total,
                "ratio": round(ratio, 3), "alerts": alerts, "top_section": top}


if __name__ == "__main__":
    assert est_tokens("你好世界") == 4 and est_tokens("abcd") == 1
    assert est_tokens("你好world") == 4

    g = ContextGauge(window=1000, warn_at=0.8)
    g.add("system", "系统提示词" * 20)          # 100 token
    g.add("history", "历史对话" * 50)           # 200 token
    g.add("retrieved", "检索到的资料" * 100)    # 600 token
    u = g.usage()
    assert u["total"] == 900 and u["ratio"] == 0.9
    assert u["alerts"] == ["高水位:接近窗口上限"], u["alerts"]
    assert u["top_section"] == "retrieved", "要能指出最大占用段"

    g.add("tool_results", "工具结果" * 50)      # 再加 200,超窗
    u2 = g.usage()
    assert u2["total"] == 1100 and u2["ratio"] > 1.0
    assert u2["alerts"] == ["超窗:必须裁剪后才能发起请求"]
    print("用量仪表通过:分项计量 900/1000 高水位告警,超窗后指认最大段")
