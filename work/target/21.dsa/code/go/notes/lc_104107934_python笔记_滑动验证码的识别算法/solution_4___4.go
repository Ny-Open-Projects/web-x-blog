// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package main // 引入依赖

// 忠实翻译自 python/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_4___4.py
import (
	"fmt"  // 「fmt」
	"math" // 「math」
	"os"   // 「os」
)

func absi(x int) int { // 定义函数/方法 absi
	if x < 0 { // 若 x 小于 0
		return -x // 返回 减 x
	}
	return x // 返回 x
}

func bestMatchWindow(bg, puzzle []int) (int, float64) { // 定义函数/方法 bestMatchWindow
	bestX := 0                        // 把 0 写入 bestX :
	bestScore := math.Inf(1)          // 把 math.Inf(1) 写入 bestScore :
	n := len(puzzle)                  // 把 长度(puzzle) 写入 n :
	for x := 0; x <= len(bg)-n; x++ { // 让 x 从 0 开始计数
		score := 0               // 把 0 写入 score :
		for y := 0; y < n; y++ { // 让 y 从 0 开始计数
			score += absi(bg[x+y] - puzzle[y]) // score累加 absi(bg[x 加 y] 减 puzzle[y])
		}
		if float64(score) < bestScore { // 若 float64(score) 小于 bestScore
			bestScore = float64(score) // 把 float64(score) 写入 bestScore
			bestX = x                  // 把 x 写入 bestX
		}
	}
	return bestX, bestScore // 返回 bestX, bestScore
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true         // 把 true 写入 ok :
	type pair struct { // 定义类型
		bg, puzzle []int   // bg, puzzle []int
		wantX      int     // wantX int
		wantScore  float64 // wantScore float64
	}
	cases := []pair{ // 把 []pair{ 写入 cases :
		{[]int{10, 10, 10, 10, 200, 200, 200, 200}, []int{10, 200, 200, 200}, 3, 0},
		{[]int{10, 10, 200, 200, 10, 10}, []int{200, 200, 10}, 2, 0},
		{[]int{1, 2}, []int{1, 2, 3, 4}, 0, math.Inf(1)}, // boundary: 空循环，bestScore 保持 +Inf
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		gx, gs := bestMatchWindow(c.bg, c.puzzle) // 把 bestMatchWindow(字符.bg, 字符.puzzle) 写入 gx, gs :
		if gx != c.wantX || gs != c.wantScore {   // 若 gx 不等于 字符.wantX 或 gs 不等于 字符.wantScore
			ok = false                                                                                                 // 把 false 写入 ok
			fmt.Printf("FAIL bestMatchWindow(%v,%v)=%v,%v want %v,%v\n", c.bg, c.puzzle, gx, gs, c.wantX, c.wantScore) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
