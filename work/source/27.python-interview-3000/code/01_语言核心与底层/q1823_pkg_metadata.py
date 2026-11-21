"""importlib.metadata:已安装发行版的版本与元数据探测。"""
import importlib.metadata as md


def probe(dists):
    found = []
    for name in dists:
        try:
            found.append((name, md.version(name)))
        except md.PackageNotFoundError:
            continue
    return found


def show_first(found):
    if not found:
        print("纯标准库环境,没有可探测的第三方发行版")
        return
    name, ver = found[0]
    meta = md.metadata(name)
    print("首个发行版:", name, ver)
    print("Summary:", (meta.get("Summary") or "")[:56])
    if hasattr(md, "packages_distributions"):     # 3.10+ 才有该 API
        mapping = md.packages_distributions().get(name, [])
        print("顶层模块映射:", sorted(mapping)[:3] or "无")


if __name__ == "__main__":
    found = probe(["setuptools", "pip", "wheel", "six", "nonexistent-xyz"])
    print("探测到:", found)
    show_first(found)
