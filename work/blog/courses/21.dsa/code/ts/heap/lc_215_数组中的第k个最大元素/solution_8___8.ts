// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// Faithful translation of python reference. Self-check via demo().
function _quickselect(nums: number[], l: number, r: number, k: number): number {
  // 定义函数/方法 _quickselect
  if (l === r) return nums[l]; // 若 左指针 全等于 右指针，直接返回 数组[左指针]
  const pidx = l + Math.floor(Math.random() * (r - l + 1)); // 把 左指针 加 向下取整(Math.random() 乘 (右指针 减 左指针 加 1)) 存入 pidx
  const t0 = nums[l];
  nums[l] = nums[pidx];
  nums[pidx] = t0; // 把 数组[左指针]; 数组[左指针] 赋值为 数组[pidx]; 数组[pidx] 赋值为 t0 存入 t0
  const pivot = nums[l]; // 把 数组[左指针] 存入 pivot
  let i = l - 1,
    j = r + 1; // 把 左指针 减 1, 下标 j 赋值为 右指针 加 1 存入 下标 i
  while (i < j) {
    // 循环，直到不满足「下标 i 小于 下标 j」
    i++;
    while (nums[i] < pivot) i++; // 下标 i 加一 ; while (数组[下标 i] 小于 pivot) 下标 i 加一 ;
    j--;
    while (nums[j] > pivot) j--; // 下标 j 减一 ; while (数组[下标 j] 超过 pivot) 下标 j 减一 ;
    if (i < j) {
      const t = nums[i];
      nums[i] = nums[j];
      nums[j] = t;
    }
  }
  if (k <= j)
    return _quickselect(nums, l, j, k); // 若 下标 k 不超过 下标 j，直接返回 _quickselect(数组, 左指针, 下标 j, 下标 k)
  else return _quickselect(nums, j + 1, r, k); // 否则
}
function find_kth_largest(nums: number[], k: number): number {
  // 定义函数/方法 find_kth_largest
  const a = nums.slice(); // 把 数组 截取 ) 存入 数组
  return _quickselect(a, 0, a.length - 1, a.length - k); // 返回 _quickselect(数组, 0, 数组.长度 减 1, 数组.长度 减 下标 k)
}
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases = [
    [[3, 2, 1, 5, 6, 4], 2],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4],
  ];
  const want = [5, 4]; // 把 [5, 4] 存入 want
  for (let i = 0; i < cases.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 cases.长度 就继续
    const got = find_kth_largest(cases[i][0].slice(), cases[i][1]);
    if (got !== want[i])
      throw new Error('FAIL case ' + i + ' got ' + got + ' want ' + want[i]);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
