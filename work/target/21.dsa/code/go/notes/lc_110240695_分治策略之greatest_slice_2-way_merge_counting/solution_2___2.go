// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Greatest Slice - 方案2: Incremental (递增求和, O(n^2))
func maxSubArrayIC(arr []int) int { // 定义函数/方法 maxSubArrayIC
	n := len(arr) // 把 长度(数组) 写入 n :
	if n == 0 {   // 若 元素个数 等于 0
		return 0 // 返回 0
	}
	gs := arr[0]             // 把 数组[0] 写入 gs :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		s := 0                   // 把 0 写入 s :
		for j := i; j < n; j++ { // 把 下标 i; 下标 j 小于 元素个数; 下标 j 加一 { 写入 for j :
			s += arr[j] // 递增得到当前区间总和: O(1)
			if gs < s { // 若 gs 小于 字符串
				gs = s // 把 字符串 写入 gs
			}
		}
	}
	return gs // 返回 gs
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{-2, 1, -3, 4, -1, 2, 1}, 6},
		{[]int{-1}, -1},
		{[]int{1}, 1},
		{[]int{-2, -1}, -1},
		{[]int{}, 0},
		{[]int{5, 4, -1, 7, 8}, 23},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxSubArrayIC(c.in); got != c.want { // 若 got : 赋值为 maxSubArrayIC(字符.in); got 不等于 字符.want
			ok = false                                                           // 把 false 写入 ok
			fmt.Printf("FAIL maxSubArrayIC(%v)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
