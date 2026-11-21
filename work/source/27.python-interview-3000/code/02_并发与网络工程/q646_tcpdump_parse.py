import re

SAMPLE = """
12:00:00.000001 IP 10.0.0.1.54321 > 10.0.0.2.8080: Flags [S], seq 1000, win 65535
12:00:00.000090 IP 10.0.0.2.8080 > 10.0.0.1.54321: Flags [S.], seq 5000, ack 1001, win 65535
12:00:00.000120 IP 10.0.0.1.54321 > 10.0.0.2.8080: Flags [.], ack 5001, win 65535
12:00:00.000200 IP 10.0.0.1.54321 > 10.0.0.2.8080: Flags [P.], seq 1001:1101, ack 5001
12:00:00.000500 IP 10.0.0.2.8080 > 10.0.0.1.54321: Flags [P.], seq 5001:5100, ack 1101
12:00:00.005000 IP 10.0.0.2.8080 > 10.0.0.1.54321: Flags [P.], seq 5001:5100, ack 1101
12:00:00.005100 IP 10.0.0.1.54321 > 10.0.0.2.8080: Flags [.], ack 5101, win 65535
"""

LINE = re.compile(
    r"(?P<ts>\d+:\d+:\d+\.\d+)\s+IP\s+(?P<src>[\d.]+)\.(?P<sport>\d+)\s+>\s+"
    r"(?P<dst>[\d.]+)\.(?P<dport>\d+):\s+Flags\s+\[(?P<flags>[^\]]+)\]"
    r"(?:, seq (?P<seq>[\d:]+))?(?:, ack (?P<ack>\d+))?"
)


def parse(text: str) -> list:
    events = []
    for line in text.strip().splitlines():
        m = LINE.search(line)
        if not m:
            continue
        ts = m.group("ts")
        h, mi, rest = ts.split(":")
        sec, frac = rest.split(".")
        t = int(h) * 3600 + int(mi) * 60 + int(sec) + int(frac) / 1e6
        events.append({
            "t": t, "dir": "C>S" if m.group("sport") == "54321" else "S>C",
            "flags": m.group("flags"), "seq": m.group("seq"),
        })
    return events


def analyze(events: list) -> None:
    syn = next(e for e in events if e["flags"] == "S")
    synack = next(e for e in events if e["flags"] == "S.")
    print(f"建连耗时: {(synack['t'] - syn['t']) * 1000:.1f}ms (SYN→SYN-ACK)")

    seen: dict = {}
    for e in events:
        if e["flags"].startswith("P") and e["seq"]:
            start = e["seq"].split(":")[0]
            if start in seen:
                print(f"发现重传: seq {e['seq']} 首见于 {seen[start] - events[0]['t']:.6f}s "
                      f"重发于 {e['t'] - events[0]['t']:.6f}s")
            else:
                seen[start] = e["t"] if isinstance(e["t"], float) else seen.get(start, e["t"])
    # 简化: 直接对比相同 seq 区间
    seqs = [e["seq"] for e in events if e["seq"] and ":" in e["seq"]]
    dup = {s for s in seqs if seqs.count(s) > 1}
    if dup:
        print(f"重复 seq 区间: {dup} → 存在重传, 结合 RTT 判断丢包率")

    flags_flow = " → ".join(e["flags"] for e in events)
    print("标志流:", flags_flow)


if __name__ == "__main__":
    events = parse(SAMPLE)
    analyze(events)
