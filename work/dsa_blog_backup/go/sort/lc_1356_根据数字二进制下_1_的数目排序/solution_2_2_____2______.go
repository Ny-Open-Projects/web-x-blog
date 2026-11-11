// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func sortByBits(arr []int) []int { // 定义函数/方法 sortByBits
	bit := make([]int, 10001)    // 把 make([]int, 10001) 写入 bit :
	for i := 1; i < 10001; i++ { // 让 下标 i 从 1 开始计数
		bit[i] = bit[i>>1] + (i & 1) // 把 bit[下标 i 超过 超过 1] 加 (下标 i 按位与 1) 写入 bit[i]
	}
	sortedArr := make([]int, len(arr))          // 把 make([]int, 长度(数组)) 写入 sortedArr :
	copy(sortedArr, arr)                        // copy(sortedArr, 数组)
	sort.Slice(sortedArr, func(i, j int) bool { // sort.Slice(sortedArr, func(下标 i, 下标 j int) bool {
		if bit[sortedArr[i]] != bit[sortedArr[j]] { // 若 bit[sortedArr[下标 i]] 不等于 bit[sortedArr[下标 j]]
			return bit[sortedArr[i]] < bit[sortedArr[j]] // 返回 bit[sortedArr[下标 i]] 小于 bit[sortedArr[下标 j]]
		}
		return sortedArr[i] < sortedArr[j] // 返回 sortedArr[下标 i] 小于 sortedArr[下标 j]
	}) // })
	return sortedArr // 返回 sortedArr
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := sortByBits([]int{1, 2, 3}); !reflect.DeepEqual(got, []int{1, 2, 3}) {
		ok = false                           // 把 false 写入 ok
		fmt.Printf("FAIL [1,2,3]=%v\n", got) // 打印输出
	}
	want := []int{0, 1, 2, 4, 8, 3, 5, 6, 7} // 把 []int{0, 1, 2, 4, 8, 3, 5, 6, 7} 写入 want :
	if got := sortByBits([]int{0, 1, 2, 3, 4, 5, 6, 7, 8}); !reflect.DeepEqual(got, want) {
		ok = false                                     // 把 false 写入 ok
		fmt.Printf("FAIL big=%v want %v\n", got, want) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
