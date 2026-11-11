#!/usr/bin/env python3
"""After triage, build per-chunk remediation task files for the FAILING batches5 rels.
Each task file embeds: rel, lang, python reference source, and trusted oracle cases
(if available) so the remediation sub-agent can translate faithfully without re-deriving.

Writes _tools/remediation_tasks/chunk_NN_eE.json  (one per remediation chunk)
and prints a summary.
"""
import json, os, re, sys

TOOLS = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/_tools"
BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
sys.path.insert(0, TOOLS)
import correctness_check as cc

# ---- build oracle map: lc_num -> {"cases":[{args,want}], "sort":bool} ----
import inspect
oracle = {}
for P in cc.PROBLEMS:
    m = re.search(r"lc_(\d+)", P["dir"])
    if not m:
        continue
    num = m.group(1)
    try:
        arity = len(inspect.signature(P["ref"]).parameters)
    except Exception:
        arity = 1
    cases = []
    for c in P["cases"]:
        if not isinstance(c, (list, tuple)):
            continue
        if len(c) == 2:
            args, want = c[0], c[1]
        elif len(c) == arity + 1:
            args, want = tuple(c[:arity]), c[arity]
        else:
            continue  # malformed, skip
        cases.append({"args": args, "want": want})
    if cases:
        oracle[num] = {"cases": cases, "sort": bool(P.get("sort", False))}

# ---- load triage bad rels ----
res = json.load(open("/tmp/triage_b5_result.json", encoding="utf-8"))
bad = res["bad"]  # [[rel, reason], ...]
rels = [b[0] for b in bad]
reason_map = {b[0]: b[1] for b in bad}
print(f"loaded {len(rels)} failing rels from triage")

# ---- map rel -> e-file batch ----
rel2efile = {}
for i in range(1, 200):
    bf = os.path.join(TOOLS, "resume_batches5", f"e{i}.json")
    if not os.path.exists(bf):
        continue
    d = json.load(open(bf, encoding="utf-8"))
    for p in d.get("problems", []):
        for t in p.get("targets", []):
            rel2efile.setdefault(t["rel"], i)

# ---- flatten all bad rels, chunk into ~80 per remediation sub-agent ----
all_rels = sorted(set(rels))
CHUNK = 80
chunks = [all_rels[i:i + CHUNK] for i in range(0, len(all_rels), CHUNK)]


def py_ref_of(rel):
    if rel.split("/")[0] in ("go", "java", "ts"):
        r = re.sub(r"^(go|java|ts)/", "python/", rel)
        r = re.sub(r"\.(go|java|ts)$", ".py", r)
        return r
    return None


os.makedirs(os.path.join(TOOLS, "remediation_tasks"), exist_ok=True)
task_files = []
for idx, chunk in enumerate(chunks):
    specs = []
    for rel in chunk:
        parts = rel.split("/")
        lang = parts[0]
        topic = parts[1] if len(parts) > 1 else ""
        dirname = parts[2] if len(parts) > 2 else ""
        m = re.search(r"lc_(\d+)", dirname)
        num = m.group(1) if m else None
        py_ref = py_ref_of(rel)
        o = oracle.get(num) if num else None
        specs.append({
            "rel": rel, "lang": lang, "topic": topic, "dir": dirname,
            "lc": num, "python_ref": py_ref,
            "oracle": o, "current_reason": reason_map.get(rel),
        })
    tf = os.path.join(TOOLS, "remediation_tasks", f"chunk_{idx:02d}.json")
    json.dump({"chunk": idx, "specs": specs},
              open(tf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    task_files.append(tf)

print(f"total bad rels: {len(all_rels)}")
print(f"total chunks (sub-agent tasks): {len(chunks)}")
for idx, chunk in enumerate(chunks):
    print(f"  chunk {idx:02d}: {len(chunk)} rels")
print("wrote task files to _tools/remediation_tasks/")
