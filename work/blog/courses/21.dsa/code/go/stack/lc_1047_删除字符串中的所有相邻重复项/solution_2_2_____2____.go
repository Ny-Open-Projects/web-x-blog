// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114201
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

func removeDuplicates(s string) string { // 定义函数/方法 removeDuplicates
	stack := []rune{}     // 把 []rune{} 写入 stack :
	for _, x := range s { // 同时取 _ 与 x 遍历
		if len(stack) > 0 && stack[len(stack)-1] == x { // 若 长度(栈) 超过 0 且 栈[长度(栈) 减 1] 等于 x
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			continue                     // 跳过本轮，进入下一次
		}
		stack = append(stack, x) // 把 append(栈, x) 写入 栈
	}
	return string(stack) // 定义函数/方法 string
}

func main() { // 程序入口：跑内嵌自测用例
	want := "abc"                      // 把 「abc」 写入 want :
	got := removeDuplicates("abc")     // 把 removeDuplicates(「abc」) 写入 got :
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Println("FAIL", got) // 打印输出
		return                   // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
