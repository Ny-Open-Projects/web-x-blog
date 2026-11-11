// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
package com.webfault.dsa; // 引入依赖

import java.util.*; // 引入依赖

class Sum4S1 { // 定义类型
  static List<List<Integer>> fourSum(int[] nums, int target) { // 定义函数/方法 fourSum
    List<List<Integer>> quadruplets =
        new ArrayList<>(); // 把 new ArrayList 小于 超过 (); 写入 List<List<Integer>> quadruplets
    Arrays.sort(nums); // 排序
    int length = nums.length; // 把 数组.长度 存入 长度
    if (length < 4) return quadruplets; // 若 长度 小于 4，直接返回 quadruplets
    for (int i = 0; i < length - 3; i++) { // 让 下标 i 从 0 开始计数，下标 i 小于 长度 减 3 就继续
      if (i > 0 && nums[i] == nums[i - 1])
        continue; // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]) continue;
      if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) break;
      if (nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target) continue;
      for (int j = i + 1; j < length - 2; j++) { // 让 下标 j 从 下标 i 加 1 开始计数，下标 j 小于 长度 减 2 就继续
        if (j > i + 1 && nums[j] == nums[j - 1])
          continue; // 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 等于 数组[下标 j 减 1]) continue;
        if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) break;
        if (nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target) continue;
        int left = j + 1, right = length - 1; // 把 下标 j 加 1, 右边界 赋值为 长度 减 1 存入 左边界
        while (left < right) { // 循环，直到不满足「左边界 小于 右边界」
          int sum =
              nums[i]
                  + nums[j]
                  + nums[left]
                  + nums[right]; // 把 数组[下标 i] 加 数组[下标 j] 加 数组[左边界] 加 数组[右边界] 存入 累计和
          if (sum == target) { // 若 累计和 等于 目标值
            quadruplets.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
            while (left < right && nums[left] == nums[left + 1])
              left++; // 循环，直到不满足「左边界 小于 右边界 且 数组[左边界] 等于 数组[左边界 加 1]) 左边界 加一 ;」
            left++; // 左边界 加一
            while (left < right && nums[right] == nums[right - 1])
              right--; // 循环，直到不满足「左边界 小于 右边界 且 数组[右边界] 等于 数组[右边界 减 1]) 右边界 减一 ;」
            right--; // 右边界 减一
          } else if (sum < target) left++; // 否则，若 累计和 小于 目标值) 左边界 加一 ;
          else right--; // 否则
        }
      }
    }
    return quadruplets; // 返回 quadruplets
  }

  static boolean eqLL(List<List<Integer>> a, List<List<Integer>> b) { // 定义函数/方法 eqLL
    if (a.size() != b.size()) return false; // 若 数组.大小() 不等于 b.大小()，直接返回 false
    for (int i = 0; i < a.size(); i++)
      if (!a.get(i).equals(b.get(i))) return false; // 让 下标 i 从 0 开始计数，下标 i 小于 数组.大小() 就继续
    return true; // 返回 true
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    boolean ok = true; // 把 true; 写入 boolean ok
    if (!eqLL(Sum4S1.fourSum(new int[] {1, 2, 3}, 1), new ArrayList<>())) {
      ok = false;
      System.out.println("FAIL empty");
    }
    List<List<Integer>> want =
        Arrays.asList(
            Arrays.asList(-2, -1, 1, 2), Arrays.asList(-2, 0, 0, 2), Arrays.asList(-1, 0, 0, 1));
    if (!eqLL(Sum4S1.fourSum(new int[] {1, 0, -1, 0, -2, 2}, 0), want)) {
      ok = false;
      System.out.println("FAIL case2");
    }
    if (!ok) throw new RuntimeException("FAILED"); // 若 取反 ok) throw new RuntimeException(「FAILED」);
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
