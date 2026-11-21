import json
import uuid
from datetime import datetime, timezone

REQUIRED_PUBLIC = ["event_id", "user_id", "event_name", "client_ts", "server_ts"]

def build_event(user_id, event_name, props):
    now = datetime.now(timezone.utc).isoformat()
    return {
        "event_id": str(uuid.uuid4()),     # 唯一 ID,服务端去重依据
        "user_id": user_id,
        "event_name": event_name,
        "client_ts": props.get("client_ts", now),
        "server_ts": now,                  # 服务端时间为准
        "props": props,                    # schema 校验后入库
    }

def validate(ev):
    missing = [k for k in REQUIRED_PUBLIC if not ev.get(k)]
    return not missing, missing

if __name__ == "__main__":
    ev = build_event("u1", "page_view",
                     {"page": "home", "client_ts": "2026-11-01T10:00:00+08:00"})
    ok, missing = validate(ev)
    assert ok
    print(json.dumps(ev, ensure_ascii=False, indent=2))
