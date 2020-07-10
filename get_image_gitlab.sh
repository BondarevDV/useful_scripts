docker run -d --hostname gitlab.nppstrela.com \
-p 443:443 -p 80:80 -p 2222:22 \
--name gitlab \
--restart unless-stopped \
--volume /storage/gitlab/config:/etc/gitlab \
--volume /storage/gitlab/logs:/var/log/gitlab \
--volume /storage/gitlab/data:/var/opt/gitlab \
gitlab/gitlab-ee:latest

