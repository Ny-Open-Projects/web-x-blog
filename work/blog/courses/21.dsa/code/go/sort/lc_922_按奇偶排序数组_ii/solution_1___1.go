// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134394571
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func sortArrayByParityII(nums []int) []int { // 定义函数/方法 sortArrayByParityII
	sort.Ints(nums)               // sort.Ints(数组)
	res := make([]int, len(nums)) // 把 make([]int, 长度(数组)) 写入 res :
	odd := 1                      // 把 1 写入 odd :
	even := 0                     // 把 0 写入 even :
	for _, item := range nums {   // 同时取 _ 与 item 遍历
		if item%2 == 1 { // 若 item 对…取模 2 等于 1
			res[odd] = item // 把 item 写入 res[odd]
			odd += 2        // odd累加 2
		} else { // 否则
			res[even] = item // 把 item 写入 res[even]
			even += 2        // even累加 2
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	want := []int{2, 5, 4, 7}                     // 把 []int{2, 5, 4, 7} 写入 want :
	got := sortArrayByParityII([]int{4, 2, 5, 7}) // 把 sortArrayByParityII([]int{4, 2, 5, 7}) 写入 got :
	if !reflect.DeepEqual(got, want) {            // 若 取反 reflect.DeepEqual(got, want
		fmt.Println("FAIL", got) // 打印输出
		return                   // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
