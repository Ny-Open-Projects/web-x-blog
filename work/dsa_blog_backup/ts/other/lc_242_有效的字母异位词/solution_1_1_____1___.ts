/**
 ** LeetCode 242. 有效的字母异位词
 ** 方案：1 ) 方案1：排序
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355461
 */

// 忠实翻译 Python 参考实现：Counter(s) == Counter(t)
function isAnagram(s: string, t: string): boolean {
  // 定义判定函数 isAnagram
  if (s.length !== t.length) return false; // 若 字符串.长度 不等于 另一字符串.长度，直接返回 false
  const a = s.split('').sort(); // 把 字符串.split('') 排序 ) 存入 数组
  const b = t.split('').sort(); // 把 另一字符串.split('') 排序 ) 存入 b
  return a.join('') === b.join(''); // 返回 数组.join('') 全等于 b.join('')
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
