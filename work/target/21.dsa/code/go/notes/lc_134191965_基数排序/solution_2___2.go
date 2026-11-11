// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134191965
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖
func radixSort(nums []int) []int { // 定义函数/方法 radixSort
	if len(nums) == 0 {
		return nums
	} // 若 长度(数组) 等于 0 { return 数组 }
	maxNum := nums[0] // 把 数组[0] 写入 maxNum :
	for _, v := range nums {
		if v > maxNum {
			maxNum = v
		}
	} // 同时取 _ 与 值 遍历
	exp := 1             // 把 1 写入 exp :
	for maxNum/exp > 0 { // for maxNum 除以 exp 超过 0 {
		countingSortByDigit(nums, exp) // countingSortByDigit(数组, exp)
		exp *= 10                      // 把 10 写入 exp *
	}
	return nums // 返回 数组
}
func countingSortByDigit(nums []int, exp int) { // 定义函数/方法 countingSortByDigit
	n := len(nums)           // 把 长度(数组) 写入 n :
	output := make([]int, n) // 把 make([]int, 元素个数) 写入 output :
	count := make([]int, 10) // 把 make([]int, 10) 写入 count :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		index := nums[i] / exp // 把 数组[下标 i] 除以 exp 写入 index :
		count[index%10]++      // 计数[index 对…取模 10] 加一
	}
	for i := 1; i < 10; i++ {
		count[i] += count[i-1]
	} // 让 下标 i 从 1 开始计数
	for i := n - 1; i >= 0; i-- { // 把 元素个数 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		index := nums[i] / exp              // 把 数组[下标 i] 除以 exp 写入 index :
		output[count[index%10]-1] = nums[i] // 把 数组[下标 i] 写入 output[count[index%10]-1]
		count[index%10]--                   // 计数[index 对…取模 10] 减一
	}
	for i := 0; i < n; i++ {
		nums[i] = output[i]
	} // 让 下标 i 从 0 开始计数
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   []int
		want []int
	}{ // 把 []struct{ in []int; want []int }{ 写入 cases :
		{[]int{1, 2, 3}, []int{1, 2, 3}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
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
