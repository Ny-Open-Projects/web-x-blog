import json
import os
import tempfile

GOLDEN = os.path.join(tempfile.gettempdir(), "q1090_golden.json")

def render(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2)

def check(data, update=False):
    actual = render(data)
    if update or not os.path.exists(GOLDEN):
        with open(GOLDEN, "w", encoding="utf-8") as f:
            f.write(actual)
        return "golden 已写入/更新"
    with open(GOLDEN, encoding="utf-8") as f:
        expected = f.read()
    return "一致" if actual == expected else "不一致,请人工审查后 --update"

if __name__ == "__main__":
    print(check({"b": 1, "a": [1.0, 2.5]}))
    print(check({"b": 1, "a": [1.0, 2.5]}))
    print(check({"b": 1, "a": [1.0, 3.0]}))
    os.remove(GOLDEN)
