store = {}  # key -> value,模拟资源

def handle(method: str, key: str, value=None):
    if method == 'GET':
        return store.get(key)
    if method == 'PUT':          # 幂等:覆盖式写入
        store[key] = value
        return value
    if method == 'POST':         # 非幂等:每次追加,结果不同
        store.setdefault(key, []).append(value)
        return store[key]
    if method == 'DELETE':       # 幂等:删除多次结果一致
        return store.pop(key, None)

for _ in range(3):
    handle('PUT', 'a', 1)
    handle('POST', 'log', 'x')
print(store)  # {'a': 1, 'log': ['x', 'x', 'x']}
