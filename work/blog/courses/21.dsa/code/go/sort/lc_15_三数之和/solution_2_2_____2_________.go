// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145233688
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func threeSum(nums []int) [][]int { // 定义函数/方法 threeSum
	sort.Ints(nums)            // sort.Ints(数组)
	result := [][]int{}        // 把 [][]int{} 写入 result :
	n := len(nums)             // 把 长度(数组) 写入 n :
	for i := 0; i < n-2; i++ { // 让 下标 i 从 0 开始计数
		if i > 0 && nums[i] == nums[i-1] { // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]
			continue // 跳过本轮，进入下一次
		}
		left, right := i+1, n-1 // 把 下标 i 加 1, 元素个数 减 1 写入 left, right :
		for left < right {      // for 左边界 小于 右边界 {
			total := nums[i] + nums[left] + nums[right] // 把 数组[下标 i] 加 数组[左边界] 加 数组[右边界] 写入 total :
			if total < 0 {                              // 若 总和 小于 0
				left++ // 左边界 加一
			} else if total > 0 { // 否则，若 总和 超过 0
				right-- // 右边界 减一
			} else { // 否则
				result = append(result, []int{nums[i], nums[left], nums[right]}) // 把 append(结果, []int{数组[下标 i], 数组[左边界], 数组[右边界]}) 写入 结果
				for left < right && nums[left] == nums[left+1] {                 // 把 赋值为 数组[左边界 加 1] { 写入 for left < right && nums[left]
					left++ // 左边界 加一
				}
				for left < right && nums[right] == nums[right-1] { // 把 赋值为 数组[右边界 减 1] { 写入 for left < right && nums[right]
					right-- // 右边界 减一
				}
				left++  // 左边界 加一
				right-- // 右边界 减一
			}
		}
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := threeSum([]int{1, 2, 3}); !reflect.DeepEqual(got, [][]int{}) {
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL [1,2,3]=%v\n", got) // 打印输出
	}
	want := [][]int{{-1, -1, 2}, {-1, 0, 1}} // 把 [][]int{{ 减 1, 减 1, 2}, { 减 1, 0, 1}} 写入 want :
	if got := threeSum([]int{-1, 0, 1, 2, -1, -4}); !reflect.DeepEqual(got, want) {
		ok = false                                         // 把 false 写入 ok
		fmt.Printf("FAIL classic=%v want %v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
