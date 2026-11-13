# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489 LeetCode 133270489. 原型链原理 — R
# 版（方案2：get 沿原型链查找属性） 定义函数 Proto（参数：name, parent 赋值为 NULL）
Proto <- function(name, parent = NULL) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$name <- name  # 把 name 存入 e$name
    e$props <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e$props
    e$parent <- parent  # 把 parent 存入 e$parent
    e
}
set_prop <- function(p, key, value) p$props[[key]] <- value  # 定义函数 set_prop（参数：节点, key, value）
get_prop <- function(p, key) {
    # 定义函数 get_prop（参数：节点, key）
    cur <- p  # 把 节点 存入 当前值
    while (!is.null(cur)) {
        # 循环，直到不满足「取反 is.null(当前值」
        if (!is.null(cur$props[[key]]))
            return(cur$props[[key]])  # 若 取反 is.null(当前值$props[[key]])) return(当前值$props[[key]]
        cur <- cur$parent  # 把 当前值$parent 存入 当前值
    }
    NULL  # NULL
}
object_proto <- Proto("Object.prototype")  # 把 Proto(「Object.prototype」) 存入 object_proto
set_prop(object_proto, "x", "x")  # set_prop(object_proto, 「x」, 「x」)
function_proto <- Proto("Function.prototype", object_proto)
set_prop(function_proto, "y", "y")  # set_prop(function_proto, 「y」, 「y」)
array_proto <- Proto("Array.prototype", object_proto)  # 把 Proto(「Array.prototype」, object_proto) 存入 array_proto
set_prop(array_proto, "z", "z")  # set_prop(array_proto, 「z」, 「z」)
obj <- Proto("obj", object_proto)  # 把 Proto(「obj」, object_proto) 存入 obj
func <- Proto("func", function_proto)  # 把 Proto(「func」, function_proto) 存入 func
arr <- Proto("arr", array_proto)  # 把 Proto(「数组」, array_proto) 存入 数组
stopifnot(identical(get_prop(obj, "x"), "x"))  # 断言校验
stopifnot(identical(get_prop(func, "y"), "y"))  # 断言校验
stopifnot(identical(get_prop(arr, "z"), "z"))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
