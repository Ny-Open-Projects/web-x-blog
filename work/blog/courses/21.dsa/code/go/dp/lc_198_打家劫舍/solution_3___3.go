// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130670245
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func rob(nums []int) int { // 定义函数/方法 rob
	prev, cur := 0, 0        // 把 0, 0 写入 prev, cur :
	for _, x := range nums { // 同时取 _ 与 x 遍历
		prev, cur = cur, maxInt(cur, prev+x) // 把 当前值, maxInt(当前值, 前一个 加 x) 写入 prev, cur
	}
	return cur // 返回 当前值
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
		{[]int{1, 2, 3, 1}, 4},
		{[]int{2, 7, 9, 3, 1}, 12},
		{[]int{2, 1, 1, 2}, 4},
	}
	fail := false             // 把 false 写入 fail :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := rob(c.nums) // 把 rob(字符.数组) 写入 got :
		if got != c.want { // 若 got 不等于 字符.want
			fmt.Printf("FAIL rob(%v)=%d want %d\n", c.nums, got, c.want) // 打印输出
			fail = true                                                  // 把 true 写入 fail
		}
	}
	if fail { // 若 fail
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
