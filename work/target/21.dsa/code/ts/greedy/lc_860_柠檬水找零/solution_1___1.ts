// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function lemonadeChange(bills: number[]): boolean {
    // 定义函数/方法 lemonadeChange
    let f5 = 0,
      f10 = 0; // 把 0, f10 赋值为 0 存入 f5
    for (const b of bills) {
      // for (const b of bills) {
      if (b === 5)
        f5++; // 若 b 全等于 5) f5 加一 ;
      else if (b === 10) {
        f10++;
        f5--;
      } // 否则，若 b 全等于 10) { f10 加一 ; f5 减一 ; }
      else {
        if (f10 > 0) {
          f10--;
          f5--;
        } else {
          f5 -= 3;
        }
      } // 否则
      if (f5 < 0) return false; // 若 f5 小于 0，直接返回 false
    }
    return true; // 返回 true
  }
  const cases = [
    { in: [5, 5, 5, 10, 20], want: true },
    { in: [5, 5, 10, 10, 20], want: false },
    { in: [5, 5, 5, 5, 20], want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = lemonadeChange(c.in); // 把 lemonadeChange(字符.in) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL ' + got + ' want ' + c.want);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
