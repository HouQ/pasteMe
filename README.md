# 生产环境部署指南

## 1. 安装依赖
```bash
# 安装Python虚拟环境
sudo apt-get install python3-venv

# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装项目依赖
pip install -r requirements.txt

# 安装Gunicorn
pip install gunicorn

# 安装Nginx
sudo apt-get install nginx
```

## 2. 配置应用
```bash
# 复制配置文件
sudo cp nginx.conf /etc/nginx/sites-available/pasteMe

# 创建符号链接
sudo ln -s /etc/nginx/sites-available/pasteMe /etc/nginx/sites-enabled/

# 测试Nginx配置
sudo nginx -t

# 重启Nginx
sudo systemctl restart nginx
```

## 3. 启动应用
```bash
# 在虚拟环境中启动应用
gunicorn -c gunicorn_config.py backend:app

# 或者以后台模式运行
gunicorn -c gunicorn_config.py --daemon backend:app
```

## 4. 设置开机启动
```bash
# 创建systemd服务文件
sudo nano /etc/systemd/system/pasteMe.service

# 添加以下内容：
[Unit]
Description=PasteMe Application
After=network.target

[Service]
User=your_user
WorkingDirectory=/workspaces/pasteMe
ExecStart=/workspaces/pasteMe/venv/bin/gunicorn -c gunicorn_config.py backend:app
Restart=always

[Install]
WantedBy=multi-user.target

# 保存后启用并启动服务
sudo systemctl enable pasteMe
sudo systemctl start pasteMe

# 查看服务状态
sudo systemctl status pasteMe
```

## 5. 访问应用
1. 确保防火墙允许HTTP流量：
```bash
sudo ufw allow 'Nginx Full'
```

2. 在浏览器中访问：
```
http://your_server_ip
```

## 6. 常见问题排查
1. 查看Gunicorn日志：
```bash
journalctl -u pasteMe.service
```

2. 查看Nginx错误日志：
```bash
sudo tail -f /var/log/nginx/error.log
```

3. 检查端口占用：
```bash
sudo netstat -tuln | grep ':5000\|:80'
```

4. 重启服务：
```bash
sudo systemctl restart pasteMe
sudo systemctl restart nginx
```
