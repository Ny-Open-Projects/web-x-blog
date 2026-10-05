/**
 * 并发编程，数字递增的线程安全性问题
 */
package main

import (
	"sync"
	"time"
	"fmt"
	"sync/atomic"
)

var data1 int = 0
var data2 *int32
var wgInt sync.WaitGroup = sync.WaitGroup{}

func main() {
	t := int32(0)
	data2 = &t
	max := 100000
	wgInt.Add(max)
	fmt.Printf("data1 add num=%d\n", max)
	time1 := time.Now().UnixNano()
	for i := 0; i < max; i++ {
		go addData1()
	}
	wgInt.Wait()
	time2 := time.Now().UnixNano()
	fmt.Printf("data1=%d, time=%d ms\n", data1, (time2-time1)/1000000)

	wgInt.Add(max)
	fmt.Printf("data2 add num=%d\n", max)
	time3 := time.Now().UnixNano()
	for i := 0; i < max; i++ {
		go addData2()
	}
	wgInt.Wait()
	time4 := time.Now().UnixNano()
	fmt.Printf("data2=%d, time=%d ms\n", *data2, (time4-time3)/1000000)
}
// 简单的+1处理，线程不安全
func addData1() {
	data1++
	wgInt.Done()
}
// 原子性+1处理，线程安全
func addData2() {
	atomic.AddInt32(data2, 1)
	wgInt.Done()
}
