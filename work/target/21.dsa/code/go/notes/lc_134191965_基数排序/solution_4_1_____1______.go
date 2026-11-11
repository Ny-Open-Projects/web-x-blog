// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
func radixSort(arr []int) []int { // 定义函数/方法 radixSort
	if len(arr) < 2 {
		return arr
	} // 若 长度(数组) 小于 2 { return 数组 }
	maxVal := arr[0]
	minVal := arr[0] // 把 数组[0]; minVal : 赋值为 数组[0] 写入 maxVal :
	for _, v := range arr {
		if v > maxVal {
			maxVal = v
		}
		if v < minVal {
			minVal = v
		}
	} // 同时取 _ 与 值 遍历
	offset := 0 // 把 0 写入 offset :
	if minVal < 0 {
		offset = -minVal
	} // 若 minVal 小于 0 { offset 赋值为 减 minVal }
	adjusted := make([]int, len(arr)) // 把 make([]int, 长度(数组)) 写入 adjusted :
	for i, v := range arr {
		adjusted[i] = v + offset
	} // 同时取 下标 i 与 值 遍历
	maxAdj := adjusted[0] // 把 adjusted[0] 写入 maxAdj :
	for _, v := range adjusted {
		if v > maxAdj {
			maxAdj = v
		}
	} // 同时取 _ 与 值 遍历
	radix := 1                   // 把 1 写入 radix :
	tmp := make([]int, len(arr)) // 把 make([]int, 长度(数组)) 写入 tmp :
	for maxAdj >= radix {        // 把 radix { 写入 for maxAdj >
		bucket := make([]int, 10) // 把 make([]int, 10) 写入 bucket :
		for _, num := range adjusted {
			bucket[(num/radix)%10]++
		} // 同时取 _ 与 num 遍历
		for i := 1; i < 10; i++ {
			bucket[i] += bucket[i-1]
		} // 让 下标 i 从 1 开始计数
		for i := len(adjusted) - 1; i >= 0; i-- { // 把 长度(adjusted) 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
			d := (adjusted[i] / radix) % 10 // 把 (adjusted[下标 i] 除以 radix) 对…取模 10 写入 d :
			tmp[bucket[d]-1] = adjusted[i]  // 把 adjusted[下标 i] 写入 tmp[bucket[d]-1]
			bucket[d]--                     // bucket[d] 减一
		}
		copy(adjusted, tmp) // copy(adjusted, 临时变量)
		radix *= 10         // 把 10 写入 radix *
	}
	for i, v := range adjusted {
		arr[i] = v - offset
	} // 同时取 下标 i 与 值 遍历
	return arr // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want []int
	}{ // 把 []struct{ in []int; want []int }{ 写入 cases :
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
		{[]int{-2, 1, 0, -9, 1, 3, 9, 99, 9, -30, -100, 100, 88, 88, 20, 1, 0, 3, 4, 5, -20}, []int{-100, -30, -20, -9, -2, 0, 0, 1, 1, 1, 3, 3, 4, 5, 9, 9, 20, 88, 88, 99, 100}},
		{[]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		in := make([]int, len(c.in))         // 把 make([]int, 长度(字符.in)) 写入 in :
		copy(in, c.in)                       // copy(in, 字符.in)
		got := radixSort(in)                 // 把 radixSort(in) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false
			fmt.Printf("FAIL radixSort(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
