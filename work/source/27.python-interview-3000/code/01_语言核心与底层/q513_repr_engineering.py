class Money:
    def __init__(self, cents):
        self.cents = cents

    def __repr__(self):
        return f"Money({self.cents!r})"       # eval 友好

    def __str__(self):
        return f"¥{self.cents / 100:.2f}"     # 面向用户

class Task:
    def __init__(self, name, status, deps=None):
        self.name = name
        self.status = status
        self.deps = deps or []

    def __repr__(self):
        deps = ",".join(self.deps[:3]) + ("..." if len(self.deps) > 3 else "")
        return f"Task(name={self.name!r}, status={self.status!r}, deps=[{deps}])"

if __name__ == "__main__":
    m = Money(1999)
    print(repr(m), "|", str(m))
    t = Task("build", "running", ["a", "b", "c", "d", "e"])
    print(repr(t))
    print([m, m])                             # 容器自动用 __repr__
    print(f"debug: {t!r}")
