-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134134491
-- LeetCode 47. 全排列II — Lua 版（方案2）
local function permute_unique(nums) -- local function permute_unique(数组)
	local arr = { table.unpack(nums) } -- 把 {table.unpack(数组)} 写入 local arr
	table.sort(arr) -- 排序
	local res = {} -- 把 {} 写入 local res
	local n = #arr -- 把 #数组 写入 local n
	local used = {} -- 把 {} 写入 local used
	local path = {} -- 把 {} 写入 local path
	local function dfs() -- local function dfs()
		if #path == n then -- 若 #当前路径 等于 元素个数 then
			res[#res + 1] = { table.unpack(path) } -- 把 {table.unpack(当前路径)} 写入 res[#res + 1]
			return -- return
		end -- 终点
		for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
			if not used[i] then -- 若 not 已用标记[下标 i] then
				if i == 1 or arr[i] ~= arr[i - 1] or used[i - 1] then
					used[i] = true -- 把 true 写入 used[i]
					path[#path + 1] = arr[i] -- 把 数组[下标 i] 写入 path[#path + 1]
					dfs() -- dfs()
					path[#path] = nil -- 把 nil 写入 path[#path]
					used[i] = false -- 把 false 写入 used[i]
				end -- 终点
			end -- 终点
		end -- 终点
	end -- 终点
	dfs() -- dfs()
	return res -- 返回 结果
end -- 终点
local got = permute_unique({ 1, 1, 2 }) -- 把 permute_unique({1, 1, 2}) 写入 local got
assert(#got == 3) -- 断言校验
assert(
	table.concat(got[1], ",") == "1,1,2"
		and table.concat(got[2], ",") == "1,2,1"
		and table.concat(got[3], ",") == "2,1,1"
) -- 打印输出
assert(#permute_unique({ 1, 2, 3 }) == 6) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
