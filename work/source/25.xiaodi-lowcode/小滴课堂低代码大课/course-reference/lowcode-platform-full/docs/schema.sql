-- ============================================================
-- 低代码平台数据库初始化脚本(MySQL 8+,字符集 utf8mb4)
-- 用法:mysql -uroot -p xdclass-lowcode < docs/schema.sql
-- 说明:5 张表 DDL + 少量示例数据(组件/问卷/资源各几条)。
--       开发期由 TypeORM synchronize 自动建表,本脚本用于
--       快速获得带示例数据的完整环境。
-- 表: user(用户) / page(页面,components 串=渲染顺序)
--      component(组件,type+options JSON) / component_data(问卷答案)
--      resources(OSS 资源索引)
-- ============================================================

/*
 Navicat Premium Data Transfer

 Source Server         : xdclass-lowcode
 Source Server Type    : MySQL
 Source Server Version : 80032
 Source Host           : localhost:3306
 Source Schema         : xdclass-lowcode

 Target Server Type    : MySQL
 Target Server Version : 80032
 File Encoding         : 65001

 Date: 17/11/2023 14:49:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for component
-- ----------------------------
DROP TABLE IF EXISTS `component`;
CREATE TABLE `component` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `page_id` int NOT NULL,
  `account_id` int NOT NULL,
  `options` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of component
-- ----------------------------
BEGIN;
INSERT INTO `component` VALUES (7, 'swiper', 1, 1, '{\"images\":[{\"id\":\"\",\"url\":\"https://lowcode.16web.net/upload_files/QD-1700118567343.png\",\"fit\":\"cover\",\"height\":200,\"handleClicked\":\"open-url\",\"name\":\"图片名称\",\"link\":\"https://xdclass.net\"},{\"id\":\"01HFBFCV150Q8D7758CE9EXF2Y\",\"url\":\"https://lowcode.16web.net/upload_files/JD-1700118572012.png\",\"fit\":\"cover\",\"height\":200,\"handleClicked\":\"open-url\",\"name\":\"图片名称\",\"link\":\"https://xdclass.net\"},{\"id\":\"01HFBFCW5S7YXQR0VQFW3ZSR5J\",\"url\":\"https://lowcode.16web.net/upload_files/HD-1700118576423.png\",\"fit\":\"cover\",\"height\":200,\"handleClicked\":\"open-url\",\"name\":\"图片名称\",\"link\":\"https://xdclass.net\"}]}');
INSERT INTO `component` VALUES (8, 'list', 1, 1, '{\"items\":[{\"id\":\"\",\"title\":\"标题\",\"description\":\"描述\",\"titleLink\":\"https://xdclass.net\",\"avatar\":\"https://lowcode.16web.net/upload_files/WechatIMG723-1700118611527.jpg\"}]}');
INSERT INTO `component` VALUES (9, 'list', 1, 1, '{\"items\":[{\"id\":\"\",\"title\":\"标题\",\"description\":\"描述\",\"titleLink\":\"https://xdclass.net\",\"avatar\":\"https://lowcode.16web.net/upload_files/WechatIMG724-1700118642835.jpg\"}]}');
INSERT INTO `component` VALUES (10, 'list', 1, 1, '{\"items\":[{\"id\":\"\",\"title\":\"标题\",\"description\":\"描述\",\"titleLink\":\"https://xdclass.net\",\"avatar\":\"https://lowcode.16web.net/upload_files/WechatIMG725-1700118600207.jpg\"}]}');
INSERT INTO `component` VALUES (11, 'list', 1, 1, '{\"items\":[{\"id\":\"\",\"title\":\"标题\",\"description\":\"描述\",\"titleLink\":\"https://xdclass.net\",\"avatar\":\"https://lowcode.16web.net/upload_files/WechatIMG726-1700118605600.jpg\"}]}');
INSERT INTO `component` VALUES (12, 'video', 1, 1, '{\"src\":\"https://lowcode.16web.net/upload_files/6-1-1700118663282.mp4\"}');
INSERT INTO `component` VALUES (13, 'input', 1, 1, '{\"title\":\"姓名\"}');
INSERT INTO `component` VALUES (14, 'textArea', 1, 1, '{\"title\":\"简介\"}');
INSERT INTO `component` VALUES (15, 'radio', 1, 1, '{\"options\":[{\"id\":\"\",\"value\":\"男\"},{\"id\":\"01HFBG2NAXXNYGNEG12K8R3KST\",\"value\":\"女\"}],\"title\":\"性别\"}');
INSERT INTO `component` VALUES (16, 'checkbox', 1, 1, '{\"options\":[{\"id\":\"\",\"value\":\"洗脚\"},{\"id\":\"01HFBG1245W7BP5NNWFTHBCRPC\",\"value\":\"按摩\"},{\"id\":\"01HFBG12W54CZXH1JN9HZJ843F\",\"value\":\"喝酒\"}],\"title\":\"爱好\"}');
COMMIT;

-- ----------------------------
-- Table structure for component_data
-- ----------------------------
DROP TABLE IF EXISTS `component_data`;
CREATE TABLE `component_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `page_id` int NOT NULL,
  `user` varchar(255) NOT NULL,
  `props` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of component_data
-- ----------------------------
BEGIN;
INSERT INTO `component_data` VALUES (1, 1, '522c1cdf4d5d1f63f3ca9151897abebc', '[{\"id\":13,\"value\":\"老王\"},{\"id\":14,\"value\":\"小滴课堂讲师\"},{\"id\":15},{\"id\":16,\"value\":[\"\",\"01HFBG1245W7BP5NNWFTHBCRPC\",\"01HFBG12W54CZXH1JN9HZJ843F\"]}]');
COMMIT;

-- ----------------------------
-- Table structure for page
-- ----------------------------
DROP TABLE IF EXISTS `page`;
CREATE TABLE `page` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account_id` int NOT NULL,
  `page_name` varchar(255) NOT NULL,
  `components` text NOT NULL,
  `tdk` varchar(255) NOT NULL,
  `desc` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of page
-- ----------------------------
BEGIN;
INSERT INTO `page` VALUES (1, 1, '小滴低代码开发页面', '7,8,9,10,11,12,13,14,15,16', 'xdclass,lowcode,低代码,小滴,小滴课堂', '小滴低代码开发页面详情');
COMMIT;

-- ----------------------------
-- Table structure for resources
-- ----------------------------
DROP TABLE IF EXISTS `resources`;
CREATE TABLE `resources` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `account_id` int NOT NULL,
  `type` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of resources
-- ----------------------------
BEGIN;
INSERT INTO `resources` VALUES (1, 'https://lowcode.16web.net/upload_files/QD-1700118567343.png', 1, 'image', 'QD.png');
INSERT INTO `resources` VALUES (2, 'https://lowcode.16web.net/upload_files/JD-1700118572012.png', 1, 'image', 'JD.png');
INSERT INTO `resources` VALUES (3, 'https://lowcode.16web.net/upload_files/HD-1700118576423.png', 1, 'image', 'HD.png');
INSERT INTO `resources` VALUES (4, 'https://lowcode.16web.net/upload_files/WechatIMG725-1700118600207.jpg', 1, 'image', 'WechatIMG725.jpg');
INSERT INTO `resources` VALUES (5, 'https://lowcode.16web.net/upload_files/WechatIMG726-1700118605600.jpg', 1, 'image', 'WechatIMG726.jpg');
INSERT INTO `resources` VALUES (6, 'https://lowcode.16web.net/upload_files/WechatIMG723-1700118611527.jpg', 1, 'image', 'WechatIMG723.jpg');
INSERT INTO `resources` VALUES (8, 'https://lowcode.16web.net/upload_files/WechatIMG724-1700118642835.jpg', 1, 'image', 'WechatIMG724.jpg');
INSERT INTO `resources` VALUES (9, 'https://lowcode.16web.net/upload_files/6-1-1700118663282.mp4', 1, 'video', '6-1.深入理解路由的概念.mp4');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `head_img` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `open_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, '编程小白5738', 'https://xd-video-pc-img.oss-cn-beijing.aliyuncs.com/xdclass_pro/default/head_img/2.jpeg', '', '', 'oiNKG0wlF2Szv5pTw-vn7RggPaDY');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
