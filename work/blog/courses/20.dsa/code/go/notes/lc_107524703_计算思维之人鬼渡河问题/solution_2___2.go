// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func solveIterative() [][2]int { // 定义函数/方法 solveIterative
	D := [][2]int{{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}} // 把 [][2]int{{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}} 写入 D :
	start := [2]int{3, 3}                                 // 把 [2]int{3, 3} 写入 start :
	goal := [2]int{0, 0}                                  // 把 [2]int{0, 0} 写入 goal :
	safe := func(r, g int) bool {                         // 把 func(右指针, g int) bool { 写入 safe :
		if r < 0 || r > 3 || g < 0 || g > 3 { // 若 右指针 小于 0 或 右指针 超过 3 或 g 小于 0 或 g 超过 3
			return false // 返回 false
		}
		return r == 0 || r == 3 || r == g // 返回 右指针 等于 0 或 右指针 等于 3 或 右指针 等于 g
	}
	var path [][2]int                         // var 当前路径 [][2]int
	visited := map[[3]int]bool{}              // 把 映射表[[3]int]bool{} 写入 visited :
	var dfs func([2]int, int) bool            // var dfs func([2]int, int) bool
	dfs = func(state [2]int, step int) bool { // 把 func(state [2]int, 步数 int) bool { 写入 dfs
		if state == goal { // 若 state 等于 goal
			return true // 返回 true
		}
		key := [3]int{state[0], state[1], step % 2} // 把 [3]int{state[0], state[1], 步数 对…取模 2} 写入 key :
		if visited[key] {                           // 若 已访问集合[key]
			return false // 返回 false
		}
		visited[key] = true        // 把 true 写入 visited[key]
		r, g := state[0], state[1] // 把 state[0], state[1] 写入 r, g :
		odd := step%2 == 1         // 把 步数 对…取模 2 等于 1 写入 odd :
		for _, dg := range D {     // 同时取 _ 与 dg 遍历
			dr, dgc := dg[0], dg[1] // 把 dg[0], dg[1] 写入 dr, dgc :
			var nr, ng int          // var nr, ng int
			if odd {                // 若 odd
				if r < dr || g < dgc { // 若 右指针 小于 dr 或 g 小于 dgc
					continue // 跳过本轮，进入下一次
				}
				nr, ng = r-dr, g-dgc // 把 右指针 减 dr, g 减 dgc 写入 nr, ng
			} else { // 否则
				if (3-r) < dr || (3-g) < dgc { // 若 3 减 右指针) 小于 dr 或 (3 减 g) 小于 dgc
					continue // 跳过本轮，进入下一次
				}
				nr, ng = r+dr, g+dgc // 把 右指针 加 dr, g 加 dgc 写入 nr, ng
			}
			if !safe(nr, ng) { // 若 取反 safe(nr, ng
				continue // 跳过本轮，进入下一次
			}
			if dfs([2]int{nr, ng}, step+1) { // 定义函数/方法 dfs
				path = append([][2]int{{dr, dgc}}, path...) // 把 append([][2]int{{dr, dgc}}, 当前路径...) 写入 当前路径
				return true                                 // 返回 true
			}
		}
		return false // 返回 false
	}
	dfs(start, 1) // dfs(起点, 1)
	return path   // 返回 当前路径
}

func main() { // 程序入口：跑内嵌自测用例
	plan := solveIterative() // 把 solveIterative() 写入 plan :
	want := [][2]int{{1, 1}, {1, 0}, {0, 2}, {0, 1}, {2, 0}, {1, 1}, {2, 0}, {0, 1}, {0, 2}, {1, 0}, {1, 1}}
	if !reflect.DeepEqual(plan, want) { // 若 取反 reflect.DeepEqual(plan, want
		fmt.Printf("FAIL plan=%v want=%v\n", plan, want) // 打印输出
		os.Exit(1)                                       // os.Exit(1)
	}
	if len(plan) != 11 { // 若 长度(plan) 不等于 11
		fmt.Printf("FAIL step count=%d want 11\n", len(plan)) // 打印输出
		os.Exit(1)                                            // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
