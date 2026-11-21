import gc


class Node:
    def __init__(self, name):
        self.name = name
        self.peer = None

    def __del__(self):
        # 危险示范:peer 可能已终结,getattr 兜底只是防炸不是防错
        peer_name = getattr(self.peer, "name", "<gone>")
        print("__del__ of", self.name, "sees peer as", peer_name)


if __name__ == "__main__":
    a, b = Node("a"), Node("b")
    a.peer, b.peer = b, a               # 循环引用
    del a, b
    gc.collect()
    print("gc.garbage:", gc.garbage, "<- PEP 442 后循环垃圾不滞留")
