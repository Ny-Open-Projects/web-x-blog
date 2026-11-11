// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381943
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function multiply(num1: string, num2: string): string {
    // 定义函数/方法 multiply
    if (num1 === '0' || num2 === '0') return '0'; // 若 num1 全等于 「0」 或 num2 全等于 「0」，直接返回 「0」
    const m = num1.length,
      n = num2.length; // 把 num1.长度, 元素个数 赋值为 num2.长度 存入 映射表
    const result: number[] = new Array(m + n).fill(0); // 把 new Array(映射表 加 元素个数).fill(0); 写入 const result: number[]
    for (let i = m - 1; i >= 0; i--) {
      // 让 下标 i 从 映射表 减 1 开始计数，下标 i 不低于 0 就继续
      for (let j = n - 1; j >= 0; j--) {
        // 让 下标 j 从 元素个数 减 1 开始计数，下标 j 不低于 0 就继续
        const mul = parseInt(num1[i], 10) * parseInt(num2[j], 10); // 把 转整数(num1[下标 i]) 乘 转整数(num2[下标 j]) 存入 mul
        const p1 = i + j,
          p2 = i + j + 1; // 把 下标 i 加 下标 j, p2 赋值为 下标 i 加 下标 j 加 1 存入 p1
        const total = mul + result[p2]; // 把 mul 加 结果[p2] 存入 总和
        result[p2] = total % 10; // 把 总和 对…取模 10; 写入 result[p2]
        result[p1] += Math.floor(total / 10); // result[p1]累加 向下取整(总和 除以 10)
      }
    }
    const s = result.join(''); // 把 结果.join(「」) 存入 字符串
    const trimmed = s.replace(/^0+/, ''); // 把 字符串.replace( 除以 按位异或 0 加 除以 , 「」) 存入 trimmed
    return trimmed === '' ? '0' : trimmed; // 返回 trimmed 全等于 「」 ? 「」 : trimmed
  }
  const cases: { a: string; b: string; want: string }[] = [
    { a: '2', b: '3', want: '6' },
    { a: '123', b: '456', want: '56088' },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = multiply(c.a, c.b); // 把 multiply(字符.数组, 字符.b) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
