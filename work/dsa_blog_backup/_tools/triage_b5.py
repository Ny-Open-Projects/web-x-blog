#!/usr/bin/env python3
"""Triage the current batches5 queue (1212 rels): re-verify each file with the
REAL runtime, in parallel (local CPU only — no LLM quota, safe vs 429).

Outputs:
  /tmp/triage_b5_result.json   -> {"ok":[rels], "bad":[[rel,reason],...]}
  _tools/resume_progress_rB5.json (JSONL) -> ok rels marked done_pass, bad rels marked fail
"""
import json, os, sys, glob, re, subprocess, shutil, tempfile
from multiprocessing import Pool

BASE = "/Users/Wang/Code/webfault-ai/dsa"
TOOLS = os.path.join(BASE, "_tools")
GO = "/usr/local/go1.26.5/bin/go"
JAVAC = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
JAVA = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"

def java_main_class(src):
    matches = list(re.finditer(r'^(?:public\s+|final\s+|abstract\s+)*class\s+(\w+)', src, re.M))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(src)
        if "static void main" in src[start:end]:
            return m.group(1)
    return None

def verify(rel):
    abs_path = os.path.join(BASE, rel)
    if not os.path.exists(abs_path):
        return (rel, False, "missing file")
    try:
        if rel.endswith(".go"):
            cmd = ["env", "GO111MODULE=off", GO, "run", abs_path]
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            except subprocess.TimeoutExpired:
                return (rel, False, "timeout")
            if r.returncode == 0 and "PASS" in (r.stdout or ""):
                return (rel, True, "ok")
            return (rel, False, f"rc={r.returncode} out={((r.stdout or '') + (r.stderr or ''))[-200:]}")
        elif rel.endswith(".java"):
            jout = tempfile.mkdtemp(prefix="jout_")
            try:
                r = subprocess.run([JAVAC, "-d", jout, abs_path], capture_output=True, text=True, timeout=240)
                if r.returncode != 0:
                    return (rel, False, "javac: " + (r.stderr or r.stdout)[-300:])
                src = open(abs_path, encoding="utf-8").read()
                cls = java_main_class(src)
                if not cls:
                    return (rel, False, "no top-level main class found")
                r = subprocess.run([JAVA, "-cp", jout, "com.webfault.dsa." + cls],
                                   capture_output=True, text=True, timeout=180)
            finally:
                shutil.rmtree(jout, ignore_errors=True)
            if r.returncode == 0 and "PASS" in (r.stdout or ""):
                return (rel, True, "ok")
            return (rel, False, f"rc={r.returncode} out={((r.stdout or '') + (r.stderr or ''))[-200:]}")
        elif rel.endswith(".ts"):
            cmd = [NODE, "--experimental-strip-types", abs_path]
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            except subprocess.TimeoutExpired:
                return (rel, False, "timeout")
            if r.returncode == 0 and "PASS" in (r.stdout or ""):
                return (rel, True, "ok")
            return (rel, False, f"rc={r.returncode} out={((r.stdout or '') + (r.stderr or ''))[-200:]}")
        else:
            return (rel, False, "unknown ext")
    except Exception as e:
        return (rel, False, f"exception: {e}")

def collect_b5_rels():
    rels = []
    for i in range(1, 200):
        bf = os.path.join(TOOLS, "resume_batches5", f"e{i}.json")
        if os.path.exists(bf):
            d = json.load(open(bf, encoding="utf-8"))
            for p in d.get("problems", []):
                for t in p.get("targets", []):
                    rels.append(t["rel"])
    return rels

def main():
    rels = collect_b5_rels()
    rels = sorted(set(rels))
    print(f"collected {len(rels)} unique batches5 rels -> triaging with real runtimes (parallel)", flush=True)
    with Pool(8) as pool:
        results = pool.map(verify, rels)
    ok = [rel for rel, good, _ in results if good]
    bad = [[rel, msg] for rel, good, msg in results if not good]
    print(f"TRIAGE DONE: total={len(results)} ok={len(ok)} bad={len(bad)}", flush=True)
    out = {"ok": ok, "bad": bad}
    with open("/tmp/triage_b5_result.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    # write JSONL progress for merge
    with open(os.path.join(TOOLS, "resume_progress_rB5.json"), "w", encoding="utf-8") as f:
        for rel in ok:
            f.write(json.dumps({"rel": rel, "status": "done_pass", "note": "triage reverified"}, ensure_ascii=False) + "\n")
        for rel, msg in bad:
            f.write(json.dumps({"rel": rel, "status": "fail", "note": msg}, ensure_ascii=False) + "\n")
    print(f"wrote /tmp/triage_b5_result.json and _tools/resume_progress_rB5.json", flush=True)
    # show first 40 bad
    for rel, msg in bad[:40]:
        print(f"  BAD: {rel} :: {msg}")

if __name__ == "__main__":
    main()
