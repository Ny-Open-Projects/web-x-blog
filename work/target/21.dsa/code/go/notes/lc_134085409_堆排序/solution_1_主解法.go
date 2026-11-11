// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func heapify(arr []int, n, root int) { // 定义函数/方法 heapify
	largest := root                     // 把 根节点 写入 largest :
	l := 2*root + 1                     // 把 2 乘 根节点 加 1 写入 l :
	r := 2*root + 2                     // 把 2 乘 根节点 加 2 写入 r :
	if l < n && arr[l] > arr[largest] { // 若 左指针 小于 元素个数 且 数组[左指针] 超过 数组[largest]
		largest = l // 把 左指针 写入 largest
	}
	if r < n && arr[r] > arr[largest] { // 若 右指针 小于 元素个数 且 数组[右指针] 超过 数组[largest]
		largest = r // 把 右指针 写入 largest
	}
	if largest != root { // 若 largest 不等于 根节点
		arr[root], arr[largest] = arr[largest], arr[root] // 把 数组[largest], 数组[根节点] 写入 arr[root], arr[largest]
		heapify(arr, n, largest)                          // heapify(数组, 元素个数, largest)
	}
}

func heapSort(arr []int) []int { // 定义函数/方法 heapSort
	a := append([]int{}, arr...)    // 把 append([]int{}, 数组...) 写入 a :
	n := len(a)                     // 把 长度(数组) 写入 n :
	for i := n/2 - 1; i >= 0; i-- { // 把 元素个数 除以 2 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		heapify(a, n, i) // heapify(数组, 元素个数, 下标 i)
	}
	for i := n - 1; i > 0; i-- { // 把 元素个数 减 1; 下标 i 超过 0; 下标 i 减一 { 写入 for i :
		a[0], a[i] = a[i], a[0] // 把 数组[下标 i], 数组[0] 写入 a[0], a[i]
		heapify(a, i, 0)        // heapify(数组, 下标 i, 0)
	}
	return a // 返回 数组
}

type maxHeap struct { // 定义类型
	data []int // data []int
}

func (h *maxHeap) push(val int) { // 定义函数/方法 push
	h.data = append(h.data, val) // 把 append(h.data, 值) 写入 h.data
	h.up(len(h.data) - 1)        // h.up(长度(h.data) 减 1)
}

func (h *maxHeap) pop() int { // 定义函数/方法 pop
	if len(h.data) == 0 { // 若 长度(h.data) 等于 0
		return 0 // 返回 0
	}
	top := h.data[0]                  // 把 h.data[0] 写入 top :
	h.data[0] = h.data[len(h.data)-1] // 把 h.data[长度(h.data) 减 1] 写入 h.data[0]
	h.data = h.data[:len(h.data)-1]   // 把 h.data[:长度(h.data) 减 1] 写入 h.data
	h.down(0)                         // h.down(0)
	return top                        // 返回 top
}

func (h *maxHeap) up(i int) { // 定义函数/方法 up
	for i > 0 && h.data[i] > h.data[(i-1)/2] { // for 下标 i 超过 0 且 h.data[下标 i] 超过 h.data[(下标 i 减 1) 除以 2] {
		h.data[i], h.data[(i-1)/2] = h.data[(i-1)/2], h.data[i]
		i = (i - 1) / 2 // 把 (下标 i 减 1) 除以 2 写入 下标 i
	}
}

func (h *maxHeap) down(i int) { // 定义函数/方法 down
	n := len(h.data) // 把 长度(h.data) 写入 n :
	for {            // for {
		l, r, m := 2*i+1, 2*i+2, i          // 把 2 乘 下标 i 加 1, 2 乘 下标 i 加 2, 下标 i 写入 l, r, m :
		if l < n && h.data[l] > h.data[m] { // 若 左指针 小于 元素个数 且 h.data[左指针] 超过 h.data[映射表]
			m = l // 把 左指针 写入 映射表
		}
		if r < n && h.data[r] > h.data[m] { // 若 右指针 小于 元素个数 且 h.data[右指针] 超过 h.data[映射表]
			m = r // 把 右指针 写入 映射表
		}
		if m == i { // 若 映射表 等于 下标 i
			break // 跳出循环
		}
		h.data[i], h.data[m] = h.data[m], h.data[i] // 把 h.data[映射表], h.data[下标 i] 写入 h.data[i], h.data[m]
		i = m                                       // 把 映射表 写入 下标 i
	}
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if got := heapSort([]int{12, 11, 13, 5, 6, 7}); !reflect.DeepEqual(got, []int{5, 6, 7, 11, 12, 13}) {
		ok = false                            // 把 false 写入 ok
		fmt.Printf("FAIL heapSort=%v\n", got) // 打印输出
	}
	h := &maxHeap{}                       // 把 按位与 maxHeap{} 写入 h :
	for _, v := range []int{4, 1, 9, 3} { // 同时取 _ 与 值 遍历
		h.push(v) // 把 值 压入栈/数组尾部
	}
	pops := []int{}          // 把 []int{} 写入 pops :
	for i := 0; i < 4; i++ { // 让 下标 i 从 0 开始计数
		pops = append(pops, h.pop()) // 弹出栈顶元素
	}
	if !reflect.DeepEqual(pops, []int{9, 4, 3, 1}) { // 若 取反 reflect.DeepEqual(pops, []int{9, 4, 3, 1}
		ok = false                                 // 把 false 写入 ok
		fmt.Printf("FAIL maxHeap pops=%v\n", pops) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
