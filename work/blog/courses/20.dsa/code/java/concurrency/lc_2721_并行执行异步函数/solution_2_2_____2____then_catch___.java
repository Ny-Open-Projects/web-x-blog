// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145383126
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖
import java.util.concurrent.*; // 引入依赖

class solution222thencatch { // 定义类型
  static class Result { // static class Result {
    final boolean ok; // final boolean ok;
    final Object value; // final Object value;

    Result(boolean ok, Object value) {
      this.ok = ok;
      this.value = value;
    }
  }

  static List<Result> promiseAll(List<Callable<Object>> functions) throws Exception {
    ExecutorService ex = Executors.newFixedThreadPool(functions.size());
    List<Future<Result>> futures =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Future<Result>> futures
    for (Callable<Object> fn : functions) { // for (Callable 小于 Object 超过 fn : functions) {
      futures.add(
          ex.submit(
              () -> { // futures 追加 ex.submit(() 减 超过 {
                try { // try {
                  return new Result(true, fn.call()); // 返回 new Result(true, fn.call())
                } catch (Exception e) { // } catch (Exception e) {
                  return new Result(false, null); // 返回 new Result(false, null)
                }
              })); // }));
    }
    List<Result> results = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Result> results
    for (Future<Result> f : futures)
      results.add(f.get()); // for (Future 小于 Result 超过 f : futures) results 追加 f 查找 ));
    ex.shutdown(); // ex.shutdown();
    return results; // 返回 results
  }

  public static void main(String[] args)
      throws Exception { // public static void main(String[] args) throws Exception {
    Callable<Object> s1 =
        () -> {
          Thread.sleep(50);
          return 1;
        };
    Callable<Object> s2 =
        () -> {
          Thread.sleep(50);
          throw new RuntimeException("boom");
        };
    Callable<Object> s3 =
        () -> {
          Thread.sleep(50);
          return 3;
        };
    List<Result> got =
        promiseAll(
            Arrays.asList(
                s1, s2, s3)); // 把 promiseAll(Arrays.asList(s1, s2, s3)); 写入 List<Result> got
    boolean ok =
        got.size() == 3 // 把 got.大小() 等于 3 写入 boolean ok
            && got.get(0).ok
            && got.get(0).value.equals(1) // 且 got 查找 0).ok 且 got 查找 0).value.equals(1)
            && !got.get(1).ok // 且 取反 got 查找 1).ok
            && got.get(2).ok
            && got.get(2).value.equals(3); // 且 got 查找 2).ok 且 got 查找 2).value.equals(3);
    if (!ok) { // 若 取反 ok
      System.out.println("FAIL promiseAll got " + got); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
