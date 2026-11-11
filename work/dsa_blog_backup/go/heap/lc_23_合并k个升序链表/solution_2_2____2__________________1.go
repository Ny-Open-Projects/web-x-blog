// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

type Status struct { // 定义类型
	val int       // 值 int
	ptr *ListNode // ptr 乘 ListNode
}

type PriorityQueue struct { // 定义类型
	heap []*Status // 堆 [] 乘 Status
}

func NewPQ() *PriorityQueue { // 定义函数/方法 NewPQ
	return &PriorityQueue{heap: []*Status{}} // 返回 按位与 PriorityQueue{堆: [] 乘 Status{}}
}

func (pq *PriorityQueue) Len() int { return len(pq.heap) } // 定义函数/方法 Len

func (pq *PriorityQueue) Push(s *Status) { // 定义函数/方法 Push
	pq.heap = append(pq.heap, s) // 把 append(优先队列.堆, 字符串) 写入 堆
	pq.siftUp(len(pq.heap) - 1)  // 优先队列.siftUp(长度(优先队列.堆) 减 1)
}

func (pq *PriorityQueue) Pop() *Status { // 定义函数/方法 Pop
	if pq.Len() == 0 { // 若 优先队列.Len() 等于 0
		return nil // 返回 nil
	}
	res := pq.heap[0]                  // 把 优先队列.堆[0] 写入 res :
	last := pq.heap[len(pq.heap)-1]    // 把 优先队列.堆[长度(优先队列.堆) 减 1] 写入 last :
	pq.heap = pq.heap[:len(pq.heap)-1] // 把 优先队列.堆[:长度(优先队列.堆) 减 1] 写入 堆
	if pq.Len() > 0 {                  // 若 优先队列.Len() 超过 0
		pq.heap[0] = last // 把 last 写入 pq.heap[0]
		pq.siftDown(0)    // 优先队列.siftDown(0)
	}
	return res // 返回 结果
}

func (pq *PriorityQueue) siftUp(i int) { // 定义函数/方法 siftUp
	for i > 0 { // for 下标 i 超过 0 {
		parent := (i - 1) >> 1                    // 把 (下标 i 减 1) 超过 超过 1 写入 parent :
		if pq.heap[parent].val > pq.heap[i].val { // 若 优先队列.堆[parent].值 超过 优先队列.堆[下标 i].值
			pq.heap[parent], pq.heap[i] = pq.heap[i], pq.heap[parent]
			i = parent // 把 parent 写入 下标 i
		} else { // 否则
			break // 跳出循环
		}
	}
}

func (pq *PriorityQueue) siftDown(i int) { // 定义函数/方法 siftDown
	size := len(pq.heap) // 把 长度(优先队列.堆) 写入 size :
	for {                // for {
		smallest := i                                                 // 把 下标 i 写入 smallest :
		left := 2*i + 1                                               // 把 2 乘 下标 i 加 1 写入 left :
		right := 2*i + 2                                              // 把 2 乘 下标 i 加 2 写入 right :
		if left < size && pq.heap[left].val < pq.heap[smallest].val { // 若 左边界 小于 大小 且 优先队列.堆[左边界].值 小于 优先队列.堆[smallest].值
			smallest = left // 把 左边界 写入 smallest
		}
		if right < size && pq.heap[right].val < pq.heap[smallest].val { // 若 右边界 小于 大小 且 优先队列.堆[右边界].值 小于 优先队列.堆[smallest].值
			smallest = right // 把 右边界 写入 smallest
		}
		if smallest == i { // 若 smallest 等于 下标 i
			break // 跳出循环
		}
		pq.heap[smallest], pq.heap[i] = pq.heap[i], pq.heap[smallest]
		i = smallest // 把 smallest 写入 下标 i
	}
}

func mergeKLists(lists []*ListNode) *ListNode { // 定义函数/方法 mergeKLists
	pq := NewPQ()                // 把 NewPQ() 写入 pq :
	for _, node := range lists { // 同时取 _ 与 节点 遍历
		if node != nil { // 若 节点 不等于 nil
			pq.Push(&Status{val: node.Val, ptr: node}) // 优先队列.Push( 按位与 Status{值: 节点.Val, ptr: 节点})
		}
	}
	dummy := &ListNode{} // 把 按位与 ListNode{} 写入 dummy :
	tail := dummy        // 把 哨兵节点 写入 tail :
	for pq.Len() > 0 {   // for 优先队列.Len() 超过 0 {
		f := pq.Pop() // 把 优先队列.Pop() 写入 f :
		if f != nil { // 若 f 不等于 nil
			tail.Next = f.ptr      // 把 f.ptr 写入 tail.Next
			tail = tail.Next       // 把 尾节点.Next 写入 尾节点
			if f.ptr.Next != nil { // 若 f.ptr.Next 不等于 nil
				pq.Push(&Status{val: f.ptr.Next.Val, ptr: f.ptr.Next}) // 优先队列.Push( 按位与 Status{值: f.ptr.Next.Val, ptr: f.ptr.Next})
			}
		}
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func build(arr []int) *ListNode { // 定义函数/方法 build
	dummy := &ListNode{}    // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy           // 把 哨兵节点 写入 curr :
	for _, v := range arr { // 同时取 _ 与 值 遍历
		curr.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 curr.Next
		curr = curr.Next              // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func toList(node *ListNode) []int { // 定义函数/方法 toList
	res := []int{}    // 把 []int{} 写入 res :
	for node != nil { // 把 nil { 写入 for node !
		res = append(res, node.Val) // 把 append(结果, 节点.Val) 写入 结果
		node = node.Next            // 把 节点.Next 写入 节点
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   [][]int // in [][]int
		want []int   // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[][]int{{1, 4, 5}, {1, 3, 4}, {2, 6}}, []int{1, 1, 2, 3, 4, 4, 5, 6}},
		{[][]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		lists := []*ListNode{}   // 把 [] 乘 ListNode{} 写入 lists :
		for _, a := range c.in { // 同时取 _ 与 数组 遍历
			lists = append(lists, build(a)) // 把 append(lists, build(数组)) 写入 lists
		}
		got := toList(mergeKLists(lists))    // 把 toList(mergeKLists(lists)) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%v want=%v\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
