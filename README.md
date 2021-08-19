# flask-mysql-restfulapi-on-docker2
Flask環境とMySQL環境をDocker化  
Flask環境でRESTfulAPIを利用可能。ORMはpeeweeを利用  
※ 基本参考資料を参考にしながら作成したが、動かないので改良。動作確認済み(2021/08/18)  
※ 開発環境はUbuntu20.04(wsl2)  

参考資料等は下記を参照  
https://github.com/Yoshiyuki-Su/flask-mysql-restfulapi-on-docker  

# 手順
```
docker-compose build
docker-compose up -d
```

# 動作確認
```
$ curl -X POST http://localhost:5000/hoges \
  -H ">   -H "Content-Type:application/json" \
>   -d "{\"name\":\"hoge3\",\"state\":\"hoge3\"}"
{
    "state": "hoge3",
    "name": "hoge3",
    "updateTime": "2021-08-18T15:23:58",
    "id": "c6381d17-70df-427e-8430-d8132c363f82",
    "createTime": "2021-08-18T15:23:58"
}

$ curl -X PUT http://localhost:5000/hoges/12c38d62-9cd8-4711-a5cf-70f4ada02dea   -H "Content-Type:application/json"   -d "{\"name\":\"hoge1_update2\"}"

$ curl http://localhost:5000/hoges/12c38d62-9cd8-4711-a5cf-70f4ada02dea
{
    "state": "hoge1",
    "name": "hoge1_update2",
    "updateTime": "2021-08-18T15:23:04",
    "id": "12c38d62-9cd8-4711-a5cf-70f4ada02dea",
    "createTime": "2021-08-18T14:10:52"
}

$ curl http://localhost:5000/hoges
{
  "items": [
    {
      "createTime": "2021-08-18T14:10:52",
      "id": "12c38d62-9cd8-4711-a5cf-70f4ada02dea",
      "name": "hoge1_update2",
      "state": "hoge1",
      "updateTime": "2021-08-18T15:23:04"
    },
    {
      "createTime": "2021-08-18T14:21:14",
      "id": "b700c2a4-5ea4-4762-96a8-5154291924c6",
      "name": "hoge2",
      "state": "hoge2",
      "updateTime": "2021-08-18T14:21:14"
    },
    {
      "createTime": "2021-08-18T15:23:59",
      "id": "c6381d17-70df-427e-8430-d8132c363f82",
      "name": "hoge3",
      "state": "hoge3",
      "updateTime": "2021-08-18T15:23:59"
    }
  ]
}
```
DBの中身を確認後
DELETE
```
$ curl http://localhost:5000/hoges
{
  "items": [
    {
      "createTime": "2021-08-18T14:10:52",
      "id": "12c38d62-9cd8-4711-a5cf-70f4ada02dea",
      "name": "hoge1_update2",
      "state": "hoge1",
      "updateTime": "2021-08-18T15:23:04"
    },
    {
      "createTime": "2021-08-18T14:21:14",
      "id": "b700c2a4-5ea4-4762-96a8-5154291924c6",
      "name": "hoge2",
      "state": "hoge2",
      "updateTime": "2021-08-18T14:21:14"
    },
    {
      "createTime": "2021-08-18T15:23:59",
      "id": "c6381d17-70df-427e-8430-d8132c363f82",
      "name": "hoge3",
      "state": "hoge3",
      "updateTime": "2021-08-18T15:23:59"
    }
  ]
}

$ curl -X DELETE http://localhost:5000/hoges/c6381d17-70df-427e-8430-d8132c363f82
$ curl  http://localhost:5000/hoges/c6381d17-70df-427e-8430-d8132c363f82
{
    "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
}
$ curl http://localhost:5000/hoges
{
  "items": [
    {
      "createTime": "2021-08-18T14:10:52",
      "id": "12c38d62-9cd8-4711-a5cf-70f4ada02dea",
      "name": "hoge1_update2",
      "state": "hoge1",
      "updateTime": "2021-08-18T15:23:04"
    },
    {
      "createTime": "2021-08-18T14:21:14",
      "id": "b700c2a4-5ea4-4762-96a8-5154291924c6",
      "name": "hoge2",
      "state": "hoge2",
      "updateTime": "2021-08-18T14:21:14"
    }
  ]
}
```

# DBの中身参考
```
mysql> select *from hoges;
+--------------------------------------+---------------+-------+---------------------+---------------------+
| id                                   | name          | state | createTime          | updateTime          |
+--------------------------------------+---------------+-------+---------------------+---------------------+
| 12c38d62-9cd8-4711-a5cf-70f4ada02dea | hoge1_update2 | hoge1 | 2021-08-18 14:10:52 | 2021-08-18 15:23:04 |
| b700c2a4-5ea4-4762-96a8-5154291924c6 | hoge2         | hoge2 | 2021-08-18 14:21:14 | 2021-08-18 14:21:14 |
+--------------------------------------+---------------+-------+---------------------+---------------------+
```
