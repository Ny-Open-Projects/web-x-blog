// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

// 人鬼渡河安全性判定（东岸人数 r、鬼数 g）：
// 人数等于 3、等于 0，或与鬼数相等时安全。
func isSafe(r, g int) bool { // 定义判定函数 isSafe
	return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

func main() { // 程序入口：跑内嵌自测用例
	states := [][2]int{{3, 3}, {3, 1}, {2, 2}, {1, 3}, {0, 0}}
	want := []bool{true, true, true, false, true} // 把 []bool{true, true, true, false, true} 写入 want :
	ok := true                                    // 把 true 写入 ok :
	for i, st := range states {                   // 同时取 下标 i 与 st 遍历
		got := isSafe(st[0], st[1]) // 把 isSafe(st[0], st[1]) 写入 got :
		if got != want[i] {         // 若 got 不等于 want[下标 i]
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL state %v got %v want %v\n", st, got, want[i]) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
