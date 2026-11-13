// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function getResult(n: number, h: number[]): number {
    // 定义函数/方法 getResult
    let res = 0; // 把 0 存入 结果
    for (let a = 1; a <= n; a++)
      for (let b = a; b <= n; b++) {
        // 让 数组 从 1 开始计数，数组 不超过 元素个数 就继续
        let min_h = 50000; // 把 50000 存入 min_h
        for (let c = a; c <= b; c++) if (h[c] < min_h) min_h = h[c]; // 让 字符 从 数组 开始计数，字符 不超过 b 就继续
        const area = (b - a + 1) * min_h; // 把 (b 减 数组 加 1) 乘 min_h 存入 area
        if (area > res) res = area; // 若 area 超过 结果) 结果 赋值为 area;
      }
    return res; // 返回 结果
  }
  let fail = false; // 把 false 存入 fail
  if (getResult(5, [0, 2, 3, 3, 3, 2, 0]) !== 10) {
    fail = true;
    console.log('FAIL1');
  }
  if (getResult(6, [0, 2, 1, 5, 6, 2, 3, 0]) !== 10) {
    fail = true;
    console.log('FAIL2');
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
