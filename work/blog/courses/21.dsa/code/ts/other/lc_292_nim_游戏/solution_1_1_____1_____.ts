/**
 ** LeetCode 292. Nim 游戏
 ** 方案：1 ) 方案1：数学推理
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145355568
 */

export function canWinNim(n: number): boolean {
  // 定义函数/方法 canWinNim
  return n % 4 !== 0; // 返回 元素个数 对…取模 4 不等于 0
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!canWinNim(1)) throw new Error('FAILED 1'); // 若 取反 canWinNim(1)) throw new Error(「FAILED 1」);
  if (canWinNim(4)) throw new Error('FAILED 4'); // 若 canWinNim(4)) throw new Error(「FAILED 4」);
  if (!canWinNim(7)) throw new Error('FAILED 7'); // 若 取反 canWinNim(7)) throw new Error(「FAILED 7」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
