"""pipeline 与 MULTI/EXEC: 省往返与保证原子是两件事"""

class Server:
    """单线程命令执行器: 按到达顺序逐条执行"""

    def __init__(self):
        self.kv = {}
        self.log = []

    def exec_cmd(self, client, cmd):
        op, key, val = cmd
        if op == "SET":
            self.kv[key] = val
        elif op == "INCR":
            self.kv[key] = self.kv.get(key, 0) + 1
        self.log.append((client, op, key))
        return self.kv[key]

def run_pipeline(server, a_cmds, b_cmd):
    """pipeline 只是打包发送, 服务器仍可能穿插其他客户端的命令"""
    for i, cmd in enumerate(a_cmds):
        server.exec_cmd("A", cmd)
        if i == 1:                        # A 的第二条之后, B 插队
            server.exec_cmd("B", b_cmd)

def run_multi(server, a_cmds, b_cmd):
    """MULTI/EXEC: 命令先入队, EXEC 时整块连续执行, 其他客户端无法穿插"""
    queued = list(a_cmds)                 # MULTI 后命令进入队列
    server.exec_cmd("B", b_cmd)           # B 的命令在 EXEC 之前执行
    for cmd in queued:                    # EXEC 原子块
        server.exec_cmd("A", cmd)

a_cmds = [("SET", "lock", "A"), ("INCR", "hits", None), ("SET", "lock", "A-again")]
b_cmd = ("SET", "lock", "B")

s1 = Server()
run_pipeline(s1, a_cmds, b_cmd)
print("pipeline 场景执行序:", [op + ":" + key for _, op, key in s1.log])
print("  最终 lock =", s1.kv["lock"], "-> B 插在中间, A 的第二次 SET 又覆盖了 B")

s2 = Server()
run_multi(s2, a_cmds, b_cmd)
print("MULTI/EXEC 场景执行序:", [op + ":" + key for _, op, key in s2.log])
print("  最终 lock =", s2.kv["lock"], "-> B 先执行完, A 的块内三条连续完成")
print("结论: pipeline 只省 RTT 不保证原子; 需要原子用 MULTI/EXEC 或 Lua; WATCH 提供 CAS 重试")
print("另注: pipeline 内某条失败不影响其他条; MULTI 块内语法错误整块不入队, 运行时错误跳过该条继续")
