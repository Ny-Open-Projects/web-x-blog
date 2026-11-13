#!/usr/bin/env python3
"""Merge per-agent resume progress (JSONL) into canonical scale_progress_chunk<N>.json.

Usage: merge_resume_progress.py [--dry-run]
- Reads _tools/resume_progress_r*.json (one JSON obj per line)
- Maps each rel -> its chunk via _tools/scale_chunks.json
- Merges into _tools/scale_progress_chunk<N>.json (dedupe by rel; later record wins;
  done_pass/skip beat fail)
- Prints summary
"""
import json, os, sys, glob, collections

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
TOOLS = os.path.join(BASE, "_tools")

def parse_jsonl(path):
    recs = []
    dec = json.JSONDecoder()
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        idx = 0
        while idx < len(line):
            try:
                obj, end = dec.raw_decode(line, idx)
                recs.append(obj); idx = end
            except Exception:
                break
    return recs

def main():
    dry = "--dry-run" in sys.argv
    chunks = json.load(open(os.path.join(TOOLS, "scale_chunks.json")))["chunks"]
    rel2chunk = {}
    for i, ch in enumerate(chunks):
        for rel in ch:
            rel2chunk[rel] = i

    # existing canonical records per chunk
    canon = {i: {} for i in range(6)}
    for i in range(6):
        p = os.path.join(TOOLS, f"scale_progress_chunk{i}.json")
        if os.path.exists(p):
            for r in parse_jsonl(p):
                rel = r.get("rel")
                if rel:
                    canon[i][rel] = r

    new_recs = []
    for p in sorted(glob.glob(os.path.join(TOOLS, "resume_progress_r*.json"))):
        for r in parse_jsonl(p):
            if r.get("rel"):
                new_recs.append(r)

    merged = collections.Counter()
    unknown = []
    for r in new_recs:
        rel = r["rel"]
        if rel not in rel2chunk:
            unknown.append(rel); continue
        i = rel2chunk[rel]
        old = canon[i].get(rel)
        # priority: done_pass/skip > fail; within same status, later record wins
        rank = {"done_pass": 3, "skip": 3, "fail": 1}
        if old is None or rank.get(r.get("status"), 0) >= rank.get(old.get("status"), 0):
            canon[i][rel] = r
        merged[r.get("status")] += 1

    if not dry:
        for i in range(6):
            p = os.path.join(TOOLS, f"scale_progress_chunk{i}.json")
            with open(p, "w", encoding="utf-8") as f:
                for rel, r in canon[i].items():
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("new records ingested:", dict(merged), "total:", len(new_recs))
    if unknown:
        print("WARN unknown rels (not in any chunk):", len(unknown))
        for u in unknown[:10]:
            print("  ", u)
    for i in range(6):
        cnt = collections.Counter(r.get("status") for r in canon[i].values())
        print(f"chunk{i}: {dict(cnt)} total={len(canon[i])}")
    tot_done = sum(1 for i in range(6) for r in canon[i].values() if r.get("status") in ("done_pass", "skip"))
    print("CANONICAL done_pass+skip total:", tot_done)

if __name__ == "__main__":
    main()
