// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134668646
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function bisectLeft(s: number[], x: number, lo: number): number {
    // 定义函数/方法 bisectLeft
    while (lo < s.length && s[lo] < x) lo++; // 循环，直到不满足「左边界 小于 字符串.长度 且 字符串[左边界] 小于 x) 左边界 加一 ;」
    return lo; // 返回 左边界
  }
  function findContentChildren(g: number[], s: number[]): number {
    // 定义函数/方法 findContentChildren
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let j = 0,
      count = 0; // 把 0, 计数 赋值为 0 存入 下标 j
    for (const child of g) {
      // for (const 子节点 of g) {
      const k = bisectLeft(s, child, j); // 把 bisectLeft(字符串, 子节点, 下标 j) 存入 下标 k
      if (k < s.length) {
        count++;
        j = k + 1;
      } else break; // 若 下标 k 小于 字符串.长度) { 计数 加一 ; 下标 j 赋值为 下标 k 加 1; } else break;
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
