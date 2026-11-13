// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
/**
 ** LeetCode 65. 有效数字
 ** 方案：方案3（线性扫描）
 */

function isNumber(s: string): boolean {
  // 定义判定函数 isNumber
  const t = s.trim(); // 把 字符串.trim() 存入 另一字符串
  if (t.length === 0) return false; // 若 另一字符串.长度 全等于 0，直接返回 false
  let hasDot = false; // 把 false 存入 hasDot
  let hasE = false; // 把 false 存入 hasE
  let hasDigit = false; // 把 false 存入 hasDigit
  for (let i = 0; i < t.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 另一字符串.长度 就继续
    const c = t[i]; // 把 另一字符串[下标 i] 存入 字符
    if (c === '.') {
      // 若 字符 全等于 「.」
      if (hasDot || hasE) return false; // 若 hasDot 或 hasE，直接返回 false
      hasDot = true; // 把 true 存入 hasDot
    } else if (c === 'e' || c === 'E') {
      // 否则，若 字符 全等于 「e」 或 字符 全等于 「e」
      if (hasE || !hasDigit) return false; // 若 hasE 或 取反 hasDigit，直接返回 false
      hasE = true; // 把 true 存入 hasE
      hasDigit = false; // 把 false 存入 hasDigit
    } else if (c === '+' || c === '-') {
      // 否则，若 字符 全等于 「 加 」 或 字符 全等于 「 加 」
      if (i > 0 && t[i - 1] !== 'e' && t[i - 1] !== 'E') return false;
    } else if (c >= '0' && c <= '9') {
      // 否则，若 字符 不低于 「0」 且 字符 不超过 「0」
      hasDigit = true; // 把 true 存入 hasDigit
    } else {
      // 否则
      return false; // 返回 false
    }
  }
  return hasDigit; // 返回 hasDigit
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (isNumber('abc') !== false)
    // 若 isNumber(「abc」) 不等于 false
    throw new Error("isNumber('abc') should be false"); // throw new Error(「isNumber('abc') should be false」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
