// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function is_safe(r: number, g: number): boolean {
    // 定义判定函数 is_safe
    return (
      0 <= r && r <= 3 && 0 <= g && g <= 3 && (r === 0 || r === 3 || r === g)
    );
  }
  const cases = [
    { r: 3, g: 3, want: true },
    { r: 3, g: 1, want: true },
    { r: 2, g: 2, want: true },
    { r: 1, g: 3, want: false },
    { r: 0, g: 0, want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    if (is_safe(c.r, c.g) !== c.want) {
      fail = true;
      console.log('FAIL is_safe(' + c.r + ',' + c.g + ')=' + is_safe(c.r, c.g));
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
