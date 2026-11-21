"""异常安全的资源注册表:注册即事务,任一步失败整体回滚。"""


class Registry:
    """资源注册表:register 里的每一步都成功才生效,否则回滚到快照。"""

    def __init__(self):
        self._items = {}          # name -> 资源描述
        self._hooks = []          # name -> 附加副作用记录

    def register(self, name, resource, validate):
        snapshot = (dict(self._items), list(self._hooks))   # 浅快照:容器历史不被原地改写
        try:
            if name in self._items:
                raise KeyError(f"重复注册:{name}")
            validate(name, resource)          # 第一步:校验,可能抛异常
            self._items[name] = resource      # 第二步:入表
            if resource.startswith("net:"):   # 第三步:附加副作用,模拟可能失败
                self._hooks.append((name, "keepalive"))
            if name == "bad":                 # 模拟第三步失败
                raise RuntimeError("副作用阶段失败")
        except BaseException:
            self._items, self._hooks = snapshot
            raise
        return self

    def __repr__(self):
        return f"Registry(items={sorted(self._items)}, hooks={self._hooks})"


def validate_nonempty(name, resource):
    if not name:
        raise ValueError("名字不能为空")
    if not isinstance(resource, str) or not resource:
        raise ValueError("资源必须是非空字符串")


if __name__ == "__main__":
    reg = Registry()
    reg.register("db", "sqlite:mem", validate_nonempty)
    reg.register("net", "net:host", validate_nonempty)
    print("两次成功后:", reg)

    try:
        reg.register("db", "mysql:xx", validate_nonempty)   # 重复注册
    except KeyError as e:
        print("重复注册被拒:", e)

    try:
        reg.register("bad", "net:x", validate_nonempty)     # 第三步失败
    except RuntimeError as e:
        print("副作用失败被拒:", e)

    try:
        reg.register("", "", validate_nonempty)             # 校验失败
    except ValueError as e:
        print("校验失败被拒:", e)

    print("所有失败后注册表保持一致:", reg)
