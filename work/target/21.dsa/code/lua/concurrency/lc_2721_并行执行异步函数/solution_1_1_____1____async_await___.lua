-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386399
-- LeetCode 2721. 并行执行异步函数 — Lua 版（方案1）
local function execute_all(functions) -- local function execute_all(functions)
	local out = {} -- 把 {} 写入 local out
	for i, v in ipairs(functions) do
		out[i] = v
	end -- 遍历取 值
	return out -- 返回 out
end -- 终点
assert(table.concat(execute_all({ 1, 2, 3 }), ",") == "1,2,3") -- 打印输出
assert(#execute_all({}) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
