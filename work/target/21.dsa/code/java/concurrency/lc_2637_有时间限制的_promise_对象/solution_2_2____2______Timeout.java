// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145371693
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖
import java.util.concurrent.*; // 引入依赖

class solution22Timeout { // 定义类型
  static <T> T timeLimit(Callable<T> fn, long tMillis) {
    ExecutorService ex =
        Executors
            .newSingleThreadExecutor(); // 把 Executors.newSingleThreadExecutor(); 写入 ExecutorService
                                        // ex
    Future<T> f = ex.submit(fn); // 把 ex.submit(fn); 写入 Future<T> f
    try { // try {
      return f.get(tMillis, TimeUnit.MILLISECONDS); // 返回 f 查找 tMillis, TimeUnit.MILLISECONDS)
    } catch (TimeoutException e) { // } catch (TimeoutException e) {
      f.cancel(true); // f.cancel(true);
      throw new RuntimeException(
          "Time Limit Exceeded"); // throw new RuntimeException(「Time Limit Exceeded」);
    } catch (Exception e) { // } catch (Exception e) {
      throw new RuntimeException(e); // throw new RuntimeException(e);
    } finally { // } finally {
      ex.shutdownNow(); // ex.shutdownNow();
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Callable<Integer> slow =
        () -> {
          Thread.sleep(150);
          return 150;
        };
    // fast enough: timeout 300ms, work 150ms -> returns 150
    int v = timeLimit(slow, 300); // 把 timeLimit(慢指针, 300) 存入 值
    if (v != 150) { // 若 值 不等于 150
      System.out.println("FAIL fast case got " + v); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    // too slow: timeout 100ms, work 150ms -> Time Limit Exceeded
    boolean threw = false; // 把 false; 写入 boolean threw
    try { // try {
      timeLimit(slow, 100); // timeLimit(慢指针, 100);
    } catch (RuntimeException e) { // } catch (RuntimeException e) {
      threw =
          "Time Limit Exceeded"
              .equals(e.getMessage()); // 把 「Time Limit Exceeded」.equals(e.getMessage()); 写入 threw
    }
    if (!threw) { // 若 取反 threw
      System.out.println("FAIL expected Time Limit Exceeded"); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
