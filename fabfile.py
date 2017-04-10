#!venv/bin/python
#
# e.g. fab -u root -H mirrors.cqu.edu.cn --port=1403 -i ~/.ssh/ test

from fabric.api import run, env, local, put

env.host  = "root"
env.hosts = ["mirrors.cqu.edu.cn"]


def test():
    run("mkdir -p /tmp/nginx-confs")
    put("", "")

