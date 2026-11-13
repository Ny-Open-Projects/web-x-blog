-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
-- LeetCode 110240695. 分治策略之 greatest slice — Lua 版（方案C：分治 best/prefix/suffix/total）
local function max_sub_array_dc(arr) -- local function max_sub_array_dc(数组)
	local n = #arr -- 把 #数组 写入 local n
	if n == 0 then
		return 0
	end -- 若 元素个数 等于 0 then return 0 终点

	local helper -- local helper
	helper = function(lo, hi) -- 把 function(左边界, 右边界) 存入 helper
		if hi - lo == 1 then -- 若 右边界 减 左边界 等于 1 then
			local v = arr[lo + 1] -- lo 为 0 基
			return v, v, v, v -- 返回 值, 值, 值, 值
		end -- 终点
		local mi = math.floor((lo + hi) / 2) -- 把 math.floor((左边界 加 右边界) 除以 2) 写入 local mi
		local l_best, l_pre, l_suf, l_sum = helper(lo, mi) -- 把 helper(左边界, mi) 写入 local l_best, l_pre, l_suf, l_sum
		local r_best, r_pre, r_suf, r_sum = helper(mi, hi) -- 把 helper(mi, 右边界) 写入 local r_best, r_pre, r_suf, r_sum
		local crossing = l_suf + r_pre -- 把 l_suf 加 r_pre 写入 local crossing
		local best = math.max(l_best, r_best, crossing) -- 把 math.取较大值 l_best, r_best, crossing) 写入 local best
		local prefix = math.max(l_pre, l_sum + r_pre) -- 把 math.取较大值 l_pre, l_sum 加 r_pre) 写入 local prefix
		local suffix = math.max(r_suf, r_sum + l_suf) -- 把 math.取较大值 r_suf, r_sum 加 l_suf) 写入 local suffix
		local total = l_sum + r_sum -- 把 l_sum 加 r_sum 写入 local total
		return best, prefix, suffix, total -- 返回 当前最优, prefix, suffix, 总和
	end -- 终点

	return helper(0, n) -- 返回 helper(0, 元素个数)
end -- 终点

assert(max_sub_array_dc({ -2, 1, -3, 4, -1, 2, 1 }) == 6, "ms1") -- 断言校验
assert(max_sub_array_dc({ 1, 2, 3 }) == 6, "ms2") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
