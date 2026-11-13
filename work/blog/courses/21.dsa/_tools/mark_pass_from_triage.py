#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Leader-side: mark files that ALREADY pass the gate (per triage_results.jsonl)
as done_pass in the canonical scale_progress_chunk<N>.json.

Only rels present in triage with status == 'pass' are recorded; anything else is
left for agents. Safe to re-run: existing canonical done_pass rels are skipped.
"""
import json, os, collections

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa"
TOOLS = os.path.join(BASE, "_tools")

def parse_jsonl(p):
    recs = []
    if not os.path.exists(p):
        return recs
    dec = json.JSONDecoder()
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        i = 0
        while i < len(line):
            try:
                o, e = dec.raw_decode(line, i)
                recs.append(o); i = e
            except Exception:
                break
    return recs

chunks = json.load(open(os.path.join(TOOLS, "scale_chunks.json"), encoding="utf-8"))["chunks"]
rel2chunk = {}
for i, ch in enumerate(chunks):
    for rel in ch:
        rel2chunk[rel] = i

canon_done = set()
for i in range(6):
    for r in parse_jsonl(os.path.join(TOOLS, "scale_progress_chunk%d.json" % i)):
        if r.get("rel") and r.get("status") in ("done_pass", "skip"):
            canon_done.add(r["rel"])

added = collections.Counter()
skipped_unknown = []
for r in parse_jsonl(os.path.join(TOOLS, "triage_results.jsonl")):
    rel = r.get("rel")
    if r.get("status") != "pass" or not rel or rel in canon_done:
        continue
    if rel not in rel2chunk:
        skipped_unknown.append(rel)
        continue
    i = rel2chunk[rel]
    with open(os.path.join(TOOLS, "scale_progress_chunk%d.json" % i), "a", encoding="utf-8") as f:
        f.write(json.dumps({"rel": rel, "status": "done_pass",
                            "note": "leader triage: real-runtime gate rc=0 + stdout PASS"}, ensure_ascii=False) + "\n")
    canon_done.add(rel)
    added[i] += 1

print("added by chunk:", dict(added), "total:", sum(added.values()))
if skipped_unknown:
    print("WARN not in any chunk:", len(skipped_unknown), skipped_unknown[:5])
