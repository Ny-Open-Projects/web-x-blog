// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107475776
package com.webfault.dsa; // 引入依赖

import java.util.ArrayList; // 引入依赖
import java.util.List; // 引入依赖

// 下楼梯问题：每步可走 1/2/3 级，递归枚举所有方案并计数（方案1）
class Main { // 定义类型
  static List<List<Integer>> climbStairs(int h) { // 定义函数/方法 climbStairs
    List<List<Integer>> plans =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> plans
    List<Integer> path = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> path
    dfs(plans, path, h); // dfs(plans, 当前路径, h);
    return plans; // 返回 plans
  }

  static void dfs(List<List<Integer>> plans, List<Integer> path, int remaining) { // 定义函数/方法 dfs
    if (remaining == 0) { // 若 remaining 等于 0
      plans.add(new ArrayList<>(path)); // plans 追加 new ArrayList 小于 超过 (当前路径));
      return; // return;
    }
    for (int step : new int[] {3, 2, 1}) { // 先尝试大步，与博客一致
      if (remaining >= step) { // 若 remaining 不低于 步数
        path.add(step); // 当前路径 追加 步数);
        dfs(plans, path, remaining - step); // dfs(plans, 当前路径, remaining 减 步数);
        path.remove(path.size() - 1); // 当前路径 弹出 当前路径.大小() 减 1);
      }
    }
  }

  static boolean eqPlan(List<Integer> a, List<Integer> b) { // 定义函数/方法 eqPlan
    return a.equals(b); // 返回 数组.equals(b)
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    List<List<Integer>> p6 = climbStairs(6); // 把 climbStairs(6); 写入 List<List<Integer>> p6
    List<List<Integer>> p0 = climbStairs(0); // 把 climbStairs(0); 写入 List<List<Integer>> p0
    List<List<Integer>> p3 = climbStairs(3); // 把 climbStairs(3); 写入 List<List<Integer>> p3
    boolean ok = true; // 把 true; 写入 boolean ok
    if (p6.size() != 24) { // 若 p6.大小() 不等于 24
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL climb_stairs(6).size=" + p6.size() + " want 24"); // 打印输出
    }
    if (!eqPlan(p6.get(0), List.of(3, 3))) { // 若 取反 eqPlan(p6 查找 0), List.of(3, 3
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL climb_stairs(6)[0]=" + p6.get(0) + " want [3, 3]"); // 打印输出
    }
    if (p0.size() != 1 || !p0.get(0).isEmpty()) { // 若 p0.大小() 不等于 1 或 取反 p0 查找 0).isEmpty(
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL climb_stairs(0)=" + p0 + " want [[]]"); // 打印输出
    }
    if (p3.size() != 4) { // 若 p3.大小() 不等于 4
      ok = false; // 把 false; 写入 ok
      System.out.println("FAIL climb_stairs(3).size=" + p3.size() + " want 4"); // 打印输出
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
