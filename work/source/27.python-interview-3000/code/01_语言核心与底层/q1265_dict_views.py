if __name__ == "__main__":
    d = {"a": 1, "b": 2}
    keys, items = d.keys(), d.items()
    print("len before:", len(keys))
    d["c"] = 3                        # 视图动态跟随
    print("len after :", len(keys), "| 'c' in keys:", "c" in keys)
    print("set op keys & {a,z}:", keys & {"a", "z"})
    d["b"] = 20
    print("items reflect updates:", sorted(items))
    snapshot = list(items)            # 需要隔离时才拷贝
    d["d"] = 4
    print("snapshot stays:", len(snapshot), "| live now:", len(items))
