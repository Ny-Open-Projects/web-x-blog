/**
 ** LeetCode 649. Dota2 参议院
 ** 方案：2 ) 方案2：栈模拟
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145244562
 */

export function predictPartyVictory(senate: string): string {
  // 定义函数/方法 predictPartyVictory
  const queue: string[] = senate.split(''); // 把 senate.split(''); 写入 const queue: string[]
  const stack: string[] = []; // 把 []; 写入 const stack: string[]
  while (queue.length) {
    // 循环，直到不满足「队列.长度」
    const s = queue.shift()!; // 把 队列.shift()取反 存入 字符串
    if (stack.length === 0 || stack[stack.length - 1] === s) {
      // 若 栈.长度 全等于 0 或 栈[栈.长度 减 1] 全等于 字符串
      stack.push(s); // 把 字符串 压入栈/数组尾部
    } else {
      // 否则
      queue.push(stack.pop()!); // 把 栈 弹出 压入栈/数组尾部
    }
  }
  return stack[stack.length - 1] === 'R' ? 'Radiant' : 'Dire'; // 返回 栈[栈.长度 减 1] 全等于 'R' ? 「Radiant」 : 「Radiant」
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  if (predictPartyVictory('RD') !== 'Radiant') throw new Error('FAILED RD'); // 若 predictPartyVictory(「RD」) 不等于 「RD」) throw new Error(「RD」);
  if (predictPartyVictory('RRRDDD') !== 'Radiant')
    throw new Error('FAILED RRRDDD');
  if (predictPartyVictory('DDR') !== 'Dire') throw new Error('FAILED DDR');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
