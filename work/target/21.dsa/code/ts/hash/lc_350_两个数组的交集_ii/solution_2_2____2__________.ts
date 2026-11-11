// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
// Faithful translation of python reference. Self-check via demo().
function intersect(nums1: number[], nums2: number[]): number[] {
  // 定义函数/方法 intersect
  const a = nums1.slice().sort((x, y) => x - y);
  const b = nums2.slice().sort((x, y) => x - y);
  const res: number[] = []; // 把 []; 写入 const res: number[]
  let i = 0,
    j = 0; // 把 0, 下标 j 赋值为 0 存入 下标 i
  while (i < a.length && j < b.length) {
    // 循环，直到不满足「下标 i 小于 数组.长度 且 下标 j 小于 b.长度」
    if (a[i] < b[j])
      i++; // 若 数组[下标 i] 小于 b[下标 j]) 下标 i 加一 ;
    else if (a[i] > b[j])
      j++; // 否则，若 数组[下标 i] 超过 b[下标 j]) 下标 j 加一 ;
    else {
      res.push(a[i]);
      i++;
      j++;
    } // 否则
  }
  return res; // 返回 结果
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [
      [1, 2, 2, 1],
      [2, 2],
    ],
    [
      [4, 9, 5],
      [9, 4, 9, 8, 4],
    ],
  ];
  const want = [
    [2, 2],
    [4, 9],
  ]; // 把 [[2, 2], [4, 9]] 存入 want
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = intersect(cases[i][0].slice(), cases[i][1].slice()); // 把 intersect(cases[下标 i][0] 截取 ), cases[下标 i][1] 截取 )) 存入 got
    if (got.length !== want[i].length)
      throw new Error('FAIL case ' + i + ' len mismatch');
    for (let j = 0; j < got.length; j++)
      if (got[j] !== want[i][j]) throw new Error('FAIL case ' + i); // 让 下标 j 从 0 开始计数，下标 j 小于 got.长度 就继续
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
