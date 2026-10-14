#!groovy

@Library('jenkins-shared-library@main') _

def test = new org.test()

pipeline {
    agent any
    stages {     
        stage('Stage 1') {
            steps {
                script {
                    test.librarytest()
                    log.info('Starting')
                    log.warning('11','22')
                }
            }
        }                      
    }
}
