// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/93536806
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func twoSumBrute(nums []int, target int) []int { // 定义函数/方法 twoSumBrute
	for i := 0; i < len(nums); i++ { // 让 下标 i 从 0 开始计数
		for j := i + 1; j < len(nums); j++ { // 把 下标 i 加 1; 下标 j 小于 长度(数组); 下标 j 加一 { 写入 for j :
			if nums[i]+nums[j] == target { // 若 数组[下标 i] 加 数组[下标 j] 等于 目标值
				return []int{i, j} // 返回 []int{下标 i, 下标 j}
			}
		}
	}
	return []int{} // 返回 []int{}
}

func twoSumHash(nums []int, target int) []int { // 定义函数/方法 twoSumHash
	seen := make(map[int]int)  // 把 make(映射表[int]int) 写入 seen :
	for i, num := range nums { // 同时取 下标 i 与 num 遍历
		if j, ok := seen[target-num]; ok { // 若 下标 j, ok : 赋值为 已见集合[目标值 减 num]; ok
			return []int{j, i} // 返回 []int{下标 j, 下标 i}
		}
		seen[num] = i // 把 下标 i 写入 seen[num]
	}
	return []int{} // 返回 []int{}
}

func main() { // 程序入口：跑内嵌自测用例
	nums := []int{2, 7, 11, 15} // 把 []int{2, 7, 11, 15} 写入 nums :
	target := 9                 // 把 9 写入 target :
	ok := true                  // 把 true 写入 ok :
	if got := twoSumBrute(nums, target); !reflect.DeepEqual(got, []int{0, 1}) {
		ok = false                               // 把 false 写入 ok
		fmt.Printf("FAIL twoSumBrute=%v\n", got) // 打印输出
	}
	if got := twoSumHash(nums, target); !reflect.DeepEqual(got, []int{0, 1}) {
		ok = false                              // 把 false 写入 ok
		fmt.Printf("FAIL twoSumHash=%v\n", got) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
