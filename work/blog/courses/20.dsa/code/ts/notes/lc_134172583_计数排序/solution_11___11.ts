// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134172583
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function countSort(nums: number[]): number[] {
    // 定义函数/方法 countSort
    if (nums.length === 0) return nums; // 若 数组.长度 全等于 0，直接返回 数组
    let maxVal = nums[0],
      minVal = nums[0]; // 把 数组[0], minVal 赋值为 数组[0] 存入 maxVal
    for (const v of nums) {
      if (v > maxVal) maxVal = v;
      if (v < minVal) minVal = v;
    }
    const range = maxVal - minVal + 1; // 把 maxVal 减 minVal 加 1 存入 range
    const count = new Array(range).fill(0); // 把 new Array(range).fill(0) 存入 计数
    const output = new Array(nums.length).fill(0); // 把 new Array(数组.长度).fill(0) 存入 输出
    for (const num of nums) count[num - minVal]++; // for (const num of 数组) 计数[num 减 minVal] 加一 ;
    for (let i = 1; i < range; i++) count[i] += count[i - 1]; // 让 下标 i 从 1 开始计数，下标 i 小于 range 就继续
    for (let i = nums.length - 1; i >= 0; i--) {
      output[count[nums[i] - minVal] - 1] = nums[i];
      count[nums[i] - minVal]--;
    } // 让 下标 i 从 数组.长度 减 1 开始计数，下标 i 不低于 0 就继续
    return output; // 返回 输出
  }
  let fail = false; // 把 false 存入 fail
  const c1 = countSort(
    [
      102, 103, 108, 107, 101, 102, 102, 102, 107, 103, 109, 108, 102, 101, 104,
      102, 104, 106, 109, 102,
    ].slice(),
  );
  if (
    JSON.stringify(c1) !==
    JSON.stringify([
      101, 101, 102, 102, 102, 102, 102, 102, 102, 103, 103, 104, 104, 106, 107,
      107, 108, 108, 109, 109,
    ])
  ) {
    fail = true;
    console.log('FAIL countSort(B)=' + JSON.stringify(c1));
  }
  const c2 = countSort([5, 3, 8, 3, 1].slice()); // 把 countSort([5,3,8,3,1] 截取 )) 存入 c2
  if (JSON.stringify(c2) !== JSON.stringify([1, 3, 3, 5, 8])) {
    fail = true;
    console.log('FAIL countSort([5,3,8,3,1])=' + JSON.stringify(c2));
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
