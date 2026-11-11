/**
 ** LeetCode 242. 有效的字母异位词
 ** 方案：2 ) 方案2：哈希表
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355461
 */

// 忠实翻译 Python 参考实现：Counter(s) == Counter(t)
function isAnagram(s: string, t: string): boolean {
  // 定义判定函数 isAnagram
  if (s.length !== t.length) return false; // 若 字符串.长度 不等于 另一字符串.长度，直接返回 false
  const table: Record<string, number> = {}; // 把 {}; 写入 const table: Record<string, number>
  for (const ch of s) {
    // for (const 字符 of 字符串) {
    table[ch] = (table[ch] ?? 0) + 1; // 把 (table[字符] ?? 0) 加 1; 写入 table[ch]
  }
  for (const ch of t) {
    // for (const 字符 of 另一字符串) {
    table[ch] = (table[ch] ?? 0) - 1; // 把 (table[字符] ?? 0) 减 1; 写入 table[ch]
    if (table[ch] < 0) return false; // 若 table[字符] 小于 0，直接返回 false
  }
  for (const key in table) {
    // for (const key in table) {
    if (table[key] !== 0) return false; // 若 table[key] 不等于 0，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 用例来自 _tools/correctness_check.py PROBLEMS["lc_242_有效的字母异位词"]
  const cases: [string, string, boolean][] = [
    ['anagram', 'nagaram', true],
    ['rat', 'car', false],
    ['aacc', 'ccac', false],
  ];
  for (const [a, b, want] of cases) {
    // for (const [数组, b, want] of cases) {
    const got = isAnagram(a, b); // 把 isAnagram(数组, b) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(`FAIL isAnagram(${a},${b}) = ${got}, want ${want}`);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
