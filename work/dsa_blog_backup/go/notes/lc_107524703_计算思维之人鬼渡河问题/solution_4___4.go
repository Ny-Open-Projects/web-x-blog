// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func solveWithDir() [][2]int { // 定义函数/方法 solveWithDir
	D := [][2]int{{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}} // 把 [][2]int{{2, 0}, {1, 0}, {1, 1}, {0, 1}, {0, 2}} 写入 D :
	startDir := -1                                        // 把 减 1 写入 startDir :
	var path [][2]int                                     // var 当前路径 [][2]int
	visited := map[[3]int]bool{}                          // 把 映射表[[3]int]bool{} 写入 visited :

	var jump func(r, g, dir, step int) bool // var jump func(右指针, g, dir, 步数 int) bool
	jump = func(r, g, dir, step int) bool { // 把 func(右指针, g, dir, 步数 int) bool { 写入 jump
		if r == 0 && g == 0 && step%2 == 0 { // 若 右指针 等于 0 且 g 等于 0 且 步数 对…取模 2 等于 0
			return true // 返回 true
		}
		key := [3]int{r, g, step % 2} // 把 [3]int{右指针, g, 步数 对…取模 2} 写入 key :
		if visited[key] {             // 若 已访问集合[key]
			return false // 返回 false
		}
		visited[key] = true             // 把 true 写入 visited[key]
		safe := func(rr, gg int) bool { // 把 func(rr, gg int) bool { 写入 safe :
			return 0 <= rr && rr <= 3 && 0 <= gg && gg <= 3 && (rr == 0 || rr == 3 || rr == gg)
		}
		for _, d := range D { // 同时取 _ 与 d 遍历
			nr := r + dir*d[0] // 把 右指针 加 dir 乘 d[0] 写入 nr :
			ng := g + dir*d[1] // 把 g 加 dir 乘 d[1] 写入 ng :
			if !safe(nr, ng) { // 若 取反 safe(nr, ng
				continue // 跳过本轮，进入下一次
			}
			if jump(nr, ng, -dir, step+1) { // 定义函数/方法 jump
				path = append(path, d) // 把 append(当前路径, d) 写入 当前路径
				return true            // 返回 true
			}
		}
		return false // 返回 false
	}
	jump(3, 3, startDir, 0) // jump(3, 3, startDir, 0)
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i] // 把 当前路径[下标 j], 当前路径[下标 i] 写入 path[i], path[j]
	}
	return path // 返回 当前路径
}

func main() { // 程序入口：跑内嵌自测用例
	plan := solveWithDir() // 把 solveWithDir() 写入 plan :
	if len(plan) != 0 {    // 若 长度(plan) 不等于 0
		fmt.Printf("FAIL plan=%v want empty\n", plan) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
