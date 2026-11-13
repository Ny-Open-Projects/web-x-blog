-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133471440
-- LeetCode 215. 数组中的第K个最大元素 — Lua 版（方案11）
local function find_kth_largest(nums, k) -- local function find_kth_largest(数组, 下标 k)
	-- 简易最大堆
	local h = {} -- 把 {} 写入 local h
	local function up(i) -- local function up(下标 i)
		while i > 1 and h[i] > h[i // 2] do -- while 下标 i 超过 1 and h[下标 i] 超过 h[下标 i
			h[i], h[i // 2] = h[i // 2], h[i] -- h[下标 i], h[下标 i
			i = i // 2 -- 把 下标 i 存入 下标 i
		end -- 终点
	end -- 终点
	local function down(i) -- local function down(下标 i)
		local n = #h -- 把 #h 写入 local n
		while true do -- while true do
			local l, r, m = 2 * i, 2 * i + 1, i -- 把 2 乘 下标 i, 2 乘 下标 i 加 1, 下标 i 写入 local l, r, m
			if l <= n and h[l] > h[m] then
				m = l
			end -- 若 左指针 不超过 元素个数 and h[左指针] 超过 h[映射表] then 映射表 赋值为 左指针 终点
			if r <= n and h[r] > h[m] then
				m = r
			end -- 若 右指针 不超过 元素个数 and h[右指针] 超过 h[映射表] then 映射表 赋值为 右指针 终点
			if m == i then
				break
			end -- 若 映射表 等于 下标 i then break 终点
			h[i], h[m] = h[m], h[i] -- 把 h[映射表], h[下标 i] 写入 h[i], h[m]
			i = m -- 把 映射表 存入 下标 i
		end -- 终点
	end -- 终点
	for _, v in ipairs(nums) do
		h[#h + 1] = v
		up(#h)
	end -- 遍历取 值
	for _ = 1, k - 1 do -- 让 _ 从 1 走到 下标 k（Lua 1 基）
		h[1] = h[#h] -- 把 h[#h] 写入 h[1]
		h[#h] = nil -- 把 nil 写入 h[#h]
		if #h > 0 then
			down(1)
		end -- 若 #h 超过 0 then down(1) 终点
	end -- 终点
	return h[1] -- 返回 h[1]
end -- 终点
assert(find_kth_largest({ 3, 2, 1, 5, 6, 4 }, 2) == 5) -- 断言校验
assert(find_kth_largest({ 3, 2, 3, 1, 2, 4, 5, 5, 6 }, 4) == 4) -- 断言校验
assert(find_kth_largest({ 1 }, 1) == 1) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
