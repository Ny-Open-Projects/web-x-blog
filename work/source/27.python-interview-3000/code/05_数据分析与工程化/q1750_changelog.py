"""changelog 自动生成:解析约定式提交,按类型分节,顺手算下一个版本号"""

import re

COMMITS = [
    "feat(board): 新增留存看板",
    "fix(etl): 修复时区偏移导致的重复计数",
    "feat(api)!: 调整分页参数为 cursor",     # ! 表示 breaking
    "chore(deps): 升级 pandas",
    "docs(readme): 补充部署说明",
]
PAT = re.compile(r"^(\w+)(?:\(([^)]*)\))?(!)?: (.+)$")


def parse(msg):
    m = PAT.match(msg)
    if not m:
        return None
    return {"type": m.group(1), "scope": m.group(2),
            "breaking": bool(m.group(3)), "subject": m.group(4)}


def bump(version, commits):
    parsed = [p for p in (parse(c) for c in commits) if p]
    major, minor, patch = map(int, version.split("."))
    if any(p["breaking"] for p in parsed):
        return f"{major + 1}.0.0"
    if "feat" in {p["type"] for p in parsed}:
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def changelog(version, commits):
    parsed = [p for p in (parse(c) for c in commits) if p]
    sections = {"feat": "### 新功能", "fix": "### 修复", "chore": "### 杂项", "docs": "### 文档"}
    out = [f"## {version}", ""]
    if any(p["breaking"] for p in parsed):
        out += ["**BREAKING**: 存在不兼容变更,升级前阅读迁移说明", ""]
    for t, title in sections.items():
        items = [p for p in parsed if p["type"] == t]
        if items:
            out.append(title)
            out += [f"- {p['scope'] + ': ' if p['scope'] else ''}{p['subject']}" for p in items]
            out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    nxt = bump("1.4.2", COMMITS)
    print(changelog(nxt, COMMITS))
    print(f"下一版本: 1.4.2 -> {nxt}")
    print("要点:changelog 是提交规范的红利,feat/fix/! 约定进 commit lint;breaking 必须附迁移说明,版本号由提交类型推导而不是拍脑袋")
