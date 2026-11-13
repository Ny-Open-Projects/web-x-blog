// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function findContentChildren(g: number[], s: number[]): number {
    // 定义函数/方法 findContentChildren
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let i = 0; // 把 0 存入 下标 i
    for (const cookie of s) {
      // for (const cookie of 字符串) {
      if (i < g.length && cookie >= g[i]) i++; // 若 下标 i 小于 g.长度 且 cookie 不低于 g[下标 i]) 下标 i 加一 ;
    }
    return i; // 返回 下标 i
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
