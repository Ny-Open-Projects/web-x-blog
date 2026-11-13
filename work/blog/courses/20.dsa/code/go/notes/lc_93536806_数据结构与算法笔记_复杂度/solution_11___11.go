// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func matrixMultiply(a, b [][]int) [][]int { // 定义函数/方法 matrixMultiply
	n := len(a)           // 把 长度(数组) 写入 n :
	c := make([][]int, n) // 把 make([][]int, 元素个数) 写入 c :
	for i := range c {    // 把 range 字符 { 写入 for i :
		c[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 c[i]
	}
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < n; j++ { // 让 下标 j 从 0 开始计数
			for k := 0; k < n; k++ { // 让 下标 k 从 0 开始计数
				c[i][j] += a[i][k] * b[k][j] // c[i][j]累加 数组[下标 i][下标 k] 乘 b[下标 k][下标 j]
			}
		}
	}
	return c // 返回 字符
}

func main() { // 程序入口：跑内嵌自测用例
	a := [][]int{{1, 2}, {3, 4}}        // 把 [][]int{{1, 2}, {3, 4}} 写入 a :
	b := [][]int{{5, 6}, {7, 8}}        // 把 [][]int{{5, 6}, {7, 8}} 写入 b :
	want := [][]int{{19, 22}, {43, 50}} // 把 [][]int{{19, 22}, {43, 50}} 写入 want :
	ok := true                          // 把 true 写入 ok :
	if got := matrixMultiply(a, b); !reflect.DeepEqual(got, want) {
		ok = false                                                // 把 false 写入 ok
		fmt.Printf("FAIL matrixMultiply=%v want %v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
