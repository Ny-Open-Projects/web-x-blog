// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
func gnomeSort(arr []int) []int { // 定义函数/方法 gnomeSort
	length := len(arr) // 把 长度(数组) 写入 length :
	i := 1             // 把 1 写入 i :
	for i < length {   // for 下标 i 小于 长度 {
		if i < 1 || arr[i-1] <= arr[i] { // 若 下标 i 小于 1 或 数组[下标 i 减 1] 不超过 数组[下标 i]
			i++ // 下标 i 加一
		} else { // 否则
			arr[i-1], arr[i] = arr[i], arr[i-1] // 把 数组[下标 i], 数组[下标 i 减 1] 写入 arr[i-1], arr[i]
			i--                                 // 下标 i 减一
		}
	}
	return arr // 返回 数组
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want []int
	}{ // 把 []struct{ in []int; want []int }{ 写入 cases :
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{3, 1, 2}, []int{1, 2, 3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := make([]int, len(c.in))         // 把 make([]int, 长度(字符.in)) 写入 in :
		copy(in, c.in)                       // copy(in, 字符.in)
		got := gnomeSort(in)                 // 把 gnomeSort(in) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false
			fmt.Printf("FAIL gnomeSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
