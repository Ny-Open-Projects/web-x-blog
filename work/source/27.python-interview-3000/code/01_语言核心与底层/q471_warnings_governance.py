import warnings

def legacy_api():
    warnings.warn("legacy_api will be removed in 2.0, use new_api",
                  DeprecationWarning, stacklevel=2)
    return "old"

def risky():
    warnings.warn("disk almost full", ResourceWarning)

if __name__ == "__main__":
    # 库作者视角:开发期把告警升级为错误,防回归
    warnings.simplefilter("error", DeprecationWarning)
    try:
        legacy_api()
    except DeprecationWarning as e:
        print("as error:", e)
    warnings.simplefilter("default")

    # 调用方视角:收集并审计
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        risky()
        legacy_api()
        for w in caught:
            print(f"[{w.category.__name__}] {w.message} at line {w.lineno}")

    warnings.filterwarnings("ignore", message=".*disk almost full.*")
    risky()                               # 被静默
    print("filtered ok")
