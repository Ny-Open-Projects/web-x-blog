"""pickle 往返与类版本演化:老字节遇到新类定义。"""
import pickle


class ProfileV1:
    def __init__(self, name):
        self.name = name


blob_v1 = pickle.dumps(ProfileV1("alice"))    # 用 V1 定义打包


class ProfileV1:                              # 同名类演进:新增字段
    default_level = 1

    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def __setstate__(self, state):
        state.setdefault("level", self.default_level)   # 旧数据补默认值
        self.__dict__.update(state)


if __name__ == "__main__":
    old = pickle.loads(blob_v1)      # 反序列化用的是「当前」的 ProfileV1
    print("老字节加载后:", old.__dict__, "| 迁移出的 level:", old.level)

    fresh = ProfileV1("bob", 3)
    back = pickle.loads(pickle.dumps(fresh))
    print("新数据往返:", back.__dict__)
    print("往返保真:", back.name == fresh.name and back.level == fresh.level)
