/**
 ** LeetCode 860. 柠檬水找零
 ** 方案：方案2：计数贪心
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134661209
 */

export function lemonadeChange(bills: number[]): boolean {
  // 定义函数/方法 lemonadeChange
  let five = 0; // 把 0 存入 five
  let ten = 0; // 把 0 存入 ten
  for (const bill of bills) {
    // for (const bill of bills) {
    if (bill === 5) {
      // 若 bill 全等于 5
      five++; // five 加一
    } else if (bill === 10) {
      // 否则，若 bill 全等于 10
      if (five === 0) return false; // 若 five 全等于 0，直接返回 false
      five--; // five 减一
      ten++; // ten 加一
    } else {
      // 否则
      if (ten > 0 && five > 0) {
        // 若 ten 超过 0 且 five 超过 0
        ten--; // ten 减一
        five--; // five 减一
      } else if (five >= 3) {
        // 否则，若 five 不低于 3
        five -= 3; // five累减 3
      } else {
        // 否则
        return false; // 返回 false
      }
    }
  }
  return true; // 返回 true
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (!lemonadeChange([5, 5, 5, 10, 20])) throw new Error('FAILED 1');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
