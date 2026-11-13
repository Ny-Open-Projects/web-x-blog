// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

func sortArrayByParityII(nums []int) []int { // 定义函数/方法 sortArrayByParityII
	n := len(nums)              // 把 长度(数组) 写入 n :
	j := 1                      // 把 1 写入 j :
	for i := 0; i < n; i += 2 { // 让 下标 i 从 0 开始计数
		if nums[i]&1 == 1 { // 若 数组[下标 i] 按位与 1 等于 1
			for nums[j]&1 == 1 { // 把 赋值为 1 { 写入 for nums[j]&1
				j += 2 // 下标 j累加 2
			}
			nums[i], nums[j] = nums[j], nums[i] // 把 数组[下标 j], 数组[下标 i] 写入 nums[i], nums[j]
		}
	}
	return nums // 返回 数组
}

func main() { // 程序入口：跑内嵌自测用例
	if !reflect.DeepEqual(sortArrayByParityII([]int{4, 2, 5, 7}), []int{4, 5, 2, 7}) {
		fmt.Println("FAIL1") // 打印输出
		return               // return
	}
	if !reflect.DeepEqual(sortArrayByParityII([]int{2, 3}), []int{2, 3}) {
		fmt.Println("FAIL2") // 打印输出
		return               // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
