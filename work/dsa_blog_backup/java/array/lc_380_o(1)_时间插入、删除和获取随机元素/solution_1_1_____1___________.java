// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145345735
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc380_solution111 { // 定义类型
  private List<Integer> nums; // private List 小于 Integer 超过 数组;
  private Map<Integer, Integer> idx; // private Map 小于 Integer, Integer 超过 idx;
  private Random rnd; // private Random rnd;

  public lc380_solution111() { // 定义函数/方法 lc380_solution111
    nums = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 数组
    idx = new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 idx
    rnd = new Random(); // 把 new Random(); 写入 rnd
  }

  public boolean insert(int val) { // 定义函数/方法 insert
    if (idx.containsKey(val)) return false; // 若 idx.containsKey(值)，直接返回 false
    idx.put(val, nums.size()); // idx.put(值, 数组.大小());
    nums.add(val); // 数组 追加 值);
    return true; // 返回 true
  }

  public boolean remove(int val) { // 定义函数/方法 remove
    if (!idx.containsKey(val)) return false; // 若 取反 idx.containsKey(值)，直接返回 false
    int i = idx.get(val); // 把 idx 查找 值) 存入 下标 i
    int last = nums.get(nums.size() - 1); // 把 数组 查找 数组.大小() 减 1) 存入 last
    nums.set(i, last); // 数组.set(下标 i, last);
    idx.put(last, i); // idx.put(last, 下标 i);
    nums.remove(nums.size() - 1); // 数组 弹出 数组.大小() 减 1);
    idx.remove(val); // idx 弹出 值);
    return true; // 返回 true
  }

  public int getRandom() { // 定义函数/方法 getRandom
    return nums.get(rnd.nextInt(nums.size())); // 返回 数组 查找 rnd.nextInt(数组.大小()))
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc380_solution111 rs =
        new lc380_solution111(); // 把 new lc380_solution111(); 写入 lc380_solution111 rs
    if (!rs.insert(1))
      throw new RuntimeException(
          "FAILED insert1"); // 若 取反 rs 插入 1)) throw new RuntimeException(「FAILED insert1」);
    if (rs.remove(2))
      throw new RuntimeException(
          "FAILED remove2"); // 若 rs 弹出 2)) throw new RuntimeException(「FAILED remove2」);
    if (!rs.insert(2))
      throw new RuntimeException(
          "FAILED insert2"); // 若 取反 rs 插入 2)) throw new RuntimeException(「FAILED insert2」);
    int g = rs.getRandom(); // 把 rs.getRandom() 存入 g
    if (g != 1 && g != 2) throw new RuntimeException("FAILED getRandom");
    if (!rs.remove(1))
      throw new RuntimeException(
          "FAILED remove1"); // 若 取反 rs 弹出 1)) throw new RuntimeException(「FAILED remove1」);
    if (rs.insert(2))
      throw new RuntimeException(
          "FAILED insert2b"); // 若 rs 插入 2)) throw new RuntimeException(「FAILED insert2b」);
    if (rs.getRandom() != 2) throw new RuntimeException("FAILED getRandom2");
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
