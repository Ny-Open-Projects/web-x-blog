// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385760
package main // 引入依赖

import (
	"bytes" // 「bytes」
	"fmt"   // 「fmt」
	"os"    // 「os」
	"sync"  // 「sync」
)

// Foo 是 Python 参考 solution_1 的忠实翻译（用两个 channel 保证 first→second→third 顺序）。
type Foo struct { // 定义类型
	firstJobDone  chan struct{} // firstJobDone chan struct{}
	secondJobDone chan struct{} // secondJobDone chan struct{}
}

func NewFoo() *Foo { // 定义函数/方法 NewFoo
	return &Foo{ // 返回 按位与 Foo{
		firstJobDone:  make(chan struct{}),
		secondJobDone: make(chan struct{}),
	}
}

func (this *Foo) First(printFirst func()) { // 定义函数/方法 First
	printFirst()             // printFirst()
	close(this.firstJobDone) // close(this.firstJobDone)
}

func (this *Foo) Second(printSecond func()) { // 定义函数/方法 Second
	<-this.firstJobDone       // 小于 减 this.firstJobDone
	printSecond()             // printSecond()
	close(this.secondJobDone) // close(this.secondJobDone)
}

func (this *Foo) Third(printThird func()) { // 定义函数/方法 Third
	<-this.secondJobDone // 小于 减 this.secondJobDone
	printThird()         // printThird()
}

func main() { // 程序入口：跑内嵌自测用例
	var buf bytes.Buffer  // var buf bytes.Buffer
	f := NewFoo()         // 把 NewFoo() 写入 f :
	var wg sync.WaitGroup // var wg sync.WaitGroup
	wg.Add(3)             // wg.Add(3)
	go func() {           // 定义函数/方法 func
		defer wg.Done()                              // defer wg.Done()
		f.First(func() { buf.WriteString("first") }) // f.First(func() { buf.WriteString(「first」) })
	}() // }()
	go func() { // 定义函数/方法 func
		defer wg.Done()                                // defer wg.Done()
		f.Second(func() { buf.WriteString("second") }) // f.Second(func() { buf.WriteString(「second」) })
	}() // }()
	go func() { // 定义函数/方法 func
		defer wg.Done()                              // defer wg.Done()
		f.Third(func() { buf.WriteString("third") }) // f.Third(func() { buf.WriteString(「third」) })
	}() // }()
	wg.Wait()                               // wg.Wait()
	if buf.String() != "firstsecondthird" { // 若 buf.String() 不等于 「firstsecondthird」
		fmt.Println("FAIL order:", buf.String()) // 打印输出
		os.Exit(1)                               // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
