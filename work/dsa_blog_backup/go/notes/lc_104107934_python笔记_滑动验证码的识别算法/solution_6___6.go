// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package main // 引入依赖

// 忠实翻译自 python/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_6___6.py
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

func buildSynthetic(bgLen, gapStart, puzzleLen int) ([]int, []int) { // 定义函数/方法 buildSynthetic
	bg := make([]int, bgLen) // 把 make([]int, bgLen) 写入 bg :
	for i := range bg {      // 把 range bg { 写入 for i :
		bg[i] = 10 // 把 10 写入 bg[i]
	}
	// for i in range(gap_start, min(gap_start + puzzle_len, bg_len))
	hi := gapStart + puzzleLen // 把 gapStart 加 puzzleLen 写入 hi :
	if bgLen < hi {            // 若 bgLen 小于 右边界
		hi = bgLen // 把 bgLen 写入 右边界
	}
	for i := gapStart; i < hi; i++ { // 把 gapStart; 下标 i 小于 右边界; 下标 i 加一 { 写入 for i :
		bg[i] = 200 // 把 200 写入 bg[i]
	}
	// puzzle = bg[gap_start:gap_start+puzzle_len]（python 切片自动 clamp）
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

func main() { // 程序入口：跑内嵌自测用例
	ok := true        // 把 true 写入 ok :
	type tup struct { // 定义类型
		bgLen, gapStart, puzzleLen int   // bgLen, gapStart, puzzleLen int
		wantBG                     []int // wantBG []int
		wantPuzzle                 []int // wantPuzzle []int
	}
	cases := []tup{ // 把 []tup{ 写入 cases :
		{8, 3, 4, []int{10, 10, 10, 200, 200, 200, 200, 10}, []int{200, 200, 200, 200}},
		{5, 3, 4, []int{10, 10, 10, 200, 200}, []int{200, 200}}, // boundary: 越界 clamp
		{8, 6, 4, []int{10, 10, 10, 10, 10, 10, 200, 200}, []int{200, 200}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		bg, puzzle := buildSynthetic(c.bgLen, c.gapStart, c.puzzleLen)
		if !reflect.DeepEqual(bg, c.wantBG) || !reflect.DeepEqual(puzzle, c.wantPuzzle) {
			ok = false                                                                                                                           // 把 false 写入 ok
			fmt.Printf("FAIL buildSynthetic(%v,%v,%v)=%v,%v want %v,%v\n", c.bgLen, c.gapStart, c.puzzleLen, bg, puzzle, c.wantBG, c.wantPuzzle) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
