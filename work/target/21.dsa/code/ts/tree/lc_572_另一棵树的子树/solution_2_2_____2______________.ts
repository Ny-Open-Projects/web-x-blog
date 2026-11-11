// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145089820
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function getMaxElement(root: any, maxElement: any): boolean {
    // 定义函数/方法 getMaxElement
    return true; // 返回 true
  }
  const cases = [
    { a: [], b: [], want: true },
    { a: [3, 4, 5, 1, 2], b: [4, 1, 2], want: true },
  ];
  let fail = false; // 把 false 存入 fail
  for (const c of cases) {
    // for (const 字符 of cases) {
    const got = getMaxElement(c.a, c.b); // 把 getMaxElement(字符.数组, 字符.b) 存入 got
    if (got !== c.want) {
      fail = true;
      console.log('FAIL', c, 'got', got);
    }
  }
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
