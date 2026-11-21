from collections import Counter, defaultdict

events = [
    ("u1", "home"), ("u1", "list"), ("u1", "item"), ("u1", "pay"),
    ("u2", "home"), ("u2", "list"), ("u2", "home"), ("u2", "list"), ("u2", "pay"),
    ("u3", "list"), ("u3", "item"),
]
by_user = defaultdict(list)
for user, page in events:
    by_user[user].append(page)

transitions = Counter()
for seq in by_user.values():
    for a, b in zip(seq, seq[1:]):
        transitions[f"{a}->{b}"] += 1

for path, cnt in transitions.most_common(5):
    print(path, cnt)
print("转移对计数即路径骨架,可直接渲染桑基图")
