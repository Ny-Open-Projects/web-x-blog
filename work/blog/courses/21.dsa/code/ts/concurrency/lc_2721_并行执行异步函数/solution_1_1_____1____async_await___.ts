/**
 ** LeetCode 2721. 并行执行异步函数
 ** 方案：1 ) 方案1：使用 async/await 语法
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145383126
 */

export async function promiseAll(
  functions: (() => Promise<any>)[],
): Promise<any[]> {
  // 定义函数/方法 promiseAll
  return new Promise((resolve, reject) => {
    if (functions.length === 0) {
      // 若 functions.长度 全等于 0
      resolve([]); // resolve([]);
      return; // return;
    }
    const res: any[] = new Array(functions.length).fill(null); // 把 new Array(functions.长度).fill(null); 写入 const res: any[]
    let resolvedCount = 0; // 把 0 存入 resolvedCount
    functions.forEach(async (el, idx) => {
      try {
        // try {
        const subResult = await el(); // 把 await el() 存入 subResult
        res[idx] = subResult; // 把 subResult; 写入 res[idx]
        resolvedCount++; // resolvedCount 加一
        if (resolvedCount === functions.length) {
          // 若 resolvedCount 全等于 functions.长度
          resolve(res); // resolve(结果);
        }
      } catch (err) {
        // } catch (err) {
        reject(err); // reject(err);
      }
    }); // });
  }); // });
}

export async function demo(): Promise<void> {
  // 程序入口：跑内嵌自测用例
  const r1 = await promiseAll([
    () => Promise.resolve(1),
    () => Promise.resolve(2),
    () => Promise.resolve(3),
  ]); // ]);
  if (JSON.stringify(r1) !== JSON.stringify([1, 2, 3])) {
    // 若 JSON.stringify(r1) 不等于 JSON.stringify([1, 2, 3]
    throw new Error('FAILED: ' + JSON.stringify(r1)); // throw new Error(「FAILED: 」 加 JSON.stringify(r1));
  }
  const r2 = await promiseAll([]); // 把 await promiseAll([]) 存入 r2
  if (JSON.stringify(r2) !== '[]')
    throw new Error('FAILED empty: ' + JSON.stringify(r2));
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo().catch((e) => {
  console.error(String(e));
  process.exit(1);
});
