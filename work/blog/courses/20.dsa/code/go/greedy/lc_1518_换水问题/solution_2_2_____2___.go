// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386044
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func numWaterBottles(numBottles, numExchange int) int { // 定义函数/方法 numWaterBottles
	ans := numBottles          // 把 numBottles 写入 ans :
	empty := numBottles        // 把 numBottles 写入 empty :
	for empty >= numExchange { // 把 numExchange { 写入 for empty >
		newBottles := empty / numExchange      // 把 empty 除以 numExchange 写入 newBottles :
		ans += newBottles                      // 答案累加 newBottles
		empty = newBottles + empty%numExchange // 把 newBottles 加 empty 对…取模 numExchange 写入 empty
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		a, b int // 数组, b int
		want int // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{9, 3, 13},
		{15, 4, 19},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := numWaterBottles(c.a, c.b); got != c.want { // 若 got : 赋值为 numWaterBottles(字符.数组, 字符.b); got 不等于 字符.want
			ok = false                                                                    // 把 false 写入 ok
			fmt.Printf("FAIL numWaterBottles(%d,%d)=%v want %v\n", c.a, c.b, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
