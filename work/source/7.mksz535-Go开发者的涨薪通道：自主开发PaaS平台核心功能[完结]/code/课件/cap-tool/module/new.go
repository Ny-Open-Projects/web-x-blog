// Package new generates micro service templates
package new

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
	"path"
	"path/filepath"
	"strings"
	"text/template"
	"time"

	tmpl "github.com/Cap1573/cap-tool/tpl"
	"github.com/xlab/treeprint"
)

func protoComments() []string {
	return []string{
		"======================说明===========================",
		"该工具为Cap老师定制工具,旨在提高同学们开发效率",
		"工具主要功能如下：",
		"1、快速创建项目目录结构。",
		"2、添加慕课网权限验证。",
		"注意：授权验证只在创建模版的时候验证，不影响生产环境使用",
		"\n",
		"======================操作============================",
		"接下来直接使用课程代码中的 make proto 来自动生成基于 proto 的相关文件",
		"具体操作如下：",
		"1、make proto ( window 下要修改 docker 命令)",
		"2、执行 go mod tidy",
		"3、go run main.go 检查是否能够启动成功",
		"4、查看注册中心服务是否存在（地址默认：127.0.0.1:8500）",
		"注意：你也可以在本机安装 proto ，protoc-gen-go，protoc-gen-micro 运行 protoc 进行生成。",
		"\n",
		"===================Cap 更多好课========================",
		"更多 Cap 老师精彩课程,点击链接访问购买：http://www.imooc.com/t/6512963",
	}
}

type config struct {
	// 服务名称
	Alias string
	// 目录地址
	Dir string
	// 在API模式下默认的后端名称
	ApiDefaultServerName  string
	// 文件地址
	Files []file
	// 说明
	Comments []string
}

type file struct {
	//路径
	Path string
	//模板
	Tmpl string
}

func write(c config, file, tmpl string) error {
	fn := template.FuncMap{
		"title": func(s string) string {
			return strings.ReplaceAll(strings.Title(s), "-", "")
		},
		"dehyphen": func(s string) string {
			return strings.ReplaceAll(s, "-", "")
		},
		"lower": func(s string) string {
			return strings.ToLower(s)
		},
	}

	f, err := os.Create(file)
	if err != nil {
		return err
	}
	defer f.Close()

	t, err := template.New("f").Funcs(fn).Parse(tmpl)
	if err != nil {
		return err
	}

	return t.Execute(f, c)
}

func create(c config) error {
	// check if dir exists
	if _, err := os.Stat(c.Dir); !os.IsNotExist(err) {
		fmt.Printf("Cap 老师提醒您 %s 目录已存在，无法创建！请删除后重新创建", c.Dir)
		return fmt.Errorf("%s already exists", c.Dir)
	}

	fmt.Printf("创建初始化项目 %s\n\n", c.Alias)

	t := treeprint.New()

	// write the files
	for _, file := range c.Files {
		f := filepath.Join(c.Dir, file.Path)
		dir := filepath.Dir(f)

		if _, err := os.Stat(dir); os.IsNotExist(err) {
			if err := os.MkdirAll(dir, 0755); err != nil {
				fmt.Println(err)
				return err
			}
		}

		addFileToTree(t, file.Path)
		if err := write(c, f, file.Tmpl); err != nil {
			fmt.Println(err)
			return err
		}
	}

	// print tree
	fmt.Println(t.String())

	for _, comment := range c.Comments {
		fmt.Println(comment)
	}

	// just wait
	<-time.After(time.Millisecond * 250)
	fmt.Println("\n************恭喜！项目初始化成功！************\n")
	return nil
}

func addFileToTree(root treeprint.Tree, file string) {
	split := strings.Split(file, "/")
	curr := root
	for i := 0; i < len(split)-1; i++ {
		n := curr.FindByValue(split[i])
		if n != nil {
			curr = n
		} else {
			curr = curr.AddBranch(split[i])
		}
	}
	if curr.FindByValue(split[len(split)-1]) == nil {
		curr.AddNode(split[len(split)-1])
	}
}

func NewServiceProject(ctx *cobra.Command, args []string) error {

	for _, serviceArg := range args {
		serviceSlice := strings.Split(serviceArg, "/")
		serviceName := serviceSlice[len(serviceSlice)-1]
		if len(serviceName) == 0 {
			fmt.Println("服务名称格式错误")
			return nil
		}

		if path.IsAbs(serviceArg) {
			fmt.Println("require relative path as service will be installed in GOPATH")
			return nil
		}

		c := config{
			Alias:    serviceName,
			Dir:      serviceArg,
			Comments: protoComments(),
			Files: []file{
				{"main.go", tmpl.MainSRV},
				//{"generate.go", tmpl.GenerateFile},
				//{"plugin.go", tmpl.Plugin},
				{"handler/" + serviceName + "Handler.go", tmpl.HandlerSRV},
				{"plugin/hystrix/hystrix.go", tmpl.Hystrix},
				{"domain/model/" + serviceName + ".go", tmpl.DomainModel},
				{"domain/repository/" + serviceName + "_repository.go", tmpl.DomainRepository},
				{"domain/service/" + serviceName + "_data_service.go", tmpl.DomainService},
				{"proto/" + serviceName + "/" + serviceName + ".proto", tmpl.ProtoSRV},
				{"Dockerfile", tmpl.DockerSRV},
				{"filebeat.yml", tmpl.Filebeat},
				{"Makefile", tmpl.Makefile},
				{"README.md", tmpl.Readme},
				{".gitignore", tmpl.GitIgnore},
				{"go.mod", tmpl.Module},
			},
		}
		// create the files

		return create(c)


	}
	return nil
}

func NewApiProject(ctx *cobra.Command, args []string) error {

	for _, serviceArg := range args {
		serviceSlice := strings.Split(serviceArg, "/")
		serviceName := serviceSlice[len(serviceSlice)-1]
		if len(serviceName) == 0 {
			fmt.Println("名称不能为空")
			return nil
		}

		if path.IsAbs(serviceArg) {
			fmt.Println("require relative path as service will be installed in GOPATH")
			return nil
		}

		apiDefaultServerName := "XXX"
		//判断在API的状态下默认的服务名称
		if strings.Contains(serviceName,"Api") {
			//替换指定Api的字符为空
			apiDefaultServerName = strings.Replace(serviceName,"Api","",1)
		}


		c := config{
			Alias:    serviceName,
			Dir:      serviceArg,
			ApiDefaultServerName :apiDefaultServerName,
			Comments: protoComments(),
			Files: []file{
				{"main.go", tmpl.MainAPI},
				//{"generate.go", tmpl.GenerateFile},
				//{"plugin.go", tmpl.Plugin},
				{"handler/" + serviceName + "Handler.go", tmpl.HandlerAPI},
				{"plugin/hystrix/hystrix.go", tmpl.Hystrix},
				{"proto/" + serviceName + "/" + serviceName + ".proto", tmpl.ProtoAPI},
				{"Dockerfile", tmpl.DockerSRV},
				{"filebeat.yml", tmpl.Filebeat},
				{"Makefile", tmpl.Makefile},
				{"README.md", tmpl.ReadmeApi},
				{".gitignore", tmpl.GitIgnore},
				{"go.mod", tmpl.ApiModule},
			},
		}
		// create the files

		return create(c)


	}
	return nil
}