import re

SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?$")
PRE_RANK = {"alpha": 0, "beta": 1, "rc": 2}

def version_key(v):
    m = SEMVER.match(v)
    if not m:
        raise ValueError(f"非法版本号: {v}")
    major, minor, patch, pre = m.groups()
    if pre is None:
        return (int(major), int(minor), int(patch), 3, "")
    return (int(major), int(minor), int(patch), PRE_RANK.get(pre.split(".")[0], -1), pre)

if __name__ == "__main__":
    vs = ["1.0.0", "1.0.0-rc.1", "1.0.0-beta", "1.0.0-alpha", "0.9.9"]
    for v in sorted(vs, key=version_key):
        print(v)
    assert version_key("1.0.0-alpha") < version_key("1.0.0-beta") < version_key("1.0.0") 
    print("pre-release 排在正式版之前,tag 驱动构建即发布")
