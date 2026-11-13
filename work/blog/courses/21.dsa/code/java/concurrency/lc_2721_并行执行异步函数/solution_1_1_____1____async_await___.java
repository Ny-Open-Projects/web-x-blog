// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145383126
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖
import java.util.concurrent.*; // 引入依赖

class solution111asyncawait { // 定义类型
  static <T> List<T> promiseAll(List<Callable<T>> functions) throws Exception {
    ExecutorService ex = Executors.newFixedThreadPool(functions.size());
    List<Future<T>> futures =
        ex.invokeAll(functions); // 把 ex.invokeAll(functions); 写入 List<Future<T>> futures
    List<T> results = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<T> results
    for (Future<T> f : futures)
      results.add(f.get()); // for (Future 小于 T 超过 f : futures) results 追加 f 查找 ));
    ex.shutdown(); // ex.shutdown();
    return results; // 返回 results
  }

  public static void main(String[] args)
      throws Exception { // public static void main(String[] args) throws Exception {
    Callable<Integer> d1 =
        () -> {
          Thread.sleep(50);
          return 1;
        };
    Callable<Integer> d2 =
        () -> {
          Thread.sleep(50);
          return 2;
        };
    Callable<Integer> d3 =
        () -> {
          Thread.sleep(50);
          return 3;
        };
    List<Integer> got = promiseAll(Arrays.asList(d1, d2, d3));
    List<Integer> want = Arrays.asList(1, 2, 3); // 把 Arrays.asList(1, 2, 3); 写入 List<Integer> want
    if (!got.equals(want)) { // 若 取反 got.equals(want
      System.out.println("FAIL promiseAll got " + got); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
