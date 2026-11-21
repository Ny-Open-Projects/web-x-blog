from typing import Protocol, runtime_checkable

@runtime_checkable
class Runner(Protocol):
    def run(self) -> str:
        """结构声明,不含实现"""

class Job:
    def run(self) -> str:
        return "job running"

class StubRunner:
    def run(self) -> str:
        raise NotImplementedError

class NotARunner:
    pass

def execute(r: Runner) -> str:
    return r.run()

if __name__ == "__main__":
    print(execute(Job()))                # 无需继承 Runner
    print(isinstance(Job(), Runner))     # True,运行时检查
    print(isinstance(NotARunner(), Runner))  # False

    class Legacy:
        def run(self):
            return "legacy"
    print(execute(Legacy()))             # 兼容旧类,结构满足即可
