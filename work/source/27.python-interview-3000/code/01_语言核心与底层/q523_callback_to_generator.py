def walk_callback(node, visit):
    """回调风格:控制权在遍历者手里"""
    visit(node["name"])
    for child in node.get("children", []):
        walk_callback(child, visit)

def walk_generator(node):
    """生成器风格:控制权交还调用方"""
    yield node["name"]
    for child in node.get("children", []):
        yield from walk_generator(child)

TREE = {"name": "root", "children": [
    {"name": "a", "children": [{"name": "a1"}]},
    {"name": "b"},
]}

if __name__ == "__main__":
    names = []
    walk_callback(TREE, names.append)
    print("callback:", names)

    gen = walk_generator(TREE)
    print("lazy next:", next(gen), next(gen))

    for name in walk_generator(TREE):
        if name == "a1":
            break                             # 调用方可提前终止
        print("visited:", name)
