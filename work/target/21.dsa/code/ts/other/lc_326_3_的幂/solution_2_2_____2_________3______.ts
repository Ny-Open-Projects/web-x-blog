/**
 ** LeetCode 326. 3 的幂
 ** 方案：2 ) 方案2：最大 3 的幂约数判定
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355653
 */

export function isPowerOfThree(n: number): boolean {
  // 定义判定函数 isPowerOfThree
  return n > 0 && 1162261467 % n === 0; // 返回 元素个数 超过 0 且 1162261467 对…取模 元素个数 全等于 0
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
