// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

func sortArrayByParityII(nums []int) []int { // 定义函数/方法 sortArrayByParityII
	res := make([]int, len(nums)) // 把 make([]int, 长度(数组)) 写入 res :
	e := 0                        // 把 0 写入 e :
	o := 1                        // 把 1 写入 o :
	for _, x := range nums {      // 同时取 _ 与 x 遍历
		if x%2 == 0 { // 若 x 对…取模 2 等于 0
			res[e] = x // 把 x 写入 res[e]
			e += 2     // e累加 2
		} else { // 否则
			res[o] = x // 把 x 写入 res[o]
			o += 2     // o累加 2
		}
	}
	return res // 返回 结果
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
