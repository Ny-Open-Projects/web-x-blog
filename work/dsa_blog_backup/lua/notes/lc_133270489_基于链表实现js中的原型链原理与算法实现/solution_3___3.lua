-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
-- LeetCode 133270489. 原型链原理 — Lua 版（方案3：get 查找 + instanceOf 判定）
local Proto = {} -- 把 {} 写入 local Proto
Proto.__index = Proto -- 把 Proto 写入 Proto.__index
function Proto.new(name, parent) -- function Proto.new(name, parent)
	return setmetatable({ name = name, props = {}, parent = parent }, Proto)
end -- 终点
function Proto:set(key, value) -- function Proto:set(key, value)
	self.props[key] = value -- 把 value 写入 self.props[key]
end -- 终点
function Proto:get(key) -- function Proto:get(key)
	local cur = self -- 把 self 写入 local cur
	while cur ~= nil do -- 把 nil do 写入 while cur ~
		if cur.props[key] ~= nil then
			return cur.props[key]
		end -- 若 当前值.props[key] ~ 赋值为 nil then return 当前值.props[key] 终点
		cur = cur.parent -- 把 当前值.parent 存入 当前值
	end -- 终点
	return nil -- 返回 nil
end -- 终点

local function instance_of(obj, prototype) -- local function instance_of(obj, prototype)
	local p = obj -- 把 obj 写入 local p
	while p ~= nil do -- 把 nil do 写入 while p ~
		if p == prototype then
			return true
		end -- 若 节点 等于 prototype then return true 终点
		p = p.parent -- 把 节点.parent 存入 节点
	end -- 终点
	return false -- 返回 false
end -- 终点

local object_proto = Proto.new("Object.prototype") -- 把 Proto.new(「Object.prototype」) 写入 local object_proto
object_proto:set("a", "aaa") -- object_proto:set(「数组」, 「数组」)
local function_proto = Proto.new("Function.prototype", object_proto)
function_proto:set("b", "bbb") -- function_proto:set(「b」, 「b」)
local obj = Proto.new("obj", object_proto) -- 把 Proto.new(「obj」, object_proto) 写入 local obj
local func = Proto.new("func", function_proto) -- 把 Proto.new(「func」, function_proto) 写入 local func

assert(obj:get("a") == "aaa", "case 0 failed") -- 断言校验
assert(obj:get("b") == nil, "case 1 failed") -- 断言校验
assert(func:get("a") == "aaa", "case 2 failed") -- 断言校验
assert(func:get("b") == "bbb", "case 3 failed") -- 断言校验
assert(instance_of(func, object_proto) == true, "case 4 failed") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
