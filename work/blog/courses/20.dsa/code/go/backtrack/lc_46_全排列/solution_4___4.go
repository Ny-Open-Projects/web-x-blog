// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134689827
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func permute(nums []int) [][]int { // 定义函数/方法 permute
	nums = append([]int{}, nums...) // 把 append([]int{}, 数组...) 写入 数组
	res := [][]int{}                // 把 [][]int{} 写入 res :
	var backtrack func(start int)   // var backtrack func(起点 int)
	backtrack = func(start int) {   // 把 func(起点 int) { 写入 backtrack
		if start == len(nums) { // 若 起点 等于 长度(数组
			res = append(res, append([]int{}, nums...)) // 把 append(结果, append([]int{}, 数组...)) 写入 结果
			return                                      // return
		}
		for i := start; i < len(nums); i++ { // 把 起点; 下标 i 小于 长度(数组); 下标 i 加一 { 写入 for i :
			nums[start], nums[i] = nums[i], nums[start] // 把 数组[下标 i], 数组[起点] 写入 nums[start], nums[i]
			backtrack(start + 1)                        // backtrack(起点 加 1)
			nums[start], nums[i] = nums[i], nums[start] // 把 数组[下标 i], 数组[起点] 写入 nums[start], nums[i]
		}
	}
	backtrack(0) // backtrack(0)
	return res   // 返回 结果
}

func norm2D(s [][]int) [][]int { // 定义函数/方法 norm2D
	out := make([][]int, len(s)) // 把 make([][]int, 长度(字符串)) 写入 out :
	for i := range s {           // 把 range 字符串 { 写入 for i :
		out[i] = append([]int{}, s[i]...) // 把 append([]int{}, 字符串[下标 i]...) 写入 out[i]
		sort.Ints(out[i])                 // sort.Ints(out[下标 i])
	}
	sort.Slice(out, func(a, b int) bool { // sort.Slice(out, func(数组, b int) bool {
		return fmt.Sprint(out[a]) < fmt.Sprint(out[b]) // 返回 fmt.Sprint(out[数组]) 小于 fmt.Sprint(out[b])
	}) // })
	return out // 返回 out
}

func main() { // 程序入口：跑内嵌自测用例
	got := norm2D(permute([]int{1, 2, 3})) // 把 norm2D(permute([]int{1, 2, 3})) 写入 got :
	want := norm2D([][]int{{1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}})
	ok := reflect.DeepEqual(got, want) // 把 reflect.DeepEqual(got, want) 写入 ok :
	if !ok {                           // 若 取反 ok
		fmt.Printf("FAIL permute([1,2,3])=%v want %v\n", got, want) // 打印输出
		os.Exit(1)                                                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
