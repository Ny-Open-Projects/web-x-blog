-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
-- LeetCode 110240695. 分治策略之 greatest slice — Lua 版（方案B：增量扫描）
local function max_sub_array_ic(arr) -- local function max_sub_array_ic(数组)
	local n = #arr -- 把 #数组 写入 local n
	if n == 0 then
		return 0
	end -- 若 元素个数 等于 0 then return 0 终点
	local gs = arr[1] -- 把 数组[1] 写入 local gs
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		local s = 0 -- 把 0 写入 local s
		for j = i, n do -- 把 下标 i, 元素个数 do 写入 for j
			s = s + arr[j] -- 把 字符串 加 数组[下标 j] 存入 字符串
			if gs < s then
				gs = s
			end -- 若 gs 小于 字符串 then gs 赋值为 字符串 终点
		end -- 终点
	end -- 终点
	return gs -- 返回 gs
end -- 终点

assert(max_sub_array_ic({ -2, 1, -3, 4, -1, 2, 1 }) == 6, "ms1") -- 断言校验
assert(max_sub_array_ic({ -1, -2, -3 }) == -1, "ms2") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
