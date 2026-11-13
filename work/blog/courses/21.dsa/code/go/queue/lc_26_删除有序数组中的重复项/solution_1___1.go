// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func RemoveDuplicates(nums []int) int { // 定义函数/方法 RemoveDuplicates
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	k := 1                           // 把 1 写入 k :
	for i := 1; i < len(nums); i++ { // 让 下标 i 从 1 开始计数
		if nums[i] != nums[i-1] { // 若 数组[下标 i] 不等于 数组[下标 i 减 1]
			nums[k] = nums[i] // 把 数组[下标 i] 写入 nums[k]
			k++               // 下标 k 加一
		}
	}
	return k // 返回 下标 k
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                               // 把 true 写入 ok :
	nums := []int{1, 1, 2}                                   // 把 []int{1, 1, 2} 写入 nums :
	k := RemoveDuplicates(nums)                              // 把 RemoveDuplicates(数组) 写入 k :
	if k != 2 || !reflect.DeepEqual(nums[:k], []int{1, 2}) { // 若 下标 k 不等于 2 或 取反 reflect.DeepEqual(数组[:下标 k], []int{1, 2}
		ok = false                                                        // 把 false 写入 ok
		fmt.Printf("FAIL removeDuplicates([1,1,2])=%d %v\n", k, nums[:k]) // 打印输出
	}
	nums2 := []int{}                  // 把 []int{} 写入 nums2 :
	if RemoveDuplicates(nums2) != 0 { // 若 RemoveDuplicates(数组2) 不等于 0
		ok = false                // 把 false 写入 ok
		fmt.Println("FAIL empty") // 打印输出
	}
	nums3 := []int{1, 2, 3}           // 把 []int{1, 2, 3} 写入 nums3 :
	if RemoveDuplicates(nums3) != 3 { // 若 RemoveDuplicates(nums3) 不等于 3
		ok = false                  // 把 false 写入 ok
		fmt.Println("FAIL no-dups") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
