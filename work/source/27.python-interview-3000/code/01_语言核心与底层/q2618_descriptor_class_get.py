"""类访问描述符:instance 为 None、owner 为类时分派的两种姿势。"""


class Versioned:
    """实例访问返回值,类访问返回描述符自身便于内省。"""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            print(f"    [类访问] owner={owner.__name__}, 返回自身")
            return self
        print(f"    [实例访问] owner={owner.__name__}, 返回存储值")
        return instance.__dict__.get(self.name, "未设置")

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Service:
    version = Versioned()


if __name__ == "__main__":
    print("类访问:")
    desc = Service.version                # instance=None 分支
    print("    拿到:", type(desc).__name__)

    print("实例访问:")
    svc = Service()
    svc.version = "2.1"
    print("    拿到:", svc.version)

    print("property 的类访问返回 property 对象本身:")
    print("    ", type(Service.__dict__.get("version", None)) is Versioned)
