import io
import pickle
import pickletools

print("default protocol:", pickle.DEFAULT_PROTOCOL, "| highest:", pickle.HIGHEST_PROTOCOL)

# 恶意负载演示:仅构造,绝不 loads
payload = pickle.dumps({"ok": 1})
pickletools.dis(io.BytesIO(payload))   # 可见 REDUCE/BUILD 等操作码即虚拟机指令

# 白名单缓解:RestrictedUnpickler
import builtins

class SafeUnpickler(pickle.Unpickler):
    ALLOWED = {("builtins", "dict"), ("builtins", "set")}
    def find_class(self, module, name):
        if (module, name) not in self.ALLOWED:
            raise pickle.UnpicklingError(f"forbidden {module}.{name}")
        return getattr(builtins, name)

try:
    SafeUnpickler(io.BytesIO(payload)).load()
    print("safe load ok")
except pickle.UnpicklingError as e:
    print("blocked:", e)

# 版本兼容坑:类路径重构即破坏旧数据
class Old:
    pass
blob = pickle.dumps(Old())
print("roundtrip:", type(pickle.loads(blob)).__name__)
# 若把 Old 改名/挪模块,旧 blob 将 UnpicklingError: 路径被编进流里
