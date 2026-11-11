// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function isSubsequence(s: string, t: string): boolean {
    // 定义判定函数 isSubsequence
    let i = 0; // 把 0 存入 下标 i
    for (let j = 0; j < t.length; j++) {
      // 让 下标 j 从 0 开始计数，下标 j 小于 另一字符串.长度 就继续
      if (i < s.length && s[i] === t[j]) i++; // 若 下标 i 小于 字符串.长度 且 字符串[下标 i] 全等于 另一字符串[下标 j]) 下标 i 加一 ;
    }
    return i === s.length; // 返回 下标 i 全等于 字符串.长度
  }
  const cases = [
    { s: 'abc', t: 'ahbgdc', want: true },
    { s: 'axc', t: 'ahbgdc', want: false },
    { s: '', t: 'ahbgdc', want: true },
    { s: 'abc', t: 'def', want: false },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = isSubsequence(c.s, c.t); // 把 isSubsequence(字符.字符串, 字符.另一字符串) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
