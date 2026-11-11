# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489 LeetCode 133270489. 原型链原理 — R
# 版（方案3：get 查找 + instanceOf 判定） 定义函数 Proto（参数：name, parent 赋值为 NULL）
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
instance_of <- function(obj, prototype) {
    # 定义函数 instance_of（参数：obj, prototype）
    p <- obj  # 把 obj 存入 节点
    while (!is.null(p)) {
        # 循环，直到不满足「取反 is.null(节点」
        if (identical(p, prototype))
            return(TRUE)  # 若 identical(节点, prototype)) return(TRUE
        p <- p$parent  # 把 节点$parent 存入 节点
    }
    FALSE  # FALSE
}
object_proto <- Proto("Object.prototype")  # 把 Proto(「Object.prototype」) 存入 object_proto
set_prop(object_proto, "a", "aaa")  # set_prop(object_proto, 「数组」, 「数组」)
function_proto <- Proto("Function.prototype", object_proto)
set_prop(function_proto, "b", "bbb")  # set_prop(function_proto, 「b」, 「b」)
obj <- Proto("obj", object_proto)  # 把 Proto(「obj」, object_proto) 存入 obj
func <- Proto("func", function_proto)  # 把 Proto(「func」, function_proto) 存入 func
stopifnot(identical(get_prop(obj, "a"), "aaa"))  # 断言校验
stopifnot(is.null(get_prop(obj, "b")))  # 断言校验
stopifnot(identical(get_prop(func, "a"), "aaa"))  # 断言校验
stopifnot(identical(get_prop(func, "b"), "bbb"))  # 断言校验
stopifnot(instance_of(func, object_proto))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
