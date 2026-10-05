/**
 * 线程是否安全的测试
 * slice切片在并发请求时不会出现异常，但也是线程不安全的，数据更新会有问题
 * go test -v
 */
package main

import (
	"fmt"
	"sync"
	"testing"

	"github.com/kataras/iris/httptest"
)

func TestMVC(t *testing.T) {
	e := httptest.New(t, newApp())

	var wg sync.WaitGroup
	e.GET("/").Expect().Status(httptest.StatusOK).
		Body().Equal("当前总共参与抽奖的用户数: 0\n")

	// 启动100个协程并发来执行用户导入操作
	// 如果是线程安全的时候，预期倒入成功100个用户
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			e.POST("/import").WithFormField("users", fmt.Sprintf("test_u%d", i)).Expect().Status(httptest.StatusOK)
		}(i)
	}

	wg.Wait()

	e.GET("/").Expect().Status(httptest.StatusOK).
		Body().Equal("当前总共参与抽奖的用户数: 100\n")
	e.GET("/lucky").Expect().Status(httptest.StatusOK)
	e.GET("/").Expect().Status(httptest.StatusOK).
		Body().Equal("当前总共参与抽奖的用户数: 99\n")
}
