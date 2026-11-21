"""Cache-Control 指令矩阵与新鲜度裁决(纯标准库)。"""

DIRECTIVES = {
    # 指令: (出现位置, 一句话语义)
    "no-store": ("请求+响应", "任何环节不得存储, 优先级最高"),
    "no-cache": ("请求+响应", "可以存储但每次使用前必须协同验证"),
    "max-age": ("请求+响应", "响应侧定义新鲜期秒数, 请求侧约束可接受年龄"),
    "s-maxage": ("仅响应", "共享缓存的新鲜期, 存在时覆盖 max-age"),
    "must-revalidate": ("仅响应", "过期后禁止直接用陈旧副本, 必须回源验证"),
    "public": ("仅响应", "允许共享缓存存储, 即使请求带凭证"),
    "private": ("仅响应", "只允许浏览器私有缓存存储"),
    "max-stale": ("仅请求", "愿意接受超期不超过 N 秒的陈旧副本"),
    "only-if-cached": ("仅请求", "只接受缓存已有副本, 没有就 504"),
}


def parse(header_value):
    """把 Cache-Control 头解析成 dict: 无参指令值为 True, 带参指令为字符串。"""
    out = {}
    for token in header_value.split(","):
        name, sep, arg = token.strip().partition("=")
        if not name:
            continue
        out[name.strip().lower()] = arg.strip('"') if sep else True
    return out


def decide(shared, resp_dirs, age):
    """按优先级裁决缓存行为: no-store > no-cache > 新鲜期 > 陈旧策略。"""
    if resp_dirs.get("no-store"):
        return "不缓存", "no-store 禁止存储, 每次都回源"
    if resp_dirs.get("no-cache"):
        return "须验证", "no-cache 每次使用前都要带条件头验证"
    max_age = resp_dirs.get("max-age", 0)
    if shared and "s-maxage" in resp_dirs:
        max_age = int(resp_dirs["s-maxage"])
    if age < int(max_age):
        return "新鲜", "age {} < 新鲜期 {}, 直接复用".format(age, max_age)
    if resp_dirs.get("must-revalidate"):
        return "须验证", "已过期且 must-revalidate, 不得回退陈旧副本"
    return "可陈旧", "过期但未禁止陈旧, 可按 max-stale 等策略权衡"


for name, (where, why) in DIRECTIVES.items():
    print("{:16s} {:6s} {}".format(name, where, why))

parsed = parse("public, max-age=60, no-cache=\"Set-Cookie\"")
assert parsed["max-age"] == "60" and parsed["public"] is True

print("-- 裁决演示 --")
for shared, dirs, age in [(False, parse("no-store, max-age=600"), 0),
                          (True, parse("max-age=60, s-maxage=300"), 100),
                          (False, parse("max-age=60"), 100),
                          (False, parse("max-age=60, must-revalidate"), 100)]:
    result, why = decide(shared, dirs, age)
    print("shared={} age={:<4} -> {:4s} | {}".format(shared, age, result, why))
assert decide(True, parse("max-age=60, s-maxage=300"), 100)[0] == "新鲜"
assert decide(False, parse("max-age=60"), 100)[0] == "可陈旧"
assert decide(False, parse("max-age=60, must-revalidate"), 100)[0] == "须验证"
print("要点: 先看 no-store 再看 no-cache, 共享缓存用 s-maxage 盖过 max-age, "
      "must-revalidate 决定过期后能不能将就")
