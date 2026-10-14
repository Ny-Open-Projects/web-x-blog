docker run --name jenkins -itd \
       -p 80:8080 \
       -p 50000:50000 \
       -v /data/jenkins:/var/jenkins_home \
       -v /var/run/docker.sock:/var/run/docker.sock \
       -v /bin/docker:/usr/bin/docker \
       -v /etc/localtime:/etc/localtime:ro \
       -e JAVA_OPTS="-Dsun.jnu.encoding=UTF-8 -Dfile.encoding=UTF-8 -Duser.timezone=Asia/Shanghai" \
       --restart=always \
       --user=root \
       --privileged=true \
       jenkins/jenkins:lts
