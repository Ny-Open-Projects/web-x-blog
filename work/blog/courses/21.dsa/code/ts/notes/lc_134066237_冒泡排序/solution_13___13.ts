// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
// 忠实翻译 python solution_13：bubble_sort_v3 提前终止版
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function bubbleSortV3(nums: number[]): void {
    // 定义函数/方法 bubbleSortV3
    let length = nums.length; // 把 数组.长度 存入 长度
    let sorted = false; // 把 false 存入 sorted
    while (!sorted) {
      // 循环，直到不满足「取反 sorted」
      sorted = true; // 把 true 存入 sorted
      for (let i = 0; i < length - 1; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 长度 减 1 就继续
        if (nums[i] > nums[i + 1]) {
          // 若 数组[下标 i] 超过 数组[下标 i 加 1]
          const t = nums[i]; // 把 数组[下标 i] 存入 另一字符串
          nums[i] = nums[i + 1]; // 把 数组[下标 i 加 1]; 写入 nums[i]
          nums[i + 1] = t; // 把 另一字符串; 写入 nums[i + 1]
          sorted = false; // 把 false 存入 sorted
        }
      }
      length -= 1; // 长度累减 1
    }
  }
  const cases: { in: number[]; want: number[] }[] = [
    { in: [5, 4, 3, 2, 1], want: [1, 2, 3, 4, 5] },
    { in: [1, 2, 3], want: [1, 2, 3] },
    { in: [], want: [] },
    { in: [2, 2, 1], want: [1, 2, 2] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const arr = c.in.slice(); // 把 字符.in 截取 ) 存入 数组
    bubbleSortV3(arr); // bubbleSortV3(数组);
    if (JSON.stringify(arr) !== JSON.stringify(c.want)) {
      // 若 JSON.stringify(数组) 不等于 JSON.stringify(字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL bubble_sort_v3(' +
          JSON.stringify(c.in) +
          ')=' +
          JSON.stringify(arr) +
          ' want ' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) {
    // 若 fail
    throw new Error('FAILED'); // throw new Error(「FAILED」);
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
