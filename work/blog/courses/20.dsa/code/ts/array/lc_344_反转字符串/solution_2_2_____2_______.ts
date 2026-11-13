/**
 ** LeetCode 344. 反转字符串
 ** 方案：1 ) 方案1：双指针
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145116781
 */

function reverseString(s: string[]): void {
  // 定义函数/方法 reverseString
  const n = s.length; // 把 字符串.长度 存入 元素个数
  for (let left = 0; left < Math.floor(n / 2); left++) {
    // 让 左边界 从 0 开始计数，左边界 小于 向下取整(元素个数 除以 2) 就继续
    const right = n - 1 - left; // 把 元素个数 减 1 减 左边界 存入 右边界
    const tmp = s[left]; // 把 字符串[左边界] 存入 临时变量
    s[left] = s[right]; // 把 字符串[右边界]; 写入 s[left]
    s[right] = tmp; // 把 临时变量; 写入 s[right]
  }
}

function eqStr(a: string[], b: string[]): boolean {
  // 定义函数/方法 eqStr
  if (a.length !== b.length) return false; // 若 数组.长度 不等于 b.长度，直接返回 false
  for (let i = 0; i < a.length; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    if (a[i] !== b[i]) return false; // 若 数组[下标 i] 不等于 b[下标 i]，直接返回 false
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const cases: [string[], string[]][] = [
    [
      ['h', 'e', 'l', 'l', 'o'],
      ['o', 'l', 'l', 'e', 'h'],
    ],
    [
      ['H', 'a', 'n', 'n', 'a', 'h'],
      ['h', 'a', 'n', 'n', 'a', 'H'],
    ],
  ];
  for (const [input, expected] of cases) {
    // for (const [input, expected] of cases) {
    reverseString(input); // reverseString(input);
    if (!eqStr(input, expected)) {
      // 若 取反 eqStr(input, expected
      throw new Error('FAIL: got ' + input + ' expected ' + expected);
    }
  }
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
