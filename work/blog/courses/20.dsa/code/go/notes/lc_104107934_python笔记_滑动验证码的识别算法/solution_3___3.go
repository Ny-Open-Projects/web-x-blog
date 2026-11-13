// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package main // 引入依赖

// 忠实翻译自 python/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_3___3.py
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

func sumInts(a []int) int { // 定义函数/方法 sumInts
	s := 0                // 把 0 写入 s :
	for _, v := range a { // 同时取 _ 与 值 遍历
		s += v // 字符串累加 值
	}
	return s // 返回 字符串
}

func nccMatch(bg, puzzle []int) int { // 定义函数/方法 nccMatch
	bestX, bestScore := 0, math.Inf(-1) // 把 0, math.Inf( 减 1) 写入 bestX, bestScore :
	n := len(puzzle)                    // 把 长度(puzzle) 写入 n :
	for x := 0; x <= len(bg)-n; x++ {   // 让 x 从 0 开始计数
		window := bg[x : x+n]                       // 把 bg[x : x 加 元素个数] 写入 window :
		bw := float64(sumInts(window)) / float64(n) // 把 float64(sumInts(window)) 除以 float64(元素个数) 写入 bw :
		pw := float64(sumInts(puzzle)) / float64(n) // 把 float64(sumInts(puzzle)) 除以 float64(元素个数) 写入 pw :
		num := 0.0                                  // 把 0.0 写入 num :
		for i := 0; i < n; i++ {                    // 让 下标 i 从 0 开始计数
			num += (float64(window[i]) - bw) * (float64(puzzle[i]) - pw)
		}
		db := 0.0                  // 把 0.0 写入 db :
		for _, v := range window { // 同时取 _ 与 值 遍历
			db += (float64(v) - bw) * (float64(v) - bw) // db累加 (float64(值) 减 bw) 乘 (float64(值) 减 bw)
		}
		db = math.Sqrt(db)         // 把 math.Sqrt(db) 写入 db
		dp := 0.0                  // 把 0.0 写入 dp :
		for _, v := range puzzle { // 同时取 _ 与 值 遍历
			dp += (float64(v) - pw) * (float64(v) - pw) // DP 表累加 (float64(值) 减 pw) 乘 (float64(值) 减 pw)
		}
		dp = math.Sqrt(dp) // 把 math.Sqrt(DP 表) 写入 DP 表
		denom := db * dp   // 把 db 乘 DP 表 写入 denom :
		var score float64  // var score float64
		if denom != 0 {    // 若 denom 不等于 0
			score = num / denom // 把 num 除以 denom 写入 score
		} else { // 否则
			score = 0 // 把 0 写入 score
		}
		if score > bestScore { // 若 score 超过 bestScore
			bestScore = score // 把 score 写入 bestScore
			bestX = x         // 把 x 写入 bestX
		}
	}
	return bestX // 返回 bestX
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true         // 把 true 写入 ok :
	type pair struct { // 定义类型
		bg, puzzle []int // bg, puzzle []int
		want       int   // want int
	}
	cases := []pair{ // 把 []pair{ 写入 cases :
		{[]int{10, 10, 10, 10, 200, 200, 200, 200}, []int{10, 200, 200, 200}, 3},
		{[]int{10, 10, 200, 200, 10, 10}, []int{200, 200, 10}, 2},
		{[]int{1, 2}, []int{1, 2, 3, 4}, 0}, // boundary: bg 短于 puzzle
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := nccMatch(c.bg, c.puzzle); got != c.want { // 若 got : 赋值为 nccMatch(字符.bg, 字符.puzzle); got 不等于 字符.want
			ok = false                                                                   // 把 false 写入 ok
			fmt.Printf("FAIL nccMatch(%v,%v)=%v want %v\n", c.bg, c.puzzle, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
