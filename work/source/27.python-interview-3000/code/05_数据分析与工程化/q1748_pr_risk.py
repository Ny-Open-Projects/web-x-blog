"""PR 风险自动分级:按触碰的文件类别打风险分,高风险强制相应评审人"""

RULES = [
    # 路径前缀, 风险分, 需要的评审角色
    ("calibers/", 5, "指标负责人"),
    ("scheduler/", 4, "调度负责人"),
    ("migrations/", 5, "DBA"),
    ("dwd/", 3, "数仓 owner"),
    ("docs/", 1, None),
]
HIGH = 5


def classify(files):
    score, roles, hits = 0, set(), []
    for f in files:
        for prefix, s, role in RULES:
            if f.startswith(prefix):
                score += s
                hits.append((f, s))
                if role:
                    roles.add(role)
                break
        else:
            hits.append((f, 1))
            score += 1
    level = "HIGH" if score >= HIGH else ("MEDIUM" if score >= 3 else "LOW")
    return level, score, roles, hits


if __name__ == "__main__":
    cases = [
        ["calibers/gmv.py"],
        ["dwd/transform_x.py", "docs/readme.md"],
        ["scheduler/daily_dag.py", "migrations/0007_add_col.sql"],
    ]
    for files in cases:
        level, score, roles, hits = classify(files)
        reviewers = ",".join(sorted(roles)) or "普通评审"
        print(f"PR {files} -> {level} ({score} 分) 评审: {reviewers}")
    print("要点:分级规则进版本库与 CI,碰口径/迁移/调度一律强制对应负责人;分数只是门槛,不替代人工评审")
