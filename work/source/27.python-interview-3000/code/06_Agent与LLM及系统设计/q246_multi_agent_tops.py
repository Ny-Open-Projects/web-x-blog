"""三种拓扑的最小可运行对比:编排者、流水线、辩论,全部 stub。"""


class StubAgent:
    def __init__(self, name, reply_fmt):
        self.name, self.fmt = name, reply_fmt

    def act(self, msg: str) -> str:
        return self.fmt.format(msg=msg)


# 拓扑一:编排者-执行者
def orchestrator(task: str) -> str:
    workers = {"检索": StubAgent("检索", "找到与{msg}相关的3篇资料"),
               "写作": StubAgent("写作", "基于[{msg}]写出草稿")}
    parts = [workers[k].act(task) for k in workers]
    return f"编排者汇总: {' | '.join(parts)}"


# 拓扑二:流水线
def pipeline(task: str) -> str:
    for agent in [StubAgent("草稿", "初稿:{msg}"),
                  StubAgent("审稿", "审后:{msg} 已修正"),
                  StubAgent("润色", "终稿:{msg}")]:
        task = agent.act(task)
    return task


# 拓扑三:辩论
def debate(topic: str, rounds: int = 2) -> str:
    pro, con = StubAgent("正方", "支持:{msg} 因为收益大"), StubAgent("反方", "反对:{msg} 因为风险高")
    msg = topic
    for _ in range(rounds):
        msg = f"{pro.act(msg)} VS {con.act(msg)}"
    return f"裁判裁决:{msg}"


if __name__ == "__main__":
    print(orchestrator("市场调研"))
    print(pipeline("新品介绍"))
    print(debate("是否上微服务"))
