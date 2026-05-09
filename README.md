# Python UI + API Automation Testing Framework

## 项目简介

本项目是一个基于 Python 的自动化测试框架，结合 API 自动化测试与 UI 自动化测试，用于演示基础测试框架设计能力。

UI 测试基于稳定测试站点：
https://the-internet.herokuapp.com/login

---

## 功能特点

### API 自动化
- 基于 requests + pytest
- 支持 YAML 数据驱动
- 日志记录调试信息

### UI 自动化
- 基于 Selenium WebDriver
- 显式等待机制（WebDriverWait）
- 登录场景自动化验证

### 框架设计
- 模块化结构（common / testcases / data）
- WebDriver 自动管理
- 日志系统封装

---

## 运行方式

```bash
pip install -r requirements.txt
python -m pytest
