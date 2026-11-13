/**
 ** LeetCode 165. 比较版本号
 ** 方案：1 ) 方案1：按点拆分逐段比较
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function compareVersion(version1: string, version2: string): number {
  // 定义函数/方法 compareVersion
  const v1 = version1.split('.'); // 把 version1.split('.') 存入 v1
  const v2 = version2.split('.'); // 把 version2.split('.') 存入 v2
  const maxLen = Math.max(v1.length, v2.length); // 把 Math.取较大值 v1.长度, v2.长度) 存入 maxLen
  for (let i = 0; i < maxLen; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 maxLen 就继续
    const num1 = i < v1.length ? parseInt(v1[i], 10) : 0; // 把 下标 i 小于 v1.长度 ? 转整数(v1[下标 i]) : 0 存入 num1
    const num2 = i < v2.length ? parseInt(v2[i], 10) : 0; // 把 下标 i 小于 v2.长度 ? 转整数(v2[下标 i]) : 0 存入 num2
    if (num1 < num2) return -1; // 若 num1 小于 num2，直接返回 减 1
    if (num1 > num2) return 1; // 若 num1 超过 num2，直接返回 1
  }
  return 0; // 返回 0
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (compareVersion('1.01', '1.001') !== 0) throw new Error('FAILED 1');
  if (compareVersion('1.0', '1.0.0') !== 0) throw new Error('FAILED 2');
  if (compareVersion('0.1', '1.1') !== -1) throw new Error('FAILED 3');
  if (compareVersion('1.2', '1.1') !== 1) throw new Error('FAILED 4');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
