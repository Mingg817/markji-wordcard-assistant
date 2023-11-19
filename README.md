# Markji的单词听写卡生成器

## 目录

- [干啥的?](#干啥的?)
- [安装](#安装)
- [用法](#用法)
- [开源协议](#开源协议)

## 干啥的?

1. 调用外部语音接口,解决默认markji语音难听的问题
2. 解决markji语音无法批量生成的问题

## 安装

需要安装docker和git

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

```bash
git clone git@github.com:Mingg817/markji-wordcard-assistant.git
docker build -t markji_wordcard_assistant .
docker run -p 80:9000 --name markji_wordcard_assistant markji_wordcard_assistant 
```

如果你需要使用代理(国内访问Openai API需要代理),请运行
```bash
docker run -p 80:9000 --env https_proxy=http://代理地址:端口 --name markji_wordcard_assistant markji_wordcard_assistant 
```

## 用法

docker容器启动后访问 [http://127.0.0.1:80](http://127.0.0.1:80)


## 开源协议

[MIT](LICENSE) © LiYiMing