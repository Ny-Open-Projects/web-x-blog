// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130734875
package main // 引入依赖

import (
	"fmt"
	"os"
	"strconv"
) // 引入依赖

func calPoints(operations []string) int { // 定义函数/方法 calPoints
	stack := []int{}                // 把 []int{} 写入 stack :
	for _, op := range operations { // 同时取 _ 与 op 遍历
		switch op { // switch op {
		case "C": // case 「C」:
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		case "D": // case 「D」:
			stack = append(stack, stack[len(stack)-1]*2) // 把 append(栈, 栈[长度(栈) 减 1] 乘 2) 写入 栈
		case "+": // case 「 加 」:
			n := len(stack)                              // 把 长度(栈) 写入 n :
			stack = append(stack, stack[n-1]+stack[n-2]) // 把 append(栈, 栈[元素个数 减 1] 加 栈[元素个数 减 2]) 写入 栈
		default: // default:
			v, _ := strconv.Atoi(op) // 把 strconv.Atoi(op) 写入 v, _ :
			stack = append(stack, v) // 把 append(栈, 值) 写入 栈
		}
	}
	sum := 0                  // 把 0 写入 sum :
	for _, v := range stack { // 同时取 _ 与 值 遍历
		sum += v // 累计和累加 值
	}
	return sum // 返回 累计和
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []string // in []string
		want int      // want int
	}{ // }{
		{[]string{"5", "2", "C", "D", "+"}, 30},
		{[]string{"5", "-2", "4", "C", "D", "9", "+", "+"}, 27},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := calPoints(c.in); got != c.want { // 若 got : 赋值为 calPoints(字符.in); got 不等于 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL calPoints(%v)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
