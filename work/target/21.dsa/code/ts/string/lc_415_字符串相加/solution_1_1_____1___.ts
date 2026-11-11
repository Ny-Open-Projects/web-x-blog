/**
 ** LeetCode 415. 字符串相加
 ** 方案：1 ) 方案1：模拟竖式加法
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function addStrings(num1: string, num2: string): string {
  // 定义函数/方法 addStrings
  let i = num1.length - 1; // 把 num1.长度 减 1 存入 下标 i
  let j = num2.length - 1; // 把 num2.长度 减 1 存入 下标 j
  let carry = 0; // 把 0 存入 carry
  const result: string[] = []; // 把 []; 写入 const result: string[]
  while (i >= 0 || j >= 0 || carry) {
    // 循环，直到不满足「下标 i 不低于 0 或 下标 j 不低于 0 或 carry」
    let total = carry; // 把 carry 存入 总和
    if (i >= 0) {
      total += parseInt(num1[i], 10);
      i--;
    } // 若 下标 i 不低于 0) { 总和 累加 转整数(num1[下标 i]); 下标 i 减一 ; }
    if (j >= 0) {
      total += parseInt(num2[j], 10);
      j--;
    } // 若 下标 j 不低于 0) { 总和 累加 转整数(num2[下标 j]); 下标 j 减一 ; }
    result.push(String(total % 10)); // 把 String(总和 对…取模 10 压入栈/数组尾部
    carry = Math.floor(total / 10); // 把 向下取整(总和 除以 10) 存入 carry
  }
  return result.reverse().join(''); // 返回 结果.reverse().join('')
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (addStrings('11', '123') !== '134')
    throw new Error('FAILED: ' + addStrings('11', '123'));
  if (addStrings('0', '0') !== '0') throw new Error('FAILED zero'); // 若 addStrings(「0」, 「0」) 不等于 「0」) throw new Error(「0」);
  if (addStrings('999', '1') !== '1000') throw new Error('FAILED carry');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
