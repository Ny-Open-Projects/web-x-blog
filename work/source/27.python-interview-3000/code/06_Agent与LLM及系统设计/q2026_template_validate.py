"""指令模板的变量注入校验:占位符与 schema 对齐 类型检查 危险片段拦截。"""
import re

VAR_RE = re.compile(r"\{(\w+)\}")
REINJECT_RE = re.compile(r"\{\w+\}")
FENCE = "`" * 3                 # 运行时拼接,避免源码里出现字面三反引号
DANGEROUS = (FENCE, "{%")       # 值里出现代码围栏或模板语法视为注入风险


def render(template, values, schema):
    placeholders = set(VAR_RE.findall(template))
    declared = set(schema)
    problems = []
    for name in sorted(placeholders - declared):
        problems.append("模板变量 %s 未在 schema 声明" % name)
    for name in sorted(placeholders & declared):
        if name not in values:
            problems.append("变量 %s 缺失" % name)
            continue
        v = values[name]
        want = schema[name]
        if want == "int" and not isinstance(v, int):
            problems.append("变量 %s 需要 int" % name)
        if want == "str" and not isinstance(v, str):
            problems.append("变量 %s 需要 str" % name)
        if isinstance(v, str):
            if any(d in v for d in DANGEROUS):
                problems.append("变量 %s 含危险片段" % name)
            if REINJECT_RE.search(v):
                problems.append("变量 %s 试图回注占位符" % name)
    if problems:
        raise ValueError(";".join(problems))
    out = template
    for name in sorted(placeholders):
        out = out.replace("{" + name + "}", str(values[name]))
    return out


if __name__ == "__main__":
    tpl = "你是{role},回答不超过{limit}字,主题:{topic}。"
    schema = {"role": "str", "limit": "int", "topic": "str"}

    ok = render(tpl, {"role": "客服", "limit": 100, "topic": "退货"}, schema)
    assert ok == "你是客服,回答不超过100字,主题:退货。"

    for values, frag in [
        ({"role": "客服", "topic": "退货"}, "缺失"),                    # 少 limit
        ({"role": "客服", "limit": "很多", "topic": "退货"}, "需要 int"),
        ({"role": "客服", "limit": 100, "topic": "退货" + FENCE}, "危险片段"),
        ({"role": "客服", "limit": 100, "topic": "{limit}"}, "回注"),
    ]:
        try:
            render(tpl, values, schema)
            raise AssertionError("应当拒绝:" + frag)
        except ValueError as e:
            assert frag in str(e), (frag, str(e))

    # 模板用了 schema 没声明的占位符:结构性错误,必须拦下
    try:
        render("你是{role},密级{level}", {"role": "客服", "level": "高"}, schema)
        raise AssertionError("未声明占位符应当拒绝")
    except ValueError as e:
        assert "未在 schema" in str(e) and "level" in str(e)

    # schema 声明了但模板没用的变量不算错误,只是沉默未用
    used = render("主题:{topic}", {"topic": "x", "role": "y"}, schema)
    assert used == "主题:x"
    print("模板校验通过:缺失 类型 危险片段 回注四类问题全拦截,合法值正常渲染")
