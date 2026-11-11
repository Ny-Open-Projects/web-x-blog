/**
 ** LeetCode 482. 密钥格式化
 ** 方案：1 ) 方案1：逆序分组
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145385760
 */

export function licenseKeyFormatting(s: string, k: number): string {
  // 定义函数/方法 licenseKeyFormatting
  s = s.replace(/-/g, '').toUpperCase(); // 把 字符串.replace( 除以 减 除以 g, '').toUpperCase() 存入 字符串
  const result: string[] = []; // 把 []; 写入 const result: string[]
  for (let i = s.length - 1; i >= 0; i--) {
    // 让 下标 i 从 字符串.长度 减 1 开始计数，下标 i 不低于 0 就继续
    result.push(s[i]); // 把 字符串[下标 i] 压入栈/数组尾部
    if ((result.length - 1) % k === k - 1 && i > 0) result.push('-');
  }
  return result.reverse().join(''); // 返回 结果.reverse().join('')
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (licenseKeyFormatting('abc', 1) !== 'A-B-C')
    throw new Error('FAILED: ' + licenseKeyFormatting('abc', 1));
  if (licenseKeyFormatting('5F3Z-2e-9-w', 4) !== '5-F3Z-2E9W')
    throw new Error('FAILED 2');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
