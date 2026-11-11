-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307
-- LeetCode 39. 组合总和 — Lua 版（方案1）
local function combination_sum(candidates, target) -- local function combination_sum(候选数组, 目标值)
	local res = {} -- 把 {} 写入 local res
	local path = {} -- 把 {} 写入 local path
	local function dfs(start, remaining) -- local function dfs(起点, remaining)
		if remaining == 0 then -- 若 remaining 等于 0 then
			res[#res + 1] = { table.unpack(path) } -- 把 {table.unpack(当前路径)} 写入 res[#res + 1]
			return -- return
		end -- 终点
		if remaining < 0 then
			return
		end -- 若 remaining 小于 0 then return 终点
		for i = start, #candidates do -- 把 起点, #候选数组 do 写入 for i
			path[#path + 1] = candidates[i] -- 把 候选数组[下标 i] 写入 path[#path + 1]
			dfs(i, remaining - candidates[i]) -- dfs(下标 i, remaining 减 候选数组[下标 i])
			path[#path] = nil -- 把 nil 写入 path[#path]
		end -- 终点
	end -- 终点
	dfs(1, target) -- dfs(1, 目标值)
	return res -- 返回 结果
end -- 终点
local got = combination_sum({ 2, 3, 6, 7 }, 7) -- 把 combination_sum({2, 3, 6, 7}, 7) 写入 local got
assert(#got == 2) -- 断言校验
assert(table.concat(got[1], ",") == "2,2,3" and table.concat(got[2], ",") == "7") -- 打印输出
local got2 = combination_sum({ 2, 3, 5 }, 8) -- 把 combination_sum({2, 3, 5}, 8) 写入 local got2
assert(#got2 == 3 and table.concat(got2[3], ",") == "3,5") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
