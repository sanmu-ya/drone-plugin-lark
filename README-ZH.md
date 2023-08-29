<img src="images/Lark.png" width="30%"/>

## drone-plugin-lark
[![Docker Pulls](https://img.shields.io/docker/pulls/sanmuya/drone-plugin-lark)]()
[![GitHub license](https://img.shields.io/github/license/sanmu-ya/drone-plugin-lark)]()
[![Docker Image-size](https://img.shields.io/docker/image-size/sanmuya/drone-plugin-lark/latest)]()

drone 飞书-自定义群聊机器人消息推送插件。

其它语言版本：[English](README.md)，[简体中文](README-ZH.md)。

## 环境变量

- `PLUGIN_WEBHOOK`: 这是一个必填参数，填写群聊机器人的webhook地址。
- `PLUGIN_SECRET`: 这是一个必填参数，为了确保您的webhook地址的安全，请开启签名验证。
- `PLUGIN_MESSAGE`: 这里填写的是需要发送的文本内容，可以像示例一样填写多行文本，效果可以参考下面的图片。这里使用`,`分隔行

## 如何使用

- 直接使用命令行终端运行docker镜像

  ```shell
  docker run --rm \
  -e PLUGIN_WEBHOOK="https://open.feishu.cn/open-apis/bot/v2/hook/f1ac0a3e-4555-420f-99a9-338cf39600f2" \
  -e PLUGIN_SECRET="tsOjqrp6RGazcs9QaFmhj" \
  -e PLUGIN_MESSAGE="========== drone message ==========,REPO: sanmu-ya/drone-plugin-lark,AUTHOR: xys.dg,COMMIT_BRANCH: master,COMMIT_MESSAGE: This is an example" \
  sanmuya/drone-plugin-lark
  ```

- 添加一个step到你的`.drone.yml`中

  ```yml
  steps:
  - name: lark
    image: sanmuya/drone-plugin-lark:latest
    settings:
      webhook: https://open.feishu.cn/open-apis/bot/v2/hook/f1ac0a3e-4555-420f-99a9-338cf39600f2
      secret:
        from_secret: lark-secret
      message:
        - ========== drone message ==========
        - REPO: ${DRONE_REPO}
        - AUTHOR: ${DRONE_COMMIT_AUTHOR_NAME}
        - COMMIT_BRANCH: ${DRONE_COMMIT_BRANCH}
        - COMMIT_MESSAGE: ${DRONE_COMMIT_MESSAGE}
  ```

## 效果

<img src="images/example.jpg" />