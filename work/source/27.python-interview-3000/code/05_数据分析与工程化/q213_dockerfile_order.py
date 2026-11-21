def layer_cache_plan(steps: list[tuple[str, str]]) -> list[str]:
    # 模拟构建:返回每步是否命中缓存
    # 依赖清单不变时,装依赖层可复用缓存
    cache = {"pyproject.toml+uv.lock": True, "src/": False}
    return [f"{action}:{cache.get(src, False)}" for action, src in steps]

def test_cache_hits():
    plan = layer_cache_plan([
        ("install deps", "pyproject.toml+uv.lock"),
        ("copy code", "src/"),
    ])
    assert plan == ["install deps:True", "copy code:False"]
