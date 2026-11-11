// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134429994
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

func firstMissingPositive(nums []int) int { // 定义函数/方法 firstMissingPositive
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 1 // 返回 1
	}
	pos := []int{}              // 把 []int{} 写入 pos :
	for _, item := range nums { // 同时取 _ 与 item 遍历
		if item > 0 { // 若 item 超过 0
			pos = append(pos, item) // 把 append(pos, item) 写入 pos
		}
	}
	if len(pos) == 0 { // 若 长度(pos) 等于 0
		return 1 // 返回 1
	}
	sort.Ints(pos)   // sort.Ints(pos)
	if pos[0] != 1 { // 若 pos[0] 不等于 1
		return 1 // 返回 1
	}
	n := len(pos)              // 把 长度(pos) 写入 n :
	for i := 0; i < n-1; i++ { // 让 下标 i 从 0 开始计数
		if pos[i+1]-pos[i] > 1 { // 若 pos[下标 i 加 1] 减 pos[下标 i] 超过 1
			return pos[i] + 1 // 返回 pos[下标 i] 加 1
		}
	}
	return pos[n-1] + 1 // 返回 pos[元素个数 减 1] 加 1
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		nums []int // 数组 []int
		want int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 0}, 3},
		{[]int{3, 4, -1, 1}, 2},
		{[]int{7, 8, 9, 11, 12}, 1},
	}
	fail := false             // 把 false 写入 fail :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := firstMissingPositive(c.nums) // 把 firstMissingPositive(字符.数组) 写入 got :
		if got != c.want {                  // 若 got 不等于 字符.want
			fmt.Printf("FAIL firstMissingPositive(%v)=%d want %d\n", c.nums, got, c.want) // 打印输出
			fail = true                                                                   // 把 true 写入 fail
		}
	}
	if fail { // 若 fail
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
