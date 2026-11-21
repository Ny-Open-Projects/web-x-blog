"""存活与就绪探针分流: 摘流量不等于重启(纯标准库状态机)。"""


class App:
    def __init__(self):
        self.state = "serving"       # serving | draining | dead

    def liveness(self):
        """失败 = 重启容器。只要进程没僵死就必须 True。"""
        return self.state != "dead"

    def readiness(self):
        """失败 = 摘出负载均衡。发布排空、过热限流时翻 False。"""
        return self.state == "serving"

    def begin_release(self):
        self.state = "draining"

    def finish_release(self):
        self.state = "serving"

    def crash(self):
        self.state = "dead"


app = App()
print("常态:     liveness", app.liveness(), "readiness", app.readiness())
app.begin_release()
print("排空中:   liveness", app.liveness(), "readiness", app.readiness(), "-> LB 摘除, 容器不重启")
app.finish_release()
print("发布完成: liveness", app.liveness(), "readiness", app.readiness())

print()
print("错误示范: 用 liveness 承担排空 -> 排空本该摘流量, 却触发容器重启, 在途请求全断,")
print("          多实例一起翻车就是重启风暴")
print("正确姿势: liveness 只看进程能不能响应本地探针, readiness 才看能不能接活")
app.crash()
print("进程僵死: liveness", app.liveness(), "-> 这才是重启的场景")
