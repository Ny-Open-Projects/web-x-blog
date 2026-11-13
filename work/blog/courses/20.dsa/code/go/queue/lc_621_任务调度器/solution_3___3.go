// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130482987
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"os"   // 「os」
	"sort" // 「sort」
)

// 忠实翻译 python/queue/lc_621_任务调度器/solution_3___3.py
// 贪心模拟：每轮从剩余任务里挑出现次数最多的前 n+1 个执行
func leastInterval(tasks []string, n int) int { // 定义函数/方法 leastInterval
	count := map[string]int{} // 把 映射表[string]int{} 写入 count :
	for _, t := range tasks { // 同时取 _ 与 另一字符串 遍历
		count[t]++ // 计数[另一字符串] 加一
	}
	cnt := []int{}            // 把 []int{} 写入 cnt :
	for _, v := range count { // 同时取 _ 与 值 遍历
		cnt = append(cnt, v) // 把 append(计数, 值) 写入 计数
	}
	time := 0          // 把 0 写入 time :
	for len(cnt) > 0 { // for 长度(计数) 超过 0 {
		sort.Sort(sort.Reverse(sort.IntSlice(cnt)))  // sort.Sort(sort.Reverse(sort.IntSlice(计数)))
		used := 0                                    // 把 0 写入 used :
		for i := 0; i < minInt(n+1, len(cnt)); i++ { // 让 下标 i 从 0 开始计数
			if cnt[i] > 0 { // 若 计数[下标 i] 超过 0
				cnt[i]-- // 计数[下标 i] 减一
				used++   // 已用标记 加一
			}
		}
		nxt := []int{}          // 把 []int{} 写入 nxt :
		for _, c := range cnt { // 同时取 _ 与 字符 遍历
			if c > 0 { // 若 字符 超过 0
				nxt = append(nxt, c) // 把 append(nxt, 字符) 写入 nxt
			}
		}
		cnt = nxt         // 把 nxt 写入 计数
		if len(cnt) > 0 { // 若 长度(计数) 超过 0
			time += n + 1 // time累加 元素个数 加 1
		} else { // 否则
			time += used // time累加 已用标记
		}
	}
	return time // 返回 time
}

func minInt(a, b int) int { // 定义函数/方法 minInt
	if a < b { // 若 数组 小于 b
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
