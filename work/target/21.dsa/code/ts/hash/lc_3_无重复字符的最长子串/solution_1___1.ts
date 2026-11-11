/**
 ** LeetCode 3. 无重复字符的最长子串
 ** 方案：方案1：滑动窗口 + 集合
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133461048
 */

export function lengthOfLongestSubstring(s: string): number {
  // 定义函数/方法 lengthOfLongestSubstring
  const charSet = new Set<string>(); // 把 new Set 小于 string 超过 () 存入 charSet
  let left = 0; // 把 0 存入 左边界
  let maxLen = 0; // 把 0 存入 maxLen
  for (let right = 0; right < s.length; right++) {
    // 让 右边界 从 0 开始计数，右边界 小于 字符串.长度 就继续
    while (charSet.has(s[right])) {
      // 循环，直到不满足「charSet.has(字符串[右边界]」
      charSet.delete(s[left]); // charSet.delete(字符串[左边界]);
      left++; // 左边界 加一
    }
    charSet.add(s[right]); // charSet 追加 字符串[右边界]);
    maxLen = Math.max(maxLen, right - left + 1); // 把 Math.取较大值 maxLen, 右边界 减 左边界 加 1) 存入 maxLen
  }
  return maxLen; // 返回 maxLen
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (lengthOfLongestSubstring('abc') !== 3) throw new Error('FAILED abc');
  if (lengthOfLongestSubstring('abcabcbb') !== 3) throw new Error('FAILED 1');
  if (lengthOfLongestSubstring('bbbbb') !== 1) throw new Error('FAILED 2');
  if (lengthOfLongestSubstring('pwwkew') !== 3) throw new Error('FAILED 3');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
