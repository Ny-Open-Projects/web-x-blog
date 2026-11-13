package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// majorityElement 多数元素。忠实翻译 Python 参考实现 ref_majorityElement：
// Counter(nums).most_common(1)[0][0]
func majorityElement(nums []int) int { // 定义函数/方法 majorityElement
	cnt := make(map[int]int) // 把 make(映射表[int]int) 写入 cnt :
	for _, v := range nums { // 同时取 _ 与 值 遍历
		cnt[v]++ // 计数[值] 加一
	}
	best, bestCnt := 0, -1  // 把 0, 减 1 写入 best, bestCnt :
	for v, c := range cnt { // 同时取 值 与 字符 遍历
		if c > bestCnt { // 若 字符 超过 bestCnt
			best, bestCnt = v, c // 把 值, 字符 写入 best, bestCnt
		}
	}
	return best // 返回 当前最优
}

func main() { // 程序入口：跑内嵌自测用例
	// 用例来自 _tools/correctness_check.py PROBLEMS["lc_169_多数元素"]
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want int   // want int
	}{ // }{
		{[]int{3, 2, 3}, 3},
		{[]int{2, 2, 1, 1, 1, 2, 2}, 2},
		{[]int{1}, 1},
	}
	allOK := true             // 把 true 写入 allOK :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := majorityElement(c.in) // 把 majorityElement(字符.in) 写入 got :
		if got != c.want {           // 若 got 不等于 字符.want
			allOK = false                                                             // 把 false 写入 allOK
			fmt.Printf("FAIL majorityElement(%v) = %v, want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !allOK { // 若 取反 allOK
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
