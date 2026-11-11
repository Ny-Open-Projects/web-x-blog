// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func hanoi(n int, src, aux, dst rune, moves *[][2]rune) { // 定义函数/方法 hanoi
	if n == 1 { // 若 元素个数 等于 1
		*moves = append(*moves, [2]rune{src, dst})
		return // return
	}
	hanoi(n-1, src, dst, aux, moves) // hanoi(元素个数 减 1, src, dst, aux, moves)
	*moves = append(*moves, [2]rune{src, dst})
	hanoi(n-1, aux, src, dst, moves) // hanoi(元素个数 减 1, aux, src, dst, moves)
}

func main() { // 程序入口：跑内嵌自测用例
	var moves [][2]rune             // var moves [][2]rune
	hanoi(3, 'A', 'B', 'C', &moves) // hanoi(3, 'A', 'B', 'C', 按位与 moves)
	want := [][2]rune{              // 把 [][2]rune{ 写入 want :
		{'A', 'C'}, {'A', 'B'}, {'C', 'B'}, {'A', 'C'}, {'B', 'A'}, {'B', 'C'}, {'A', 'C'},
	}
	ok := true                                              // 把 true 写入 ok :
	if len(moves) != 7 || !reflect.DeepEqual(moves, want) { // 定义函数/方法 len
		ok = false                                         // 把 false 写入 ok
		fmt.Printf("FAIL hanoi=%v want %v\n", moves, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
