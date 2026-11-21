try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    facts = [("u1", "01-01", 100), ("u1", "01-02", 200)]
    dims = [("u1", "01-01", "vip")]
    for f in facts:
        match = [d for d in dims if d[0] == f[0] and d[1] == f[1]]
        print(f, "->", match[0] if match else None)
else:
    facts = pd.DataFrame({
        "user_id": ["u1", "u1", "u2"],
        "dt": ["01-01", "01-02", "01-01"],
        "amount": [100, 200, 50],
        "level": ["tmp", "tmp", "tmp"],
    })
    dims = pd.DataFrame({
        "user_id": ["u1", "u1", "u2"],
        "dt": ["01-01", "01-02", "01-01"],
        "level": ["vip", "normal", "normal"],
    })
    m = facts.drop(columns=["level"]).merge(
        dims, on=["user_id", "dt"], validate="1:1", suffixes=("_fact", "_dim")
    )
    print(m)
