// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355797
/** 来源: LeetCode 383 赎金信 */
export function canConstruct(ransomNote: string, magazine: string): boolean {
  // 定义函数/方法 canConstruct
  if (ransomNote.length > magazine.length) return false; // 若 ransomNote.长度 超过 magazine.长度，直接返回 false
  const cnt = new Array(26).fill(0); // 把 new Array(26).fill(0) 存入 计数
  for (const c of magazine) cnt[c.charCodeAt(0) - 97]++; // for (const 字符 of magazine) 计数[字符.charCodeAt(0) 减 97] 加一 ;
  for (const c of ransomNote) {
    // for (const 字符 of ransomNote) {
    const i = c.charCodeAt(0) - 97; // 把 字符.charCodeAt(0) 减 97 存入 下标 i
    cnt[i]--; // 计数[下标 i] 减一 ;
    if (cnt[i] < 0) return false; // 若 计数[下标 i] 小于 0，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [string, string, boolean][] = [
    ['a', 'b', false],
    ['aa', 'ab', false],
    ['aa', 'aab', true],
  ];
  for (const [r, m, want] of cases) {
    // for (const [右指针, 映射表, want] of cases) {
    const got = canConstruct(r, m); // 把 canConstruct(右指针, 映射表) 存入 got
    if (got !== want)
      throw new Error(`FAIL ransom=${r} mag=${m} want=${want} got=${got}`);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
