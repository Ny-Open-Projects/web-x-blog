// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// binarySearch 二分查找（减治策略）
func binarySearch(arr []int, target int) int { // 定义函数/方法 binarySearch
	left, right := 0, len(arr)-1 // 把 0, 长度(数组) 减 1 写入 left, right :
	for left <= right {          // 把 右边界 { 写入 for left <
		mid := (left + right) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
		if arr[mid] == target {   // 若 数组[中点] 等于 目标值
			return mid // 返回 中点
		}
		if arr[mid] < target { // 若 数组[中点] 小于 目标值
			left = mid + 1 // 把 中点 加 1 写入 左边界
		} else { // 否则
			right = mid - 1 // 把 中点 减 1 写入 右边界
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	if binarySearch([]int{1, 3, 5, 7, 9}, 5) != 2 { // 若 binarySearch([]int{1, 3, 5, 7, 9}, 5) 不等于 2
		fmt.Println("FAIL binarySearch 5") // 打印输出
		os.Exit(1)                         // os.Exit(1)
	}
	if binarySearch([]int{1, 3, 5, 7, 9}, 4) != -1 { // 若 binarySearch([]int{1, 3, 5, 7, 9}, 4) 不等于 减 1
		fmt.Println("FAIL binarySearch 4") // 打印输出
		os.Exit(1)                         // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
