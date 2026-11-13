/**
 ** LeetCode 2721. 并行执行异步函数
 ** 方案：2 ) 方案2：使用 then/catch 语法（捕获错误，返回 {ok, value|error}）
 ** 来源：https://blog.csdn.net/tyro_java/article/details/145383126
 */

export async function promiseAll(
  functions: (() => Promise<any>)[],
): Promise<any[]> {
  // 定义函数/方法 promiseAll
  const tasks = functions.map(async (fn) => {
    try {
      // try {
      const value = await fn(); // 把 await fn() 存入 value
      return { ok: true, value }; // 返回 { ok: true, value }
    } catch (error) {
      // } catch (error) {
      return { ok: false, error }; // 返回 { ok: false, error }
    }
  }); // });
  return Promise.all(tasks); // 返回 Promise.all(tasks)
}

export async function demo(): Promise<void> {
  // 程序入口：跑内嵌自测用例
  const results = await promiseAll([
    () => Promise.resolve(1),
    () => Promise.reject(new Error('boom')),
    () => Promise.resolve(3),
  ]); // ]);
  if (!results[0].ok || results[0].value !== 1) throw new Error('FAILED[0]');
  if (results[1].ok) throw new Error('FAILED[1] expected error');
  if (!results[2].ok || results[2].value !== 3) throw new Error('FAILED[2]');
  console.log('PASS'); // 全部用例通过，输出 PASS
}

demo().catch((e) => {
  console.error(String(e));
  process.exit(1);
});
