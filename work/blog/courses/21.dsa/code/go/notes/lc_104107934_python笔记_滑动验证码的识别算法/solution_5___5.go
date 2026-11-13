// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
package main // 引入依赖

// 忠实翻译自 python/notes/lc_104107934_python笔记_滑动验证码的识别算法/solution_5___5.py
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

func findGap(bg, puzzle []int) (int, []int) { // 定义函数/方法 findGap
	bgEdges := detectEdges(bg)                  // 把 detectEdges(bg) 写入 bgEdges :
	puzzleEdges := detectEdges(puzzle)          // 把 detectEdges(puzzle) 写入 puzzleEdges :
	responses := []int{}                        // 把 []int{} 写入 responses :
	for x := 0; x <= len(bg)-len(puzzle); x++ { // 让 x 从 0 开始计数
		score := 0                         // 把 0 写入 score :
		for y := 0; y < len(puzzle); y++ { // 让 y 从 0 开始计数
			if bgEdges[x+y] && puzzleEdges[y] { // 若 bgEdges[x 加 y] 且 puzzleEdges[y]
				score++ // score 加一
			}
		}
		responses = append(responses, score) // 把 append(responses, score) 写入 responses
	}
	// best_x = max(range(len(responses)), key=lambda i: responses[i])，取首个最大值
	bestX := 0                            // 把 0 写入 bestX :
	for i := 1; i < len(responses); i++ { // 让 下标 i 从 1 开始计数
		if responses[i] > responses[bestX] { // 若 responses[下标 i] 超过 responses[bestX]
			bestX = i // 把 下标 i 写入 bestX
		}
	}
	return bestX, responses // 返回 bestX, responses
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true         // 把 true 写入 ok :
	type pair struct { // 定义类型
		bg, puzzle   []int // bg, puzzle []int
		wantX        int   // wantX int
		wantResponse []int // wantResponse []int
	}
	cases := []pair{ // 把 []pair{ 写入 cases :
		{[]int{10, 10, 10, 10, 200, 200, 200, 200}, []int{10, 200, 200, 200}, 3, []int{0, 0, 0, 1, 0}},
		{[]int{10, 10, 200, 200, 10, 10}, []int{200, 200, 10}, 0, []int{1, 0, 1, 0}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		gx, resp := findGap(c.bg, c.puzzle) // 把 findGap(字符.bg, 字符.puzzle) 写入 gx, resp :
		if gx != c.wantX || !reflect.DeepEqual(resp, c.wantResponse) {
			ok = false                                                                                              // 把 false 写入 ok
			fmt.Printf("FAIL findGap(%v,%v)=%v,%v want %v,%v\n", c.bg, c.puzzle, gx, resp, c.wantX, c.wantResponse) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
