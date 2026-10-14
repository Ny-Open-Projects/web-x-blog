package org

def scm(build_branch,url){
    checkout scmGit(branches: [[name: "${build_branch}"]], extensions: [], 
    userRemoteConfigs: [[credentialsId: 'gitlab', url: "${url}"]])        
}

