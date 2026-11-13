#!/usr/bin/env node
/**
 * Manually reconstruct the 69 still-broken TS files (list: /tmp/ts_still_bad.txt).
 * Each fix entry: file -> [{line (1-based), text (replacement line, keep indent via leading spaces in source)}]
 * Re-parse after each file; report remaining.
 */
const ts = require('/Applications/DSH Desktop.app/Contents/Resources/app/node_modules/typescript');
const fs = require('fs');
const path = require('path');

const DSA = '/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa';

// ---------- per-file manual fixes (line -> new content, without leading indent) ----------
// Indent is preserved by matching the original line's leading whitespace.
const FIXES = {
  // ===== tree =====
  'ts/tree/lc_654_最大二叉树/solution_1_1_____1___.ts': [
    { line: 25, text: 'for (let i = left + 1; i < right; i++) { if (nums[i] > nums[best]) { best = i; } }' },
  ],
  'ts/tree/lc_654_最大二叉树/solution_2_2_____2____.ts': [
    { line: 27, text: 'while (i < n) { while (stack.length && nums[stack[stack.length - 1]] < nums[i]) { right[stack.pop()] = i; } if (stack.length) { left[i] = stack[stack.length - 1]; } stack.push(i); i++; }' },
  ],
  'ts/tree/lc_654_最大二叉树/solution_3_3_____3______.ts': [
    { line: 25, text: 'while (i < n) { while (stack.length && nums[stack[stack.length - 1]] < nums[i]) { right[stack.pop()] = i; } if (stack.length) { left[i] = stack[stack.length - 1]; } stack.push(i); i++; }' },
  ],
  'ts/tree/lc_98_验证二叉搜索树/solution_5_1_____1_____.ts': [
    { line: 34, text: 'for (let i = 0, length = traversalArr.length; i + 1 < length && traversalArr[i] >= traversalArr[i + 1]; i++) { return false; }' },
  ],
  'ts/tree/lc_114_二叉树展开为链表/solution_1_1____1___________.ts': [
    { line: 28, text: 'for (let i = 1; i < nodes.length; i++) { const node = nodes[i - 1]; if (node) { node.left = null; node.right = nodes[i]; } }' },
  ],
  'ts/tree/lc_222_完全二叉树的节点个数/solution_1_1_____1___________.ts': [
    { line: 29, text: 'while (low + 1 < high) { const mid = (low + high) >> 1; if (level(mid, h - 1)) { low = mid; } else { high = mid; } }' },
  ],

  // ===== sort =====
  'ts/sort/lc_41_缺失的第一个正数/solution_1___1.ts': [
    { line: 20, text: 'for (let i = 0; i < n; i++) { if (nums[i] !== i + 1) { return nums[i] + 1; } }' },
  ],
  'ts/sort/lc_41_缺失的第一个正数/solution_2___2.ts': [
    { line: 17, text: 'for (let i = 0; i < nums.length; i++) { if (i + 1 !== nums[i]) { return i + 1; } } return n + 1;' },
  ],
  'ts/sort/lc_41_缺失的第一个正数/solution_4___4.ts': [
    { line: 12, text: 'for (let i = 0; i < n; i++) { if (nums[i] !== i + 1) { return i + 1; } }' },
  ],
  'ts/sort/lc_41_缺失的第一个正数/solution_5___5.ts': [
    { line: 11, text: 'for (i = 0; i < n; i++) { if (nums[i] !== i + 1) { break; } }' },
  ],
  'ts/sort/lc_15_三数之和/solution_1_1_____1_________.ts': [
    { line: 13, text: 'for (let first = 0; first < n; first++) {' },
    { line: 20, text: 'for (let second = first + 1; second < n; second++) {' },
  ],
  'ts/sort/lc_15_三数之和/solution_2_2_____2_________.ts': [
    { line: 12, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/sort/lc_18_四数之和/solution_1_1_____1__________.ts': [
    { line: 11, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/sort/lc_18_四数之和/solution_2_2_____2________.ts': [
    { line: 20, text: 'for (let i = index; i < n; i++) {' },
  ],
  'ts/sort/lc_937_重新排列日志文件/solution_1_1_____1______.ts': [
    // whole function region: lines 10..~40 are mangled (map/swap comparator lost its shape)
    { line: 10, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/sort/lc_1356_根据数字二进制下_1_的数目排序/solution_2_2_____2______.ts': [
    { line: 10, text: 'for (let i = 1; i < n; i++) {' },
  ],

  // ===== array =====
  'ts/array/lc_89_格雷编码/solution_1_1_____1___.ts': [
    { line: 15, text: 'for (let i = 0, len = prev.length; i < len; i++) {' },
  ],
  'ts/array/lc_167_两数之和_ii_-_输入有序数组/solution_1_1_____1______.ts': [
    { line: 8, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/array/lc_977_有序数组的平方/solution_2_2_____2____.ts': [
    { line: 11, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/array/lc_977_有序数组的平方/solution_3_3_____3_____.ts': [
    { line: 19, text: '// line removed (dangling brace from mangled loop)' },
  ],
  'ts/array/lc_605_种花问题/solution_1_1____1_____.ts': [
    { line: 18, text: 'return true;' },
  ],
  'ts/array/lc_605_种花问题/solution_2_2_____2__________.ts': [
    // L16 error is cascade from earlier mangled body; comment the demo export fix below
  ],
  'ts/array/lc_541_反转字符串_ii/solution_1_1_____1____.ts': [
    { line: 11, text: 'for (let i = 0; i < s.length; i += 2 * k) {' },
  ],
  'ts/array/lc_209_长度最小的子数组/solution_1_1_____1_________.ts': [
    { line: 13, text: 'for (let i = 0; i < n; i++) { let sum = 0; for (let j = i; j < n; j++) { sum += nums[j]; if (sum >= target) { ans = Math.min(ans, j - i + 1); break; } } }' },
  ],
  'ts/array/lc_209_长度最小的子数组/solution_2_2_____2___________.ts': [
    { line: 15, text: 'for (let i = 1; i <= n; i++) {' },
  ],
  'ts/array/lc_17_电话号码的字母组合/solution_1_1_____1________.ts': [
    { line: 9, text: "if (digits.length === 0) { return [];" },
  ],

  // ===== backtrack =====
  'ts/backtrack/lc_79_单词搜索/solution_1_1_____1____.ts': [
    { line: 11, text: 'for (let i = 0; i < m; i++) { for (let j = 0; j < n; j++) {' },
  ],
  'ts/backtrack/lc_131_分割回文串/solution_1_1_____1______________.ts': [
    { line: 13, text: 'for (let j = i + 1; j <= n; j++) {' },
  ],
  'ts/backtrack/lc_39_组合总和/solution_2_2_____2____.ts': [
    { line: 21, text: 'for (let j = i; j < n; j++) {' },
  ],
  'ts/backtrack/lc_51_n_皇后/solution_2_2_____2__________.ts': [
    { line: 14, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/backtrack/lc_51_n_皇后/solution_3_3_____3___-____.ts': [
    { line: 23, text: 'for (let col = 0; col < n; col++) { if (isValid(row, col)) { queens[row] = col; backtrack(row + 1); queens[row] = -1; } }' },
  ],
  'ts/backtrack/lc_37_解数独/solution_2_2_____2_______.ts': [
    { line: 18, text: 'function flip(i, j, digit) { const mask = 1 << digit; cells[i * 9 + j] ^= mask; rows[i] ^= mask; cols[j] ^= mask; boxes[i / 3 | 0] * 3 + (j / 3 | 0); }' },
  ],
  'ts/backtrack/lc_37_解数独/solution_3_3_____3______.ts': [
    { line: 18, text: 'const mask = 1 << digit; rows[i] ^= mask; cols[j] ^= mask; boxes[(i / 3 | 0) * 3 + (j / 3 | 0)] ^= mask;' },
  ],

  // ===== graph =====
  'ts/graph/lc_417_太平洋大西洋水流问题/solution_1___1.ts': [
    { line: 21, text: 'const inBounds = nr >= 0 && nr < m && nc >= 0 && nc < n; if (inBounds && !flow[nr][nc] && matrix[nr][nc] >= matrix[r][c]) { dfs(nr, nc, flow); }' },
  ],

  // ===== queue =====
  'ts/queue/lc_621_任务调度器/solution_1___1.ts': [
    { line: 22, text: 'for (let i = 0; i < tasks.length; i++) { const item = tasks[i]; dict[item] = (dict[item] || 0) + 1; if (dict[item] > max) { max = dict[item]; }' },
  ],

  // ===== hash =====
  'ts/hash/lc_350_两个数组的交集_ii/solution_2_2____2__________.ts': [
    { line: 19, text: '// removed dangling brace' },
  ],
  'ts/hash/lc_3_无重复字符的最长子串/solution_1___1.ts': [
    { line: 12, text: 'for (let r = 0; r < n; r++) { if (dict.has(s[r]) && dict.get(s[r]) >= l) { l = dict.get(s[r]) + 1; } res = Math.max(res, r - l + 1); dict.set(s[r], r); }' },
  ],

  // ===== heap =====
  'ts/heap/lc_451_根据字符出现频率排序/solution_2___2.ts': [
    { line: 24, text: 'for (let j = 0; j < freq; j++) { res.push(arr[largest]); }' },
  ],
  'ts/heap/lc_215_数组中的第k个最大元素/solution_3___3.ts': [
    { line: 10, text: 'for (let j = 0; j < n; j++) {' },
  ],

  // ===== greedy =====
  'ts/greedy/lc_122_买卖股票的最佳时机ii/solution_1___1.ts': [
    { line: 15, text: '// removed dangling brace' },
  ],
  'ts/greedy/lc_122_买卖股票的最佳时机ii/solution_2___2.ts': [
    { line: 12, text: '// removed dangling brace' },
  ],
  'ts/greedy/lc_455_分饼干/solution_2___2.ts': [
    { line: 15, text: 'while (i < kids.length && j < candies.length) { if (candies[j] >= kids[i]) { count++; i++; } j++; }' },
  ],
  'ts/greedy/lc_45_跳跃游戏_ii/solution_1_1_____1__________.ts': [
    { line: 11, text: 'for (let i = 0; i < n; i++) { if (i > position) { break; } position = Math.max(position, i + nums[i]); }' },
  ],
  'ts/greedy/lc_452_用最少数量的箭引爆气球/solution_1_1_____1_________.ts': [
    { line: 12, text: 'for (let i = 1; i < n; i++) {' },
  ],
  'ts/greedy/lc_435_无重叠区间/solution_1_1_____1____.ts': [
    { line: 15, text: 'for (let i = 1; i < n; i++) {' },
  ],

  // ===== dp =====
  'ts/dp/lc_3105_最长的严格递增或递减子数组/solution_2_2_____2_________.ts': [
    { line: 17, text: '// removed dangling brace' },
  ],
  'ts/dp/lc_1027_最长等差数列/solution_1_1_____1_____.ts': [
    { line: 12, text: 'for (let d = -diff; d < n; d++) {' },
  ],
  'ts/dp/lc_674_最长连续递增序列/solution_1_1_____1____.ts': [
    { line: 13, text: '// removed dangling brace' },
  ],
  'ts/dp/lc_1494_并行课程_ii/solution_2_2_____2___________.ts': [
    { line: 10, text: 'pre1[r[1] - 1] |= 1 << r[0];' },
    { line: 22, text: 'for (let j = (i1 - 1) & i1; j; j = (j - 1) & i1) {' },
  ],
  'ts/dp/lc_673_最长递增子序列的个数/solution_1_1_____1______.ts': [
    { line: 11, text: 'for (let i = 0; i < n; i++) { for (let j = 0; j < i; j++) { if (nums[j] < nums[i]) {' },
  ],
  'ts/dp/lc_121_买卖股票的最佳时机/solution_1_1_____1____.ts': [
    { line: 10, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/dp/lc_121_买卖股票的最佳时机/solution_2_2_____2______.ts': [
    { line: 11, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/dp/lc_714_买卖股票的最佳时机含手续费/solution_2_2_____2____.ts': [
    { line: 11, text: 'for (let i = 1; i < n; i++) {' },
  ],
  'ts/dp/lc_63_不同路径_ii/solution_2___2.ts': [
    { line: 14, text: 'for (let i = 0; i < m; i++) { for (let j = 0; j < n; j++) { if (obstacleGrid[i][j] === 1) { dp[i][j] = 0; continue; }' },
  ],

  // ===== string =====
  'ts/string/lc_165_比较版本号/solution_1_1_____1_______.ts': [
    { line: 10, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/string/lc_567_字符串的排列/solution_3_3_____3____.ts': [
    { line: 20, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/string/lc_8_字符串转换整数_(atoi)/solution_2_2_____2___________.ts': [
    { line: 32, text: 'for (let j = i; j < n; j++) {' },
  ],
  'ts/string/lc_791_自定义字符串排序/solution_2_2_____2_____.ts': [
    { line: 12, text: 'for (let i = 0; i < n; i++) {' },
    { line: 19, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/string/lc_791_自定义字符串排序/solution_1_1_____1______.ts': [
    { line: 12, text: 'const cmp = (c0, c1) => { const index0 = c0.charCodeAt(0) - \'a\'.charCodeAt(0); const index1 = c1.charCodeAt(0) - \'a\'.charCodeAt(0); return val[index0] - val[index1]; };' },
  ],
  'ts/string/lc_125_验证回文串/solution_2_2_____2_____.ts': [
    { line: 21, text: 'while (left < right) { while (left < right && !isAlnum(s[left])) { left++; } while (left < right && !isAlnum(s[right])) { right--; }' },
  ],
  'ts/string/lc_125_验证回文串/solution_3_3____3___________.ts': [
    { line: 11, text: 'while (left < right) { while (left < right && !isAlnum(s[left])) { left++; } while (left < right && !isAlnum(s[right])) { right--; }' },
  ],

  // ===== stack =====
  'ts/stack/lc_150_逆波兰表达式求值/solution_1_1_____1_____.ts': [
    { line: 14, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/stack/lc_151_反转字符串中的单词/solution_2_2_____2___________.ts': [
    { line: 15, text: '// removed dangling brace' },
  ],
  'ts/stack/lc_151_反转字符串中的单词/solution_3_3_____3______.ts': [
    { line: 18, text: '// removed dangling brace' },
  ],
  'ts/stack/lc_2454_下一个更大元素_iv/solution_2_2_____2_____.ts': [
    { line: 18, text: '// removed dangling brace' },
  ],
  'ts/stack/lc_2454_下一个更大元素_iv/solution_1_1_____1___________.ts': [
    { line: 13, text: 'for (let i = 0; i < n; i++) {' },
  ],
  'ts/stack/lc_556_下一个更大元素_iii/solution_2_2_____2___.ts': [
    { line: 33, text: '// removed dangling brace' },
  ],
  'ts/stack/lc_739_每日温度/solution_2_2____2____.ts': [
    { line: 12, text: 'for (let i = 0; i < n; i++) {' },
  ],

  // ===== matrix =====
  'ts/matrix/lc_1329_将矩阵按对角线排序/solution_2_2_____2____.ts': [
    { line: 10, text: 'for (let k = 1 - n; k < m; k++) {' },
  ],
  'ts/matrix/lc_1329_将矩阵按对角线排序/solution_1_1_____1___.ts': [
    { line: 13, text: 'for (let i = 0; i < m; i++) { const d = []; for (let j = i; j < n; j++) { d.push(matrix[i][j]); } d.sort((a, b) => b - a); let ii = i, jj = 0; while (ii < m && jj < n) { matrix[ii][jj] = d[jj]; ii++; jj++; } }' },
  ],
};

function stateOf(fp) {
  const src = fs.readFileSync(fp, 'utf8');
  const sf = ts.createSourceFile(fp, src, ts.ScriptTarget.ES2020, true, ts.ScriptKind.TS);
  return { sf, src, lines: src.split('\n'), diags: (sf.parseDiagnostics || []).filter(d => d.category === ts.DiagnosticCategory.Error) };
}

function applyFixes() {
  const files = fs.readFileSync('/tmp/ts_still_bad.txt', 'utf8').trim().split('\n').filter(Boolean);
  let ok = 0, fail = 0;
  const stillBad = [];
  for (const rel of files) {
    const fp = path.join(DSA, rel);
    if (!fs.existsSync(fp)) { fail++; stillBad.push(rel); continue; }
    const entries = FIXES[rel];
    if (entries && entries.length) {
      const L = fs.readFileSync(fp, 'utf8').split('\n');
      for (const e of entries) {
        const li = e.line - 1;
        if (li < 0 || li >= L.length) { fail++; stillBad.push(rel + ' (bad line ' + e.line + ')'); break; }
        const indent = (L[li].match(/^\s*/)[0]) || '';
        L[li] = indent + e.text;
      }
      fs.writeFileSync(fp, L.join('\n'));
    }
    const clean = stateOf(fp).diags.length === 0;
    if (clean) ok++;
    else { fail++; stillBad.push(rel); }
  }
  console.log(`manual fixes: ok=${ok} fail=${fail} / ${files.length}`);
  if (stillBad.length) {
    fs.writeFileSync('/tmp/ts_still_bad.txt', stillBad.join('\n'));
    console.log(`still-bad -> /tmp/ts_still_bad.txt (${stillBad.length})`);
    stillBad.slice(0, 10).forEach(f => console.log('  ' + f));
  }
}

applyFixes();
