"""模拟: pipeline 批量但可被并发插入, Lua 脚本原子执行"""
import threading

class FakeServer:
    def __init__(self):
        self.kv = {}
        self.lock = threading.Lock()

    def exec_pipeline(self, cmds):
        """pipeline: 一次传输, 但逐条执行, 中间可能插队"""
        results = []
        for op, k, v in cmds:
            with self.lock:
                if op == "set":
                    self.kv[k] = v
                results.append(("ok", k))
            time_would_allow_interruption = None  # 真实 redis 此处可能执行他人命令
        return results

    def eval_atomic(self, script):
        """lua: 整段脚本作为单命令原子执行"""
        with self.lock:
            before = dict(self.kv)
            script(self.kv)                      # 脚本内部无需再加锁
            return before, dict(self.kv)

if __name__ == "__main__":
    srv = FakeServer()
    cmds = [("set", "k1", 1), ("set", "k2", 2), ("set", "k3", 3)]
    print("pipeline 结果:", srv.exec_pipeline(cmds))

    def transfer(store):                         # 等价 lua: 转账两步
        store["a"] = store.get("a", 100) - 30
        store["b"] = store.get("b", 0) + 30
    before, after = srv.eval_atomic(transfer)
    print("lua 原子: before a=%s b=%s -> after a=%s b=%s"
          % (before.get("a"), before.get("b"), after["a"], after["b"]))
