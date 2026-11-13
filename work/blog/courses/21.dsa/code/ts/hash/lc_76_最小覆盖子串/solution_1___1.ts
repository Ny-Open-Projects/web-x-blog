/**
 ** LeetCode 76. 最小覆盖子串
 ** 方案：方案1：滑动窗口 + 计数器
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133465616
 */

export function minWindow(s: string, t: string): string {
  // 定义函数/方法 minWindow
  if (!s || !t) return ''; // 若 取反 字符串 或 取反 另一字符串，直接返回 「」
  const targetCount: { [c: string]: number } = {}; // 把 {}; 写入 const targetCount: { [c: string]: number }
  for (const c of t) targetCount[c] = (targetCount[c] || 0) + 1;
  const required = Object.keys(targetCount).length; // 把 Object.keys(targetCount).长度 存入 required
  let left = 0; // 把 0 存入 左边界
  let right = 0; // 把 0 存入 右边界
  let formed = 0; // 把 0 存入 formed
  const windowCount: { [c: string]: number } = {}; // 把 {}; 写入 const windowCount: { [c: string]: number }
  let minLen = Infinity; // 把 Infinity 存入 minLen
  let minLeft = 0; // 把 0 存入 minLeft
  while (right < s.length) {
    // 循环，直到不满足「右边界 小于 字符串.长度」
    const char = s[right]; // 把 字符串[右边界] 存入 char
    windowCount[char] = (windowCount[char] || 0) + 1; // 把 (windowCount[char] 或 0) 加 1; 写入 windowCount[char]
    if (char in targetCount && windowCount[char] === targetCount[char])
      formed++;
    while (left <= right && formed === required) {
      // 循环，直到不满足「左边界 不超过 右边界 且 formed 全等于 required」
      const c = s[left]; // 把 字符串[左边界] 存入 字符
      if (right - left + 1 < minLen) {
        // 若 右边界 减 左边界 加 1 小于 minLen
        minLen = right - left + 1; // 把 右边界 减 左边界 加 1 存入 minLen
        minLeft = left; // 把 左边界 存入 minLeft
      }
      windowCount[c] -= 1; // windowCount[c]累减 1
      if (c in targetCount && windowCount[c] < targetCount[c]) formed--;
      left++; // 左边界 加一
    }
    right++; // 右边界 加一
  }
  return minLen === Infinity ? '' : s.substring(minLeft, minLeft + minLen);
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (minWindow('abc', '') !== '') throw new Error('FAILED empty t'); // 若 minWindow(「abc」, 「abc」) 不等于 「abc」) throw new Error(「abc」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
