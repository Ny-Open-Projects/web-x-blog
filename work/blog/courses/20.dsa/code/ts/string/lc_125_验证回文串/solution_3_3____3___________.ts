/**
 ** LeetCode 125. 验证回文串
 ** 方案：3 ）方案3：在原字符串上直接判断
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145114949
 */

// 忠实翻译 Python 参考实现：t = [c.lower() for c in s if c.isalnum()]; t == t[::-1]
function isPalindrome(s: string): boolean {
  // 定义判定函数 isPalindrome
  const isAlphanumeric = (ch: string): boolean => {
    const code = ch.charCodeAt(0); // 把 字符.charCodeAt(0) 存入 code
    return (
      (code >= 48 && code <= 57) ||
      (code >= 65 && code <= 90) ||
      (code >= 97 && code <= 122)
    );
  };
  let left = 0; // 把 0 存入 左边界
  let right = s.length - 1; // 把 字符串.长度 减 1 存入 右边界
  while (left < right) {
    // 循环，直到不满足「左边界 小于 右边界」
    if (!isAlphanumeric(s[left])) {
      // 若 取反 isAlphanumeric(字符串[左边界]
      left++; // 左边界 加一
    } else if (!isAlphanumeric(s[right])) {
      // 否则，若 取反 isAlphanumeric(字符串[右边界]
      right--; // 右边界 减一
    } else if (s[left].toLowerCase() !== s[right].toLowerCase()) {
      // 否则，若 字符串[左边界].toLowerCase() 不等于 字符串[右边界].toLowerCase(
      return false; // 返回 false
    } else {
      // 否则
      left++; // 左边界 加一
      right--; // 右边界 减一
    }
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
