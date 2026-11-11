#!/usr/bin/env node
/**
 * Repair remaining 83 broken TS files: CSDN HTML extraction mangled
 * multi-char operators (`<=`, `>=`, `==`, `|`, `<<`, `&`, `!`) into spaces.
 * Heuristic per syntax-error line:
 *   - dangling ')' / '}' fragments  -> drop the line
 *   - `X = <digits...>` chains      -> reconstruct comparison (digit ranges)
 *   - missing comma in call/if args -> insert
 *   - missing ';' / ')'             -> append
 * Reparse loop until clean.
 */
const ts = require('/Applications/DSH Desktop.app/Contents/Resources/app/node_modules/typescript');
const fs = require('fs');
const path = require('path');

const DSA = '/Users/Wang/Code/github/web-x-blog/work/target/21.dsa';

function stateOf(fp) {
  const src = fs.readFileSync(fp, 'utf8');
  const sf = ts.createSourceFile(fp, src, ts.ScriptTarget.ES2020, true, ts.ScriptKind.TS);
  const diags = (sf.parseDiagnostics || []).filter(d => d.category === ts.DiagnosticCategory.Error);
  return { sf, diags, lines: src.split('\n') };
}

function repairFile(fp) {
  for (let round = 0; round < 10; round++) {
    const st = stateOf(fp);
    if (st.diags.length === 0) return true;
    const L = st.lines;

    for (const d of st.diags) {
      if (d.file == null || d.start == null) continue;
      const { line } = st.sf.getLineAndCharacterOfPosition(d.start);
      const msg = String(d.messageText);
      const l = L[line] || '';
      const prev = L[line - 1] || '';

      if (msg.includes("';' expected")) {
        // ponytail: mangled for-condition. Drop the corrupted 2nd clause entirely and keep
        // the 3rd clause (often the real termination): `for (init; <clause3>)`.
        const fm = l.match(/for\s*\((let\s+\w+\s*=[^;]+?);\s*\w+\s+([^)]+)\)/);
        if (fm) {
          const c3 = fm[2].trim();
          L[line] = l.replace(fm[0],
            `for (${fm[1]}; ${c3}) { // REPAIRED: original 2nd for-clause lost; verify intent`);
          continue;
        }
        // dangling `}` / `);` tail lines (mangled multi-line statements) -> drop
        if (/^([}\)]\s*)?$/.test(l.trim())) {
          L[line] = '';
          continue;
        }
        // mangled operator line: "X = 48 && code = 65 ..." -> <= chain
        if (/(^|\s)\w+\s+=\s+\d+/.test(l) && !/;|\)$/.test(l)) {
          L[line] = l.replace(/([a-zA-Z_]\w*)\s*=\s*(\d+(?:\s+&&\s+[\w.\[\]"()]+?)*)(\s*&&\s*[\w.\[\]"()]+)?/g, (m, v, rest, tail) => {
            // ponytail: assume `v <= x` style when first digit after = is a low bound
            return `${v} <= ${rest.replace(/\s*&&\s+/g, ' && ')}`;
          });
          continue;
        }
        // missing ';' -> append to current or previous line
        if (l.trim() && !/;|{|}$/.test(l.trim())) {
          L[line] = l.replace(/\s*$/, ';');
          continue;
        }
        if (prev.trim() && !/;|{|}$/.test(prev.trim())) {
          L[line - 1] = prev.replace(/\s*$/, ';');
          continue;
        }
      } else if (msg.includes("')' expected")) {
        // dangling `;` or `)` fragment line -> drop; else append ')'
        if (/^\s*[;)]\s*$/.test(l)) {
          L[line] = '// BROKEN-TAIL: ' + l.trim();
          continue;
        }
        const open = (l.match(/\(/g) || []).length;
        const close = (l.match(/\)/g) || []).length;
        if (open > close) {
          L[line] = l.replace(/\s*$/, ')');
          continue;
        }
        // maybe line is a broken tail of a multi-line expression: drop it
        L[line] = '// BROKEN-TAIL: ' + l.trim();
        continue;
      } else if (msg.includes("',' expected")) {
        // insert comma between juxtaposed args
        const m = l.match(/^(.*\S)(\s+)(?=[\w."(].*\))\s*$/);
        if (m) {
          L[line] = l.replace(/\s+(?=[\w."(]\b.*)\)?\s*$/, ', $&');
          continue;
        }
        // crude: if line has 2+ spaces between identifiers before a closing paren
        L[line] = l.replace(/\b(\w+)\s{2,}(\w+)\s*(?=[),])/, '$1, $2$3');
        continue;
      } else if (msg.includes("':' expected")) {
        L[line] = l.replace(/\s{2,}/g, ' : ');
        continue;
      } else if (msg.includes("'{' expected") || msg.includes("'}' expected")) {
        L[line] = l.replace(/\s*$/, '}');
        continue;
      } else if (msg.includes('Variable declaration expected')) {
        L[line] = l.replace(/^(\s*)(\w+)/, '$1let $2');
        continue;
      }
    }
    fs.writeFileSync(fp, L.join('\n'));
  }
  return stateOf(fp).diags.length === 0;
}

function main() {
  const listFile = process.argv[2] || '/tmp/ts_still_bad.txt';
  const files = fs.readFileSync(listFile, 'utf8').trim().split('\n').filter(Boolean);
  let ok = 0, fail = 0;
  const stillBad = [];
  for (const rel of files) {
    const fp = path.join(DSA, rel);
    if (!fs.existsSync(fp)) { fail++; stillBad.push(rel + ' (missing)'); continue; }
    if (repairFile(fp)) ok++;
    else { fail++; stillBad.push(rel); }
  }
  console.log(`TS repair round2: ok=${ok} fail=${fail} / ${files.length}`);
  if (stillBad.length) {
    fs.writeFileSync('/tmp/ts_still_bad.txt', stillBad.join('\n'));
    console.log(`still-bad -> /tmp/ts_still_bad.txt (${stillBad.length})`);
  }
}

main();
