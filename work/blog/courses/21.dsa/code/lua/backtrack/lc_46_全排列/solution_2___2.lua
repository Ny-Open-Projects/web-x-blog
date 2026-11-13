-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133767953
-- LeetCode 46. 全排列 — Lua 版（方案2）
local function permute(nums) -- local function permute(数组)
	local res = {} -- 把 {} 写入 local res
	local n = #nums -- 把 #数组 写入 local n
	local used = {} -- 把 {} 写入 local used
	local path = {} -- 把 {} 写入 local path
	local function dfs() -- local function dfs()
		if #path == n then -- 若 #当前路径 等于 元素个数 then
			local cp = { table.unpack(path) } -- 把 {table.unpack(当前路径)} 写入 local cp
			res[#res + 1] = cp -- 把 cp 写入 res[#res + 1]
			return -- return
		end -- 终点
		for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
			if not used[i] then -- 若 not 已用标记[下标 i] then
				used[i] = true -- 把 true 写入 used[i]
				path[#path + 1] = nums[i] -- 把 数组[下标 i] 写入 path[#path + 1]
				dfs() -- dfs()
				path[#path] = nil -- 把 nil 写入 path[#path]
				used[i] = false -- 把 false 写入 used[i]
			end -- 终点
		end -- 终点
	end -- 终点
	dfs() -- dfs()
	return res -- 返回 结果
end -- 终点
local got = permute({ 1, 2, 3 }) -- 把 permute({1, 2, 3}) 写入 local got
assert(#got == 6) -- 断言校验
assert(table.concat(got[1], ",") == "1,2,3") -- 打印输出
assert(table.concat(got[2], ",") == "1,3,2") -- 打印输出
assert(table.concat(got[3], ",") == "2,1,3") -- 打印输出
assert(table.concat(got[6], ",") == "3,2,1") -- 打印输出
assert(#permute({ 0, 1 }) == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
