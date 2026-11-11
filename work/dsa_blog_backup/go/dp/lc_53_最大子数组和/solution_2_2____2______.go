// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847570
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func maxSubArray(nums []int) int { // 定义函数/方法 maxSubArray
	best := nums[0]              // 把 数组[0] 写入 best :
	cur := nums[0]               // 把 数组[0] 写入 cur :
	for _, x := range nums[1:] { // 同时取 _ 与 x 遍历
		cur = maxInt(x, cur+x) // 把 maxInt(x, 当前值 加 x) 写入 当前值
		if cur > best {        // 若 当前值 超过 当前最优
			best = cur // 把 当前值 写入 当前最优
		}
	}
	return best // 返回 当前最优
}

func maxInt(a, b int) int { // 定义函数/方法 maxInt
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}, 6},
		{[]int{1}, 1},
		{[]int{5, 4, -1, 7, 8}, 23},
	}
	fail := false             // 把 false 写入 fail :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := maxSubArray(c.nums) // 把 maxSubArray(字符.数组) 写入 got :
		if got != c.want {         // 若 got 不等于 字符.want
			fmt.Printf("FAIL maxSubArray(%v)=%d want %d\n", c.nums, got, c.want) // 打印输出
			fail = true                                                          // 把 true 写入 fail
		}
	}
	if fail { // 若 fail
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
