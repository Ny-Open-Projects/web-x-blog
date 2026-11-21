
OLD_SERVICE = {"auth", "billing", "search", "notify"}
NEW_SERVICE = {"auth", "billing", "search-v2", "audit", "notify"}

GRANTED = frozenset({"read", "write", "export"})
REQUIRED_EXPORT = frozenset({"read", "export"})

DOCS = {
    "a1": {"python", "db"},
    "a2": {"python"},
    "a3": {"db", "cache"},
    "a4": {"cache", "queue"},
}


def diff_report(old, new):
    added = sorted(new - old)
    removed = sorted(old - new)
    kept = sorted(old & new)
    changed = sorted(old ^ new)
    return added, removed, kept, changed


if __name__ == "__main__":
    added, removed, kept, changed = diff_report(OLD_SERVICE, NEW_SERVICE)
    print("added  :", added)
    print("removed:", removed)
    print("kept   :", kept)
    print("changed:", changed)

    # 权限:所需 ⊆ 已授
    print("export allowed:", REQUIRED_EXPORT <= GRANTED)
    print("admin denied  :", not ({"admin"} <= GRANTED))

    # 标签过滤:全部命中用子集,任一命中用交集
    python_docs = sorted(k for k, tags in DOCS.items() if "python" in tags)
    tagged_all = sorted(k for k, tags in DOCS.items() if {"db", "cache"} <= tags)
    tagged_any = sorted(k for k, tags in DOCS.items() if tags & {"db", "queue"})
    print("python docs  :", python_docs)
    print("db AND cache :", tagged_all)
    print("db OR queue  :", tagged_any)
