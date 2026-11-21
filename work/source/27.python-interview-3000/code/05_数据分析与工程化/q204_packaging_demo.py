import importlib.metadata

def get_version(fallback="0.0.0.dev0"):
    # 安装后可从包元数据读取版本,未安装时用 fallback
    try:
        return importlib.metadata.version("myproj")
    except importlib.metadata.PackageNotFoundError:
        return fallback

def test_version_fallback():
    assert isinstance(get_version(), str)
