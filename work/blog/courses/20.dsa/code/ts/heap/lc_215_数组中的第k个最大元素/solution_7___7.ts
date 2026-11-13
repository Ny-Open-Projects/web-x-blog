// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
// Faithful translation of python reference. Self-check via demo().
function _quickselect(nums: number[], l: number, r: number, k: number): number {
  // 定义函数/方法 _quickselect
  if (l === r) return nums[l]; // 若 左指针 全等于 右指针，直接返回 数组[左指针]
  const pidx = l + Math.floor(Math.random() * (r - l + 1)); // 把 左指针 加 向下取整(Math.random() 乘 (右指针 减 左指针 加 1)) 存入 pidx
  const t = nums[r];
  nums[r] = nums[pidx];
  nums[pidx] = t; // 把 数组[右指针]; 数组[右指针] 赋值为 数组[pidx]; 数组[pidx] 赋值为 另一字符串 存入 另一字符串
  const pivot = nums[r]; // 把 数组[右指针] 存入 pivot
  let i = l; // 把 左指针 存入 下标 i
  for (let j = l; j < r; j++) {
    // 让 下标 j 从 左指针 开始计数，下标 j 小于 右指针 就继续
    if (nums[j] <= pivot) {
      const x = nums[i];
      nums[i] = nums[j];
      nums[j] = x;
      i++;
    }
  }
  const y = nums[i];
  nums[i] = nums[r];
  nums[r] = y; // 把 数组[下标 i]; 数组[下标 i] 赋值为 数组[右指针]; 数组[右指针] 赋值为 y 存入 y
  if (i === k)
    return nums[i]; // 若 下标 i 全等于 下标 k，直接返回 数组[下标 i]
  else if (i > k) return _quickselect(nums, l, i - 1, k);
  else return _quickselect(nums, i + 1, r, k); // 否则
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
