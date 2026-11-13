// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134083295
package com.webfault.dsa; // 引入依赖

import java.util.Arrays; // 引入依赖

/**
 * 归并排序 忠实翻译自 python/notes/lc_134083295_归并排序/solution_6___6.py 运行即自检：失败抛 RuntimeException（非 0
 * 退出），通过打印 PASS
 */
class Main { // 定义类型

  static void mergeSort(int[] nums) { // 定义函数/方法 mergeSort
    msFn(nums, 0, nums.length - 1); // msFn(数组, 0, 数组.长度 减 1);
  }

  static void msFn(int[] arr, int left, int right) { // 定义函数/方法 msFn
    if (left >= right) { // 若 左边界 不低于 右边界
      return; // return;
    }
    int mid = left + (right - left) / 2; // 把 (左边界 加 右边界) 除以 2 存入 中点
    msFn(arr, left, mid); // msFn(数组, 左边界, 中点);
    msFn(arr, mid + 1, right); // msFn(数组, 中点 加 1, 右边界);
    merge(arr, left, mid, right); // merge(数组, 左边界, 中点, 右边界);
  }

  static void merge(int[] arr, int left, int mid, int right) { // 定义函数/方法 merge
    int[] temp = new int[right - left + 1]; // 把 new int[右边界 减 左边界 加 1]; 写入 int[] temp
    int i = left, j = mid + 1, k = 0; // 把 左边界, 下标 j 赋值为 中点 加 1, 下标 k 赋值为 0 存入 下标 i
    while (i <= mid && j <= right) { // 循环，直到不满足「下标 i 不超过 中点 且 下标 j 不超过 右边界」
      if (arr[i] <= arr[j]) { // 若 数组[下标 i] 不超过 数组[下标 j]
        temp[k] = arr[i]; // 把 数组[下标 i]; 写入 temp[k]
        i++; // 下标 i 加一
      } else { // 否则
        temp[k] = arr[j]; // 把 数组[下标 j]; 写入 temp[k]
        j++; // 下标 j 加一
      }
      k++; // 下标 k 加一
    }
    while (i <= mid) { // 循环，直到不满足「下标 i 不超过 中点」
      temp[k] = arr[i]; // 把 数组[下标 i]; 写入 temp[k]
      i++; // 下标 i 加一
      k++; // 下标 k 加一
    }
    while (j <= right) { // 循环，直到不满足「下标 j 不超过 右边界」
      temp[k] = arr[j]; // 把 数组[下标 j]; 写入 temp[k]
      j++; // 下标 j 加一
      k++; // 下标 k 加一
    }
    for (int idx = 0; idx < temp.length; idx++) { // 让 idx 从 0 开始计数，idx 小于 临时变量.长度 就继续
      arr[left + idx] = temp[idx]; // 把 临时变量[idx]; 写入 arr[left + idx]
    }
  }

  public static void main(String[] args) { // public static void main(String[] args) {
    int[][] inputs = { // 把 { 写入 int[][] inputs
      {5, 4, 3, 2, 1},
      {},
      {1},
      {3, 1, 2, 1, 3},
      {-3, 0, 5, -10, 8},
      {2, 2, 2},
    };
    int[][] wants = { // 把 { 写入 int[][] wants
      {1, 2, 3, 4, 5},
      {},
      {1},
      {1, 1, 2, 3, 3},
      {-10, -3, 0, 5, 8},
      {2, 2, 2},
    };
    boolean ok = true; // 把 true; 写入 boolean ok
    for (int ci = 0; ci < inputs.length; ci++) { // 让 ci 从 0 开始计数，ci 小于 inputs.长度 就继续
      int[] nums = inputs[ci].clone(); // 把 inputs[ci].clone(); 写入 int[] nums
      mergeSort(nums); // mergeSort(数组);
      if (!Arrays.equals(nums, wants[ci])) { // 若 取反 Arrays.equals(数组, wants[ci]
        ok = false; // 把 false; 写入 ok
        System.out.println(
            "FAIL mergeSort("
                + Arrays.toString(inputs[ci])
                + ")="
                + Arrays.toString(nums) // 打印输出
                + " want "
                + Arrays.toString(wants[ci])); // 加 「 want 」 加 Arrays.toString(wants[ci]));
      }
    }
    if (!ok) { // 若 取反 ok
      throw new RuntimeException("FAILED"); // throw new RuntimeException(「FAILED」);
    }
    System.out.println("PASS"); // 全部用例通过，输出 PASS
  }
}
