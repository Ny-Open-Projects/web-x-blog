# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489 LeetCode 133270489. 原型链原理 — R
# 版（方案1：instanceOf 沿原型链判定） 节点用 environment 引用语义 定义函数 Proto（参数：name, parent 赋值为
# NULL）
Proto <- function(name, parent = NULL) {
    e <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e
    e$name <- name  # 把 name 存入 e$name
    e$props <- new.env(parent = emptyenv())  # 把 new.env(parent 赋值为 emptyenv()) 存入 e$props
    e$parent <- parent  # 把 parent 存入 e$parent
    e
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
function_proto <- Proto("Function.prototype", object_proto)
array_proto <- Proto("Array.prototype", object_proto)  # 把 Proto(「Array.prototype」, object_proto) 存入 array_proto
obj <- Proto("obj", object_proto)  # 把 Proto(「obj」, object_proto) 存入 obj
func <- Proto("func", function_proto)  # 把 Proto(「func」, function_proto) 存入 func
arr <- Proto("arr", array_proto)  # 把 Proto(「数组」, array_proto) 存入 数组
stopifnot(instance_of(obj, object_proto))  # 断言校验
stopifnot(instance_of(func, function_proto))  # 断言校验
stopifnot(instance_of(func, object_proto))  # 断言校验
stopifnot(instance_of(arr, array_proto))  # 断言校验
stopifnot(instance_of(arr, object_proto))  # 断言校验
cat("PASS\n")  # 全部用例通过，输出 PASS
