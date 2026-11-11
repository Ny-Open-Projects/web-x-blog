// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/99759428
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func twoSumN(nums []int, target int) []int { // 定义函数/方法 twoSumN
	mp := make(map[int]int)    // 把 make(映射表[int]int) 写入 mp :
	for i, num := range nums { // 同时取 下标 i 与 num 遍历
		complement := target - num       // 把 目标值 减 num 写入 complement :
		if j, ok := mp[complement]; ok { // 若 下标 j, ok : 赋值为 mp[complement]; ok
			return []int{j, i} // 返回 []int{下标 j, 下标 i}
		}
		mp[num] = i // 把 下标 i 写入 mp[num]
	}
	return []int{} // 返回 []int{}
}

func maxSubArray(nums []int) int { // 定义函数/方法 maxSubArray
	maxSum := nums[0]                // 把 数组[0] 写入 maxSum :
	currentSum := nums[0]            // 把 数组[0] 写入 currentSum :
	for i := 1; i < len(nums); i++ { // 让 下标 i 从 1 开始计数
		if nums[i] > currentSum+nums[i] { // 若 数组[下标 i] 超过 currentSum 加 数组[下标 i]
			currentSum = nums[i] // 把 数组[下标 i] 写入 currentSum
		} else { // 否则
			currentSum = currentSum + nums[i] // 把 currentSum 加 数组[下标 i] 写入 currentSum
		}
		if currentSum > maxSum { // 若 currentSum 超过 maxSum
			maxSum = currentSum // 把 currentSum 写入 maxSum
		}
	}
	return maxSum // 返回 maxSum
}

func reverseArr(arr []int, left, right int) { // 定义函数/方法 reverseArr
	for left < right { // for 左边界 小于 右边界 {
		arr[left], arr[right] = arr[right], arr[left] // 把 数组[右边界], 数组[左边界] 写入 arr[left], arr[right]
		left++                                        // 左边界 加一
		right--                                       // 右边界 减一
	}
}

func rotateArray(nums []int, k int) { // 定义函数/方法 rotateArray
	n := len(nums) // 把 长度(数组) 写入 n :
	if n == 0 {    // 若 元素个数 等于 0
		return // return
	}
	k %= n                   // 把 元素个数 写入 k %
	reverseArr(nums, 0, n-1) // reverseArr(数组, 0, 元素个数 减 1)
	reverseArr(nums, 0, k-1) // reverseArr(数组, 0, 下标 k 减 1)
	reverseArr(nums, k, n-1) // reverseArr(数组, 下标 k, 元素个数 减 1)
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := twoSumN([]int{2, 7, 11, 15}, 9); !reflect.DeepEqual(got, []int{0, 1}) {
		ok = false                          // 把 false 写入 ok
		fmt.Printf("FAIL twoSum=%v\n", got) // 打印输出
	}
	if got := maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}); got != 6 {
		ok = false                               // 把 false 写入 ok
		fmt.Printf("FAIL maxSubArray=%d\n", got) // 打印输出
	}
	arr := []int{1, 2, 3, 4, 5}                        // 把 []int{1, 2, 3, 4, 5} 写入 arr :
	rotateArray(arr, 2)                                // rotateArray(数组, 2)
	if !reflect.DeepEqual(arr, []int{4, 5, 1, 2, 3}) { // 若 取反 reflect.DeepEqual(数组, []int{4, 5, 1, 2, 3}
		ok = false                               // 把 false 写入 ok
		fmt.Printf("FAIL rotateArray=%v\n", arr) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
