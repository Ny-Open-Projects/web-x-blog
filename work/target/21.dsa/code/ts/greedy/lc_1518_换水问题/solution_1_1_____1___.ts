// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386044
export function demo(): void {
  // 程序入口：跑内嵌自测用例
  function numWaterBottles(numBottles: number, numExchange: number): number {
    // 定义函数/方法 numWaterBottles
    let ans = numBottles,
      empty = numBottles; // 把 numBottles, empty 赋值为 numBottles 存入 答案
    while (empty >= numExchange) {
      // 循环，直到不满足「empty 不低于 numExchange」
      const newB = Math.floor(empty / numExchange); // 把 向下取整(empty 除以 numExchange) 存入 newB
      ans += newB; // 答案累加 newB
      empty = newB + (empty % numExchange); // 把 newB 加 (empty 对…取模 numExchange) 存入 empty
    }
    return ans; // 返回 答案
  }
  let fail = false; // 把 false 存入 fail
  if (numWaterBottles(9, 3) !== 13) {
    fail = true;
    console.log('FAIL1');
  } // 若 numWaterBottles(9,3) 不等于 13){fail 赋值为 true;输出(「FAIL1」);}
  if (numWaterBottles(15, 4) !== 19) {
    fail = true;
    console.log('FAIL2');
  } // 若 numWaterBottles(15,4) 不等于 19){fail 赋值为 true;输出(「FAIL2」);}
  if (fail) throw new Error('FAILED'); // 若 fail) throw new Error(「FAILED」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}
demo(); // demo();
