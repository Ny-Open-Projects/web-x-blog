// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
func getResultBruteforce(n int, ele []int) []int { // 定义函数/方法 getResultBruteforce
	ans := []int{}   // 把 []int{} 写入 ans :
	stack := []int{} // 把 []int{} 写入 stack :
	i := 0           // 把 0 写入 i :
	for i < n {      // for 下标 i 小于 元素个数 {
		mx := 0 // 把 0 写入 mx :
		for j := i; j < n; j++ {
			if ele[j] > mx {
				mx = ele[j]
			}
		}
		if len(stack) > 0 && ele[stack[len(stack)-1]] > mx { // 若 长度(栈) 超过 0 且 ele[栈[长度(栈) 减 1]] 超过 mx
			ans = append(ans, ele[stack[len(stack)-1]]) // 把 append(答案, ele[栈[长度(栈) 减 1]]) 写入 答案
			stack = stack[:len(stack)-1]                // 把 栈[:长度(栈) 减 1] 写入 栈
		} else { // 否则
			for mx != ele[i] {
				stack = append(stack, i)
				i++
			} // 把 ele[下标 i] { 栈 赋值为 append(栈, 下标 i); 下标 i 加一 } 写入 for mx !
			ans = append(ans, ele[i]) // 把 append(答案, ele[下标 i]) 写入 答案
			i++                       // 下标 i 加一
		}
	}
	for len(stack) > 0 { // for 长度(栈) 超过 0 {
		ans = append(ans, ele[stack[len(stack)-1]]) // 把 append(答案, ele[栈[长度(栈) 减 1]]) 写入 答案
		stack = stack[:len(stack)-1]                // 把 栈[:长度(栈) 减 1] 写入 栈
	}
	return ans // 返回 答案
}
func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := getResultBruteforce(5, []int{4, 1, 3, 5, 2}); !reflect.DeepEqual(got, []int{5, 3, 2, 1, 4}) {
		ok = false
		fmt.Printf("FAIL1=%v\n", got)
	}
	if got := getResultBruteforce(1, []int{3}); !reflect.DeepEqual(got, []int{3}) {
		ok = false
		fmt.Printf("FAIL2=%v\n", got)
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
