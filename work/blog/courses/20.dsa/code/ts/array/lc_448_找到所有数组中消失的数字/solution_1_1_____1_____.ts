// 找到所有数组中消失的数字
// 忠实翻译 Python ref_findDisappearedNumbers: 用集合标记后按顺序收集 1..n 中缺失者

function findDisappearedNumbers(nums: number[]): number[] {
  // 定义函数/方法 findDisappearedNumbers
  const s = new Set(nums); // 把 new Set(数组) 存入 字符串
  const res: number[] = []; // 把 []; 写入 const res: number[]
  for (let i = 1; i <= nums.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 不超过 数组.长度 就继续
    if (!s.has(i)) res.push(i); // 若 取反 字符串.has(下标 i)) 结果 追加 下标 i);
  }
  return res; // 返回 结果
}

// 自检用例：(nums, 期望)
const cases: [number[], number[]][] = [
  [
    [4, 3, 2, 7, 8, 2, 3, 1],
    [5, 6],
  ],
  [[1, 1], [2]],
];

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  for (const [nums, want] of cases) {
    // for (const [数组, want] of cases) {
    const got = findDisappearedNumbers(nums); // 把 findDisappearedNumbers(数组) 存入 got
    if (got.length !== want.length || got.some((v, i) => v !== want[i])) {
      throw new Error(
        `FAIL: findDisappearedNumbers(${JSON.stringify(nums)})=${JSON.stringify(got)} want ${JSON.stringify(want)}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
