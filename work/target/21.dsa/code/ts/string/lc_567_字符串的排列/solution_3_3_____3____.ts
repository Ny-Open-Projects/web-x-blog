/**
 ** LeetCode 567. 字符串的排列
 ** 方案：3 ) 方案3：滑动窗口 + 计数
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function checkInclusion(s1: string, s2: string): boolean {
  // 定义判定函数 checkInclusion
  if (s1.length > s2.length) return false; // 若 s1.长度 超过 s2.长度，直接返回 false
  const s1c = new Array(26).fill(0); // 把 new Array(26).fill(0) 存入 s1c
  const s2c = new Array(26).fill(0); // 把 new Array(26).fill(0) 存入 s2c
  for (let i = 0; i < s1.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 s1.长度 就继续
    s1c[s1.charCodeAt(i) - 97]++; // s1c[s1.charCodeAt(下标 i) 减 97] 加一 ;
    s2c[s2.charCodeAt(i) - 97]++; // s2c[s2.charCodeAt(下标 i) 减 97] 加一 ;
  }
  const eq = () => s1c.every((v: number, idx: number) => v === s2c[idx]);
  if (eq()) return true; // 若 eq()，直接返回 true
  for (let i = s1.length; i < s2.length; i++) {
    // 让 下标 i 从 s1.长度 开始计数，下标 i 小于 s2.长度 就继续
    s2c[s2.charCodeAt(i) - 97]++; // s2c[s2.charCodeAt(下标 i) 减 97] 加一 ;
    s2c[s2.charCodeAt(i - s1.length) - 97]--; // s2c[s2.charCodeAt(下标 i 减 s1.长度) 减 97] 减一 ;
    if (eq()) return true; // 若 eq()，直接返回 true
  }
  return false; // 返回 false
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!checkInclusion('ab', 'eidbaooo')) throw new Error('FAILED 1'); // 若 取反 checkInclusion(「ab」, 「ab」)) throw new Error(「ab」);
  if (checkInclusion('ab', 'eidboaoo')) throw new Error('FAILED 2'); // 若 checkInclusion(「ab」, 「ab」)) throw new Error(「ab」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
