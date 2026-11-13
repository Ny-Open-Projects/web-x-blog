// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380711
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// minNumberOfSemesters 是 Python 参考 solution_1 的忠实翻译（状态压缩 DFS + combinations）。
func minNumberOfSemesters(n int, relations [][]int, k int) int { // 定义函数/方法 minNumberOfSemesters
	pre := make([]int, n)         // 把 make([]int, 元素个数) 写入 pre :
	for _, r := range relations { // 同时取 _ 与 右指针 遍历
		u, v := r[0]-1, r[1]-1 // 把 右指针[0] 减 1, 右指针[1] 减 1 写入 u, v :
		pre[v] |= 1 << u       // 把 1 小于 小于 节点 u 写入 pre[v] |
	}
	target := (1 << n) - 1 // 把 (1 小于 小于 元素个数) 减 1 写入 target :
	memo := map[int]int{}  // 把 映射表[int]int{} 写入 memo :

	var dfs func(mask int) int // var dfs func(mask int) int
	dfs = func(mask int) int { // 把 func(mask int) int { 写入 dfs
		if mask == target { // 若 mask 等于 目标值
			return 0 // 返回 0
		}
		if v, ok := memo[mask]; ok { // 若 值, ok : 赋值为 记忆化表[mask]; ok
			return v // 返回 值
		}
		cand := []int{}          // 把 []int{} 写入 cand :
		for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
			if ((mask>>i)&1) == 0 && (pre[i]&mask) == pre[i] {
				cand = append(cand, i) // 把 append(cand, 下标 i) 写入 cand
			}
		}
		best := n + 1       // 把 元素个数 加 1 写入 best :
		sz := k             // 把 下标 k 写入 sz :
		if len(cand) < sz { // 若 长度(cand) 小于 sz
			sz = len(cand) // 把 长度(cand) 写入 sz
		}
		var gen func(start, r int, cur []int) // var gen func(起点, 右指针 int, 当前值 []int)
		gen = func(start, r int, cur []int) { // 把 func(起点, 右指针 int, 当前值 []int) { 写入 gen
			if r == 0 { // 若 右指针 等于 0
				nmask := mask           // 把 mask 写入 nmask :
				for _, c := range cur { // 同时取 _ 与 字符 遍历
					nmask |= 1 << c // 把 1 小于 小于 字符 写入 nmask |
				}
				v := 1 + dfs(nmask) // 把 1 加 dfs(nmask) 写入 v :
				if v < best {       // 若 值 小于 当前最优
					best = v // 把 值 写入 当前最优
				}
				return // return
			}
			for i := start; i < len(cand); i++ { // 把 起点; 下标 i 小于 长度(cand); 下标 i 加一 { 写入 for i :
				gen(i+1, r-1, append(cur, cand[i])) // gen(下标 i 加 1, 右指针 减 1, append(当前值, cand[下标 i]))
			}
		}
		for r := 1; r <= sz; r++ { // 让 右指针 从 1 开始计数
			gen(0, r, []int{}) // gen(0, 右指针, []int{})
		}
		memo[mask] = best // 把 当前最优 写入 memo[mask]
		return best       // 返回 当前最优
	}
	return dfs(0) // 定义函数/方法 dfs
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n         int     // 元素个数 int
		relations [][]int // relations [][]int
		k, want   int     // 下标 k, want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{4, [][]int{{2, 1}, {3, 1}, {1, 4}}, 2, 3},
		{5, [][]int{{2, 1}, {3, 1}, {4, 1}, {1, 5}}, 2, 4},
		{3, [][]int{{1, 2}, {2, 3}}, 2, 3},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minNumberOfSemesters(c.n, c.relations, c.k); got != c.want {
			fmt.Printf("FAIL n=%d rel=%v k=%d got=%d want=%d\n", c.n, c.relations, c.k, got, c.want) // 打印输出
			os.Exit(1)                                                                               // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
