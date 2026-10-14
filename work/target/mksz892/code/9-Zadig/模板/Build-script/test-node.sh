#!/bin/bash
set -e

cd /$WORKSPACE/node-cache;ls -la

cp $WORKSPACE/$REPONAME_0/package.json /$WORKSPACE/node-cache

cd /$WORKSPACE/node-cache && npm install --registry=https://registry.npmmirror.com

cp -r /$WORKSPACE/node-cache/node_modules $WORKSPACE/$REPONAME_0

cd $WORKSPACE/$REPONAME_0

npm run build

pwd;ls -la
