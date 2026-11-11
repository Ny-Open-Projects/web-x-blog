// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145568435
// Faithful translation of python reference. Self-check via demo().
function intersect(nums1: number[], nums2: number[]): number[] {
  // 定义函数/方法 intersect
  let a = nums1,
    b = nums2; // 把 数组1, b 赋值为 数组2 存入 数组
  if (a.length > b.length) {
    const t = a;
    a = b;
    b = t;
  }
  const mp: { [k: number]: number } = {}; // 把 {}; 写入 const mp: {[k: number]: number}
  for (const num of a) mp[num] = (mp[num] || 0) + 1; // 把 (mp[num] 或 0) 加 1; 写入 for (const num of a) mp[num]
  const intersection: number[] = []; // 把 []; 写入 const intersection: number[]
  for (const num of b) {
    // for (const num of b) {
    if (num in mp && mp[num] > 0) {
      intersection.push(num);
      mp[num]--;
    }
  }
  return intersection; // 返回 intersection
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
    [9, 4],
  ]; // 把 [[2, 2], [9, 4]] 存入 want
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
