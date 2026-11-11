// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107573690
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type position struct { // 定义类型
	x, y int // x, y int
}

var horseMoves = []position{ // 把 []position{ 存入 horseMoves
	{1, 2}, {2, 1}, {2, -1}, {1, -2},
}
var horseGoal = position{8, 4} // 把 position{8, 4} 存入 horseGoal

// horseJumpRefactored 跳马问题算法重构：与下楼共用同一套递归框架
// 从 (0,0) 走到 (8,4)，统计方案总数
func horseJumpRefactored() int { // 定义函数/方法 horseJumpRefactored
	count := 0 // 把 0 写入 count :

	isDone := func(p position) bool { return p.x == horseGoal.x && p.y == horseGoal.y }
	isValid := func(p position) bool { return p.x >= 0 && p.x <= 8 && p.y >= 0 && p.y <= 4 }
	getNewPos := func(p position, k int) position { // 把 func(节点 position, 下标 k int) position { 写入 getNewPos :
		return position{p.x + horseMoves[k].x, p.y + horseMoves[k].y}
	}

	var dfs func(p position) // var dfs func(节点 position)
	dfs = func(p position) { // 把 func(节点 position) { 写入 dfs
		if isDone(p) { // 定义判定函数 isDone
			count++ // 计数 加一
			return  // return
		}
		for k := 0; k < 4; k++ { // 让 下标 k 从 0 开始计数
			nxt := getNewPos(p, k) // 把 getNewPos(节点, 下标 k) 写入 nxt :
			if !isValid(nxt) {     // 若 取反 isValid(nxt
				continue // 跳过本轮，进入下一次
			}
			dfs(nxt) // dfs(nxt)
		}
	}
	dfs(position{0, 0}) // dfs(position{0, 0})
	return count        // 返回 计数
}

func main() { // 程序入口：跑内嵌自测用例
	got := horseJumpRefactored() // 把 horseJumpRefactored() 写入 got :
	if got != 37 {               // 若 got 不等于 37
		fmt.Printf("FAIL horseJump=%d want=37\n", got) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
