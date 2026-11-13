// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/112548608
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"strings" // 「strings」
)

// solveFarmer 农夫过河（狼、羊、菜）：状态 (h,w,s,v) 每位 0/1 表示是否在起点岸。
// 农夫每次必过河，可单独或带狼/羊/菜之一；无人看管时羊吃菜、狼吃羊则非法。目标全部到达对岸。
func solveFarmer() string { // 定义函数/方法 solveFarmer
	invalid := func(st [4]int) bool { // 把 func(st [4]int) bool { 写入 invalid :
		h, w, s, v := st[0], st[1], st[2], st[3] // 把 st[0], st[1], st[2], st[3] 写入 h, w, s, v :
		if h != s && s == w {                    // 若 h 不等于 字符串 且 字符串 等于 权重
			return true // 返回 true
		}
		if h != s && s == v { // 若 h 不等于 字符串 且 字符串 等于 值
			return true // 返回 true
		}
		return false // 返回 false
	}
	itemIndex := map[byte]int{'W': 1, 'S': 2, 'V': 3} // 把 映射表[byte]int{'W': 1, 'S': 2, 'V': 3} 写入 itemIndex :
	visited := map[[4]int]bool{}                      // 把 映射表[[4]int]bool{} 写入 visited :
	path := []byte{}                                  // 把 []byte{} 写入 path :

	var goFn func(st [4]int) bool // var goFn func(st [4]int) bool
	goFn = func(st [4]int) bool { // 把 func(st [4]int) bool { 写入 goFn
		if st == [4]int{1, 1, 1, 1} { // 若 st 等于 [4]int{1, 1, 1, 1}
			return true // 返回 true
		}
		if visited[st] { // 若 已访问集合[st]
			return false // 返回 false
		}
		visited[st] = true                                // 把 true 写入 visited[st]
		for _, role := range []byte{'-', 'W', 'S', 'V'} { // 同时取 _ 与 role 遍历
			ns := st          // 把 st 写入 ns :
			ns[0] = 1 - ns[0] // 农夫总是过河
			if role != '-' {  // 若 role 不等于 ' 减 '
				idx := itemIndex[role] // 把 itemIndex[role] 写入 idx :
				if st[0] != st[idx] {  // 农夫必须与所带物品在出发前同岸
					continue // 跳过本轮，进入下一次
				}
				ns[idx] = 1 - ns[idx] // 把 1 减 ns[idx] 写入 ns[idx]
			}
			if invalid(ns) { // 定义函数/方法 invalid
				continue // 跳过本轮，进入下一次
			}
			if goFn(ns) { // 定义函数/方法 goFn
				path = append(path, role) // 把 append(当前路径, role) 写入 当前路径
				return true               // 返回 true
			}
		}
		return false // 返回 false
	}
	goFn([4]int{0, 0, 0, 0}) // goFn([4]int{0, 0, 0, 0})

	// 还原可读方案
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i] // 把 当前路径[下标 j], 当前路径[下标 i] 写入 path[i], path[j]
	}
	parts := []string{}      // 把 []string{} 写入 parts :
	for _, r := range path { // 同时取 _ 与 右指针 遍历
		if r == '-' { // 若 右指针 等于 ' 减 '
			parts = append(parts, "H") // 把 append(parts, 「H」) 写入 parts
		} else { // 否则
			parts = append(parts, "H"+string(r)) // 把 append(parts, 「H」 加 string(右指针)) 写入 parts
		}
	}
	return strings.Join(parts, " ") // 返回 strings.Join(parts, 「 」)
}

func main() { // 程序入口：跑内嵌自测用例
	plan := solveFarmer()             // 把 solveFarmer() 写入 plan :
	if plan != "HS H HW HS HV H HS" { // 若 plan 不等于 「HS H HW HS HV H HS」
		fmt.Printf("FAIL plan=%q\n", plan) // 打印输出
		os.Exit(1)                         // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
