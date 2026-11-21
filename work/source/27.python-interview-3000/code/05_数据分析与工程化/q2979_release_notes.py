"""发布说明自动汇总器: 约定式提交解析 -> 分类分组 -> 破坏性变更置顶 -> Markdown 成稿"""
import os
import re
import tempfile
from datetime import date

COMMITS = [
    "feat(api): 新增 POST /v2/orders 批量下单接口",
    "fix(auth): 修复 token 过期后无限重定向",
    "feat!: 下线 v1 下单接口, 客户端必须迁移到 v2",
    "perf(db): 订单查询增加 user_id,created_at 复合索引",
    "fix(web): 空购物车页面偶发白屏",
    "docs: 更新接入指南与限流说明",
    "chore: 例行依赖升级",
    "merge branch 'hotfix-x'",   # 不合规范的提交, 应进未归类
]

COMMIT_RE = re.compile(r"^(feat|fix|perf|docs|chore|refactor|test|build|ci)(!)?(?:\(([^)]*)\))?: (.+)$")
SECTION = {"feat": "新功能", "fix": "问题修复", "perf": "性能优化",
           "docs": "文档", "chore": "维护", "refactor": "重构", "test": "测试", "build": "构建", "ci": "CI"}


def classify(commits):
    """解析约定式提交: 返回 按类分组 + 破坏性变更 + 未归类"""
    grouped, breaking, unknown = {}, [], []
    for c in commits:
        m = COMMIT_RE.match(c)
        if not m:
            unknown.append(c)
            continue
        typ, bang, scope, msg = m.groups()
        entry = {"scope": scope or "", "msg": msg}
        if bang:
            breaking.append(entry)
        grouped.setdefault(typ, []).append(entry)
    return grouped, breaking, unknown


def render(version, grouped, breaking, unknown, day):
    lines = ["# 发布说明 %s (%s)" % (version, day), ""]
    if breaking:
        lines += ["## 破坏性变更 - 升级前必读", ""]
        lines += ["- **%s**%s" % (e["msg"], " - [%s]" % e["scope"] if e["scope"] else "")
                  for e in breaking] + [""]
    for typ in ("feat", "fix", "perf", "docs", "chore"):
        entries = grouped.get(typ)
        if not entries:
            continue
        lines += ["## %s" % SECTION[typ], ""]
        lines += ["- %s%s" % (e["msg"], " - [%s]" % e["scope"] if e["scope"] else "")
                  for e in entries] + [""]
    if unknown:
        lines += ["## 未归类提交 - 请规范提交信息", ""]
        lines += ["- `%s`" % c for c in unknown] + [""]
    lines.append("共 %d 个提交, 其中破坏性 %d 个, 未归类 %d 个"
                 % (len(COMMITS), len(breaking), len(unknown)))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    grouped, breaking, unknown = classify(COMMITS)
    day = date(2026, 3, 1).isoformat()
    md = render("v2.4.0", grouped, breaking, unknown, day)
    out = os.path.join(tempfile.mkdtemp(prefix="notes_"), "RELEASE_v2.4.0.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(md)
    print("已生成:", out)
    print(md.rstrip())
    print("要点: 发布说明的原料是提交历史, 约定式提交让分类零人工; 破坏性变更必须置顶, 未归类条目反过来倒逼提交规范")
