// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Sum3S1 { // 定义类型
  static List<List<Integer>> threeSum(int[] nums) { // 定义函数/方法 threeSum
    List<List<Integer>> ans =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> ans
    Arrays.sort(nums); // 排序
    int n = nums.length; // 把 数组.长度 存入 元素个数
    for (int first = 0; first < n; first++) { // 让 first 从 0 开始计数，first 小于 元素个数 就继续
      if (first > 0 && nums[first] == nums[first - 1])
        continue; // 若 first 超过 0 且 数组[first] 等于 数组[first 减 1]) continue;
      int third = n - 1; // 把 元素个数 减 1 存入 third
      int target = -nums[first]; // 把 减 数组[first] 存入 目标值
      for (int second = first + 1;
          second < n;
          second++) { // 让 second 从 first 加 1 开始计数，second 小于 元素个数 就继续
        if (second > first + 1 && nums[second] == nums[second - 1]) continue;
        while (second < third && nums[second] + nums[third] > target) third--;
        if (second == third) break; // 若 second 等于 third) break;
        if (nums[second] + nums[third] == target) { // 若 数组[second] 加 数组[third] 等于 目标值
          ans.add(
              Arrays.asList(
                  nums[first],
                  nums[second],
                  nums[third])); // 答案 追加 Arrays.asList(数组[first], 数组[second], 数组[third]));
        }
      }
    }
    return ans; // 返回 答案
  }

  static boolean eqLL(List<List<Integer>> a, List<List<Integer>> b) { // 定义函数/方法 eqLL
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++)
      if (!a.get(i).equals(b.get(i))) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!eqLL(Sum3S1.threeSum(new int[] {1, 2, 3}), new ArrayList<>())) {
      ok = false;
      System.out.println("FAIL empty");
    }
    List<List<Integer>> want = Arrays.asList(Arrays.asList(-1, -1, 2), Arrays.asList(-1, 0, 1));
    if (!eqLL(Sum3S1.threeSum(new int[] {-1, 0, 1, 2, -1, -4}), want)) {
      ok = false;
      System.out.println("FAIL case2=" + Sum3S1.threeSum(new int[] {-1, 0, 1, 2, -1, -4}));
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
