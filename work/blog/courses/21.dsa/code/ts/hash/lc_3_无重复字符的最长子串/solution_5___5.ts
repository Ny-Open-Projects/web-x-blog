/**
 ** LeetCode 3. 无重复字符的最长子串
 ** 方案：方案5：滑动窗口 + 字符末次位置哈希
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133461048
 */

export function lengthOfLongestSubstring(s: string): number {
  // 定义函数/方法 lengthOfLongestSubstring
  const last: { [k: string]: number } = {}; // 把 {}; 写入 const last: { [k: string]: number }
  let l = 0; // 把 0 存入 左指针
  let res = 0; // 把 0 存入 结果
  for (let r = 0; r < s.length; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 字符串.长度 就继续
    const ch = s[r]; // 把 字符串[右指针] 存入 字符
    if (ch in last && last[ch] >= l) l = last[ch] + 1; // 若 字符 in last 且 last[字符] 不低于 左指针) 左指针 赋值为 last[字符] 加 1;
    res = Math.max(res, r - l + 1); // 把 Math.取较大值 结果, 右指针 减 左指针 加 1) 存入 结果
    last[ch] = r; // 把 右指针; 写入 last[ch]
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (lengthOfLongestSubstring('abcabcbb') !== 3) throw new Error('FAILED 1');
  if (lengthOfLongestSubstring('bbbbb') !== 1) throw new Error('FAILED 2');
  if (lengthOfLongestSubstring('pwwkew') !== 3) throw new Error('FAILED 3');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
