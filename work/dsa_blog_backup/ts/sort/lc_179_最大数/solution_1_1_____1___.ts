// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
/**
 ** LeetCode 179. 最大数
 ** 方案：方案1（自定义比较排序）
 */

function largestNumber(nums: number[]): string {
  // 定义函数/方法 largestNumber
  const strs = nums.map(String); // 把 数组.映射表(String) 存入 strs
  strs.sort((a, b) => {
    const ab = a + b; // 把 数组 加 b 存入 ab
    const ba = b + a; // 把 b 加 数组 存入 ba
    if (ab > ba) return -1; // 若 ab 超过 ba，直接返回 减 1
    if (ab < ba) return 1; // 若 ab 小于 ba，直接返回 1
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
