// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// MaxHeap 实现最大堆（方式二：max_heapify 原地建堆 + 堆排序）
type MaxHeap struct { // 定义类型
	heap []int // 堆 []int
}

func (h *MaxHeap) swap(i, j int) { // 定义函数/方法 swap
	if i == j { // 若 下标 i 等于 下标 j
		return // return
	}
	h.heap[i], h.heap[j] = h.heap[j], h.heap[i] // 把 h.堆[下标 j], h.堆[下标 i] 写入 h.heap[i], h.heap[j]
}

func (h *MaxHeap) maxHeapify(i, size int) { // 定义函数/方法 maxHeapify
	largest := i                                       // 把 下标 i 写入 largest :
	left := 2*i + 1                                    // 把 2 乘 下标 i 加 1 写入 left :
	right := 2*i + 2                                   // 把 2 乘 下标 i 加 2 写入 right :
	if left < size && h.heap[left] > h.heap[largest] { // 若 左边界 小于 大小 且 h.堆[左边界] 超过 h.堆[largest]
		largest = left // 把 左边界 写入 largest
	}
	if right < size && h.heap[right] > h.heap[largest] { // 若 右边界 小于 大小 且 h.堆[右边界] 超过 h.堆[largest]
		largest = right // 把 右边界 写入 largest
	}
	if largest != i { // 若 largest 不等于 下标 i
		h.swap(largest, i)          // h.交换 largest, 下标 i)
		h.maxHeapify(largest, size) // h.maxHeapify(largest, 大小)
	}
}

func (h *MaxHeap) sort() []int { // 定义函数/方法 sort
	n := len(h.heap) // 把 长度(h.堆) 写入 n :
	if n <= 1 {      // 若 元素个数 不超过 1
		return h.heap // 返回 h.堆
	}
	for i := n/2 - 1; i >= 0; i-- { // 把 元素个数 除以 2 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		h.maxHeapify(i, n) // h.maxHeapify(下标 i, 元素个数)
	}
	for j := 0; j < n-1; j++ { // 让 下标 j 从 0 开始计数
		h.swap(0, n-1-j)         // h.交换 0, 元素个数 减 1 减 下标 j)
		h.maxHeapify(0, n-1-j-1) // h.maxHeapify(0, 元素个数 减 1 减 下标 j 减 1)
	}
	return h.heap // 返回 h.堆
}

func main() { // 程序入口：跑内嵌自测用例
	mh := &MaxHeap{}                                             // 把 按位与 MaxHeap{} 写入 mh :
	mh.heap = []int{1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98} // 把 []int{1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, 减 1, 98} 写入 堆
	got := mh.sort()                                             // 排序
	want := []int{-1, 1, 1, 3, 3, 5, 9, 9, 10, 11, 11, 13, 98}
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL sort=%v\n", got) // 打印输出
		os.Exit(1)                        // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
