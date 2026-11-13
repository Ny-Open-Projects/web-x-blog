// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145354164
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func dailyTemperatures(temperatures []int) []int { // 定义函数/方法 dailyTemperatures
	length := len(temperatures)   // 把 长度(temperatures) 写入 length :
	ans := make([]int, length)    // 把 make([]int, 长度) 写入 ans :
	stack := []int{}              // 把 []int{} 写入 stack :
	for i := 0; i < length; i++ { // 让 下标 i 从 0 开始计数
		temperature := temperatures[i]                                          // 把 temperatures[下标 i] 写入 temperature :
		for len(stack) > 0 && temperature > temperatures[stack[len(stack)-1]] { // for 长度(栈) 超过 0 且 temperature 超过 temperatures[栈[长度(栈) 减 1]] {
			prev := stack[len(stack)-1]  // 把 栈[长度(栈) 减 1] 写入 prev :
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			ans[prev] = i - prev         // 把 下标 i 减 前一个 写入 ans[prev]
		}
		stack = append(stack, i) // 把 append(栈, 下标 i) 写入 栈
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{73, 74, 75, 71, 69, 72, 76, 73}, []int{1, 1, 4, 2, 1, 1, 0, 0}},
		{[]int{30, 40, 50, 60}, []int{1, 1, 1, 0}},
		{[]int{30, 60, 90}, []int{1, 1, 0}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := dailyTemperatures(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                               // 把 false 写入 ok
			fmt.Printf("FAIL dailyTemperatures(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
