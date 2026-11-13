// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133530983
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// MaxHeap 实现最大堆（方式一：insert/pop 构建并排序）
type MaxHeap struct { // 定义类型
	heap []int // 堆 []int
}

func (h *MaxHeap) getParentIndex(i int) int { return (i - 1) >> 1 }                         // 定义函数/方法 getParentIndex
func (h *MaxHeap) getLeftIndex(i int) int   { return (i << 1) + 1 }                         // 定义函数/方法 getLeftIndex
func (h *MaxHeap) getRightIndex(i int) int  { return (i << 1) + 2 }                         // 定义函数/方法 getRightIndex
func (h *MaxHeap) swap(i, j int)            { h.heap[i], h.heap[j] = h.heap[j], h.heap[i] } // 定义函数/方法 swap

func (h *MaxHeap) shiftUp(index int) { // 定义函数/方法 shiftUp
	if index == 0 { // 若 index 等于 0
		return // return
	}
	parentIndex := h.getParentIndex(index)   // 把 h.getParentIndex(index) 写入 parentIndex :
	if h.heap[parentIndex] < h.heap[index] { // 若 h.堆[parentIndex] 小于 h.堆[index]
		h.swap(parentIndex, index) // h.交换 parentIndex, index)
		h.shiftUp(parentIndex)     // h.shiftUp(parentIndex)
	}
}

func (h *MaxHeap) shiftDown(index int) { // 定义函数/方法 shiftDown
	if index >= len(h.heap)-1 { // 若 index 不低于 长度(h.堆) 减 1
		return // return
	}
	size := h.size()                                           // 把 h.大小() 写入 size :
	leftIndex := h.getLeftIndex(index)                         // 把 h.getLeftIndex(index) 写入 leftIndex :
	rightIndex := h.getRightIndex(index)                       // 把 h.getRightIndex(index) 写入 rightIndex :
	if leftIndex < size && h.heap[leftIndex] > h.heap[index] { // 若 leftIndex 小于 大小 且 h.堆[leftIndex] 超过 h.堆[index]
		h.swap(leftIndex, index) // h.交换 leftIndex, index)
		h.shiftDown(leftIndex)   // h.shiftDown(leftIndex)
	}
	if rightIndex < size && h.heap[rightIndex] > h.heap[index] { // 若 rightIndex 小于 大小 且 h.堆[rightIndex] 超过 h.堆[index]
		h.swap(rightIndex, index) // h.交换 rightIndex, index)
		h.shiftDown(rightIndex)   // h.shiftDown(rightIndex)
	}
}

func (h *MaxHeap) insert(value int) { // 定义函数/方法 insert
	h.heap = append(h.heap, value) // 把 append(h.堆, value) 写入 堆
	h.shiftUp(len(h.heap) - 1)     // h.shiftUp(长度(h.堆) 减 1)
}

func (h *MaxHeap) pop() { // 定义函数/方法 pop
	if len(h.heap) <= 1 { // 若 长度(h.堆) 不超过 1
		return // return
	}
	h.heap[0] = h.heap[len(h.heap)-1] // 把 h.堆[长度(h.堆) 减 1] 写入 h.heap[0]
	h.heap = h.heap[:len(h.heap)-1]   // 把 h.堆[:长度(h.堆) 减 1] 写入 堆
	h.shiftDown(0)                    // h.shiftDown(0)
}

func (h *MaxHeap) peak() int { // 定义函数/方法 peak
	if len(h.heap) == 0 { // 若 长度(h.堆) 等于 0
		return 0 // 返回 0
	}
	return h.heap[0] // 返回 h.堆[0]
}

func (h *MaxHeap) size() int { return len(h.heap) } // 定义函数/方法 size

func (h *MaxHeap) sort(arr []int) []int { // 定义函数/方法 sort
	for _, n := range arr { // 同时取 _ 与 元素个数 遍历
		h.insert(n) // h 插入 元素个数)
	}
	result := []int{}  // 把 []int{} 写入 result :
	for h.size() > 1 { // for h.大小() 超过 1 {
		result = append(result, h.peak()) // 把 append(结果, h.peak()) 写入 结果
		h.pop()                           // 弹出栈顶元素
	}
	result = append(result, h.peak()) // 把 append(结果, h.peak()) 写入 结果
	h.heap = result                   // 把 结果 写入 堆
	return result                     // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	mh := &MaxHeap{}                                                   // 把 按位与 MaxHeap{} 写入 mh :
	got := mh.sort([]int{1, 10, 9, 5, 3, 11, 3, 9, 11, 13, 1, -1, 98}) // 排序
	want := []int{98, 13, 11, 11, 10, 9, 9, 5, 3, 3, 1, 1, -1}
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL sort=%v\n", got) // 打印输出
		os.Exit(1)                        // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
