// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/98685358
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func isSafe(state [4]int) bool { // 定义判定函数 isSafe
	farmer, wolf, goat, cabbage := state[0], state[1], state[2], state[3]
	if wolf == goat && farmer != wolf { // 若 wolf 等于 goat 且 farmer 不等于 wolf
		return false // 返回 false
	}
	if goat == cabbage && farmer != goat { // 若 goat 等于 cabbage 且 farmer 不等于 goat
		return false // 返回 false
	}
	return true // 返回 true
}

func solve() [][4]int { // 定义函数/方法 solve
	start := [4]int{0, 0, 0, 0}                // 把 [4]int{0, 0, 0, 0} 写入 start :
	goal := [4]int{1, 1, 1, 1}                 // 把 [4]int{1, 1, 1, 1} 写入 goal :
	sentinel := [4]int{-1, -1, -1, -1}         // 把 [4]int{ 减 1, 减 1, 减 1, 减 1} 写入 sentinel :
	prev := map[[4]int][4]int{start: sentinel} // 把 映射表[[4]int][4]int{起点: sentinel} 写入 prev :
	queue := [][4]int{start}                   // 把 [][4]int{起点} 写入 queue :
	for len(queue) > 0 {                       // for 长度(队列) 超过 0 {
		cur := queue[0]   // 把 队列[0] 写入 cur :
		queue = queue[1:] // 把 队列[1:] 写入 队列
		if cur == goal {  // 若 当前值 等于 goal
			path := [][4]int{cur}                     // 把 [][4]int{当前值} 写入 path :
			for prev[path[len(path)-1]] != sentinel { // 把 sentinel { 写入 for prev[path[len(path)-1]] !
				path = append(path, prev[path[len(path)-1]]) // 把 append(当前路径, 前一个[当前路径[长度(当前路径) 减 1]]) 写入 当前路径
			}
			for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
				path[i], path[j] = path[j], path[i] // 把 当前路径[下标 j], 当前路径[下标 i] 写入 path[i], path[j]
			}
			return path // 返回 当前路径
		}
		farmer := cur[0]         // 把 当前值[0] 写入 farmer :
		for i := 0; i < 4; i++ { // 让 下标 i 从 0 开始计数
			if i != 0 && cur[i] != farmer { // 若 下标 i 不等于 0 且 当前值[下标 i] 不等于 farmer
				continue // 跳过本轮，进入下一次
			}
			nxt := cur          // 把 当前值 写入 nxt :
			nxt[0] = 1 - farmer // 把 1 减 farmer 写入 nxt[0]
			if i != 0 {         // 若 下标 i 不等于 0
				nxt[i] = 1 - farmer // 把 1 减 farmer 写入 nxt[i]
			}
			if _, ok := prev[nxt]; ok { // 若 _, ok : 赋值为 前一个[nxt]; ok
				continue // 跳过本轮，进入下一次
			}
			if !isSafe(nxt) { // 若 取反 isSafe(nxt
				continue // 跳过本轮，进入下一次
			}
			prev[nxt] = cur            // 把 当前值 写入 prev[nxt]
			queue = append(queue, nxt) // 把 append(队列, nxt) 写入 队列
		}
	}
	return nil // 返回 nil
}

func main() { // 程序入口：跑内嵌自测用例
	path := solve()  // 把 solve() 写入 path :
	ok := true       // 把 true 写入 ok :
	if path == nil { // 若 当前路径 等于 nil
		ok = false                      // 把 false 写入 ok
		fmt.Println("FAIL no solution") // 打印输出
	} else { // 否则
		start := [4]int{0, 0, 0, 0}                        // 把 [4]int{0, 0, 0, 0} 写入 start :
		goal := [4]int{1, 1, 1, 1}                         // 把 [4]int{1, 1, 1, 1} 写入 goal :
		if path[0] != start || path[len(path)-1] != goal { // 若 当前路径[0] 不等于 起点 或 当前路径[长度(当前路径) 减 1] 不等于 goal
			ok = false                    // 把 false 写入 ok
			fmt.Println("FAIL endpoints") // 打印输出
		}
		for _, s := range path { // 同时取 _ 与 字符串 遍历
			if !isSafe(s) { // 若 取反 isSafe(字符串
				ok = false                       // 把 false 写入 ok
				fmt.Println("FAIL unsafe state") // 打印输出
				break                            // 跳出循环
			}
		}
		for i := 1; i < len(path); i++ { // 让 下标 i 从 1 开始计数
			a, b := path[i-1], path[i] // 把 当前路径[下标 i 减 1], 当前路径[下标 i] 写入 a, b :
			diff := 0                  // 把 0 写入 diff :
			for k := 0; k < 4; k++ {   // 让 下标 k 从 0 开始计数
				if a[k] != b[k] { // 若 数组[下标 k] 不等于 b[下标 k]
					diff++ // 差值 加一
				}
			}
			if a[0] == b[0] || diff < 1 || diff > 2 { // 若 数组[0] 等于 b[0] 或 差值 小于 1 或 差值 超过 2
				ok = false                       // 把 false 写入 ok
				fmt.Println("FAIL invalid step") // 打印输出
				break                            // 跳出循环
			}
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
