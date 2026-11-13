-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359
-- LeetCode 337. 打家劫舍III — Lua 版（方案1）
local function rob_tree(vals) -- local function rob_tree(vals)
	if #vals == 0 then
		return 0
	end -- 若 #vals 等于 0 then return 0 终点
	local N = "null" -- 把 「null」 写入 local N
	local function dfs(i) -- local function dfs(下标 i)
		if not vals[i] or vals[i] == N then
			return 0, 0
		end -- 若 not vals[下标 i] or vals[下标 i] 等于 N then return 0, 0 终点
		local li, le = dfs(2 * i) -- 把 dfs(2 乘 下标 i) 写入 local li, le
		local ri, re = dfs(2 * i + 1) -- 把 dfs(2 乘 下标 i 加 1) 写入 local ri, re
		local include = vals[i] + le + re -- 把 vals[下标 i] 加 le 加 re 写入 local include
		local exclude = math.max(li, le) + math.max(ri, re) -- 把 math.取较大值 li, le) 加 math.取较大值 ri, re) 写入 local exclude
		return include, exclude -- 返回 include, exclude
	end -- 终点
	local inc, exc = dfs(1) -- 把 dfs(1) 写入 local inc, exc
	return math.max(inc, exc) -- 返回 math.取较大值 inc, exc)
end -- 终点
assert(rob_tree({ 3, 2, 3, "null", 3, "null", 1 }) == 7) -- 断言校验
assert(rob_tree({ 3, 4, 5, 1, 3, "null", 1 }) == 9) -- 断言校验
assert(rob_tree({}) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
