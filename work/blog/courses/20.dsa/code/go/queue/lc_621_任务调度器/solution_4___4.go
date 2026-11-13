// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 忠实翻译 python/queue/lc_621_任务调度器/solution_4___4.py
// 公式法（显式统计）：以任务频率桶实现
func leastInterval(tasks []string, n int) int { // 定义函数/方法 leastInterval
	freq := make([]int, 26)   // 把 make([]int, 26) 写入 freq :
	for _, t := range tasks { // 同时取 _ 与 另一字符串 遍历
		freq[t[0]-'A']++ // 频次表[另一字符串[0] 减 'A'] 加一
	}
	maxFreq := 0             // 把 0 写入 maxFreq :
	for _, f := range freq { // 同时取 _ 与 f 遍历
		if f > maxFreq { // 若 f 超过 maxFreq
			maxFreq = f // 把 f 写入 maxFreq
		}
	}
	same := 0                // 把 0 写入 same :
	for _, f := range freq { // 同时取 _ 与 f 遍历
		if f == maxFreq { // 若 f 等于 maxFreq
			same++ // same 加一
		}
	}
	return maxInt((maxFreq-1)*(n+1)+same, len(tasks)) // 定义函数/方法 maxInt
}

func maxInt(a, b int) int { // 定义函数/方法 maxInt
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	type caseT struct { // 定义类型
		tasks []string // tasks []string
		n     int      // 元素个数 int
		want  int      // want int
	}
	cases := []caseT{ // 把 []caseT{ 写入 cases :
		{[]string{"A", "A", "A", "B", "B", "B"}, 2, 8},
		{[]string{"A", "A", "A", "B", "B", "B"}, 0, 6},
		{[]string{"A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"}, 2, 16},
		{[]string{"A"}, 5, 1},
		{[]string{"A", "A", "B", "B"}, 3, 6},
		{[]string{"A", "B", "C", "D", "E", "F", "G"}, 0, 7},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := leastInterval(c.tasks, c.n); got != c.want {
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL leastInterval(%v,%d)=%d want %d\n", c.tasks, c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
