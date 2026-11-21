from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Ctx:
    filename: str
    size_mb: float = 0
    validated: bool = False
    thumbnails: list = field(default_factory=list)
    db_id: str = ""
    failed_step: str = ""


def validate(ctx: Ctx) -> Ctx:
    if ctx.size_mb <= 0:
        raise ValueError("empty file")
    ctx.validated = True
    return ctx


def thumbnail(ctx: Ctx) -> Ctx:
    ctx.thumbnails = [f"{ctx.filename}_small.jpg"]
    return ctx


def save_db(ctx: Ctx) -> Ctx:
    ctx.db_id = f"id-{ctx.filename}"
    return ctx


class Pipeline:
    def __init__(self):
        self.steps: list[tuple[str, Callable]] = []

    def add(self, name: str, step: Callable) -> "Pipeline":
        self.steps.append((name, step))
        return self  # 链式构建

    def run(self, ctx: Ctx) -> Ctx:
        for name, step in self.steps:
            try:
                ctx = step(ctx)
            except Exception as exc:
                ctx.failed_step = name
                print(f"[pipeline] failed at {name}: {exc}")
                break
        return ctx


if __name__ == "__main__":
    pipe = Pipeline().add("validate", validate).add("thumbnail", thumbnail).add("save", save_db)
    ok = pipe.run(Ctx(filename="a.jpg", size_mb=2.0))
    print(ok.db_id, ok.failed_step)
    bad = pipe.run(Ctx(filename="b.jpg", size_mb=0))
    print(bad.db_id, bad.failed_step)  # 在 validate 失败
