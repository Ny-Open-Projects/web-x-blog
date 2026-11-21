
PINNED = {"requests": "2.31.0", "urllib3": "2.0.7", "pydantic": "1.10.0"}
LATEST = {"requests": "2.32.3", "urllib3": "2.2.1", "pydantic": "2.9.0"}
MAJOR_BREAK = {"pydantic"}

def plan(pinned, latest):
    actions = []
    for pkg, cur in sorted(pinned.items()):
        new = latest[pkg]
        if new.split(".")[0] != cur.split(".")[0] and pkg in MAJOR_BREAK:
            actions.append((pkg, cur, new, "单独 PR + 迁移说明 + 人工评审"))
        elif new != cur:
            actions.append((pkg, cur, new, "批量小版本 PR,CI 绿自动合并"))
    return actions

for pkg, cur, new, how in plan(PINNED, LATEST):
    print(f"{pkg} {cur} -> {new}({how})")
