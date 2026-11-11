// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144830623
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func longestConsecutive(nums []int) int { // 定义函数/方法 longestConsecutive
	set := make(map[int]bool) // 把 make(映射表[int]bool) 写入 set :
	for _, v := range nums {  // 同时取 _ 与 值 遍历
		set[v] = true // 把 true 写入 set[v]
	}
	best := 0              // 把 0 写入 best :
	for num := range set { // 把 range set { 写入 for num :
		if !set[num-1] { // 若 取反 set[num 减 1]
			current := num       // 把 num 写入 current :
			streak := 1          // 把 1 写入 streak :
			for set[current+1] { // for set[current 加 1] {
				current++ // current 加一
				streak++  // streak 加一
			}
			if streak > best { // 若 streak 超过 当前最优
				best = streak // 把 streak 写入 当前最优
			}
		}
	}
	return best // 返回 当前最优
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{100, 4, 200, 1, 3, 2}, 4},
		{[]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}, 9},
		{[]int{1, 0, 1, 2}, 3},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := longestConsecutive(c.in) // 把 longestConsecutive(字符.in) 写入 got :
		if got != c.want {              // 若 got 不等于 字符.want
			fmt.Printf("FAIL in=%v want=%d got=%d\n", c.in, c.want, got) // 打印输出
			ok = false                                                   // 把 false 写入 ok
		}
	}
	if !ok { // 若 取反 ok
		fmt.Println("RESULT: FAIL") // 打印输出
		os.Exit(1)                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
