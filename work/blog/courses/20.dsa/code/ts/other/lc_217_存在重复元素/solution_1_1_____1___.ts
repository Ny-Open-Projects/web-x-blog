/**
 ** LeetCode 217. 存在重复元素
 ** 方案：1 ) 方案1：集合去重
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145344295
 */

export function containsDuplicate(nums: number[]): boolean {
  // 定义函数/方法 containsDuplicate
  return new Set(nums).size !== nums.length; // 返回 new Set(数组).大小 不等于 数组.长度
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (containsDuplicate([1, 2, 3]) !== false) throw new Error('FAILED 1');
  if (containsDuplicate([1, 2, 3, 1]) !== true) throw new Error('FAILED 2');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
