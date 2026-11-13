// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func maxBottlesDrunk(numBottles, numExchange int) int { // 定义函数/方法 maxBottlesDrunk
	total := numBottles             // 把 numBottles 写入 total :
	for numBottles >= numExchange { // 把 numExchange { 写入 for numBottles >
		numBottles += 1 - numExchange // numBottles累加 1 减 numExchange
		numExchange += 1              // numExchange累加 1
		total += 1                    // 总和累加 1
	}
	return total // 返回 总和
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		b  int // b int
		ex int // ex int
		w  int // 权重 int
	}{ // }{
		{10, 3, 13},
		{13, 6, 15},
		{1, 2, 1},
		{3, 3, 4},
		{15, 4, 18},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := maxBottlesDrunk(c.b, c.ex); got != c.w { // 若 got : 赋值为 maxBottlesDrunk(字符.b, 字符.ex); got 不等于 字符.权重
			ok = false                                                                  // 把 false 写入 ok
			fmt.Printf("FAIL maxBottlesDrunk(%d,%d)=%d want %d\n", c.b, c.ex, got, c.w) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
