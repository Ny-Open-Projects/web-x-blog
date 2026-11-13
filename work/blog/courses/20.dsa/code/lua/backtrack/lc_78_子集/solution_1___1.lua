-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616
-- LeetCode 78. 子集 — Lua 版（方案1）
local function subsets(nums) -- local function subsets(数组)
	local res = {} -- 把 {} 写入 local res
	local n = #nums -- 把 #数组 写入 local n
	local path = {} -- 把 {} 写入 local path
	local function dfs(start) -- local function dfs(起点)
		res[#res + 1] = { table.unpack(path) } -- 把 {table.unpack(当前路径)} 写入 res[#res + 1]
		for i = start, n do -- 把 起点, 元素个数 do 写入 for i
			path[#path + 1] = nums[i] -- 把 数组[下标 i] 写入 path[#path + 1]
			dfs(i + 1) -- dfs(下标 i 加 1)
			path[#path] = nil -- 把 nil 写入 path[#path]
		end -- 终点
	end -- 终点
	dfs(1) -- dfs(1)
	return res -- 返回 结果
end -- 终点
assert(#subsets({ 1, 2, 3 }) == 8) -- 断言校验
assert(#subsets({ 0 }) == 2) -- 断言校验
local s = subsets({ 1, 2, 3 }) -- 把 subsets({1, 2, 3}) 写入 local s
local found = false -- 把 false 写入 local found
for _, sub in ipairs(s) do -- 遍历取 sub
	if #sub == 3 and table.concat(sub, ",") == "1,2,3" then
		found = true
	end
end -- 终点
assert(found) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
