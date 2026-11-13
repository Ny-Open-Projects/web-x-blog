// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func seqSearch(nums []int, target int) int { // 定义函数/方法 seqSearch
	for i := 0; i < len(nums); i++ { // 让 下标 i 从 0 开始计数
		if nums[i] == target { // 若 数组[下标 i] 等于 目标值
			return i // 返回 下标 i
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums   []int // 数组 []int
		target int   // 目标值 int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{15, 4, 23, 52, 1}, 23, 2},
		{[]int{15, 4, 23, 52, 1}, 123, -1},
		{[]int{}, 1, -1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := seqSearch(c.nums, c.target); got != c.want { // 若 got : 赋值为 seqSearch(字符.数组, 字符.目标值); got 不等于 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL seqSearch(%v,%d)=%d want %d\n", c.nums, c.target, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
