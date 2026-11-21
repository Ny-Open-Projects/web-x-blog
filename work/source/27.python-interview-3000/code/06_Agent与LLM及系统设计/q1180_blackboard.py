"""黑板模式:共享工作区 + 槽位认领 + 专家循环感知-行动。"""
import threading


class Blackboard:
    def __init__(self):
        self.slots = {}                       # slot -> {"status": open/claimed/done, "owner", "value"}
        self.lock = threading.Lock()

    def register(self, slot):
        self.slots[slot] = {"status": "open", "owner": None, "value": None}

    def claim(self, slot, agent):
        with self.lock:
            s = self.slots[slot]
            if s["status"] == "open":
                s.update(status="claimed", owner=agent)
                return True
            return False

    def write(self, slot, agent, value):
        with self.lock:
            s = self.slots[slot]
            if s["status"] != "claimed" or s["owner"] != agent:
                raise PermissionError(f"{slot} 未被 {agent} 认领")
            s.update(status="done", value=value)

    def open_slots(self):
        return [k for k, v in self.slots.items() if v["status"] == "open"]


class Specialist:
    def __init__(self, name, skill, board):
        self.name, self.skill, self.board = name, skill, board

    def act(self):
        for slot in self.board.open_slots():
            if self.skill in slot:
                if self.board.claim(slot, self.name):
                    self.board.write(slot, self.name, f"{self.name} 完成 {slot}")
                    return slot
        return None


if __name__ == "__main__":
    board = Blackboard()
    for s in ["数据收集区", "数据分析区", "图表制作区", "文案撰写区"]:
        board.register(s)
    agents = [Specialist("数据组", "数据", board), Specialist("可视化组", "图表", board),
              Specialist("写作组", "文案", board)]
    rounds = 0
    while board.open_slots() and rounds < 10:
        rounds += 1
        for a in agents:
            a.act()
    for k, v in board.slots.items():
        print(f"  {k}: {v['status']} by {v['owner']} -> {v['value']}")
    assert all(v["status"] == "done" for v in board.slots.values()), "全部槽位应被完成"
    assert board.claim("数据收集区", "写作组") is False, "已完成槽位不可再认领"
    print(f"黑板协作完成,共 {rounds} 轮,认领互斥生效")
