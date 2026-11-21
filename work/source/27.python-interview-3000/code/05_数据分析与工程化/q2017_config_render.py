"""配置模板渲染:环境变量注入,必填缺失显式报错,禁止静默空值"""

import re

TEMPLATE = """host = ${DB_HOST}
port = ${DB_PORT}
pool = ${DB_POOL}
"""
REQUIRED = ["DB_HOST", "DB_PORT"]
DEFAULTS = {"DB_POOL": "5"}
PLACEHOLDER = re.compile(r"\$\{(\w+)\}")


def render(template, env):
    keys = sorted(set(PLACEHOLDER.findall(template)))
    missing = [k for k in keys if k not in env and k not in DEFAULTS]
    if missing:
        raise ValueError(f"缺少必填配置: {missing},拒绝渲染")
    out = template
    for k in keys:
        value = env.get(k, DEFAULTS.get(k))
        if value in (None, ""):
            raise ValueError(f"{k} 为空,禁止静默渲染空值")
        out = out.replace("${" + k + "}", str(value))
    return out


if __name__ == "__main__":
    print(render(TEMPLATE, {"DB_HOST": "db.internal", "DB_PORT": "5432"}))
    try:
        render(TEMPLATE, {"DB_HOST": "db.internal"})
    except ValueError as e:
        print("故意缺配置:", e)
    print("要点:占位符缺失要一次性列全再报错,别改一处跑一次;默认值只给低危项;渲染产物落盘留档,排查环境问题时直接 diff 渲染结果")
