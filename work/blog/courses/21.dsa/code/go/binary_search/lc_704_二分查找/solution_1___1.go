// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134221939
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func search(nums []int, target int) int { // 定义函数/方法 search
	left, right := 0, len(nums)-1 // 把 0, 长度(数组) 减 1 写入 left, right :
	for left <= right {           // 把 右边界 { 写入 for left <
		mid := (left + right) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
		if nums[mid] == target {  // 若 数组[中点] 等于 目标值
			return mid // 返回 中点
		}
		if nums[mid] < target { // 若 数组[中点] 小于 目标值
			left = mid + 1 // 把 中点 加 1 写入 左边界
		} else { // 否则
			right = mid - 1 // 把 中点 减 1 写入 右边界
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		nums   []int // 数组 []int
		target int   // 目标值 int
		want   int   // want int
	}{ // }{
		{[]int{1, 2, 3}, 1, 0},
		{[]int{-1, 0, 3, 5, 9, 12}, 9, 4},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := search(c.nums, c.target); got != c.want { // 若 got : 赋值为 search(字符.数组, 字符.目标值); got 不等于 字符.want
			ok = false                                                                   // 把 false 写入 ok
			fmt.Printf("FAIL search(%v,%d)=%d want %d\n", c.nums, c.target, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
