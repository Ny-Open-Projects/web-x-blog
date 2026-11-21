
TAGS = {
    "app:latest": "会漂移,禁止在生产引用",
    "app:1.4.2": "语义版本,推荐",
    "app:1.4.2-20261101": "版本+日期,可追溯构建时间",
    "app@sha256:abc123": "digest 级不可变,最强保证",
}

def deploy_ref(ref):
    if ref.endswith(":latest"):
        raise ValueError("生产禁止 latest")
    return f"kubectl set image deploy/app {ref}"

if __name__ == "__main__":
    for t, note in TAGS.items():
        print(f"{t:<24} {note}")
    print(deploy_ref("app:1.4.2"))
    try:
        deploy_ref("app:latest")
    except ValueError as e:
        print("已拦截:", e)
