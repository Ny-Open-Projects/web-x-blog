import json

AVAILABLE = {
    "requests": {"2.31.0": [], "2.32.0": ["urllib3>=1.21.1"]},
    "urllib3": {"2.0.7": [], "2.2.1": []},
}

def resolve(requirements, locked=None):
    """简化解析器:返回确定性的 pinned 版本,模拟 lock 的思想"""
    locked = dict(locked or {})
    for name in requirements:
        versions = sorted(AVAILABLE[name], reverse=True)
        locked[name] = versions[0]
        for dep in AVAILABLE[name][locked[name]]:
            dep_name = dep.split(">=")[0].strip()
            if dep_name not in locked:
                locked.update(resolve([dep_name]))
    return locked

if __name__ == "__main__":
    # uv 命令:uv lock 生成锁文件 / uv sync 按 lock 安装 / uv lock --upgrade-package requests
    lock = resolve(["requests"])
    print(json.dumps(lock, indent=2))
    assert resolve(["requests"]) == lock, "解析必须确定性,这就是 lock 的意义"
