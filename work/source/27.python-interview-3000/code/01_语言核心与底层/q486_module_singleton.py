import sys

import collections
import collections as collections_alias

if __name__ == "__main__":
    print("module identity stable:", collections is collections_alias)
    print("cached in sys.modules:", sys.modules["collections"] is collections)
    print("same module object for every importer — this is the singleton")

    state = {"calls": 0}              # 演示:模块级可变状态的全局性

    def get_state():
        state["calls"] += 1
        return dict(state)

    print(get_state(), get_state())
