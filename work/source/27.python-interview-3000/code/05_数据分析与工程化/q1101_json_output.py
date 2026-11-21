import json
import sys

def collect():
    return [
        {"name": "api", "p95_ms": 120, "error_rate": 0.002},
        {"name": "worker", "p95_ms": 300, "error_rate": 0.0},
    ]

def main(argv):
    data = collect()
    if "--json" in argv:
        json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return 0
    print(f"{'服务':<8}{'p95':>8}{'错误率':>10}")
    for row in data:
        print(f"{row['name']:<8}{row['p95_ms']:>8}{row['error_rate']:>10.3%}")
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
    print("提示:追加 --json 查看机器可读输出;日志应走 stderr 保持 stdout 纯净")
