// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850170
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func max2(a, b int) int { // 定义函数/方法 max2
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

// rob 是 Python 参考 solution_3 的忠实翻译（robRange 区间 DP）。
func rob(nums []int) int { // 定义函数/方法 rob
	length := len(nums) // 把 长度(数组) 写入 length :
	if length == 1 {    // 若 长度 等于 1
		return nums[0] // 返回 数组[0]
	}
	if length == 2 { // 若 长度 等于 2
		return max2(nums[0], nums[1]) // 定义函数/方法 max2
	}
	return max2(robRange(nums, 0, length-2), robRange(nums, 1, length-1)) // 定义函数/方法 max2
}

func robRange(nums []int, start, end int) int { // 定义函数/方法 robRange
	first := nums[start]                       // 把 数组[起点] 写入 first :
	second := max2(nums[start], nums[start+1]) // 把 max2(数组[起点], 数组[起点 加 1]) 写入 second :
	for i := start + 2; i <= end; i++ {        // 把 起点 加 2; 下标 i 不超过 终点; 下标 i 加一 { 写入 for i :
		temp := second                       // 把 second 写入 temp :
		second = max2(first+nums[i], second) // 把 max2(first 加 数组[下标 i], second) 写入 second
		first = temp                         // 把 临时变量 写入 first
	}
	return second // 返回 second
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{2, 3, 2}, 3},
		{[]int{1, 2, 3, 1}, 4},
		{[]int{1, 2, 1, 1}, 3},
		{[]int{5}, 5},
		{[]int{2, 1, 1, 2}, 3},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := rob(c.nums); got != c.want { // 若 got : 赋值为 rob(字符.数组); got 不等于 字符.want
			fmt.Printf("FAIL %v got=%d want=%d\n", c.nums, got, c.want) // 打印输出
			os.Exit(1)                                                  // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
