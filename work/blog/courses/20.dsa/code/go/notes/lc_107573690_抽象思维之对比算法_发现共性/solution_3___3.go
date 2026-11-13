// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type gposition struct { // 定义类型
	x, y int // x, y int
}

var gMoves = []gposition{ // 把 []gposition{ 存入 gMoves
	{1, 2}, {2, 1}, {2, -1}, {1, -2},
}
var gGoal = gposition{8, 4} // 把 gposition{8, 4} 存入 gGoal

// genericSearch 通用递归枚举框架：返回从 start 到达目标的方案总数
func genericSearch(start gposition, isDone func(gposition) bool, isValid func(gposition) bool,
	getNewPos func(gposition, int) gposition, nMoves int) int { // getNewPos func(gposition, int) gposition, nMoves int) int {
	count := 0 // 把 0 写入 count :

	var dfs func(p gposition) // var dfs func(节点 gposition)
	dfs = func(p gposition) { // 把 func(节点 gposition) { 写入 dfs
		if isDone(p) { // 定义判定函数 isDone
			count++ // 计数 加一
			return  // return
		}
		for k := 0; k < nMoves; k++ { // 让 下标 k 从 0 开始计数
			nxt := getNewPos(p, k) // 把 getNewPos(节点, 下标 k) 写入 nxt :
			if !isValid(nxt) {     // 若 取反 isValid(nxt
				continue // 跳过本轮，进入下一次
			}
			dfs(nxt) // dfs(nxt)
		}
	}
	dfs(start)   // dfs(起点)
	return count // 返回 计数
}

func main() { // 程序入口：跑内嵌自测用例
	start := gposition{0, 0} // 把 gposition{0, 0} 写入 start :
	total := genericSearch(
		start,
		func(p gposition) bool { return p.x == gGoal.x && p.y == gGoal.y },
		func(p gposition) bool { return p.x >= 0 && p.x <= 8 && p.y >= 0 && p.y <= 4 },
		func(p gposition, k int) gposition { // func(节点 gposition, 下标 k int) gposition {
			return gposition{p.x + gMoves[k].x, p.y + gMoves[k].y} // 返回 gposition{节点.x 加 gMoves[下标 k].x, 节点.y 加 gMoves[下标 k].y}
		},
		4,
	)
	if total != 37 { // 若 总和 不等于 37
		fmt.Printf("FAIL genericSearch=%d want=37\n", total) // 打印输出
		os.Exit(1)                                           // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
