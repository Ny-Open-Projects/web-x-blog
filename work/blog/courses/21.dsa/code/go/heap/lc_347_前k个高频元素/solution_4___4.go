// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133493400
package main // 引入依赖
import (
	"fmt"
	"os"
	"reflect" // 引入依赖
	"sort"
)

func topKFrequent(nums []int, k int) []int { // 定义函数/方法 topKFrequent
	cnt := map[int]int{} // 把 映射表[int]int{} 写入 cnt :
	for _, n := range nums {
		cnt[n]++
	} // 同时取 _ 与 元素个数 遍历
	type kv struct{ num, freq int } // 定义类型
	lst := []kv{}                   // 把 []kv{} 写入 lst :
	for num, f := range cnt {
		lst = append(lst, kv{num, f})
	} // 同时取 num 与 f 遍历
	sort.Slice(lst, func(i, j int) bool { return lst[i].freq > lst[j].freq })
	res := []int{} // 把 []int{} 写入 res :
	for i := 0; i < k && i < len(lst); i++ {
		res = append(res, lst[i].num)
	} // 让 下标 i 从 0 开始计数
	return res // 返回 结果
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		nums []int
		k    int
		want []int
	}{ // 把 []struct{ 数组 []int; 下标 k int; want []int }{ 写入 cases :
		{[]int{1, 1, 1, 2, 2, 3}, 2, []int{1, 2}},
		{[]int{1, 1, 1, 2, 2, 3, 3, 3, 3, 4}, 2, []int{1, 3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := topKFrequent(c.nums, c.k) // 把 topKFrequent(字符.数组, 字符.下标 k) 写入 got :
		g := append([]int{}, got...)     // 把 append([]int{}, got...) 写入 g :
		sort.Ints(g)                     // sort.Ints(g)
		w := append([]int{}, c.want...)  // 把 append([]int{}, 字符.want...) 写入 w :
		sort.Ints(w)                     // sort.Ints(权重)
		if !reflect.DeepEqual(g, w) {    // 若 取反 reflect.DeepEqual(g, 权重
			ok = false
			fmt.Printf("FAIL got %v want %v\n", got, c.want) // 打印输出
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
