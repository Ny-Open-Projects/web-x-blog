/**
 ** LeetCode 649. Dota2 参议院
 ** 方案：1 ) 方案1：贪心 + 循环队列
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145244562
 */

export function predictPartyVictory(senate: string): string {
  // 定义函数/方法 predictPartyVictory
  const n = senate.length; // 把 senate.长度 存入 元素个数
  const radiant: number[] = []; // 把 []; 写入 const radiant: number[]
  const dire: number[] = []; // 把 []; 写入 const dire: number[]
  for (let i = 0; i < n; i++) {
    // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
    if (senate[i] === 'R')
      radiant.push(i); // 若 senate[下标 i] 全等于 'R') radiant 追加 下标 i);
    else dire.push(i); // 否则
  }
  while (radiant.length && dire.length) {
    // 循环，直到不满足「radiant.长度 且 dire.长度」
    if (radiant[0] < dire[0])
      radiant.push(radiant[0] + n); // 若 radiant[0] 小于 dire[0]) radiant 追加 radiant[0] 加 元素个数);
    else dire.push(dire[0] + n); // 否则
    radiant.shift(); // 取出队首元素
    dire.shift(); // 取出队首元素
  }
  return radiant.length ? 'Radiant' : 'Dire'; // 返回 radiant.长度 ? 「Radiant」 : 「Radiant」
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
