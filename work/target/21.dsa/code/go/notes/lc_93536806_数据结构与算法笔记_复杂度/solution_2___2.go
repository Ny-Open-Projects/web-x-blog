// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func binarySearch(arr []int, target int) int { // 定义函数/方法 binarySearch
	left, right := 0, len(arr)-1 // 把 0, 长度(数组) 减 1 写入 left, right :
	for left <= right {          // 把 右边界 { 写入 for left <
		mid := (left + right) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
		if arr[mid] == target {   // 若 数组[中点] 等于 目标值
			return mid // 返回 中点
		} else if arr[mid] < target { // 否则，若 数组[中点] 小于 目标值
			left = mid + 1 // 把 中点 加 1 写入 左边界
		} else { // 否则
			right = mid - 1 // 把 中点 减 1 写入 右边界
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	arr := []int{1, 3, 5, 7, 9}            // 把 []int{1, 3, 5, 7, 9} 写入 arr :
	ok := true                             // 把 true 写入 ok :
	if v := binarySearch(arr, 5); v != 2 { // 若 值 : 赋值为 binarySearch(数组, 5); 值 不等于 2
		ok = false                                        // 把 false 写入 ok
		fmt.Printf("FAIL binarySearch(5)=%d want 2\n", v) // 打印输出
	}
	if v := binarySearch(arr, 4); v != -1 { // 若 值 : 赋值为 binarySearch(数组, 4); 值 不等于 减 1
		ok = false                                         // 把 false 写入 ok
		fmt.Printf("FAIL binarySearch(4)=%d want -1\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
