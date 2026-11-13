/**
 ** LeetCode 860. 柠檬水找零
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134661209
 */

export function lemonadeChange(bills: number[]): boolean {
  // 定义函数/方法 lemonadeChange
  const pocket: number[] = []; // 把 []; 写入 const pocket: number[]
  for (const bill of bills) {
    // for (const bill of bills) {
    let need = bill - 5; // 把 bill 减 5 存入 need
    if (need) {
      // 若 need
      pocket.sort((a, b) => b - a);
      const used: number[] = []; // 把 []; 写入 const used: number[]
      for (const note of pocket) {
        // for (const note of pocket) {
        if (note <= need) {
          // 若 note 不超过 need
          need -= note; // need累减 note
          used.push(note); // 把 note 压入栈/数组尾部
          if (need === 0) break; // 若 need 全等于 0) break;
        }
      }
      if (need) return false; // 若 need，直接返回 false
      for (const note of used) {
        // for (const note of 已用标记) {
        const idx = pocket.indexOf(note); // 把 pocket 查找 note) 存入 idx
        if (idx >= 0) pocket.splice(idx, 1); // 若 idx 不低于 0) pocket.splice(idx, 1);
      }
    }
    pocket.push(bill); // 把 bill 压入栈/数组尾部
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!lemonadeChange([5, 5, 5, 10, 20])) throw new Error('FAILED 1');
  if (lemonadeChange([5, 5, 10, 10, 20]) !== false) throw new Error('FAILED 2');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
