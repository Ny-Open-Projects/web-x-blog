"""模板组合渲染:include 递归展开,栈检测循环包含与深度超限。"""
import re

INCLUDE_RE = re.compile(r"\{%\s*include\s+(\w+)\s*%\}")
MAX_DEPTH = 8


def render(templates, root, values, _stack=None, _depth=0):
    _stack = _stack or []
    if root in _stack:
        cycle = " -> ".join(_stack + [root])
        raise ValueError("循环包含:" + cycle)
    if _depth > MAX_DEPTH:
        raise ValueError("包含深度超过上限 %d" % MAX_DEPTH)
    if root not in templates:
        raise ValueError("模板 %s 不存在" % root)
    body = templates[root]

    def sub(m):
        return render(templates, m.group(1), values, _stack + [root], _depth + 1)

    out = INCLUDE_RE.sub(sub, body)
    for k in sorted(values):
        out = out.replace("{{" + k + "}}", str(values[k]))
    return out


if __name__ == "__main__":
    templates = {
        "base": "{% include header %}\n{{content}}\n{% include footer %}",
        "header": "【{{title}}】",
        "footer": "—— {{team}}",
    }
    out = render(templates, "base", {"title": "客服手册", "team": "平台组",
                                     "content": "正文第一段"})
    assert "【客服手册】" in out and "正文第一段" in out and "—— 平台组" in out
    assert "include" not in out, "渲染后不得残留 include 指令"

    # 循环包含:a 引 b b 引 a
    loop = {"a": "A {% include b %}", "b": "B {% include a %}"}
    try:
        render(loop, "a", {})
        raise AssertionError("循环包含必须报错")
    except ValueError as e:
        assert "循环包含" in str(e) and "a -> b -> a" in str(e)

    # 深度超限:一条长链
    chain = {"t0": "{% include t1 %}"}
    for i in range(1, 12):
        chain["t%d" % i] = "{%% include t%d %%}" % (i + 1)
    try:
        render(chain, "t0", {})
        raise AssertionError("深度超限必须报错")
    except ValueError as e:
        assert "深度" in str(e)

    try:
        render(templates, "ghost", {})
        raise AssertionError("缺失模板必须报错")
    except ValueError as e:
        assert "不存在" in str(e)
    print("组合渲染通过:递归展开正常,循环 链超长 缺失三类结构错误全拦截")
