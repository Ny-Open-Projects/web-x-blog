// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package main // 引入依赖

// 忠实翻译自 python/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_1___1.py
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

func main() { // 程序入口：跑内嵌自测用例
	ok := true         // 把 true 写入 ok :
	type pair struct { // 定义类型
		bg, puzzle []int // bg, puzzle []int
		want       int   // want int
	}
	cases := []pair{ // 把 []pair{ 写入 cases :
		{[]int{10, 10, 10, 10, 200, 200, 200, 200}, []int{10, 200, 200, 200}, 3},
		{[]int{10, 10, 200, 200, 10, 10}, []int{200, 200, 10}, 0},
		{[]int{1, 2}, []int{1, 2, 3, 4}, 0}, // boundary: bg 短于 puzzle，空循环
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := recognizeCaptcha(c.bg, c.puzzle); got != c.want {
			ok = false                                                                           // 把 false 写入 ok
			fmt.Printf("FAIL recognizeCaptcha(%v,%v)=%v want %v\n", c.bg, c.puzzle, got, c.want) // 打印输出
		}
	}
	// boundary: detectEdges 空数组
	if got := detectEdges([]int{}); len(got) != 0 { // 若 got : 赋值为 detectEdges([]int{}); 长度(got) 不等于 0
		ok = false                                              // 把 false 写入 ok
		fmt.Printf("FAIL detectEdges([])=%v want empty\n", got) // 打印输出
	}
	// normal: detectEdges 对默认背景
	if got := detectEdges([]int{10, 10, 10, 10, 200, 200, 200, 200}); !reflect.DeepEqual(got, []bool{false, false, false, false, true, false, false, false}) {
		ok = false                                   // 把 false 写入 ok
		fmt.Printf("FAIL detectEdges(bg)=%v\n", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
