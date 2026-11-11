// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package main // 引入依赖

// 忠实翻译自 python/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_7___7.py
import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func absi(x int) int { // 定义函数/方法 absi
	if x < 0 { // 若 x 小于 0
		return -x // 返回 减 x
	}
	return x // 返回 x
}

func detectEdges(image []int) []bool { // 定义函数/方法 detectEdges
	edges := make([]bool, len(image)) // 把 make([]bool, 长度(image)) 写入 edges :
	for i := 1; i < len(image); i++ { // 让 下标 i 从 1 开始计数
		if absi(image[i]-image[i-1]) > 50 { // 若 absi(image[下标 i] 减 image[下标 i 减 1]) 超过 50
			edges[i] = true // 把 true 写入 edges[i]
		}
	}
	return edges // 返回 边集
}

func recognizeCaptcha(bg, puzzle []int) int { // 定义函数/方法 recognizeCaptcha
	bgEdges := detectEdges(bg)                  // 把 detectEdges(bg) 写入 bgEdges :
	puzzleEdges := detectEdges(puzzle)          // 把 detectEdges(puzzle) 写入 puzzleEdges :
	bestX, bestScore := 0, -1                   // 把 0, 减 1 写入 bestX, bestScore :
	for x := 0; x <= len(bg)-len(puzzle); x++ { // 让 x 从 0 开始计数
		score := 0                         // 把 0 写入 score :
		for y := 0; y < len(puzzle); y++ { // 让 y 从 0 开始计数
			if bgEdges[x+y] && puzzleEdges[y] { // 若 bgEdges[x 加 y] 且 puzzleEdges[y]
				score++ // score 加一
			}
		}
		if score > bestScore { // 若 score 超过 bestScore
			bestScore = score // 把 score 写入 bestScore
			bestX = x         // 把 x 写入 bestX
		}
	}
	return bestX // 返回 bestX
}

func buildSynthetic(bgLen, gapStart, puzzleLen int) ([]int, []int) { // 定义函数/方法 buildSynthetic
	bg := make([]int, bgLen) // 把 make([]int, bgLen) 写入 bg :
	for i := range bg {      // 把 range bg { 写入 for i :
		bg[i] = 10 // 把 10 写入 bg[i]
	}
	hi := gapStart + puzzleLen // 把 gapStart 加 puzzleLen 写入 hi :
	if bgLen < hi {            // 若 bgLen 小于 右边界
		hi = bgLen // 把 bgLen 写入 右边界
	}
	for i := gapStart; i < hi; i++ { // 把 gapStart; 下标 i 小于 右边界; 下标 i 加一 { 写入 for i :
		bg[i] = 200 // 把 200 写入 bg[i]
	}
	end := gapStart + puzzleLen // 把 gapStart 加 puzzleLen 写入 end :
	if end > bgLen {            // 若 终点 超过 bgLen
		end = bgLen // 把 bgLen 写入 终点
	}
	start := gapStart  // 把 gapStart 写入 start :
	if start > bgLen { // 若 起点 超过 bgLen
		start = bgLen // 把 bgLen 写入 起点
	}
	puzzle := bg[start:end] // 把 bg[起点:终点] 写入 puzzle :
	return bg, puzzle       // 返回 bg, puzzle
}

type pipelineResult struct { // 定义类型
	Background   []int // Background []int
	Puzzle       []int // Puzzle []int
	PredictedGap int   // PredictedGap int
}

func fullPipeline(bgLen, gapStart, puzzleLen int) pipelineResult { // 定义函数/方法 fullPipeline
	bg, puzzle := buildSynthetic(bgLen, gapStart, puzzleLen) // 把 buildSynthetic(bgLen, gapStart, puzzleLen) 写入 bg, puzzle :
	pred := recognizeCaptcha(bg, puzzle)                     // 把 recognizeCaptcha(bg, puzzle) 写入 pred :
	return pipelineResult{Background: bg, Puzzle: puzzle, PredictedGap: pred}
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true        // 把 true 写入 ok :
	type tup struct { // 定义类型
		bgLen, gapStart, puzzleLen int   // bgLen, gapStart, puzzleLen int
		wantBG                     []int // wantBG []int
		wantPuzzle                 []int // wantPuzzle []int
		wantGap                    int   // wantGap int
	}
	cases := []tup{ // 把 []tup{ 写入 cases :
		{8, 3, 4, []int{10, 10, 10, 200, 200, 200, 200, 10}, []int{200, 200, 200, 200}, 0},
		{5, 3, 4, []int{10, 10, 10, 200, 200}, []int{200, 200}, 0},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		r := fullPipeline(c.bgLen, c.gapStart, c.puzzleLen) // 把 fullPipeline(字符.bgLen, 字符.gapStart, 字符.puzzleLen) 写入 r :
		if !reflect.DeepEqual(r.Background, c.wantBG) || !reflect.DeepEqual(r.Puzzle, c.wantPuzzle) || r.PredictedGap != c.wantGap {
			ok = false                                                                                                                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL fullPipeline(%v,%v,%v)=%v,%v,%v want %v,%v,%v\n", c.bgLen, c.gapStart, c.puzzleLen, r.Background, r.Puzzle, r.PredictedGap, c.wantBG, c.wantPuzzle, c.wantGap) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
