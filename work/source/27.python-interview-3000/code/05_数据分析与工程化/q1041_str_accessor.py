try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    import re
    codes = ["AB-001", "CD-02", None, "EF-3x"]
    pat = re.compile(r"([A-Z]+)-(\d+)")
    for c in codes:
        m = pat.match(c) if c else None
        print(c, "->", (m.group(1), m.group(2)) if m else None)
else:
    df = pd.DataFrame({"code": ["AB-001", "CD-02", None, "EF-3x"]})
    parsed = df["code"].str.extract(r"([A-Z]+)-(\d+)")
    parsed.columns = ["prefix", "num"]
    print(parsed, end="\n\n")
    print("包含连字符:", df["code"].str.contains("-", regex=False).tolist())
    print("长度:", df["code"].str.len().tolist())
    print("补零到 6 位:", df["code"].str.split("-").str[-1].str.zfill(5).tolist())
