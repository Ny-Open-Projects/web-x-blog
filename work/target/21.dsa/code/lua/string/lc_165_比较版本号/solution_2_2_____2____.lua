-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135004886
-- LeetCode 165. 比较版本号 — Lua 版（方案2）
local function compare_version(v1, v2) -- local function compare_version(v1, v2)
	local p1, p2 = {}, {} -- 把 {}, {} 写入 local p1, p2
	v1:gsub("([^.]+)", function(x)
		p1[#p1 + 1] = tonumber(x)
	end)
	v2:gsub("([^.]+)", function(x)
		p2[#p2 + 1] = tonumber(x)
	end)
	local n = math.max(#p1, #p2) -- 把 math.取较大值 #p1, #p2) 写入 local n
	for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
		local a = p1[i] or 0 -- 把 p1[下标 i] or 0 写入 local a
		local b = p2[i] or 0 -- 把 p2[下标 i] or 0 写入 local b
		if a < b then
			return -1
		end -- 若 数组 小于 b then return 减 1 终点
		if a > b then
			return 1
		end -- 若 数组 超过 b then return 1 终点
	end -- 终点
	return 0 -- 返回 0
end -- 终点
assert(compare_version("1.01", "1.001") == 0) -- 断言校验
assert(compare_version("1.0", "1.0.0") == 0) -- 断言校验
assert(compare_version("0.1", "1.1") == -1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
