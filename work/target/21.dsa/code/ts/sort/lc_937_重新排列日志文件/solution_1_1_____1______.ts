// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145374559
/**
 ** LeetCode 937. 重新排列日志文件
 ** 方案：方案1（自定义排序）
 */

function reorderLogFiles(logs: string[]): string[] {
  // 定义函数/方法 reorderLogFiles
  const isDigit = (s: string) => s[0] >= '0' && s[0] <= '9';
  const splitLog = (log: string): [string, string] => {
    const idx = log.indexOf(' '); // 把 log 查找 「 」) 存入 idx
    return [log.slice(0, idx), log.slice(idx + 1)]; // 返回 [log 截取 0, idx), log 截取 idx 加 1)]
  };
  const digitLogs: string[] = []; // 把 []; 写入 const digitLogs: string[]
  const letterLogs: string[] = []; // 把 []; 写入 const letterLogs: string[]
  for (const log of logs) {
    // for (const log of logs) {
    const [, content] = splitLog(log); // 把 splitLog(log); 写入 const [, content]
    if (isDigit(content))
      digitLogs.push(log); // 若 isDigit(content)) digitLogs 追加 log);
    else letterLogs.push(log); // 否则
  }
  letterLogs.sort((a, b) => {
    const [, c1] = splitLog(a); // 把 splitLog(数组); 写入 const [, c1]
    const [, c2] = splitLog(b); // 把 splitLog(b); 写入 const [, c2]
    const d1 = isDigit(c1); // 把 isDigit(c1) 存入 d1
    const d2 = isDigit(c2); // 把 isDigit(c2) 存入 d2
    if (d1 && d2) return c1 < c2 ? -1 : c1 > c2 ? 1 : 0; // 若 d1 且 d2，直接返回 c1 小于 c2 ? 减 1 : c1 超过 c2 ? 1 : 0
    if (!d1 && !d2) {
      // 若 取反 d1 且 取反 d2
      if (c1 !== c2) return c1 < c2 ? -1 : 1; // 若 c1 不等于 c2，直接返回 c1 小于 c2 ? 减 1 : 1
      const id1 = splitLog(a)[0]; // 把 splitLog(数组)[0] 存入 id1
      const id2 = splitLog(b)[0]; // 把 splitLog(b)[0] 存入 id2
      return id1 < id2 ? -1 : id1 > id2 ? 1 : 0; // 返回 id1 小于 id2 ? 减 1 : id1 超过 id2 ? 1 : 0
    }
    return d1 ? 1 : -1; // 返回 d1 ? 1 : 减 1
  }); // });
  return letterLogs.concat(digitLogs); // 返回 letterLogs.concat(digitLogs)
}

export function demo(): void {
  // 程序入口：跑内嵌自测用例
  const logs = [
    'dig1 8 1 5 1',
    'let1 art can',
    'dig2 3 6',
    'let2 own kit dig',
    'let3 art zero',
  ];
  const got = reorderLogFiles(logs); // 把 reorderLogFiles(logs) 存入 got
  const expected = [
    'let1 art can',
    'let3 art zero',
    'let2 own kit dig',
    'dig1 8 1 5 1',
    'dig2 3 6',
  ];
  if (got.length !== expected.length || got.some((v, i) => v !== expected[i]))
    throw new Error('reorderLogFiles mismatch'); // throw new Error(「reorderLogFiles mismatch」);
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo(); // demo();
