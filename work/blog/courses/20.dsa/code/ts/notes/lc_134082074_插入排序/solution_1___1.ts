// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
/**
 ** 笔记：插入排序
 ** 方案：方案1（直接插入排序）
 ** 来源：python 参考忠实移植
 */

function insertionSort(nums: number[]): number[] {
  // 定义函数/方法 insertionSort
  for (let i = 1; i < nums.length; i++) {
    // 让 下标 i 从 1 开始计数，下标 i 小于 数组.长度 就继续
    const key = nums[i]; // 把 数组[下标 i] 存入 key
    let j = i - 1; // 把 下标 i 减 1 存入 下标 j
    while (j >= 0 && nums[j] > key) {
      // 循环，直到不满足「下标 j 不低于 0 且 数组[下标 j] 超过 key」
      nums[j + 1] = nums[j]; // 把 数组[下标 j]; 写入 nums[j + 1]
      j--; // 下标 j 减一
    }
    nums[j + 1] = key; // 把 key; 写入 nums[j + 1]
  }
  return nums; // 返回 数组
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases: { in: number[]; want: number[] }[] = [
    { in: [1, 2, 3], want: [1, 2, 3] },
    { in: [3, 2, 1], want: [1, 2, 3] },
    { in: [5, 1, 4, 2, 8], want: [1, 2, 4, 5, 8] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = insertionSort(c.in.slice()); // 把 insertionSort(字符.in 截取 )) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL',
        JSON.stringify(c.in),
        'want',
        JSON.stringify(c.want),
        'got',
        JSON.stringify(got),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
