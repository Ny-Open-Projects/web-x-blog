/**
 ** LeetCode 76. 最小覆盖子串
 ** 来源：https://blog.csdn.net/tyro_java/article/details/133465616
 */

export function minWindow(s: string, t: string): string {
  // 定义函数/方法 minWindow
  if (!s || !t) return ''; // 若 取反 字符串 或 取反 另一字符串，直接返回 「」
  const need: { [c: string]: number } = {}; // 把 {}; 写入 const need: { [c: string]: number }
  for (const c of t) need[c] = (need[c] || 0) + 1; // 把 (need[字符] 或 0) 加 1; 写入 for (const c of t) need[c]
  let mSize = Object.keys(need).length; // 把 Object.keys(need).长度 存入 mSize
  let l = 0; // 把 0 存入 左指针
  let res = ''; // 把 「」 存入 结果
  for (let r = 0; r < s.length; r++) {
    // 让 右指针 从 0 开始计数，右指针 小于 字符串.长度 就继续
    const c = s[r]; // 把 字符串[右指针] 存入 字符
    if (c in need) {
      // 若 字符 in need
      need[c] -= 1; // need[c]累减 1
      if (need[c] === 0) mSize -= 1; // 若 need[字符] 全等于 0) mSize 累减 1;
    }
    while (mSize === 0) {
      // 循环，直到不满足「mSize 全等于 0」
      const newRes = s.substring(l, r + 1); // 把 字符串 截取 左指针, 右指针 加 1) 存入 newRes
      if (res === '' || newRes.length < res.length) res = newRes; // 若 结果 全等于 「」 或 newRes.长度 小于 结果.长度) 结果 赋值为 newRes;
      const c2 = s[l]; // 把 字符串[左指针] 存入 c2
      if (c2 in need) {
        // 若 c2 in need
        need[c2] += 1; // need[c2]累加 1
        if (need[c2] === 1) mSize += 1; // 若 need[c2] 全等于 1) mSize 累加 1;
      }
      l += 1; // 左指针累加 1
    }
  }
  return res; // 返回 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (minWindow('ADOBECODEBANC', 'ABC') !== 'BANC')
    throw new Error('FAILED 1: ' + minWindow('ADOBECODEBANC', 'ABC'));
  if (minWindow('a', 'a') !== 'a') throw new Error('FAILED 2'); // 若 minWindow(「数组」, 「数组」) 不等于 「数组」) throw new Error(「数组」);
  if (minWindow('a', 'aa') !== '') throw new Error('FAILED 3'); // 若 minWindow(「数组」, 「数组」) 不等于 「数组」) throw new Error(「数组」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
