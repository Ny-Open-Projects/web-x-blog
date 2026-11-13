#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Full-cohort triage of remaining go/java/ts files with real runtimes.

For every file in _tools/resume_queue.json, run the language runtime and record
whether it already satisfies the gate (exit 0 AND stdout contains PASS).
Output: _tools/triage_results.jsonl (append-only, resumable - existing rels skipped).

Usage:
  triage_remaining.py --workers 8            # process all pending
  triage_remaining.py --workers 8 --limit 200
"""
import argparse, json, os, re, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
TOOLS = os.path.join(BASE, "_tools")
GO = "/usr/local/go1.26.5/bin/go"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"
OUT = os.path.join(TOOLS, "triage_results.jsonl")

ENV = dict(os.environ)
ENV["GO111MODULE"] = "off"
ENV["GOCACHE"] = os.path.join(tempfile.gettempdir(), "dsa_gocache")
os.makedirs(ENV["GOCACHE"], exist_ok=True)

TOPCLASS = re.compile(r"^(?:public\s+)?(?:final\s+|abstract\s+)?class\s+(\w+)", re.M)


def done_rels():
    out = set()
    if not os.path.exists(OUT):
        return out
    dec = json.JSONDecoder()
    for line in open(OUT, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        i = 0
        while i < len(line):
            try:
                o, e = dec.raw_decode(line, i)
                if isinstance(o, dict) and o.get("rel"):
                    out.add(o["rel"])
                i = e
            except Exception:
                break
    return out


def java_main_class(src):
    m = TOPCLASS.search(src)
    return "com.webfault.dsa." + (m.group(1) if m else "Main")


def verify(rel, idx):
    """Return (status, detail). status: pass | broken | missing"""
    path = os.path.join(BASE, rel)
    if not os.path.exists(path):
        return "missing", "file not found"

    if rel.endswith(".go"):
        cmd, timeout = [GO, "run", path], 90
    elif rel.endswith(".java"):
        d = os.path.join(tempfile.gettempdir(), "dsa_jout_%d" % idx)
        os.makedirs(d, exist_ok=True)
        try:
            c = subprocess.run([JAVAC, "-d", d, path], capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            return "broken", "javac timeout"
        if c.returncode != 0:
            return "broken", "javac: " + ((c.stderr or c.stdout).strip().replace("\n", " ")[:200])
        cls = java_main_class(open(path, encoding="utf-8", errors="replace").read())
        cmd, timeout = [JAVA, "-cp", d, cls], 90
    elif rel.endswith(".ts"):
        cmd, timeout = [NODE, "--experimental-strip-types", path], 60
    else:
        return "broken", "unknown extension"

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=ENV)
    except subprocess.TimeoutExpired:
        return "broken", "timeout"
    if r.returncode == 0 and "PASS" in (r.stdout or ""):
        return "pass", "already passing gate"
    tail = ((r.stdout or "") + " | " + (r.stderr or "")).strip().replace("\n", " ")
    return "broken", "rc=%d %s" % (r.returncode, tail[-160:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    queue = json.load(open(os.path.join(TOOLS, "resume_queue.json"), encoding="utf-8"))
    already = done_rels()
    pending = [e["rel"] for e in queue if e["rel"] not in already]
    if args.limit:
        pending = pending[: args.limit]
    print("queue=%d already_triaged=%d pending=%d" % (len(queue), len(already), len(pending)), flush=True)
    if not pending:
        print("nothing to do")
        return

    counts = {"pass": 0, "broken": 0, "missing": 0}
    with open(OUT, "a", encoding="utf-8") as out:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(verify, rel, i): rel for i, rel in enumerate(pending)}
            done_n = 0
            for fut in as_completed(futs):
                rel = futs[fut]
                try:
                    status, detail = fut.result()
                except Exception as exc:
                    status, detail = "broken", "triage exception: %s" % exc
                counts[status] = counts.get(status, 0) + 1
                out.write(json.dumps({"rel": rel, "status": status, "note": detail[:300]}, ensure_ascii=False) + "\n")
                out.flush()
                done_n += 1
                if done_n % 100 == 0:
                    print("  ...%d/%d %s" % (done_n, len(pending), counts), flush=True)
    print("TRIAGE DONE:", counts, flush=True)


if __name__ == "__main__":
    main()
