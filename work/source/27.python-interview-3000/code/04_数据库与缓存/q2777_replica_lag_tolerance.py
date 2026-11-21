"""只读副本的读延迟容忍: 场景标注容忍度, 写令牌保读己之写"""
LAG_S = [2.0]      # 当前观测到的副本延迟

TOLERANCE = {"profile": 5.0, "recommend": 60.0, "payment": 0.0}

def route(scene, session_last_write_ago):
    tol = TOLERANCE[scene]
    if session_last_write_ago is not None and session_last_write_ago < 3.0:
        return "primary", "会话 3 秒内写过, 读己之写"
    if tol == 0.0:
        return "primary", "该场景零容忍"
    if LAG_S[0] > tol:
        return "primary", "副本延迟 %.0fs 超过容忍度 %.0fs" % (LAG_S[0], tol)
    return "replica", "延迟 %.0fs 在容忍度 %.0fs 内" % (LAG_S[0], tol)

cases = [("profile", None), ("profile", 1.0), ("recommend", None),
         ("payment", None), ("recommend", 10.0)]
for scene, ago in cases:
    target, why = route(scene, ago)
    print("%-10s 会话写于 %s -> %-8s (%s)"
          % (scene, "刚刚" if ago is not None else "很久前", target, why))

LAG_S[0] = 12.0
print("--- 延迟尖峰到 12s 之后 ---")
for scene in ("profile", "recommend"):
    target, why = route(scene, None)
    print("%-10s -> %-8s (%s)" % (scene, target, why))
