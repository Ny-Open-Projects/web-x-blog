// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// climbStairsRefactored 下楼问题算法重构：用辅助函数隔离差异
// 步长 1/2/3，从 0 走到 goal，统计方案总数
func climbStairsRefactored(h int) int { // 定义函数/方法 climbStairsRefactored
	goal := h  // 把 h 写入 goal :
	count := 0 // 把 0 写入 count :

	isDone := func(pos int) bool { return pos == goal } // 把 func(pos int) bool { return pos 等于 goal } 写入 isDone :
	isValid := func(pos int) bool { return pos >= 0 && pos <= goal }
	getNewPos := func(pos, k int) int { return pos + (k + 1) }

	var dfs func(pos int) // var dfs func(pos int)
	dfs = func(pos int) { // 把 func(pos int) { 写入 dfs
		if isDone(pos) { // 定义判定函数 isDone
			count++ // 计数 加一
			return  // return
		}
		for k := 0; k < 3; k++ { // 让 下标 k 从 0 开始计数
			nxt := getNewPos(pos, k) // 把 getNewPos(pos, 下标 k) 写入 nxt :
			if !isValid(nxt) {       // 若 取反 isValid(nxt
				continue // 跳过本轮，进入下一次
			}
			dfs(nxt) // dfs(nxt)
		}
	}
	dfs(0)       // dfs(0)
	return count // 返回 计数
}

func main() { // 程序入口：跑内嵌自测用例
	got := climbStairsRefactored(10) // 把 climbStairsRefactored(10) 写入 got :
	if got != 274 {                  // 若 got 不等于 274
		fmt.Printf("FAIL climbStairs(10)=%d want=274\n", got) // 打印输出
		os.Exit(1)                                            // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
