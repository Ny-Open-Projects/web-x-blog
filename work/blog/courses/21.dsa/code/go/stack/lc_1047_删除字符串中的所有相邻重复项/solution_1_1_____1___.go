// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114201
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

func removeDuplicates(s string) string { // 定义函数/方法 removeDuplicates
	stk := []rune{}        // 把 []rune{} 写入 stk :
	for _, ch := range s { // 同时取 _ 与 字符 遍历
		if len(stk) > 0 && stk[len(stk)-1] == ch { // 若 长度(栈) 超过 0 且 栈[长度(栈) 减 1] 等于 字符
			stk = stk[:len(stk)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		} else { // 否则
			stk = append(stk, ch) // 把 append(栈, 字符) 写入 栈
		}
	}
	return string(stk) // 定义函数/方法 string
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
