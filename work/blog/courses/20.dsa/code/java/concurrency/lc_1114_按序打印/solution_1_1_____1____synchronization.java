// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖
import java.util.concurrent.*; // 引入依赖

class solution111synchronization { // 定义类型
  static class Foo { // static class Foo {
    private final Semaphore sem2 =
        new Semaphore(0); // 把 new Semaphore(0); 写入 private final Semaphore sem2
    private final Semaphore sem3 =
        new Semaphore(0); // 把 new Semaphore(0); 写入 private final Semaphore sem3

    public void first(Runnable printFirst) { // 定义函数/方法 first
      printFirst.run(); // printFirst.run();
      sem2.release(); // sem2.release();
    }

    public void second(Runnable printSecond) { // 定义函数/方法 second
      try {
        sem2.acquire();
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
      }
      printSecond.run(); // printSecond.run();
      sem3.release(); // sem3.release();
    }

    public void third(Runnable printThird) { // 定义函数/方法 third
      try {
        sem3.acquire();
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
      }
      printThird.run(); // printThird.run();
    }
  }

  public static void main(String[] args)
      throws Exception { // public static void main(String[] args) throws Exception {
    Foo foo = new Foo(); // 把 new Foo(); 写入 Foo foo
    List<String> order = Collections.synchronizedList(new ArrayList<>());
    Thread t2 = new Thread(() -> foo.second(() -> order.add("second")));
    Thread t1 = new Thread(() -> foo.first(() -> order.add("first")));
    Thread t3 = new Thread(() -> foo.third(() -> order.add("third")));
    // start in scrambled order to prove synchronization works
    t2.start(); // t2.起点();
    t1.start(); // t1.起点();
    t3.start(); // t3.起点();
    t1.join();
    t2.join();
    t3.join(); // 拼接为字符串
    List<String> want = Arrays.asList("first", "second", "third");
    if (!order.equals(want)) { // 若 取反 order.equals(want
      System.out.println("FAIL order=" + order); // 打印输出
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
