/**
 ** LeetCode 2637. 有时间限制的 Promise 对象
 ** 方案：2 ）方案2：处理清除 Timeout
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145371693
 */

type Fn = (...params: any[]) => Promise<any>; // 定义类型

export function timeLimit(fn: Fn, t: number): Fn {
  // 定义函数/方法 timeLimit
  return async function (...args: any[]) {
    // 返回 async function(...args: any[]) {
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        reject('Time Limit Exceeded'); // reject(「Time Limit Exceeded」);
      }, t); // }, 另一字符串);
      fn(...args) // fn(...args)
        .then(resolve) // then(resolve)
        .catch(reject) // catch(reject)
        .finally(() => clearTimeout(timeout));
    }); // });
  };
}

export async function demo(): Promise<void> {
  // 程序入口：跑内嵌自测用例
  const slow = (ms: number) =>
    new Promise<number>((r) => setTimeout(() => r(ms), ms));
  // case 1: limit 50ms, fn resolves at 150ms -> reject
  let rejected = false; // 把 false 存入 rejected
  try {
    // try {
    await timeLimit((ms: number) => slow(ms), 50)(150);
  } catch (e) {
    // } catch (e) {
    rejected = true; // 把 true 存入 rejected
    if (e !== 'Time Limit Exceeded')
      throw new Error('FAILED wrong msg: ' + String(e));
  }
  if (!rejected) throw new Error('FAILED expected timeout'); // 若 取反 rejected) throw new Error(「FAILED expected timeout」);
  // case 2: limit 300ms, fn resolves at 150ms -> resolve 150
  const v = await timeLimit((ms: number) => slow(ms), 300)(150);
  if (v !== 150) throw new Error('FAILED expected 150 got ' + String(v));
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo().catch((e) => {
  console.error(String(e));
  process.exit(1);
});
