FROM mysql
EXPOSE 3306

# 設定ファイルの読み込み
ADD ./my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf

CMD ["mysqld"]
