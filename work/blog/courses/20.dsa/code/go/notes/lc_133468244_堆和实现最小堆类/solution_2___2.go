// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133468244
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type MinHeap struct { // 定义类型
	heap []int // 堆 []int
}

func (h *MinHeap) getParentIndex(i int) int { return (i - 1) >> 1 }                         // 定义函数/方法 getParentIndex
func (h *MinHeap) getLeftIndex(i int) int   { return (i << 1) + 1 }                         // 定义函数/方法 getLeftIndex
func (h *MinHeap) getRightIndex(i int) int  { return (i << 1) + 2 }                         // 定义函数/方法 getRightIndex
func (h *MinHeap) swap(i, j int)            { h.heap[i], h.heap[j] = h.heap[j], h.heap[i] } // 定义函数/方法 swap

func (h *MinHeap) shiftUp(i int) { // 定义函数/方法 shiftUp
	if i == 0 { // 若 下标 i 等于 0
		return // return
	}
	pi := h.getParentIndex(i)   // 把 h.getParentIndex(下标 i) 写入 pi :
	if h.heap[pi] > h.heap[i] { // 若 h.堆[pi] 超过 h.堆[下标 i]
		h.swap(pi, i) // h.交换 pi, 下标 i)
		h.shiftUp(pi) // h.shiftUp(pi)
	}
}

func (h *MinHeap) shiftDown(i int) { // 定义函数/方法 shiftDown
	size := h.size()                   // 把 h.大小() 写入 size :
	li := h.getLeftIndex(i)            // 把 h.getLeftIndex(下标 i) 写入 li :
	ri := h.getRightIndex(i)           // 把 h.getRightIndex(下标 i) 写入 ri :
	cur := h.heap[i]                   // 把 h.堆[下标 i] 写入 cur :
	smallest := i                      // 把 下标 i 写入 smallest :
	if li < size && h.heap[li] < cur { // 若 li 小于 大小 且 h.堆[li] 小于 当前值
		smallest = li // 把 li 写入 smallest
	}
	if ri < size && h.heap[ri] < h.heap[smallest] { // 若 ri 小于 大小 且 h.堆[ri] 小于 h.堆[smallest]
		smallest = ri // 把 ri 写入 smallest
	}
	if smallest != i { // 若 smallest 不等于 下标 i
		h.swap(smallest, i)   // h.交换 smallest, 下标 i)
		h.shiftDown(smallest) // h.shiftDown(smallest)
	}
}

func (h *MinHeap) insert(value int) { // 定义函数/方法 insert
	h.heap = append(h.heap, value) // 把 append(h.堆, value) 写入 堆
	h.shiftUp(len(h.heap) - 1)     // h.shiftUp(长度(h.堆) 减 1)
}

func (h *MinHeap) pop() { // 定义函数/方法 pop
	if h.size() == 0 { // 若 h.大小() 等于 0
		return // return
	}
	h.heap[0] = h.heap[len(h.heap)-1] // 把 h.堆[长度(h.堆) 减 1] 写入 h.heap[0]
	h.heap = h.heap[:len(h.heap)-1]   // 把 h.堆[:长度(h.堆) 减 1] 写入 堆
	h.shiftDown(0)                    // h.shiftDown(0)
}

func (h *MinHeap) peek() int { // 定义函数/方法 peek
	if h.size() == 0 { // 若 h.大小() 等于 0
		return 0 // 返回 0
	}
	return h.heap[0] // 返回 h.堆[0]
}

func (h *MinHeap) size() int { return len(h.heap) } // 定义函数/方法 size

func main() { // 程序入口：跑内嵌自测用例
	heap := &MinHeap{}                                          // 把 按位与 MinHeap{} 写入 heap :
	heap.insert(3)                                              // 堆 插入 3)
	heap.insert(1)                                              // 堆 插入 1)
	heap.insert(6)                                              // 堆 插入 6)
	heap.insert(5)                                              // 堆 插入 5)
	heap.insert(2)                                              // 堆 插入 2)
	heap.insert(4)                                              // 堆 插入 4)
	if !reflect.DeepEqual(heap.heap, []int{1, 2, 4, 5, 3, 6}) { // 若 取反 reflect.DeepEqual(堆.堆, []int{1, 2, 4, 5, 3, 6}
		fmt.Printf("FAIL after insertions=%v\n", heap.heap) // 打印输出
		os.Exit(1)                                          // os.Exit(1)
	}
	if heap.peek() != 1 { // 若 堆.peek() 不等于 1
		fmt.Println("FAIL peek") // 打印输出
		os.Exit(1)               // os.Exit(1)
	}
	heap.pop()                                               // 弹出栈顶元素
	if !reflect.DeepEqual(heap.heap, []int{2, 3, 4, 5, 6}) { // 若 取反 reflect.DeepEqual(堆.堆, []int{2, 3, 4, 5, 6}
		fmt.Printf("FAIL after pop1=%v\n", heap.heap) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	heap.pop()                                            // 弹出栈顶元素
	if !reflect.DeepEqual(heap.heap, []int{3, 5, 4, 6}) { // 若 取反 reflect.DeepEqual(堆.堆, []int{3, 5, 4, 6}
		fmt.Printf("FAIL after pop2=%v\n", heap.heap) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	if heap.size() != 4 { // 若 堆.大小() 不等于 4
		fmt.Println("FAIL size") // 打印输出
		os.Exit(1)               // os.Exit(1)
	}
	empty := &MinHeap{}    // 把 按位与 MinHeap{} 写入 empty :
	_ = empty.peek()       // 把 empty.peek() 写入 _
	empty.pop()            // 弹出栈顶元素
	if empty.size() != 0 { // 若 empty.大小() 不等于 0
		fmt.Println("FAIL empty size") // 打印输出
		os.Exit(1)                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
