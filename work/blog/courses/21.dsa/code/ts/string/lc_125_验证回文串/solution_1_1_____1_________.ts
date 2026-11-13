/**
 ** LeetCode 125. 验证回文串
 ** 方案：1 ) 方案1: 筛选 + 判断
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145114949
 */

// 忠实翻译 Python 参考实现：t = [c.lower() for c in s if c.isalnum()]; t == t[::-1]
function isAlphanumeric(c: string): boolean {
  // 定义判定函数 isAlphanumeric
  return /[a-zA-Z0-9]/.test(c); // 返回 除以 [数组 减 zA 减 Z0 减 9] 除以 .test(字符)
}
function isPalindrome(s: string): boolean {
  // 定义判定函数 isPalindrome
  let filtered = ''; // 把 「」 存入 filtered
  for (const ch of s) {
    // for (const 字符 of 字符串) {
    if (isAlphanumeric(ch)) {
      // 若 isAlphanumeric(字符
      filtered += ch.toLowerCase(); // filtered累加 字符.toLowerCase()
    }
  }
  let left = 0,
    right = filtered.length - 1; // 把 0, 右边界 赋值为 filtered.长度 减 1 存入 左边界
  while (left < right) {
    // 循环，直到不满足「左边界 小于 右边界」
    if (filtered[left] !== filtered[right]) return false; // 若 filtered[左边界] 不等于 filtered[右边界]，直接返回 false
    left++; // 左边界 加一
    right--; // 右边界 减一
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // 用例来自 _tools/correctness_check.py PROBLEMS["lc_125_验证回文串"]
  const cases: [string, boolean][] = [
    ['A man, a plan, a canal: Panama', true],
    ['race a car', false],
    [' ', true],
  ];
  for (const [input, want] of cases) {
    // for (const [input, want] of cases) {
    const got = isPalindrome(input); // 把 isPalindrome(input) 存入 got
    if (got !== want) {
      // 若 got 不等于 want
      throw new Error(
        `FAIL isPalindrome(${JSON.stringify(input)}) = ${got}, want ${want}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
