// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233077
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// searchInsert 是 Python 参考 solution_1 的忠实翻译（二分查找返回 left）。
func searchInsert(nums []int, target int) int { // 定义函数/方法 searchInsert
	left, right := 0, len(nums) // 把 0, 长度(数组) 写入 left, right :
	for left < right {          // for 左边界 小于 右边界 {
		mid := (left + right) / 2 // 把 (左边界 加 右边界) 除以 2 写入 mid :
		if nums[mid] < target {   // 若 数组[中点] 小于 目标值
			left = mid + 1 // 把 中点 加 1 写入 左边界
		} else { // 否则
			right = mid // 把 中点 写入 右边界
		}
	}
	return left // 返回 左边界
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums   []int // 数组 []int
		target int   // 目标值 int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, 1, 0},
		{[]int{1, 3, 5, 6}, 5, 2},
		{[]int{1, 3, 5, 6}, 2, 1},
		{[]int{1, 3, 5, 6}, 7, 4},
		{[]int{1, 3, 5, 6}, 0, 0},
		{[]int{}, 5, 0},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := searchInsert(c.nums, c.target); got != c.want { // 若 got : 赋值为 searchInsert(字符.数组, 字符.目标值); got 不等于 字符.want
			fmt.Printf("FAIL %v %d got=%d want=%d\n", c.nums, c.target, got, c.want) // 打印输出
			os.Exit(1)                                                               // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
