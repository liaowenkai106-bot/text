# Scrapling Demo

这是一个给本地学习用的 Scrapling 试用目录，不是对上游项目的整仓镜像。

## 你会得到什么

- `basic_fetch.py`：最小可运行示例，抓取 `quotes.toscrape.com`
- `parser_demo.py`：离线解析示例，不发网络请求，只练 HTML 解析

## 先安装

### 只想试解析功能

```bash
pip install scrapling
```

### 想跑抓取示例

```bash
pip install "scrapling[fetchers]"
scrapling install
```

> `scrapling install` 会安装浏览器相关依赖。第一次会比较慢。

## 运行方式

### 1) 基础抓取示例

```bash
python scrapling-demo/basic_fetch.py
```

它会访问 `https://quotes.toscrape.com/`，然后打印前几条名言和作者。

### 2) 离线解析示例

```bash
python scrapling-demo/parser_demo.py
```

这个文件不联网，只是把一段 HTML 字符串交给 Scrapling 解析，适合先理解选择器用法。

## 你应该先关注什么

先看这几个点：

1. `Fetcher.get(...)` 是怎么拿页面的
2. `page.css(...)` 是怎么选元素的
3. `::text` 是怎么取文本的
4. `.get()` 和 `.getall()` 的区别
5. 不联网时，`Selector(html)` 怎么直接解析字符串

## 后续建议

等你跑通后，可以自己再加：

- 把结果保存成 txt / json
- 抓详情页
- 处理分页
- 提取链接后进入下一层页面

## 说明

这个目录只用于学习 Scrapling 的基础用法，不包含任何绕过网站安全验证的内容。

上游项目：D4Vinci / Scrapling
