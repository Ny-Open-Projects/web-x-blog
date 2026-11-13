-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135749595
-- LeetCode 295. 数据流的中位数 — Lua 版（方案1）
local MedianFinder = {} -- 把 {} 写入 local MedianFinder
MedianFinder.__index = MedianFinder -- 把 MedianFinder 写入 MedianFinder.__index
function MedianFinder.new() -- function MedianFinder.new()
	return setmetatable({ maxh = {}, minh = {} }, MedianFinder) -- 返回 setmetatable({maxh 赋值为 {}, minh 赋值为 {}}, MedianFinder)
end -- 终点
local function hpush(h, v, less) -- local function hpush(h, 值, less)
	h[#h + 1] = v -- 把 值 写入 h[#h + 1]
	local i = #h -- 把 #h 写入 local i
	while i > 1 do -- while 下标 i 超过 1 do
		local p = i // 2 -- 把 下标 i 写入 local p
		if not less(h[i], h[p]) then
			break
		end -- 若 not less(h[下标 i], h[节点]) then break 终点
		h[i], h[p] = h[p], h[i] -- 把 h[节点], h[下标 i] 写入 h[i], h[p]
		i = p -- 把 节点 存入 下标 i
	end -- 终点
end -- 终点
local function hpop(h, less) -- local function hpop(h, less)
	local top = h[1] -- 把 h[1] 写入 local top
	h[1] = h[#h] -- 把 h[#h] 写入 h[1]
	h[#h] = nil -- 把 nil 写入 h[#h]
	local i, n = 1, #h -- 把 1, #h 写入 local i, n
	while true do -- while true do
		local l, r, m = 2 * i, 2 * i + 1, i -- 把 2 乘 下标 i, 2 乘 下标 i 加 1, 下标 i 写入 local l, r, m
		if l <= n and less(h[l], h[m]) then
			m = l
		end -- 若 左指针 不超过 元素个数 and less(h[左指针], h[映射表]) then 映射表 赋值为 左指针 终点
		if r <= n and less(h[r], h[m]) then
			m = r
		end -- 若 右指针 不超过 元素个数 and less(h[右指针], h[映射表]) then 映射表 赋值为 右指针 终点
		if m == i then
			break
		end -- 若 映射表 等于 下标 i then break 终点
		h[i], h[m] = h[m], h[i] -- 把 h[映射表], h[下标 i] 写入 h[i], h[m]
		i = m -- 把 映射表 存入 下标 i
	end -- 终点
	return top -- 返回 top
end -- 终点
function MedianFinder:add_num(num) -- function MedianFinder:add_num(num)
	if #self.maxh == 0 or num <= self.maxh[1] then -- 若 #self.maxh 等于 0 or num 不超过 self.maxh[1] then
		hpush(self.maxh, num, function(a, b)
			return a > b
		end) -- hpush(self.maxh, num, function(数组, b) return 数组 超过 b 终点)
	else -- 否则
		hpush(self.minh, num, function(a, b)
			return a < b
		end) -- hpush(self.minh, num, function(数组, b) return 数组 小于 b 终点)
	end -- 终点
	if #self.maxh > #self.minh + 1 then -- 若 #self.maxh 超过 #self.minh 加 1 then
		hpush(
			self.minh,
			hpop(self.maxh, function(a, b)
				return a > b
			end),
			function(a, b)
				return a < b
			end
		)
	elseif #self.minh > #self.maxh then -- elseif #self.minh 超过 #self.maxh then
		hpush(
			self.maxh,
			hpop(self.minh, function(a, b)
				return a < b
			end),
			function(a, b)
				return a > b
			end
		)
	end -- 终点
end -- 终点
function MedianFinder:find_median() -- function MedianFinder:find_median()
	if #self.maxh == #self.minh then -- 若 #self.maxh 等于 #self.minh then
		return (self.maxh[1] + self.minh[1]) / 2 -- 返回 (self.maxh[1] 加 self.minh[1]) 除以 2
	end -- 终点
	return self.maxh[1] -- 返回 self.maxh[1]
end -- 终点
local mf = MedianFinder.new() -- 把 MedianFinder.new() 写入 local mf
for _, x in ipairs({ 1, 2, 3, 4, 5 }) do
	mf:add_num(x)
end -- 遍历取 x
assert(mf:find_median() == 3) -- 断言校验
local mf2 = MedianFinder.new() -- 把 MedianFinder.new() 写入 local mf2
mf2:add_num(1)
mf2:add_num(2) -- mf2:add_num(1); mf2:add_num(2)
assert(mf2:find_median() == 1.5) -- 断言校验
mf2:add_num(3) -- mf2:add_num(3)
assert(mf2:find_median() == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
