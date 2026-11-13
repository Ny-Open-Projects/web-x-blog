// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"strconv" // 「strconv」
)

func evalRPN(tokens []string) int { // 定义函数/方法 evalRPN
	n := len(tokens)                 // 把 长度(tokens) 写入 n :
	stack := make([]int, 0, (n+1)/2) // 把 make([]int, 0, (元素个数 加 1) 除以 2) 写入 stack :
	for _, token := range tokens {   // 同时取 _ 与 token 遍历
		switch token { // switch token {
		case "+", "-", "*", "/": // case 「 加 」, 「 加 」, 「 加 」, 「 加 」:
			num2 := stack[len(stack)-1]  // 把 栈[长度(栈) 减 1] 写入 num2 :
			num1 := stack[len(stack)-2]  // 把 栈[长度(栈) 减 2] 写入 num1 :
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			var res int                  // var 结果 int
			switch token {               // switch token {
			case "+": // case 「 加 」:
				res = num1 + num2 // 把 num1 加 num2 写入 结果
			case "-": // case 「 减 」:
				res = num1 - num2 // 把 num1 减 num2 写入 结果
			case "*": // case 「 乘 」:
				res = num1 * num2 // 把 num1 乘 num2 写入 结果
			case "/": // case 「 除以 」:
				res = num1 / num2 // 把 num1 除以 num2 写入 结果
			}
			stack[len(stack)-1] = res // 把 结果 写入 stack[len(stack)-1]
		default: // default:
			v, _ := strconv.Atoi(token) // 把 strconv.Atoi(token) 写入 v, _ :
			stack = append(stack, v)    // 把 append(栈, 值) 写入 栈
		}
	}
	return stack[len(stack)-1] // 返回 栈[长度(栈) 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []string // in []string
		want int      // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]string{"2", "1", "+", "3", "*"}, 9},
		{[]string{"4", "13", "5", "/", "+"}, 6},
		{[]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}, 22},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := evalRPN(c.in); got != c.want { // 若 got : 赋值为 evalRPN(字符.in); got 不等于 字符.want
			ok = false                                                     // 把 false 写入 ok
			fmt.Printf("FAIL evalRPN(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
