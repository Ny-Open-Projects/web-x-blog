"""概念级 DAG 演示:用标准库表达 依赖 + 幂等任务 + 逻辑日期,
生产上对应 Airflow 的 DAG 定义。"""
from dataclasses import dataclass, field

@dataclass
class Task:
    task_id: str
    fn: callable
    upstream: list = field(default_factory=list)

class Dag:
    def __init__(self, dag_id, execution_date):
        self.dag_id = dag_id
        self.execution_date = execution_date   # 逻辑日期,即数据日期
        self.tasks = {}

    def add(self, task):
        self.tasks[task.task_id] = task
        return self

    def run(self):
        done = {}
        def visit(tid):
            if tid in done:
                return done[tid]
            t = self.tasks[tid]
            for up in t.upstream:              # 依赖先行
                visit(up)
            done[tid] = t.fn(self.execution_date)
            return done[tid]
        for tid in self.tasks:
            visit(tid)
        return done

def extract(date): return f"raw@{date}"
def transform(date): return f"clean@{date}"
def load(date): return f"loaded@{date}"

if __name__ == "__main__":
    dag = Dag("user_etl", "2026-11-01")
    dag.add(Task("extract", extract))
    dag.add(Task("transform", transform, ["extract"]))
    dag.add(Task("load", load, ["transform"]))
    print(dag.run())
