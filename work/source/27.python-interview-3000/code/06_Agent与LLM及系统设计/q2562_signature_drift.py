"""Q2562 结果签名漂移的三种处置:严格拒收、降级读取与豁免名单。

上游工具悄悄换了 schema(字段改名、新增字段),读方有三种姿态:
strict 直接拒收并上报漂移;degrade 只读双方都认识的键并补缺省;
豁免名单里的工具允许静默降级,但必须留审计记录。
"""

V2_RESULT = {"tool": "scorer", "schema": 2, "confidence": 0.9, "model": "glm-x"}
V1_KNOWN = {"score": None, "confidence": None}  # v1 读方认识的键与缺省值


def strict_read(res):
    if "score" not in res:
        raise KeyError("契约字段 score 缺失,疑似 schema 漂移")
    return {"score": res["score"]}


def degrade_read(res, known):
    return {key: res.get(key, default) for key, default in known.items()}


def read_result(res, policy, exempt, audit):
    tool = res["tool"]
    if policy == "strict" and tool not in exempt:
        try:
            return strict_read(res), "strict"
        except KeyError as exc:
            audit.append("rejected:" + tool + ":" + str(exc))
            return None, "rejected"
    out = degrade_read(res, V1_KNOWN)
    if tool in exempt:
        audit.append("degraded-exempt:" + tool)
    else:
        audit.append("degraded:" + tool)
    return out, "degrade"


def main():
    audit = []
    r1, mode1 = read_result(V2_RESULT, "strict", set(), audit)
    assert r1 is None and mode1 == "rejected"
    r2, mode2 = read_result(V2_RESULT, "degrade", set(), audit)
    assert r2 == {"score": None, "confidence": 0.9}, r2
    r3, mode3 = read_result(V2_RESULT, "strict", {"scorer"}, audit)
    assert r3["confidence"] == 0.9 and mode3 == "degrade"
    assert any(a.startswith("rejected:") for a in audit)
    assert "degraded-exempt:scorer" in audit
    print("严格拒收并留痕:", audit[0])
    print("降级读取结果:", r2)
    print("豁免名单静默降级:", audit[-1])


if __name__ == "__main__":
    main()
