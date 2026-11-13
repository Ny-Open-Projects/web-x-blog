package main

import (
	"container/heap"
	"fmt"
	"sort"
)

type pHeap []int

func (h pHeap) Len() int            { return len(h) }
func (h pHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h pHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pHeap) Push(x any)         { *h = append(*h, x.(int)) }
func (h *pHeap) Pop() any {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	n := len(profits)
	indices := make([]int, n)
	for i := 0; i < n; i++ {
		indices[i] = i
	}
	sort.Slice(indices, func(a, b int) bool {
		return capital[indices[a]] < capital[indices[b]]
	})
	maxHeap := &pHeap{}
	heap.Init(maxHeap)
	i := 0
	for t := 0; t < k; t++ {
		for i < n && capital[indices[i]] <= w {
			heap.Push(maxHeap, profits[indices[i]])
			i++
		}
		if maxHeap.Len() == 0 {
			break
		}
		w += heap.Pop(maxHeap).(int)
	}
	return w
}

func main() {
	type tc struct {
		k       int
		w       int
		profits []int
		capital []int
		want    int
	}
	cases := []tc{
		{2, 0, []int{1, 2, 3}, []int{0, 1, 1}, 4},
	}
	ok := true
	for _, c := range cases {
		got := findMaximizedCapital(c.k, c.w, c.profits, c.capital)
		if got != c.want {
			ok = false
			fmt.Printf("FAIL got=%d want=%d\n", got, c.want)
		}
	}
	if !ok {
		panic("FAILED")
	}
	fmt.Println("PASS")
}
