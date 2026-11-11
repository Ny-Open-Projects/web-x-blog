/**
 ** LeetCode 326. 3 的幂
 ** 方案：1 ) 方案1：试除法
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355653
 */

export function isPowerOfThree(n: number): boolean {
  // 定义判定函数 isPowerOfThree
  while (n !== 0 && n % 3 === 0) n = Math.floor(n / 3);
  return n === 1; // 返回 元素个数 全等于 1
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!isPowerOfThree(1)) throw new Error('FAILED 1'); // 若 取反 isPowerOfThree(1)) throw new Error(「FAILED 1」);
  if (!isPowerOfThree(27)) throw new Error('FAILED 27'); // 若 取反 isPowerOfThree(27)) throw new Error(「FAILED 27」);
  if (isPowerOfThree(0)) throw new Error('FAILED 0'); // 若 isPowerOfThree(0)) throw new Error(「FAILED 0」);
  if (isPowerOfThree(2)) throw new Error('FAILED 2'); // 若 isPowerOfThree(2)) throw new Error(「FAILED 2」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
