"""weakref.finalize 清理链:对象消亡触发的级联资源释放。"""
import gc
import os
import tempfile
import weakref


class Session:
    """持有临时文件;对象消亡时由 finalize 回调清理,回调不持有 self。"""

    def __init__(self, user):
        self.user = user
        fd, path = tempfile.mkstemp(prefix="sess_")
        os.close(fd)
        self.path = path
        # 关键:回调与参数必须是普通函数和数据,一旦引用 self 对象就永远不死
        self._finalizer = weakref.finalize(self, Session._cleanup, path, user)

    @staticmethod
    def _cleanup(path, user):
        os.unlink(path)
        print(f"  finalize 触发:{user} 的临时文件已删除")

    def close(self):
        """显式关闭:finalize 至多执行一次,重复调用是安全的。"""
        if self._finalizer.alive:
            self._finalizer()
        print(f"  close {self.user}:alive={self._finalizer.alive}")


if __name__ == "__main__":
    sessions = [Session("alice"), Session("bob")]
    paths = [s.path for s in sessions]
    print("临时文件存在:", all(os.path.exists(p) for p in paths))

    print("alice 走显式 close:")
    sessions[0].close()
    print("重复 close:")
    sessions[0].close()

    print("bob 走对象消亡触发的隐式清理:")
    del sessions[1]
    gc.collect()                 # CPython 引用归零即触发,collect 只是兜底

    print("bob 的临时文件已不存在:", not os.path.exists(paths[1]))
