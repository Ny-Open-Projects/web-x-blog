// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func linearSearch(arr []int, target int) int { // 定义函数/方法 linearSearch
	for i := 0; i < len(arr); i++ { // 让 下标 i 从 0 开始计数
		if arr[i] == target { // 若 数组[下标 i] 等于 目标值
			return i // 返回 下标 i
		}
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	arr := []int{3, 1, 4, 1, 5, 9, 2, 6}   // 把 []int{3, 1, 4, 1, 5, 9, 2, 6} 写入 arr :
	ok := true                             // 把 true 写入 ok :
	if v := linearSearch(arr, 5); v != 4 { // 若 值 : 赋值为 linearSearch(数组, 5); 值 不等于 4
		ok = false                                        // 把 false 写入 ok
		fmt.Printf("FAIL linearSearch(5)=%d want 4\n", v) // 打印输出
	}
	if v := linearSearch(arr, 7); v != -1 { // 若 值 : 赋值为 linearSearch(数组, 7); 值 不等于 减 1
		ok = false                                         // 把 false 写入 ok
		fmt.Printf("FAIL linearSearch(7)=%d want -1\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
