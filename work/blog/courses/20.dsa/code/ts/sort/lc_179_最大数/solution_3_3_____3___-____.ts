// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
/**
 ** LeetCode 179. 最大数
 ** 方案：方案3（自定义比较排序-改造快排）
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
  if (largestNumber([10, 2]) !== '210')
    // 若 largestNumber([10, 2]) 不等于 「210」
    throw new Error("largestNumber([10,2]) should be '210'"); // throw new Error(「largestNumber([10,2]) should be '210'」);
  if (largestNumber([3, 30, 34, 5, 9]) !== '9534330')
    // 若 largestNumber([3, 30, 34, 5, 9]) 不等于 「9534330」
    throw new Error("largestNumber([3,30,34,5,9]) should be '9534330'");
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
