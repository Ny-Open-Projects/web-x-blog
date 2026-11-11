// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// Faithful translation of python reference. Self-check via demo().
function quickselect(nums: number[], l: number, r: number, k: number): number {
  // 定义函数/方法 quickselect
  if (l === r) return nums[k]; // 若 左指针 全等于 右指针，直接返回 数组[下标 k]
  const pivot = nums[l]; // 把 数组[左指针] 存入 pivot
  let i = l - 1,
    j = r + 1; // 把 左指针 减 1, 下标 j 赋值为 右指针 加 1 存入 下标 i
  while (i < j) {
    // 循环，直到不满足「下标 i 小于 下标 j」
    while (true) {
      i++;
      if (nums[i] <= pivot) continue;
      break;
    }
    while (true) {
      j--;
      if (nums[j] >= pivot) continue;
      break;
    }
    if (i < j) {
      const t = nums[i];
      nums[i] = nums[j];
      nums[j] = t;
    }
  }
  return k <= j ? quickselect(nums, l, j, k) : quickselect(nums, j + 1, r, k);
}
function findKthLargest(nums: number[], k: number): number {
  // 定义函数/方法 findKthLargest
  const n = nums.length; // 把 数组.长度 存入 元素个数
  return quickselect(nums.slice(), 0, n - 1, n - k); // 返回 quickselect(数组 截取 ), 0, 元素个数 减 1, 元素个数 减 下标 k)
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [[1], 1],
    [[2, 1, 3], 1],
    [[2, 1, 1, 3], 1],
  ];
  const want = [1, 3, 3]; // 把 [1, 3, 3] 存入 want
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = findKthLargest(cases[i][0].slice(), cases[i][1]); // 把 findKthLargest(cases[下标 i][0] 截取 ), cases[下标 i][1]) 存入 got
    if (got !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
