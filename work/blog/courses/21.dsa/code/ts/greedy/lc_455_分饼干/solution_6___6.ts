// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function findContentChildren(g: number[], s: number[]): number {
    // 定义函数/方法 findContentChildren
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let j = 0; // 把 0 存入 下标 j
    let n = s.length,
      count = 0; // 把 字符串.长度, 计数 赋值为 0 存入 元素个数
    for (const child of g) {
      // for (const 子节点 of g) {
      while (j < n && s[j] < child) j++; // 循环，直到不满足「下标 j 小于 元素个数 且 字符串[下标 j] 小于 子节点) 下标 j 加一 ;」
      if (j < n) {
        count++;
        j++;
      } else break; // 若 下标 j 小于 元素个数) { 计数 加一 ; 下标 j 加一 ; } else break;
    }
    return count; // 返回 计数
  }
  const cases: { g: number[]; s: number[]; want: number }[] = [
    { g: [1, 2, 3], s: [1, 1], want: 1 },
    { g: [1, 2], s: [1, 2, 3], want: 2 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = findContentChildren(c.g.slice(), c.s.slice()); // 把 findContentChildren(字符.g 截取 ), 字符.字符串 截取 )) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
