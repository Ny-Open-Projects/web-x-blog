/**
 ** LeetCode 860. 柠檬水找零
 ** 来源：https://blog.csdn.net/tyro_java/article/details/134661209
 */

export function lemonadeChange(bills: number[]): boolean {
  // 定义函数/方法 lemonadeChange
  const box: number[] = []; // 把 []; 写入 const box: number[]
  for (const money of bills) {
    // for (const money of bills) {
    let change = money - 5; // 把 money 减 5 存入 change
    if (change > 0) {
      // 若 change 超过 0
      box.sort((a, b) => b - a);
      for (let i = 0; i < box.length; i++) {
        // 让 下标 i 从 0 开始计数，下标 i 小于 box.长度 就继续
        if (box[i] <= change) {
          // 若 box[下标 i] 不超过 change
          change -= box[i]; // change累减 box[下标 i]
          box[i] = 0; // 把 0; 写入 box[i]
          if (change === 0) break; // 若 change 全等于 0) break;
        }
      }
      if (change !== 0) return false; // 若 change 不等于 0，直接返回 false
      for (let i = box.length - 1; i >= 0; i--) {
        // 让 下标 i 从 box.长度 减 1 开始计数，下标 i 不低于 0 就继续
        if (box[i] === 0) box.splice(i, 1); // 若 box[下标 i] 全等于 0) box.splice(下标 i, 1);
      }
    }
    box.push(money); // 把 money 压入栈/数组尾部
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
