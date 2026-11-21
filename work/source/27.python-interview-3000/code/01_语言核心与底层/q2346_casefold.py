"""casefold 与 lower:大小写折叠的边界差异与查表惯例。"""

if __name__ == "__main__":
    samples = ["HELLO", "Straße", "ΣΊΣΥΦΟΣ", "İstanbul"]
    for s in samples:
        print(f"{s!r:>12} lower={s.lower()!r} casefold={s.casefold()!r}")

    print("ß 折叠一致:", "straße".casefold() == "strasse".casefold())
    print("lower 会漏判:", "straße".lower() == "strasse".lower())

    known = {"strasse": "德国公路"}
    query = "STRASSE"
    print("casefold 查表:", known.get(query.casefold()))
