try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

class QualityReport:
    def __init__(self):
        self.results = []

    def check(self, name, ok, detail=""):
        self.results.append((name, ok, detail))

    def assert_all(self):
        failed = [r for r in self.results if not r[1]]
        for name, ok, detail in self.results:
            print(("PASS" if ok else "FAIL"), name, detail)
        if failed:
            raise AssertionError(f"{len(failed)} quality checks failed")

def run_checks(df, expect_min_rows=1):
    rep = QualityReport()
    rep.check("row_count", len(df) >= expect_min_rows, f"rows={len(df)}")
    rep.check("pk_unique", df["order_id"].is_unique)
    rep.check("null_rate", df["amt"].isna().mean() < 0.1,
              f"null_rate={df['amt'].isna().mean():.2%}")
    rep.check("amt_positive", (df["amt"] > 0).all())
    rep.assert_all()
    return rep

if __name__ == "__main__":
    if PANDAS:
        good = pd.DataFrame({"order_id": [1, 2], "amt": [10.0, 20.0]})
        run_checks(good)
        try:
            bad = pd.DataFrame({"order_id": [1, 1], "amt": [10.0, None]})
            run_checks(bad)
        except AssertionError as e:
            print("blocked:", e)
    else:
        rows = [(1, 10.0), (2, 20.0)]
        ids = [r[0] for r in rows]
        print("pk_unique:", len(ids) == len(set(ids)))
        print("amt_positive:", all(r[1] > 0 for r in rows))
