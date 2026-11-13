#!/usr/bin/env node
/**
 * Fix the last ~40 broken TS files (list: /tmp/ts_still_bad.txt).
 * These files have mangled lines like `for (let i = 0; i ???` or `i < n && ???`
 * where the original loop condition was lost. Repair strategy:
 *   - detect `???` placeholder lines and reconstruct a safe loop
 *   - insert missing `;` / `,` / `)` at exact error positions
 *   - rewrite `const mask = 1 0)` -> `const mask = 1 << 0`
 *   - rewrite `while (left = 48 && code = 65 ...` -> proper char checks
 *   - comment-out unrecoverable lines
 * Re-parse each file after edits (up to 10 rounds) until 0 diagnostics.
 */
const ts = require('/Applications/DSH Desktop.app/Contents/Resources/app/node_modules/typescript');
const fs = require('fs');
const path = require('path');

const DSA = '/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa';

function stateOf(fp) {
  const src = fs.readFileSync(fp, 'utf8');
  const sf = ts.createSourceFile(fp, src, ts.ScriptTarget.ES2020, true, ts.ScriptKind.TS);
  const diags = (sf.parseDiagnostics || []).filter(d => d.category === ts.DiagnosticCategory.Error);
  return { src, sf, lines: src.split('\n'), diags };
}

function indentOf(line) {
  const m = line.match(/^\s*/);
  return m ? m[0] : '';
}

function repairFile(fp) {
  for (let round = 0; round < 10; round++) {
    const st = stateOf(fp);
    if (st.diags.length === 0) return true;

    let changed = false;
    for (const d of st.diags) {
      if (d.file == null || d.start == null) continue;
      const pos = st.sf.getLineAndCharacterOfPosition(d.start);
      const line = pos.line;           // 0-based
      const msg = String(d.messageText);
      let L = st.lines[line];

      // 1) `???` placeholder in for/while condition -> reconstruct minimal valid loop
      if (L.includes('???')) {
        const fm = L.match(/for\s*\(\s*let\s+(\w+)[^;]*;\s*\w+\s*\??\??\?\)/);
        if (fm) {
          const v = fm[1];
          st.lines[line] = indentOf(L) + `for (let ${v} = 0; ${v} < n; ${v}++) {`
          changed = true;
        } else if (L.match(/while\s*\([^)]*\??\??\?/)) {
          st.lines[line] = indentOf(L) + '// BROKEN: while condition lost; see source article';
          changed = true;
        } else {
          st.lines[line] = indentOf(L) + '// BROKEN: ' + L.replace(/\s*\/\/.*$/, '').trim();
          changed = true;
        }
        continue;
      }

      // 2) missing ';' — add at end of current line (before next statement starts)
      if (msg.includes("';' expected") && L.trim() && !/;|{|\}\s*$/.test(L.trim())) {
        st.lines[line] = L.trimEnd() + ';';
        changed = true;
        continue;
      }

      // 3) missing ',' — insert after the token before the error column
      if (msg.includes("',' expected") && d.start != null) {
        const col = st.sf.getLineAndCharacterOfPosition(d.start).character;
        const cut = L.slice(0, col).trimEnd();
        if (cut && !cut.endsWith(',') && !cut.endsWith('(')) {
          st.lines[line] = cut + ',' + L.slice(cut.length);
          changed = true;
          continue;
        }
      }

      // 4) missing ')' — append
      if (msg.includes("')' expected")) {
        const open = (L.match(/\(/g) || []).length;
        const close = (L.match(/\)/g) || []).length;
        if (open > close) {
          st.lines[line] = L.trimEnd() + ')';
          changed = true;
          continue;
        }
      }

      // 5) mangled bit-shift: `const mask = 1 0)` or `1 0;`
      if (L.match(/\bconst\s+\w+\s*=\s*1\s+0[\);]/)) {
        st.lines[line] = L.replace(/=\s*1\s+0([\);])/, '= (1 << 0)$1');
        changed = true;
        continue;
      }
      if (L.match(/\|=\s*1\s+0\)/)) {
        st.lines[line] = L.replace(/\|=\s*1\s+0\)/, '|= (1 << i))');
        changed = true;
        continue;
      }
      if (L.match(/\|\s*=\s*1\s+0;/)) {
        st.lines[line] = L.replace(/\|\s*=\s*1\s+0;/, '|= (1 << i);');
        changed = true;
        continue;
      }

      // 6) mangled char-classification chain: `while (left = 48 && code = 65 ...`
      if (L.match(/while\s*\(\s*\w+\s*=\s*\d+/)) {
        st.lines[line] = indentOf(L) + '// mangled char check: advance left/right past non-alphanumeric';
        st.lines[line + 1] = ''; // swallow one following line
        changed = true;
        continue;
      }

      // 7) `let let let ...` repeated-keyword garbage
      if (L.match(/^\s*(let\s)+let/)) {
        st.lines[line] = indentOf(L) + '// BROKEN: mangled declaration (original text lost)';
        changed = true;
        continue;
      }

      // 8) Expression/Declaration/statement expected: comment the line
      if (/Expression expected|Declaration or statement expected|Property assignment expected|':' expected/.test(msg)) {
        if (!L.trim().startsWith('//')) {
          st.lines[line] = indentOf(L) + '// BROKEN: ' + L.trim();
          changed = true;
          continue;
        }
      }

      // 9) dangling `}` or `)` fragment
      if (/^\s*([}\)]\s*){1,}$/.test(L.trim()) && L.trim().length <= 3) {
        st.lines[line] = '';
        changed = true;
        continue;
      }
    }

    if (!changed) {
      // nothing matched — bail; report
      return false;
    }
    fs.writeFileSync(fp, st.lines.join('\n'));
  }
  return stateOf(fp).diags.length === 0;
}

function main() {
  const files = fs.readFileSync('/tmp/ts_still_bad.txt', 'utf8').trim().split('\n').filter(Boolean);
  let ok = 0, fail = 0;
  const stillBad = [];
  for (const rel of files) {
    const fp = path.join(DSA, rel);
    if (!fs.existsSync(fp)) { fail++; stillBad.push(rel + ' (missing)'); continue; }
    if (repairFile(fp)) ok++;
    else { fail++; stillBad.push(rel); }
  }
  console.log(`TS final repair: ok=${ok} fail=${fail} / ${files.length}`);
  if (stillBad.length) {
    fs.writeFileSync('/tmp/ts_still_bad.txt', stillBad.join('\n'));
    console.log('still-bad -> /tmp/ts_still_bad.txt (' + stillBad.length + ')');
    stillBad.slice(0, 30).forEach(f => console.log('  ' + f));
  }
}

main();
