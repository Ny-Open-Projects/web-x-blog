// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145115578
/**
 ** LeetCode 167. 两数之和 II - 输入有序数组
 ** 方案2: 双指针
 */

function twoSum(numbers: number[], target: number): number[] {
  // 定义函数/方法 twoSum
  let low = 0; // 把 0 存入 low
  let high = numbers.length - 1; // 把 numbers.长度 减 1 存入 high
  while (low < high) {
    // 循环，直到不满足「low 小于 high」
    const sum = numbers[low] + numbers[high]; // 把 numbers[low] 加 numbers[high] 存入 累计和
    if (sum === target) {
      // 若 累计和 全等于 目标值
      return [low + 1, high + 1]; // 返回 [low 加 1, high 加 1]
    } else if (sum < target) {
      // 否则，若 累计和 小于 目标值
      ++low; // 加一 low;
    } else {
      // 否则
      --high; // 减一 high;
    }
  }
  return [-1, -1]; // 返回 [ 减 1, 减 1]
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function eqArr(a: number[], b: number[]): boolean {
    // 定义函数/方法 eqArr
    if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return true; // 返回 true
  }
  const cases: { in: [number[], number]; want: number[] }[] = [
    { in: [[2, 7, 11, 15], 9], want: [1, 2] },
    { in: [[2, 3, 4], 6], want: [1, 3] },
    { in: [[-1, 0], -1], want: [1, 2] },
    { in: [[1, 2, 3, 4, 5], 10], want: [-1, -1] },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = twoSum(c.in[0], c.in[1]); // 把 twoSum(字符.in[0], 字符.in[1]) 存入 got
    if (!eqArr(got, c.want)) {
      // 若 取反 eqArr(got, 字符.want
      fail = true; // 把 true 存入 fail
      console.log(
        'FAIL twoSum(' +
          JSON.stringify(c.in[0]) +
          ',' +
          c.in[1] +
          ')=' +
          JSON.stringify(got) +
          ' want ' +
          JSON.stringify(c.want),
      ); // 打印输出
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
