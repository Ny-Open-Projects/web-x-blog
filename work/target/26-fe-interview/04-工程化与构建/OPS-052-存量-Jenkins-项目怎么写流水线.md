---
title: [OPS-052] 存量 Jenkins 项目怎么写流水线？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-052：存量 Jenkins 项目怎么写流水线？
**答**：
- 存量团队常见 Jenkins + 声明式 Jenkinsfile：stages 与 GH Actions 概念一一对应，凭据用 credentials() 解耦，凭证零明文。
- agent 标签选择构建机（前端构建机要装 nvm/node 指定版本）；用 stash/archive 传递产物。
- 生产发布用 input 阶段做人工审批，timeout 控制审批有效期，审批通过才继续。
- Jenkinsfile 入库（Pipeline script from SCM），构建配置代码化可审计。

```groovy
// Jenkinsfile（声明式）
pipeline {
  agent { label 'fe-builder' }   // 带 node22 环境的构建机

  options { timestamps(); disableConcurrentBuilds(); timeout(time: 30, unit: 'MINUTES') }

  environment {
    NODE_ENV = 'production'
    DEPLOY_HOST = 'web01'
  }

  stages {
    stage('Install') {
      steps { sh 'npm ci --registry=https://registry.npmmirror.com' }
    }
    stage('Lint & Test') {
      parallel {
        stage('lint') { steps { sh 'npm run lint' } }
        stage('test') { steps { sh 'npm test -- --coverage' } }
      }
      post {
        always { junit 'junit.xml'; publishCoverage adapters: [istanbulCoberturaAdapter('coverage/cobertura-coverage.xml')] }
      }
    }
    stage('Build') {
      steps {
        sh "npm run build -- --version=${env.BUILD_NUMBER}-${env.GIT_COMMIT[0..7]}"
        archiveArtifacts artifacts: 'dist/**', fingerprint: true   // 产物留档可追溯
      }
    }
    stage('Deploy Staging') {
      steps {
        sh "rsync -azc dist/ deploy@staging:/data/web/mall/releases/${env.BUILD_NUMBER}/"
      }
    }
    stage('Approve Production') {      // 人工审批卡点
      steps {
        timeout(time: 24, unit: 'HOURS') {
          input message: '发布到生产?', ok: '发布',
                submitter: 'release-manager,fe-oncall'
        }
      }
    }
    stage('Deploy Prod') {
      steps {
        withCredentials([sshUserPrivateKey(credentialsId: 'deploy-key', keyFileVariable: 'K')]) {
          sh "rsync -azc -e 'ssh -i $K' dist/ deploy@$DEPLOY_HOST:/data/web/mall/releases/${env.BUILD_NUMBER}/"
          sh "ssh -i $K deploy@$DEPLOY_HOST ln -sfn /data/web/mall/releases/${env.BUILD_NUMBER} /data/web/mall/current"
        }
      }
    }
  }
  post {
    failure { slackSend channel: '#fe-oncall', message: "构建失败 ${env.JOB_NAME} #${env.BUILD_NUMBER}" }
  }
}
```
