// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function seqSearch(arr: number[], target: number): number {
    // 定义函数/方法 seqSearch
    for (let i = 0; i < arr.length; i++) if (arr[i] === target) return i; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.长度 就继续
    return -1; // 返回 减 1
  }
  const cases = [
    { arr: [1, 2, 3], t: 1, want: 0 },
    { arr: [1, 2, 3], t: 3, want: 2 },
    { arr: [1, 2, 3], t: 5, want: -1 },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = seqSearch(c.arr, c.t); // 把 seqSearch(字符.数组, 字符.另一字符串) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
