// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Sum4S2 { // 定义类型
  List<List<Integer>> list =
      new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> list
  List<Integer> tmp = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<Integer> tmp
  int n; // int 元素个数;

  List<List<Integer>> fourSum(int[] nums, int target) { // 定义函数/方法 fourSum
    list = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 列表
    tmp = new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 临时变量
    n = nums.length; // 把 数组.长度; 写入 元素个数
    Arrays.sort(nums); // 排序
    dfs(nums, target, 0, 4); // dfs(数组, 目标值, 0, 4);
    return list; // 返回 列表
  }

  void dfs(int[] nums, int target, int index, int count) { // 定义函数/方法 dfs
    if (count == 0 && target == 0) { // 若 计数 等于 0 且 目标值 等于 0
      list.add(new ArrayList<>(tmp)); // 列表 追加 new ArrayList 小于 超过 (临时变量));
      return; // return;
    }
    if (count > 0) { // 若 计数 超过 0
      for (int i = index; i < n; i++) { // 让 下标 i 从 index 开始计数，下标 i 小于 元素个数 就继续
        if (i > index && nums[i] == nums[i - 1])
          continue; // 若 下标 i 超过 index 且 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
        if (tmp.isEmpty()
            || tmp.get(tmp.size() - 1)
                <= nums[i]) { // 若 临时变量.isEmpty() 或 临时变量 查找 临时变量.大小() 减 1) 不超过 数组[下标 i]
          tmp.add(nums[i]); // 临时变量 追加 数组[下标 i]);
          dfs(
              nums,
              target - nums[i],
              i + 1,
              count - 1); // dfs(数组, 目标值 减 数组[下标 i], 下标 i 加 1, 计数 减 1);
          tmp.remove(tmp.size() - 1); // 临时变量 弹出 临时变量.大小() 减 1);
        }
      }
    }
  }

  static boolean eqLL(List<List<Integer>> a, List<List<Integer>> b) { // 定义函数/方法 eqLL
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++)
      if (!a.get(i).equals(b.get(i))) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    Sum4S2 s = new Sum4S2(); // 把 new Sum4S2(); 写入 Sum4S2 s
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!eqLL(s.fourSum(new int[] {1, 2, 3}, 1), new ArrayList<>())) {
      ok = false;
      System.out.println("FAIL empty");
    }
    List<List<Integer>> want =
        Arrays.asList(
            Arrays.asList(-2, -1, 1, 2), Arrays.asList(-2, 0, 0, 2), Arrays.asList(-1, 0, 0, 1));
    if (!eqLL(s.fourSum(new int[] {1, 0, -1, 0, -2, 2}, 0), want)) {
      ok = false;
      System.out.println("FAIL case2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
