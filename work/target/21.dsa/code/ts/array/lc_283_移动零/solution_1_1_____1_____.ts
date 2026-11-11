/**
 ** LeetCode 283. 移动零
 ** 方案：1 ) 方案1: 双指针
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145116601
 */

// 双指针原地交换，把 0 移到末尾，保持非零元素相对顺序。
// 忠实翻译自 Python 参考实现，返回结果数组。
function moveZeroes(nums: number[]): number[] {
  // 定义函数/方法 moveZeroes
  const res = nums.slice(); // 把 数组 截取 ) 存入 结果
  let left = 0; // 把 0 存入 左边界
  for (let right = 0; right < res.length; right++) {
    // 让 右边界 从 0 开始计数，右边界 小于 结果.长度 就继续
    if (res[right] !== 0) {
      // 若 结果[右边界] 不等于 0
      const tmp = res[left]; // 把 结果[左边界] 存入 临时变量
      res[left] = res[right]; // 把 结果[右边界]; 写入 res[left]
      res[right] = tmp; // 把 临时变量; 写入 res[right]
      left++; // 左边界 加一
    }
  }
  return res; // 返回 结果
}

function eqArray(a: number[], b: number[]): boolean {
  // 定义函数/方法 eqArray
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

// 自检入口：遍历 cases 逐一比对，任一不符则 throw（非 0 退出）。
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  // (args, expected) 取自 _tools/correctness_check.py 的 lc_283_移动零 cases
  const cases: Array<{ name: string; in: number[]; want: number[] }> = [
    { name: 'case1', in: [0, 1, 0, 3, 12], want: [1, 3, 12, 0, 0] },
    { name: 'case2', in: [0], want: [0] },
    { name: 'case3', in: [1, 2, 3], want: [1, 2, 3] },
  ];
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = moveZeroes(c.in); // 把 moveZeroes(字符.in) 存入 got
    if (!eqArray(got, c.want)) {
      // 若 取反 eqArray(got, 字符.want
      throw new Error(
        `FAIL ${c.name}: got ${JSON.stringify(got)} want ${JSON.stringify(c.want)}`,
      );
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
