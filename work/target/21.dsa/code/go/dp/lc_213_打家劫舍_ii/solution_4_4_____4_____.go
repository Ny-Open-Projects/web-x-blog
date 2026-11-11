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

// rob 是 Python 参考 solution_4 的忠实翻译（helper 滚动 DP + 两段比较）。
func rob(nums []int) int { // 定义函数/方法 rob
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	if n == 1 { // 若 元素个数 等于 1
		return nums[0] // 返回 数组[0]
	}
	helper := func(arr []int) int { // 把 func(数组 []int) int { 写入 helper :
		f0, f1 := 0, 0          // 把 0, 0 写入 f0, f1 :
		for _, x := range arr { // 同时取 _ 与 x 遍历
			f0, f1 = f1, max2(f1, f0+x) // 把 f1, max2(f1, f0 加 x) 写入 f0, f1
		}
		return f1 // 返回 f1
	}
	return max2(nums[0]+helper(nums[2:n-1]), helper(nums[1:n])) // 定义函数/方法 max2
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
