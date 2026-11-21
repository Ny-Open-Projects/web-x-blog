"""断线重连: 指数退避加抖动 与 命令失败后的未知语义"""
import random
import time

random.seed(11)

class FlakyClient:
    def __init__(self, fail_times):
        self.calls, self.fail_times = 0, fail_times
        self.connected = True

    def connect(self):
        self.connected = True
        print("  连接恢复")

    def execute(self, cmd):
        if not self.connected:
            raise ConnectionError("连接已断开")
        self.calls += 1
        if self.calls in self.fail_times:
            self.connected = False
            raise ConnectionError("半途断连: 命令是否已执行未知")

def call_with_retry(client, cmd, max_retry=5):
    attempt, backoff = 0, 0.05
    while attempt <= max_retry:
        try:
            return client.execute(cmd)
        except ConnectionError as e:
            attempt += 1
            sleep = backoff + random.uniform(0, backoff / 2)   # 指数退避 + 抖动
            print(f"  第 {attempt} 次失败: {e}; {sleep * 1000:.0f} ms 后重连重试")
            time.sleep(sleep)
            backoff *= 2
            if not client.connected:
                client.connect()
    raise RuntimeError("重试耗尽, 上抛给调用方决定降级")

client = FlakyClient(fail_times={1, 2})
print("调用 INCR stock:")
try:
    call_with_retry(client, "INCR")
except RuntimeError:
    print("  放弃, 走降级读库")
print("要点: 断连时最后一条命令的结果未知 -> 所有写命令必须幂等或可重入;")
print("      重试要有预算与退避上限, 否则故障恢复瞬间会雪崩式重连")
