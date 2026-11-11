// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
func rangeMax(ele []int, i int) int { // 定义函数/方法 rangeMax
	mx := ele[i] // 把 ele[下标 i] 写入 mx :
	for j := i + 1; j < len(ele); j++ {
		if ele[j] > mx {
			mx = ele[j]
		}
	}
	return mx // 返回 mx
}
func suffixMax(ele []int) []int { // 定义函数/方法 suffixMax
	n := len(ele)                 // 把 长度(ele) 写入 n :
	res := make([]int, n)         // 把 make([]int, 元素个数) 写入 res :
	res[n-1] = ele[n-1]           // 把 ele[元素个数 减 1] 写入 res[n-1]
	for i := n - 2; i >= 0; i-- { // 把 元素个数 减 2; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		if res[i+1] > ele[i] {
			res[i] = res[i+1]
		} else {
			res[i] = ele[i]
		}
	}
	return res // 返回 结果
}
func main() { // 程序入口：跑内嵌自测用例
	ele := []int{4, 1, 3, 5, 2} // 把 []int{4,1,3,5,2} 写入 ele :
	ok := true                  // 把 true 写入 ok :
	if got := rangeMax(ele, 0); got != 5 {
		ok = false
		fmt.Printf("FAIL range=%d\n", got)
	}
	if got := suffixMax(ele); !reflect.DeepEqual(got, []int{5, 5, 5, 5, 2}) {
		ok = false
		fmt.Printf("FAIL suffix=%v\n", got)
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
