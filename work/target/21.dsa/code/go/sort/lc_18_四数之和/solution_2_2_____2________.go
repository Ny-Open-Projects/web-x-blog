// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245574
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func fourSum(nums []int, target int) [][]int { // 定义函数/方法 fourSum
	sort.Ints(nums)            // sort.Ints(数组)
	res := [][]int{}           // 把 [][]int{} 写入 res :
	n := len(nums)             // 把 长度(数组) 写入 n :
	for i := 0; i < n-3; i++ { // 让 下标 i 从 0 开始计数
		if i > 0 && nums[i] == nums[i-1] { // 若 下标 i 超过 0 且 数组[下标 i] 等于 数组[下标 i 减 1]
			continue // 跳过本轮，进入下一次
		}
		for j := i + 1; j < n-2; j++ { // 把 下标 i 加 1; 下标 j 小于 元素个数 减 2; 下标 j 加一 { 写入 for j :
			if j > i+1 && nums[j] == nums[j-1] { // 若 下标 j 超过 下标 i 加 1 且 数组[下标 j] 等于 数组[下标 j 减 1]
				continue // 跳过本轮，进入下一次
			}
			l, r := j+1, n-1 // 把 下标 j 加 1, 元素个数 减 1 写入 l, r :
			for l < r {      // for 左指针 小于 右指针 {
				sum := nums[i] + nums[j] + nums[l] + nums[r] // 把 数组[下标 i] 加 数组[下标 j] 加 数组[左指针] 加 数组[右指针] 写入 sum :
				if sum == target {                           // 若 累计和 等于 目标值
					res = append(res, []int{nums[i], nums[j], nums[l], nums[r]})
					for l < r && nums[l] == nums[l+1] { // 把 赋值为 数组[左指针 加 1] { 写入 for l < r && nums[l]
						l++ // 左指针 加一
					}
					for l < r && nums[r] == nums[r-1] { // 把 赋值为 数组[右指针 减 1] { 写入 for l < r && nums[r]
						r-- // 右指针 减一
					}
					l++ // 左指针 加一
					r-- // 右指针 减一
				} else if sum < target { // 否则，若 累计和 小于 目标值
					l++ // 左指针 加一
				} else { // 否则
					r-- // 右指针 减一
				}
			}
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := fourSum([]int{1, 2, 3}, 1); !reflect.DeepEqual(got, [][]int{}) {
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL [1,2,3]=%v\n", got) // 打印输出
	}
	want := [][]int{{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}}
	if got := fourSum([]int{1, 0, -1, 0, -2, 2}, 0); !reflect.DeepEqual(got, want) {
		ok = false                                         // 把 false 写入 ok
		fmt.Printf("FAIL classic=%v want %v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
