-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290
-- LeetCode 77. 组合 — Lua 版（方案3）
local function combine(n, k) -- local function combine(元素个数, 下标 k)
	local res = {} -- 把 {} 写入 local res
	local path = {} -- 把 {} 写入 local path
	local function dfs(start) -- local function dfs(起点)
		if #path == k then -- 若 #当前路径 等于 下标 k then
			res[#res + 1] = { table.unpack(path) } -- 把 {table.unpack(当前路径)} 写入 res[#res + 1]
			return -- return
		end -- 终点
		for i = start, n - (k - #path) + 1 do -- 把 起点, 元素个数 减 (下标 k 减 #当前路径) 加 1 do 写入 for i
			path[#path + 1] = i -- 把 下标 i 写入 path[#path + 1]
			dfs(i + 1) -- dfs(下标 i 加 1)
			path[#path] = nil -- 把 nil 写入 path[#path]
		end -- 终点
	end -- 终点
	dfs(1) -- dfs(1)
	return res -- 返回 结果
end -- 终点
local got = combine(4, 2) -- 把 combine(4, 2) 写入 local got
assert(#got == 6) -- 断言校验
assert(table.concat(got[1], ",") == "1,2" and table.concat(got[6], ",") == "3,4") -- 打印输出
assert(#combine(1, 1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
