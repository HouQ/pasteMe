# pasteMe - 在线剪贴板应用

## 项目简介
pasteMe是一个简单的在线剪贴板应用，允许用户按日期保存和管理文本记录。支持Markdown语法渲染，适合用于个人笔记、代码片段保存等场景。

## 主要功能
- 按日期组织文本记录
- 支持文本输入和自动保存
- 提供复制和删除记录功能
- 支持Markdown语法渲染
- 响应式设计，适配移动端和桌面端

## 技术栈
### 前端
- Vue.js
- Tailwind CSS
- Font Awesome
- Notyf
- marked.js

### 后端
- Flask
- SQLite

## 项目结构
```
pasteMe/
├── backend.py         # Flask后端服务
├── paste.html         # 前端页面
├── paste.db           # SQLite数据库
├── README.md          # 项目说明文件
├── static/            # 前端静态资源
│   ├── font-aswsome.min.css
│   ├── marked.min.js
│   ├── notyf.min.css
│   ├── notyf.min.js
│   ├── tailwind.min.css
│   └── vue.global.js
└── webfonts/          # 字体文件
    ├── fa-brands-400.ttf
    ├── fa-brands-400.woff2
    ├── fa-regular-400.ttf
    ├── fa-regular-400.woff2
    ├── fa-solid-900.ttf
    └── fa-solid-900.woff2
```

## 使用说明
1. 安装依赖：
   ```bash
   pip install flask
   ```

2. 启动服务：
   ```bash
   python backend.py
   ```

3. 访问应用：
   打开浏览器，访问 `http://localhost:5000`

4. 使用说明：
   - 在文本框中输入或粘贴内容，系统会自动保存
   - 点击日期查看历史记录
   - 点击复制按钮将内容复制到剪贴板
   - 点击删除按钮删除记录

## 注意事项
- 首次运行会自动创建数据库文件 `paste.db`
- 确保端口5000未被占用
- 建议在本地开发环境中使用
