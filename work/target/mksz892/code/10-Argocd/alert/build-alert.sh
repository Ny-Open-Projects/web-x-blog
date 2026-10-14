#!/bin/bash
username=${1}
password=${2}
branch=${3}
projectName=${4}

argocd login 10.0.7.101:32471 --insecure --username ${username} --password ${password}
counter=0
max_attempts=60
branch=`echo ${branch} | awk -F'/' '{print $NF}'`
while [ $counter -lt $max_attempts ]
do
    sync_status=`argocd app get argocd/${branch}-${projectName} -o json | jq -r '.status.sync.status'`
    app_health=`argocd app get argocd/${branch}-${projectName} -o json | jq -r '.status.health.status'`
    if [ "$sync_status" = "Synced" ] && [ "$app_health" = "Healthy" ]
    then
        echo "### ${branch}-${projectName} deploy success ###"
        echo "argocd/${branch}-${projectName} current sync_status is $sync_status and app_health is $app_health"
        break
    else
        sleep 1
        echo "argocd/${branch}-${projectName} current sync_status is $sync_status and app_health is $app_health, Walting ${counter}s..."
        counter=$((counter+1))
        if [ $counter -eq $max_attempts ]
        then
            echo "Timeout: argocd/${branch}-${projectName}  Deploy has exceeded the maximum limit time, please review, timeout ${counter}s"
            exit 1
        fi
        if [ "$sync_status" = "Error" ] || [ "$sync_status" = "Unknown" ] || [ "$app_health" = "Unknown" ] || [ "$app_health" = "Degraded" ]
        then
            echo "failed: argocd/${branch}-${projectName}  Deploy failed，current sync_status is $sync_status and app_health is $app_health"
            exit 1
        fi
    fi
done