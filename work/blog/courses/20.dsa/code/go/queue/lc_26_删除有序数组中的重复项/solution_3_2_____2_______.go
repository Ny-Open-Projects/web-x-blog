// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114454
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func removeDuplicates(nums []int) int { // 定义函数/方法 removeDuplicates
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return 0 // 返回 0
	}
	slow := 0                                 // 把 0 写入 slow :
	for fast := 1; fast < len(nums); fast++ { // 让 快指针 从 1 开始计数
		if nums[fast] != nums[slow] { // 若 数组[快指针] 不等于 数组[慢指针]
			slow++                  // 慢指针 加一
			nums[slow] = nums[fast] // 把 数组[快指针] 写入 nums[slow]
		}
	}
	return slow + 1 // 返回 慢指针 加 1
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                                         // 把 true 写入 ok :
	if v := removeDuplicates([]int{1, 2, 3}); v != 3 { // 若 值 : 赋值为 removeDuplicates([]int{1, 2, 3}); 值 不等于 3
		ok = false                         // 把 false 写入 ok
		fmt.Printf("FAIL [1,2,3]=%d\n", v) // 打印输出
	}
	if v := removeDuplicates([]int{1, 1, 2}); v != 2 { // 若 值 : 赋值为 removeDuplicates([]int{1, 1, 2}); 值 不等于 2
		ok = false                         // 把 false 写入 ok
		fmt.Printf("FAIL [1,1,2]=%d\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
