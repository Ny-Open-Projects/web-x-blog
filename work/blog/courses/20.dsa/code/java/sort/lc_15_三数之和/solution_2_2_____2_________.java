// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Sum3S2 { // 定义类型
  static List<List<Integer>> threeSum(int[] nums) { // 定义函数/方法 threeSum
    List<List<Integer>> ans =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> ans
    Arrays.sort(nums); // 排序
    int n = nums.length; // 把 数组.长度 存入 元素个数
    for (int i = 0; i < n; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 元素个数 就继续
      if (i > 0 && nums[i] == nums[i - 1])
        continue; // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
      int left = i + 1, right = n - 1; // 把 下标 i 加 1, 右边界 赋值为 元素个数 减 1 存入 左边界
      while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
        int sum = nums[i] + nums[left] + nums[right]; // 把 数组[下标 i] 加 数组[左边界] 加 数组[右边界] 存入 累计和
        if (sum == 0) { // 若 累计和 等于 0
          ans.add(
              Arrays.asList(
                  nums[i],
                  nums[left],
                  nums[right])); // 答案 追加 Arrays.asList(数组[下标 i], 数组[左边界], 数组[右边界]));
          while (left < right && nums[left] == nums[left + 1])
            left++; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 等于 数组[左边界 加 1]) 左边界 加一 ;」
          left++; // 左边界 加一
          while (left < right && nums[right] == nums[right - 1])
            right--; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 等于 数组[右边界 减 1]) 右边界 减一 ;」
          right--; // 右边界 减一
        } else if (sum < 0) left++; // 否则，若 累计和 小于 0) 左边界 加一 ;
        else right--; // 否则
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
    if (!eqLL(Sum3S2.threeSum(new int[] {1, 2, 3}), new ArrayList<>())) {
      ok = false;
      System.out.println("FAIL empty");
    }
    List<List<Integer>> want = Arrays.asList(Arrays.asList(-1, -1, 2), Arrays.asList(-1, 0, 1));
    if (!eqLL(Sum3S2.threeSum(new int[] {-1, 0, 1, 2, -1, -4}), want)) {
      ok = false;
      System.out.println("FAIL case2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
