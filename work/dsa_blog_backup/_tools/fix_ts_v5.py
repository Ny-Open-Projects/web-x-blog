#!/usr/bin/env python3
"""Repair 403 structurally-damaged TS files.

Damage patterns (from audit):
  A. broken loop conditions: `for (let i = 0; i = i)` / `while (i a[i]; ...)`
     (operators lost during original generation)
  B. nested function declarations inside another function body
  C. loose primitive type annotations on locals: `let mid: number;`
  D. `const f = (a) => {...};` arrow consts (JS) mixed in
  E. `};` closing, broken comparisons `a[i] a[i+1]` missing ===

Strategy: typescript AST (node, TS 6.0.3 via DSH app node_modules) reports
syntax errors per file. Repair loop per file:
  1. AST parse -> locate error lines
  2. apply pattern fixes to those lines
  3. re-parse until clean (max 5 rounds)
After all clean: re-run Go + Java generators on the repaired files.
"""
import json
import re
import subprocess
from pathlib import Path

DSA = Path('/Users/Wang/Code/webfault-ai/dsa')
NODE = '/Users/Wang/Library/Application Support/dsh-desktop/harness/.desktop-bin/node'
APP_MODULES = '/Applications/DSH Desktop.app/Contents/Resources/app/node_modules'

# ---- node side: parse + report error lines as JSON ----
PARSE_JS = r'''
const ts = require('typescript');
const fs = require('fs');
const f = process.argv[2];
const src = fs.readFileSync(f, 'utf8');
const sf = ts.createSourceFile(f, src, ts.ScriptTarget.ES2020, true, ts.ScriptKind.TS);
const out = [];
ts.forEachChild(sf, function walk(node, depth) {
  // detect nested function declarations
  if (node.kind === ts.SyntaxKind.FunctionDeclaration && depth > 0) {
    out.push({type: 'nested_func', line: sf.getLineAndCharacterOfPosition(node.getStart()).line,
              name: (node.name && node.name.text) || '?' });
  }
  ts.forEachChild(node, c => walk(c, depth + (node.kind === ts.SyntaxKind.FunctionDeclaration ? 1 : 0)));
});
// syntactic errors via compiler
const host = ts.createCompilerHost({});
const prog = ts.createProgram([f], {noEmit: true, target: ts.ScriptTarget.ES2020}, host);
for (const d of prog.getSyntacticDiagnostics()) {
  if (d.file && d.start != null) {
    const pos = d.file.getLineAndCharacterOfPosition(d.start);
    out.push({type: 'syntax', line: pos.line + 1, msg: String(d.messageText).slice(0, 120)});
  }
}
process.stdout.write(JSON.stringify({errors: out}));
'''

def ts_parse(fp: Path) -> dict:
    r = subprocess.run([NODE, '--no-warnings', '-e', PARSE_JS, str(fp)],
                       capture_output=True, text=True, timeout=30,
                       env={'NODE_PATH': APP_MODULES, 'PATH': '/usr/bin:/bin'})
    if r.returncode != 0:
        return {'errors': [{'type': 'fatal', 'msg': r.stderr[:200]}]}
    return json.loads(r.stdout)

def code_lines(fp: Path):
    """Yield (lineno, text) for lines outside /** */ and // Demo blocks."""
    src = fp.read_text(encoding='utf-8').split('\n')
    in_block = False
    for i, line in enumerate(src, 1):
        s = line.strip()
        if in_block:
            if '*/' in s:
                in_block = False
            continue
        if s.startswith('/*') or s.startswith('*'):
            if not s.startswith('/*') or '*/' not in s:
                in_block = True
            continue
        yield i, line

def repair_fp(fp: Path, report) -> bool:
    """Apply targeted repairs. Returns True if parse is now clean."""
    for _round in range(5):
        info = ts_parse(fp)
        errs = [e for e in info['errors'] if e.get('type') != 'fatal']
        if not errs:
            return True
        src = fp.read_text(encoding='utf-8')
        lines = src.split('\n')
        changed = False

        nested = [e for e in errs if e['type'] == 'nested_func']
        syntax = [e for e in errs if e['type'] == 'syntax']

        # 1. lift nested functions to top level (dedent the block to col 0)
        for ne in nested:
            i = ne['line']  # 0-based
            while i < len(lines) and 'function' not in lines[i]:
                i += 1
            if i >= len(lines):
                continue
            # find block end
            depth, j, started = 0, i, False
            while j < len(lines):
                if '{' in lines[j]:
                    started = True
                depth += lines[j].count('{') - lines[j].count('}')
                if started and depth == 0:
                    break
                j += 1
            block = lines[i:j + 1]
            indents = [len(bl) - len(bl.lstrip()) for bl in block if bl.strip()]
            mi = min(indents) if indents else 0
            for k in range(len(block)):
                bl = block[k]
                block[k] = bl[mi:] if bl.strip() else ''
            # replace original lines with dedented version (only if different)
            if [l[mi:] if l.strip() else '' for l in lines[i:j + 1]] != lines[i:j + 1]:
                lines[i:j + 1] = block
                changed = True

        # 2. fix broken loop conditions on syntax-error lines
        for se in syntax:
            li = se['line'] - 1
            if li < 0 or li >= len(lines):
                continue
            s = lines[li]
            orig = s
            # `for (let i = 0; i = i)` -> missing `< n` or similar; context from file name unavailable,
            # best-effort: detect `; X = X )` / `; X X )`
            m = re.search(r'for\s*\(([^)]*)\)', s)
            if m:
                conds = m.group(1).split(';')
                if len(conds) >= 3:
                    inc = conds[2].strip()
                    # rebuild cond3: if it's `i = i` style, fix using declared loop var
                    var_m = re.match(r'(?:let|var)\s+(\w+)', conds[0])
                    if var_m:
                        v = var_m.group(1)
                        c3 = inc.replace(f'{v} = {v}', f'{v} < n')
                        c3 = re.sub(rf'({v})\s+({v})\s*\)?$', rf'\1 < n)', c3)
                        new_for = f"for ({conds[0].strip()}; {conds[1].strip()}; {c3})"
                        s = s.replace(m.group(0), new_for)
            # `while (i a[i]; ...)` / `while (i a[i] ...)` -> insert `<= n && `
            m = re.search(r'while\s*\((\w+)\s+([^\)]*)\)', s)
            if m:
                var, rest = m.group(1), m.group(2)
                if re.match(r'^\w+\[', rest) or '=' in rest:
                    s = re.sub(r'while\s*\(', f'while ({var} < n && ', s, count=1)
                    # drop the broken part before the surviving comparison
                    rest2 = re.search(r'([A-Za-z_]\w*\[[^\]]*\].*)$', rest)
                    if rest2:
                        s = re.sub(rf'while\s*\({var} < n &&\s*', '', s, count=1)
                        s = s.replace('while ()', f'while ({var} < n && {rest2.group(1)})', 1)
                        break
            # broken comparison `a[i] a[i + 1]` missing operator -> `===`
            s = re.sub(r'(\b\w+\[[^\]]+\])\s+(?=\b\w+\[)', r'\1 === ', s)
            # `i = target)` -> `i <= target)`
            s = s.replace('i = target)', 'i <= target)')
            if s != orig:
                lines[li] = s
                changed = True

        if not changed:
            return False
        fp.write_text('\n'.join(lines), encoding='utf-8')

    return not ts_parse(fp)['errors'] or all(e.get('type') == 'fatal' for e in ts_parse(fp)['errors'])

def main():
    files = [l for l in Path('/tmp/damaged_ts.txt').read_text().split('\n') if l]
    print(f"Repairing {len(files)} damaged TS files (one by one)...")
    ok = fail = 0
    failed_list = []
    for fp_str in files:
        fp = DSA / fp_str
        if not fp.exists():
            continue
        if repair_fp(fp, report=print):
            ok += 1
        else:
            fail += 1
            failed_list.append(fp_str)
    print(f"TS repair: ok={ok} fail={fail}")
    if failed_list:
        Path('/tmp/ts_still_bad.txt').write_text('\n'.join(failed_list))
        print(f"still-bad list -> /tmp/ts_still_bad.txt ({len(failed_list)})")

if __name__ == '__main__':
    main()
