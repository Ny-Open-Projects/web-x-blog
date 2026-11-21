"""JSON vs 精简 DTO 的 value 大小对比"""
import json

def big_dto(user):
    return {**user, "orders": [f"order{i}" for i in range(200)],
            "logs": [f"log{i}" for i in range(100)]}

def slim_dto(user):
    return {"id": user["id"], "name": user["name"]}

if __name__ == "__main__":
    user = {"id": 1, "name": "alice", "phone": "138...", "_internal": "xx"}
    b = json.dumps(big_dto(user)).encode()
    s = json.dumps(slim_dto(user)).encode()
    print(f"全量 dump: {len(b)} bytes")
    print(f"精简 DTO: {len(s)} bytes, 节省 {1 - len(s) / len(b):.0%}")
    print("规范: value < 100KB 优先; 1MB+ 拆分; 二进制协议可再省 30~50%")
