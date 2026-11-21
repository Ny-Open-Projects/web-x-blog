from collections import defaultdict

first_purchase = {"u1": "2026-01", "u2": "2026-01", "u3": "2026-02"}
active_months = defaultdict(set)
active_months["u1"] = {"2026-01", "2026-02", "2026-03"}
active_months["u2"] = {"2026-01", "2026-03"}
active_months["u3"] = {"2026-02", "2026-03"}

def offset(a, b):
    ya, ma = int(a[:4]), int(a[5:])
    yb, mb = int(b[:4]), int(b[5:])
    return (yb - ya) * 12 + (mb - ma)

cohort_size = defaultdict(int)
matrix = defaultdict(lambda: defaultdict(int))
for user, c in first_purchase.items():
    cohort_size[c] += 1
    for m in active_months[user]:
        matrix[c][offset(c, m)] += 1

months = sorted(cohort_size)
print("cohort  人数  M0    M1    M2")
for c in months:
    row = [f"{matrix[c][k] / cohort_size[c]:.0%}" if matrix[c][k] else "-" for k in range(3)]
    print(f"{c}  {cohort_size[c]:>4}  " + "  ".join(f"{x:>4}" for x in row))
