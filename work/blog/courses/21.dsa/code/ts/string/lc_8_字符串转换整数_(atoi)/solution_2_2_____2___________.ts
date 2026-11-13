/**
 ** LeetCode 8. 字符串转换整数 (atoi)
 ** 方案：2 ) 方案2：直接扫描
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function myAtoi(s: string): number {
  // 定义函数/方法 myAtoi
  s = s.trim(); // 把 字符串.trim() 存入 字符串
  if (!s) return 0; // 若 取反 字符串，直接返回 0
  let i = 0; // 把 0 存入 下标 i
  let sign = 1; // 把 1 存入 sign
  if (s[0] === '+')
    i++; // 若 字符串[0] 全等于 ' 加 ') 下标 i 加一 ;
  else if (s[0] === '-') {
    sign = -1;
    i++;
  } // 否则，若 字符串[0] 全等于 ' 减 ') { sign 赋值为 减 1; 下标 i 加一 ; }
  let res = 0; // 把 0 存入 结果
  const INT_MAX = 2 ** 31 - 1; // 把 2 乘 乘 31 减 1 存入 INT_MAX
  while (i < s.length && s[i] >= '0' && s[i] <= '9') {
    const digit = parseInt(s[i], 10); // 把 转整数(字符串[下标 i]) 存入 digit
    if (
      res > Math.floor(INT_MAX / 10) ||
      (res === Math.floor(INT_MAX / 10) && digit > 7)
    ) {
      return sign === 1 ? INT_MAX : -INT_MAX - 1; // 返回 sign 全等于 1 ? INT_MAX : 减 INT_MAX 减 1
    }
    res = res * 10 + digit; // 把 结果 乘 10 加 digit 存入 结果
    i++; // 下标 i 加一
  }
  return sign * res; // 返回 sign 乘 结果
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (myAtoi('   -42') !== -42) throw new Error('FAILED 1'); // 若 myAtoi(「 减 42」) 不等于 减 42) throw new Error(「 减 42」);
  if (myAtoi('4193 with words') !== 4193) throw new Error('FAILED 2');
  if (myAtoi('words and 987') !== 0) throw new Error('FAILED 3');
  if (myAtoi('-91283472332') !== -2147483648)
    throw new Error('FAILED 4: ' + myAtoi('-91283472332'));
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
