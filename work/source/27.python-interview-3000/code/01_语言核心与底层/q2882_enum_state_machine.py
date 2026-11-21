"""枚举驱动的状态机:事件表迁移、非法迁移防护与历史轨迹。"""
from enum import Enum


class State(Enum):
    DRAFT = "draft"
    REVIEW = "review"
    PUBLISHED = "published"
    RETIRED = "retired"


class Event(Enum):
    SUBMIT = "submit"
    APPROVE = "approve"
    RETIRE = "retire"


TRANSITIONS = {
    (State.DRAFT, Event.SUBMIT): State.REVIEW,
    (State.REVIEW, Event.APPROVE): State.PUBLISHED,
    (State.REVIEW, Event.RETIRE): State.RETIRED,
    (State.PUBLISHED, Event.RETIRE): State.RETIRED,
}


class Document:
    def __init__(self, title):
        self.title = title
        self.state = State.DRAFT
        self.history = [State.DRAFT]

    def fire(self, event):
        key = (self.state, event)
        if key not in TRANSITIONS:
            raise ValueError(f"状态 {self.state.value} 不接受事件 {event.value}")
        self.state = TRANSITIONS[key]
        self.history.append(self.state)
        return self.state


if __name__ == "__main__":
    doc = Document("设计文档")
    for ev in (Event.SUBMIT, Event.APPROVE):
        doc.fire(ev)
        print(f"事件 {ev.value:<8} -> 状态 {doc.state.value}")

    try:
        doc.fire(Event.SUBMIT)
    except ValueError as e:
        print("非法迁移被拒:", e)

    doc.fire(Event.RETIRE)
    print("完整轨迹:", " -> ".join(s.value for s in doc.history))
