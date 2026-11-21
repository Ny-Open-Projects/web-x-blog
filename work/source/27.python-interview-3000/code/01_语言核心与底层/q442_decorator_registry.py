HANDLERS = {}

def register(event_type):
    def deco(func):
        if event_type in HANDLERS:
            raise ValueError(f"duplicate handler for {event_type}")
        HANDLERS[event_type] = func
        return func                   # 返回原函数:不改变调用方式
    return deco

@register("user.created")
def on_user_created(payload):
    return f"welcome {payload['name']}"

@register("user.deleted")
def on_user_deleted(payload):
    return f"bye {payload['name']}"

def dispatch(event_type, payload):
    return HANDLERS[event_type](payload)

if __name__ == "__main__":
    print(dispatch("user.created", {"name": "Alice"}))
    print(dispatch("user.deleted", {"name": "Bob"}))
    print("registry keys:", sorted(HANDLERS))
