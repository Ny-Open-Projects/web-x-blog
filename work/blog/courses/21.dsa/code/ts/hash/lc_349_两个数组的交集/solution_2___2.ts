// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133279737
/** 来源: LeetCode 349 两个数组的交集 */
export function intersection(nums1: number[], nums2: number[]): number[] {
  // 定义函数/方法 intersection
  const s1 = new Set(nums1); // 把 new Set(数组1) 存入 s1
  const res: number[] = []; // 把 []; 写入 const res: number[]
  const seen = new Set<number>(); // 把 new Set 小于 number 超过 () 存入 已见集合
  for (const v of nums2) {
    // for (const 值 of 数组2) {
    if (s1.has(v) && !seen.has(v)) {
      res.push(v);
      seen.add(v);
    } // 若 s1.has(值) 且 取反 已见集合.has(值)) { 结果 追加 值); 已见集合 追加 值); }
  }
  return res; // 返回 结果
}

function eqList(a: number[], b: number[], sortRes: boolean): boolean {
  // 定义函数/方法 eqList
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  let x = [...a],
    y = [...b]; // 把 复制的 数组 , y 赋值为 复制的 b 存入 x
  if (sortRes) {
    x.sort((m, n) => m - n);
    y.sort((m, n) => m - n);
  }
  for (let i = 0; i < x.length; i++) if (x[i] !== y[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 x.长度 就继续
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [number[], number[], number[]][] = [
    [[1, 2, 2, 1], [2, 2], [2]],
    [
      [4, 9, 5],
      [9, 4, 9, 8, 4],
      [9, 4],
    ],
    [[1, 2], [3, 4], []],
  ];
  for (const [n1, n2, want] of cases) {
    // for (const [n1, n2, want] of cases) {
    const got = intersection(n1, n2); // 把 intersection(n1, n2) 存入 got
    if (!eqList(got, want, true)) {
      // 若 取反 eqList(got, want, true
      throw new Error(
        `FAIL nums1=${JSON.stringify(n1)} nums2=${JSON.stringify(n2)} want=${JSON.stringify(want)} got=${JSON.stringify(got)}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
