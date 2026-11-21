"""自定义容器的迭代协议全家桶:__iter__、__len__、__contains__、__reversed__。"""


class Playlist:
    """一个只进不改的播放列表:演示容器该实现的最小迭代面。"""

    def __init__(self, title):
        self.title = title
        self._tracks = []

    def add(self, name):
        self._tracks.append(name)
        return self            # 链式添加

    def __len__(self):
        return len(self._tracks)

    def __iter__(self):
        # 每次调用返回独立生成器:多个循环互不干扰
        index = 0
        while index < len(self._tracks):
            yield self._tracks[index]
            index += 1

    def __reversed__(self):
        yield from reversed(self._tracks)

    def __contains__(self, name):
        return name in self._tracks

    def __repr__(self):
        return f"Playlist({self.title!r}, {len(self)} tracks)"


if __name__ == "__main__":
    pl = Playlist("面试歌单").add("Map").add("Filter").add("Reduce")
    print(pl)
    print("顺序:", list(pl))
    print("倒序:", list(reversed(pl)))
    print("Filter 在列表里:", "Filter" in pl)     # 走 __contains__
    print("Zip 不在列表里:", "Zip" in pl)

    it1, it2 = iter(pl), iter(pl)
    next(it1)
    print("两个独立迭代器互不干扰:", next(it1), next(it2))

    try:
        pl[0]
    except TypeError as e:
        print("未实现 __getitem__ 时的下标访问:", e)
