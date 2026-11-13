// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233483
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// findMin 是 Python 参考 solution_1 的忠实翻译（二分查找）。
func findMin(nums []int) int { // 定义函数/方法 findMin
	low := 0              // 把 0 写入 low :
	high := len(nums) - 1 // 把 长度(数组) 减 1 写入 high :
	for low < high {      // for low 小于 high {
		pivot := low + (high-low)/2   // 把 low 加 (high 减 low) 除以 2 写入 pivot :
		if nums[pivot] < nums[high] { // 若 数组[pivot] 小于 数组[high]
			high = pivot // 把 pivot 写入 high
		} else { // 否则
			low = pivot + 1 // 把 pivot 加 1 写入 low
		}
	}
	return nums[low] // 返回 数组[low]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, 1},
		{[]int{3, 4, 5, 1, 2}, 1},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 0},
		{[]int{11, 13, 15, 17}, 11},
		{[]int{2, 1}, 1},
		{[]int{1}, 1},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := findMin(c.nums); got != c.want { // 若 got : 赋值为 findMin(字符.数组); got 不等于 字符.want
			fmt.Printf("FAIL %v got=%d want=%d\n", c.nums, got, c.want) // 打印输出
			os.Exit(1)                                                  // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
