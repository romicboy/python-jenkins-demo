#!/usr/bin/python
# -*- coding: utf-8 -*-
import jenkins
import logging
import json

logging.basicConfig(level=logging.DEBUG)

# 定义远程的jenkins master server的url，以及port
jenkins_server_url='http://jenkins.demo.com'

# 定义用户的User Id 和 API Token，获取方式同上文
user_id='user_id'
api_token='api_token'

# 实例化jenkins对象，连接远程的jenkins master server
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

# 获取服务信息，包含所有job
info = server.get_info()
jobs = info['jobs']
logging.info(json.dumps(jobs))

# 定义job名字
job_name = 'job_name'

#获取job名为job_name的job的相关信息
result = server.get_job_info(job_name)

# 执行job任务
server.build_job(job_name)

# 获取job执行的结果
result2 = server.get_build_info(job_name,26)

logging.info(json.dumps(result2))