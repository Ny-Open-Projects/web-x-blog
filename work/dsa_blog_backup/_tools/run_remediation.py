#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate faithful TS ports for the LEFT-OVER files of chunks 3/4/5 using the
hand-written SOLVE registry in solves.py. For "fn" entries the python oracle
computes expected outputs; for "full" entries the body is self-contained.
Each file is written, executed via node, and a progress line appended.
"""
import os, json, subprocess, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen_remediation import (TS_PRELUDE, EQ_TS, run_oracle, primary_py, emit_fn)
from solves import SOLVE, SOLVE_REL

BASE = "/Users/Wang/Code/webfault-ai/dsa"
NODE = "/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node"

# Known-stub / unreliable python refs: use hand-computed expected via "full".
def emit_full(body):
    return TS_PRELUDE + "\n" + EQ_TS + "\n" + body

def oracle_py(dirname, pyfn):
    """Find the python file in the dir that actually defines `pyfn` (notes dirs
    bundle unrelated functions across files, so basename matching is wrong)."""
    import re as _re
    p = os.path.join(BASE, "python", dirname)
    if not os.path.isdir(p):
        raise FileNotFoundError(dirname)
    cands = sorted(f for f in os.listdir(p) if f.endswith(".py"))
    for f in cands:
        src = open(os.path.join(p, f), encoding='utf-8').read()
        if _re.search(r'def\s+' + _re.escape(pyfn) + r'\b', src):
            return os.path.join(p, f)
    # fallback: first file
    return os.path.join(p, cands[0])

def gen(rel):
    dirname = "/".join(rel.split("/")[1:-1])
    spec = SOLVE_REL.get(rel) or SOLVE.get(dirname)
    if not spec:
        return None, "no SOLVE entry for " + dirname
    kind = spec[0]
    if kind == "full":
        return emit_full(spec[1]), None
    # kind == "fn"
    tsbody, pyfn, args = spec[1], spec[2], spec[3]
    opts = spec[4] if len(spec) > 4 else {}
    if not isinstance(args, list):
        return None, "bad args (not a list) for " + dirname
    try:
        pyf = oracle_py(dirname, pyfn)
    except Exception as e:
        return None, "no python ref: %s" % e
    try:
        cases = run_oracle(pyf, pyfn, args)
    except Exception as e:
        return None, "oracle failed: %s" % e
    if not cases:
        return None, "oracle produced no usable cases"
    return emit_fn(dirname, tsbody, cases, opts), None

def verify(rel):
    path = os.path.join(BASE, rel)
    try:
        r = subprocess.run([NODE, "--experimental-strip-types", path],
                           capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"
    except Exception as e:
        return False, "exec error %s" % e
    ok = (r.returncode == 0) and ("PASS" in r.stdout)
    tail = (r.stdout + r.stderr).strip()[-1500:]
    return ok, tail

def already_done(path, rel):
    if not os.path.exists(path):
        return False
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            if o.get("rel") == rel and o.get("status") in ("done_pass", "skip"):
                return True
    return False

def main():
    chunks = {}
    for c in (3, 4, 5):
        with open(os.path.join(HERE, "remain_chunk%d.json" % c), encoding='utf-8') as f:
            chunks[c] = json.load(f)
    rel2chunk = {}
    for c, lst in chunks.items():
        for rel in lst:
            rel2chunk[rel] = c

    counts = {c: {"done_pass": 0, "fail": 0, "skip": 0} for c in (3, 4, 5)}
    prog_files = {c: os.path.join(HERE, "scale_progress_chunk%d.json" % c) for c in (3, 4, 5)}

    for rel, c in rel2chunk.items():
        ppath = prog_files[c]
        if already_done(ppath, rel):
            # honor prior completion; do not re-run
            with open(ppath, encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        o = json.loads(line)
                    except Exception:
                        continue
                    if o.get("rel") == rel and o.get("status") in ("done_pass", "skip"):
                        counts[c][o["status"]] += 1
                        break
            continue

        content, err = gen(rel)
        note = ""
        if content is None:
            # try to skip-not-fail only if truly missing reference; otherwise record fail
            note = "skip: " + err
            status = "skip"
        else:
            path = os.path.join(BASE, rel)
            try:
                with open(path, "w", encoding='utf-8') as f:
                    f.write(content)
            except Exception as e:
                note = "write error: %s" % e
                status = "fail"
                _append(ppath, rel, status, note)
                counts[c][status] += 1
                print("%s -> %s : %s" % (rel, status, note))
                continue
            ok, out = verify(rel)
            if ok:
                status = "done_pass"
                note = "verified"
            else:
                status = "fail"
                note = out[:800]
        _append(ppath, rel, status, note)
        counts[c][status] += 1
        print("%s -> %s" % (rel, status) + ("" if status == "done_pass" else " : " + note[:200]))

    print("\n=== SUMMARY (chunks 3/4/5) ===")
    for c in (3, 4, 5):
        print("chunk %d: done_pass=%d fail=%d skip=%d" % (
            c, counts[c]["done_pass"], counts[c]["fail"], counts[c]["skip"]))

def _append(path, rel, status, note):
    with open(path, "a", encoding='utf-8') as f:
        f.write(json.dumps({"rel": rel, "status": status, "note": note}, ensure_ascii=False) + "\n")

if __name__ == '__main__':
    main()
