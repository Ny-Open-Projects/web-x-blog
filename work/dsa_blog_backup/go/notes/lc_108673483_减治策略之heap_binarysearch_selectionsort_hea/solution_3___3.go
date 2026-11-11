// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/108673483
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// majorityElement 求多数元素（出现次数 > n/2），使用 Boyer-Moore 投票法。无多数元素时返回 -1。
func majorityElement(arr []int) int { // 定义函数/方法 majorityElement
	candidate := 0            // 把 0 写入 candidate :
	count := 0                // 把 0 写入 count :
	for _, num := range arr { // 同时取 _ 与 num 遍历
		if count == 0 { // 若 计数 等于 0
			candidate = num // 把 num 写入 candidate
		}
		if num == candidate { // 若 num 等于 candidate
			count++ // 计数 加一
		} else { // 否则
			count-- // 计数 减一
		}
	}
	// 验证候选是否真的为多数元素
	cnt := 0                  // 把 0 写入 cnt :
	for _, num := range arr { // 同时取 _ 与 num 遍历
		if num == candidate { // 若 num 等于 candidate
			cnt++ // 计数 加一
		}
	}
	if cnt > len(arr)/2 { // 若 计数 超过 长度(数组) 除以 2
		return candidate // 返回 candidate
	}
	return -1 // 返回 减 1
}

func main() { // 程序入口：跑内嵌自测用例
	if majorityElement([]int{2, 2, 1, 1, 1, 1, 1}) != 1 { // 若 majorityElement([]int{2, 2, 1, 1, 1, 1, 1}) 不等于 1
		fmt.Println("FAIL majorityElement 1") // 打印输出
		os.Exit(1)                            // os.Exit(1)
	}
	if majorityElement([]int{1, 2, 3}) != -1 { // 若 majorityElement([]int{1, 2, 3}) 不等于 减 1
		fmt.Println("FAIL majorityElement -1") // 打印输出
		os.Exit(1)                             // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
