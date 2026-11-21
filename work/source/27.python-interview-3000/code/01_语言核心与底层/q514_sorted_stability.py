rows = [
    {"dept": "sales", "name": "Carol", "score": 88},
    {"dept": "dev", "name": "Alice", "score": 92},
    {"dept": "dev", "name": "Bob", "score": 88},
    {"dept": "sales", "name": "Dave", "score": 92},
]

if __name__ == "__main__":
    # 多级排序:先按分数,再按部门(稳定性保留分数序)
    by_score = sorted(rows, key=lambda r: -r["score"])
    result = sorted(by_score, key=lambda r: r["dept"])
    for r in result:
        print(r)

    print("---")
    # 等价的单次复合 key
    result2 = sorted(rows, key=lambda r: (r["dept"], -r["score"]))
    print("two-pass equals composite key:", result == result2)
