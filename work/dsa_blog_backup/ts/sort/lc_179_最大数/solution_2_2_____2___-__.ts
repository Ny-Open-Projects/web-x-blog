// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
/**
 ** LeetCode 179. 最大数
 ** 方案：方案2（自定义比较排序-优化）
 */

function largestNumber(nums: number[]): string {
  // 定义函数/方法 largestNumber
  const strs = nums.map(String); // 把 数组.映射表(String) 存入 strs
  strs.sort((x, y) => {
    const xy = x + y; // 把 x 加 y 存入 xy
    const yx = y + x; // 把 y 加 x 存入 yx
    if (xy > yx) return -1; // 若 xy 超过 yx，直接返回 减 1
    if (xy < yx) return 1; // 若 xy 小于 yx，直接返回 1
    return 0; // 返回 0
  }); // });
  if (strs[0] === '0') return '0'; // 若 strs[0] 全等于 「0」，直接返回 「0」
  return strs.join(''); // 返回 strs.join(「」)
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (largestNumber([1, 2, 3]) !== '321')
    // 若 largestNumber([1, 2, 3]) 不等于 「321」
    throw new Error("largestNumber([1,2,3]) should be '321'"); // throw new Error(「largestNumber([1,2,3]) should be '321'」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
