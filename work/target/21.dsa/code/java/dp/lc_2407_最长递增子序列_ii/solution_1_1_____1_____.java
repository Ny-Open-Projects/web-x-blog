// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144827578
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class lc2407_solution111 { // 定义类型
  public int lengthOfLIS(int[] nums, int k) { // 定义函数/方法 lengthOfLIS
    if (nums.length == 0) return 0; // 若 数组.长度 等于 0，直接返回 0
    TreeSet<Integer> set = new TreeSet<>(); // 把 new TreeSet 小于 超过 (); 写入 TreeSet<Integer> set
    for (int v : nums) set.add(v); // for (int 值 : 数组) set 追加 值);
    ArrayList<Integer> vals =
        new ArrayList<>(set); // 把 new ArrayList 小于 超过 (set); 写入 ArrayList<Integer> vals
    int m = vals.size(); // 把 vals.大小() 存入 映射表
    HashMap<Integer, Integer> comp =
        new HashMap<>(); // 把 new HashMap 小于 超过 (); 写入 HashMap<Integer, Integer> comp
    for (int i = 0; i < m; i++) comp.put(vals.get(i), i); // 让 下标 i 从 0 开始计数，下标 i 小于 映射表 就继续
    int size = 1; // 把 1 存入 大小
    while (size < m) size <<= 1; // 循环，直到不满足「大小 小于 映射表) 大小 小于 不超过 1;」
    int[] tree = new int[2 * size]; // 把 new int[2 乘 大小]; 写入 int[] tree
    int ans = 0; // 把 0 存入 答案
    for (int x : nums) { // for (int x : 数组) {
      int ci = comp.get(x); // 把 comp 查找 x) 存入 ci
      int lo = lowerBound(vals, x - k); // 把 lowerBound(vals, x 减 下标 k) 存入 左边界
      int best = 0; // 把 0 存入 当前最优
      if (lo <= ci - 1)
        best =
            query(
                tree, size, lo, ci - 1); // 若 左边界 不超过 ci 减 1) 当前最优 赋值为 query(tree, 大小, 左边界, ci 减 1);
      int cur = best + 1; // 把 当前最优 加 1 存入 当前值
      if (cur > ans) ans = cur; // 若 当前值 超过 答案) 答案 赋值为 当前值;
      update(tree, size, ci, cur); // update(tree, 大小, ci, 当前值);
    }
    return ans; // 返回 答案
  }

  private void update(int[] tree, int size, int pos, int val) { // 定义函数/方法 update
    pos += size; // pos累加 大小
    if (val > tree[pos]) tree[pos] = val; // 若 值 超过 tree[pos]) tree[pos] 赋值为 值;
    pos >>= 1; // 把 1; 写入 pos >>
    while (pos > 0) { // 循环，直到不满足「pos 超过 0」
      tree[pos] =
          Math.max(
              tree[2 * pos],
              tree[2 * pos + 1]); // 把 Math.取较大值 tree[2 乘 pos], tree[2 乘 pos 加 1]); 写入 tree[pos]
      pos >>= 1; // 把 1; 写入 pos >>
    }
  }

  private int query(int[] tree, int size, int l, int r) { // 定义函数/方法 query
    l += size;
    r += size; // 把 大小; 右指针 累加 大小; 写入 l +
    int res = 0; // 把 0 存入 结果
    while (l <= r) { // 循环，直到不满足「左指针 不超过 右指针」
      if ((l & 1) == 1) {
        res = Math.max(res, tree[l]);
        l++;
      }
      if ((r & 1) == 0) {
        res = Math.max(res, tree[r]);
        r--;
      }
      l >>= 1;
      r >>= 1; // 把 1; 右指针 超过 不低于 1; 写入 l >>
    }
    return res; // 返回 结果
  }

  private int lowerBound(List<Integer> vals, int target) { // 定义函数/方法 lowerBound
    int lo = 0, hi = vals.size(); // 把 0, 右边界 赋值为 vals.大小() 存入 左边界
    while (lo < hi) { // 循环，直到不满足「左边界 小于 右边界」
      int mid = (lo + hi) >>> 1; // 把 (左边界 加 右边界) 超过 超过 超过 1 存入 中点
      if (vals.get(mid) < target) lo = mid + 1; // 若 vals 查找 中点) 小于 目标值) 左边界 赋值为 中点 加 1;
      else hi = mid; // 否则
    }
    return lo; // 返回 左边界
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    lc2407_solution111 s =
        new lc2407_solution111(); // 把 new lc2407_solution111(); 写入 lc2407_solution111 s
    int got = s.lengthOfLIS(new int[] {4, 2, 1, 4, 3, 4, 5, 8, 15}, 3);
    if (got != 5) {
      System.out.println("FAIL got " + got);
      throw new RuntimeException("FAILED");
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
