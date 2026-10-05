/**
 * 并发编程，map的线程安全性问题
 */
package main

import (
	"fmt"
	"sync"
	"time"
)

var data map[int]int = make(map[int]int)
var wgMap sync.WaitGroup = sync.WaitGroup{}
var muMap sync.Mutex = sync.Mutex{}

func main() {
	// 并发启动的协程数量
	max := 100000
	fmt.Printf("map add num=%d\n", max)
	wgMap.Add(max)
	time1 := time.Now().UnixNano()
	for i := 0; i < max; i++ {
		go modifyNotSafe(i)
	}
	wgMap.Wait()
	time2 := time.Now().UnixNano()
	fmt.Printf("map len=%d, time=%d ms\n", len(data), (time2-time1)/1000000)

	// 覆盖后再执行一次
	data = make(map[int]int)
	fmt.Printf("new map add num=%d\n", max)
	wgMap.Add(max)
	time3 := time.Now().UnixNano()
	for i := 0; i < max; i++ {
		go modifySafe(i)
	}
	wgMap.Wait()
	time4 := time.Now().UnixNano()
	fmt.Printf("new map len=%d, time=%d ms\n", len(data), (time4-time3)/1000000)
}

// 线程不安全的方法
func modifyNotSafe(i int) {
	data[i] = i
	wgMap.Done()
}

// 线程安全的方法，增加了互斥锁
func modifySafe(i int) {
	muMap.Lock()
	data[i] = i
	muMap.Unlock()
	wgMap.Done()
}
