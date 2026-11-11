// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113233
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
	"strconv" // 「strconv」
)

func evalRPN(tokens []string) int { // 定义函数/方法 evalRPN
	stack := []int{}               // 把 []int{} 写入 stack :
	for _, token := range tokens { // 同时取 _ 与 token 遍历
		if token != "+" && token != "-" && token != "*" && token != "/" {
			v, _ := strconv.Atoi(token) // 把 strconv.Atoi(token) 写入 v, _ :
			stack = append(stack, v)    // 把 append(栈, 值) 写入 栈
		} else { // 否则
			num2 := stack[len(stack)-1]  // 把 栈[长度(栈) 减 1] 写入 num2 :
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			num1 := stack[len(stack)-1]  // 把 栈[长度(栈) 减 1] 写入 num1 :
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
			stack = append(stack, res) // 把 append(栈, 结果) 写入 栈
		}
	}
	return stack[len(stack)-1] // 返回 栈[长度(栈) 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	if !reflect.DeepEqual(evalRPN([]string{"2", "1", "+", "3", "*"}), 9) {
		fmt.Println("FAIL1") // 打印输出
		return               // return
	}
	if !reflect.DeepEqual(evalRPN([]string{"4", "13", "5", "/", "+"}), 6) {
		fmt.Println("FAIL2") // 打印输出
		return               // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
