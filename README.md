# ProxyPool-Heroku

在WiseDoge的ProxyPool基础上改造的[PorxyPool](https://github.com/WiseDoge/ProxyPool)，并且部署到Heroku上简单使用

> 使用详情请见WiseDoge的项目说明。

## 如何部署到Heroku平台

***请确保注册了Heroku平台的账号，以及绑定了一张信用卡.虽然部署依赖的Redis Nano版本免费，但是附加RedisToGo这个plugin是需要绑定信用卡的。注意每月的免费时长为950小时，足够使用了。***

> 另外一个前置条件是安装Heroku Cli，请从这个地址[下载](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)。

``` bash
git clone https://github.com/EmptyChan/ProxyPool-Heroku.git

cd ProxyPool-Heroku/

heroku create [APP]  # APP是一个项目名称，随意取，最好特殊一点，允许连字符，不允许下划线

git add .

git commit -m 'some content' # 添加提交信息

git push heroku master  # 将内容提交并部署到Heroku平台

heroku logs --tail  # 检查logs，可以看到内容输出
```

## 测试是否部署成功

> 请参考WiseDoge的项目说明 => [PorxyPool](https://github.com/WiseDoge/ProxyPool)

注意部署后的地址不是```127.0.0.1```，而是```heroku app```的地址。

## 查看RedisToGo中的数据

如果想要查看```RedisToGo```中的数据，请参考这个[StackOverFlow](https://stackoverflow.com/questions/17846371/how-to-connect-to-redistogo-how-to-see-the-data)链接。
