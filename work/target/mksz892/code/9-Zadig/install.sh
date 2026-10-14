#!/bin/bash
set -o errexit

# This script is meant for fast & easy installation of zadig
# The possible environment variables is listed below:
#|--------------------|--------------------------------------------------|---------------------|
#|      Key           |                   Description                    |      Default        |
#|--------------------|--------------------------------------------------|---------------------|
#|      NAMESPACE     | The namespace Zadig to be installed in.          | zadig               |
#|--------------------|--------------------------------------------------|---------------------|
#|        DOMAIN      | The hostname of Zadig system.                    | ""                  |
#|--------------------|--------------------------------------------------|---------------------|
#|                    | The ip of Zadig system, if domain is not         |                     |
#|         IP         | applicable. Note that either DOMAIN or IP must   | ""                  |
#|                    | be provided otherwise the installation WILL fail |                     |
#|--------------------|--------------------------------------------------|---------------------|
#|       PORT         | The port of Zadig system. This variable must be  | ""                  |
#|                    | set if IP is set                                 |                     |
#|--------------------|--------------------------------------------------|---------------------|
#|                    | If no custom ingress class is provided.          |                     |
#|    SERVICE_TYPE    | SERVICE_TYPE should be set. Only NodePort        | NodePort            |
#|                    | and LoadBalancer service type is supported.      |                     |
#|--------------------|--------------------------------------------------|---------------------|
#|  INSECURE_REGISTRY | Custom insecure registry address                 | ""                  |
#|--------------------|--------------------------------------------------|---------------------|
#|                    | The connection string of user-provide mongodb    |                     |
#|    MONGO_URI       | This shouldn't be set if the customer wants to   | ""                  |
#|                    | use the build-in mongodb                         |                     |
#|--------------------|--------------------------------------------------|---------------------|
#|     MONGO_DB       | The DB of the Zadig system                       | zadig               |
#|--------------------|--------------------------------------------------|---------------------|
#|                    | The host of user-provide mysql                   |                     |
#|    MYSQL_HOST      | This shouldn't be set if the customer wants to   | ""                  |
#|                    | use the build-in mysql                           |                     |
#|--------------------|--------------------------------------------------|---------------------|
#|    MYSQL_PORT      | The port of user-provide mysql                   | ""                  |
#|--------------------|--------------------------------------------------|---------------------|
#|  MYSQL_USERNAME    | The username of the given mysql                  | ""                  |
#|--------------------|--------------------------------------------------|---------------------|
#|   MYSQL_PASSWORD   | The password of the given mysql                  | ""                  |
#|--------------------|--------------------------------------------------|---------------------|
#|    STORAGE_SIZE    | The pvc size of the build-in mongodb             | 20Gi                |
#|--------------------|--------------------------------------------------|---------------------|
#|   ENCRYPTION_KEY   | The system-wide encryption key. If not provided, | ""                  |
#|                    | installer will randomize a key.                  |                     |
#|--------------------|--------------------------------------------------|---------------------|
#|     DRY_RUN        | Check install log without real installation      | ""                  |
#|--------------------|--------------------------------------------------|---------------------|
#|       EMAIL        | Email address of the initial user                | "admin@example.com" |
#|--------------------|--------------------------------------------------|---------------------|
#|      PASSWORD      | Password of the initial user                     | "Zadig123"          |
#|--------------------|--------------------------------------------------|---------------------|

ZADIG_VERSION=1.18.0

# Koderover bin path
KODEROVER_HOME=${HOME}/.koderover
KODEROVER_BIN=${KODEROVER_HOME}/bin
HELM_REPO=${HELM_REPO:-https://koderover.tencentcloudcr.com/chartrepo/chart}
PATH=${KODEROVER_BIN}:$PATH
EMAIL=${EMAIL:-admin@example.com}
PASSWORD=${PASSWORD:-Zadig123}

# logging color
RED='\033[0;31m'
NOCOLOR='\033[0m'
# helm install parameters
INSTALL_PARAMETER=

checkCmdExists() {
  command -v "$@" > /dev/null 2>&1
}

ensure_parameter() {
  # opensource version
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set tags.enterprise=false"
  ensure_api_gateway
  ensure_endpoint
  ensure_mongodb
  ensure_mysql
  ensure_minio
  ensure_apiserver
  ensure_encryption_key
  ensure_default_user
  ensure_dex
  # dry-run if it is set
  if [ -n "${DRY_RUN}" ]; then
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --dry-run"
  fi
}

ensure_dex() {
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.fullnameOverride=zadig-${NAMESPACE:=zadig}-dex"
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.issuer=http://zadig-${NAMESPACE:=zadig}-dex:5556/dex"
}

ensure_api_gateway() {
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set global.extensions.extAuth.extauthzServerRef.namespace=${NAMESPACE:-zadig}"
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set gloo.gatewayProxies.gatewayProxy.service.type=${SERVICE_TYPE:-NodePort}"
}

ensure_apiserver() {
  APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set kubernetes.server=${APISERVER}"
}

ensure_endpoint() {
  # Make sure only one of IP+PORT OR DOMAIN is provided
  if { { [ -z "${IP}" ] || [ -z "${PORT}" ];} && [ -z "${DOMAIN}" ]; } || { [ -n "${IP}" ] && [ -n "${DOMAIN}" ]; }; then
    printf "${RED}Either IP+PORT or DOMAIN shoule be provided${NOCOLOR}\n"
    exit 1
  fi

  # Set corresponding install parameters
  if [ -n "${IP}" ]; then
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set endpoint.type=IP --set endpoint.IP=${IP} --set gloo.gatewayProxies.gatewayProxy.service.httpNodePort=${PORT}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.staticClients[0].redirectURIs[0]=http://${IP}:${PORT}/api/v1/callback,dex.config.staticClients[0].id=zadig,dex.config.staticClients[0].name=zadig,dex.config.staticClients[0].secret=ZXhhbXBsZS1hcHAtc2VjcmV0"
  else
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set endpoint.type=FQDN --set endpoint.FQDN=${DOMAIN}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.staticClients[0].redirectURIs[0]=http://${DOMAIN}/api/v1/callback,dex.config.staticClients[0].id=zadig,dex.config.staticClients[0].name=zadig,dex.config.staticClients[0].secret=ZXhhbXBsZS1hcHAtc2VjcmV0"
  fi
}

ensure_mongodb() {
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set connections.mongodb.db=${MONGO_DB:-zadig}"
  # if a MONGO_URI env variable is set, built-in mongodb does not need to be installed
  if [ -n "${MONGO_URI}" ]; then
    # disable the installation of built-in mongodb
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set tags.mongodb=false"
    # set the connection string for zadig services
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set connections.mongodb.connectionString=${MONGO_URI}"
  # otherwise we need to install the built-in mongodb
  else
    # enable the installation of built-in mongodb
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set tags.mongodb=true"
    # set the storage size of the built-in mongodb
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set mongodb.persistence.size=${STORAGE_SIZE:-20Gi}"
  fi
}

ensure_mysql() {
  # if a MYSQL_URI env variable is set, built-in mysql does not need to be installed
  if [ -n "${MYSQL_HOST}" ]; then
    # disable the installation of built-in mysql
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set tags.mysql=false"
    # set the connection string for zadig services
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set connections.mysql.host=${MYSQL_HOST}:${MYSQL_PORT}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set connections.mysql.auth.user=${MYSQL_USERNAME}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set connections.mysql.auth.password=${MYSQL_PASSWORD}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.storage.config.host=${MYSQL_HOST}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.storage.config.port=${MYSQL_PORT}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.storage.config.user=${MYSQL_USERNAME}"
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set dex.config.storage.config.password=${MYSQL_PASSWORD}"
  # otherwise we need to install the built-in mysql
  else
    # enable the installation of built-in mysql
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set tags.mysql=true"
    # set the storage size of the built-in mysql
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set mysql.persistence.size=${STORAGE_SIZE:-20Gi}"
  fi
}

ensure_minio() {
  # built-in minio is required for opensource version of zadig to work
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set tags.minio=true"
  if [ -n "${STORAGE_CLASS}" ]; then
    INSTALL_PARAMETER="${INSTALL_PARAMETER} --set minio.persistence.storageClass=${STORAGE_CLASS}"
  fi
}

ensure_encryption_key() {
  # if no encryption key is provided, the installer will generate a random encryption key.
  if [ -z "${ENCRYPTION_KEY}" ]; then
    EXISTING_KEY=$(kubectl -n ${NAMESPACE:-zadig} get secret zadig-aes-key -o=jsonpath='{.data.aesKey}' 2>/dev/null | base64 -d)
    if [ -z "${EXISTING_KEY}" ]; then
      ENCRYPTION_KEY=$(openssl enc -aes-128-cbc -k secret -P -md sha1 | grep key | cut -d "=" -f2-)
      printf "NO ENCRYPTION KEY PROVIDED, ZADIG HAS GENERATED AN ENCRYPTION KEY\n" 1>&2
      printf "${ENCRYPTION_KEY}\n"
      printf "THIS KEY WILL BE USED FOR POSSIBLE FUTURE REINSTALLATION, PLEASE SAVE THIS KEY CAREFULLY\n"
    else
      ENCRYPTION_KEY=${EXISTING_KEY}
    fi
  fi
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set global.encryption.key=${ENCRYPTION_KEY}"
}

ensure_default_user() {
  INSTALL_PARAMETER="${INSTALL_PARAMETER} --set init.adminPassword=${PASSWORD} --set init.adminEmail=${EMAIL}"
}

install_helm() {
  HELM_DIR=$KODEROVER_HOME/helm
  mkdir -p "$KODEROVER_BIN"
  mkdir -p "$HELM_DIR"

  if [ -x $KODEROVER_BIN/helm ]; then
    return
  fi

  echo "installing helm client..."
  if [ $(uname -s) == "Darwin" ]; then
    curl -fsSL -o $HELM_DIR/helm.tar.gz "https://resources.koderover.com/tools/helm-v3.6.1-darwin-amd64.tar.gz"
    tar -xzf $HELM_DIR/helm.tar.gz -C $HELM_DIR
  else
    curl -fsSL -o $HELM_DIR/helm.tar.gz "https://resources.koderover.com/tools/helm-v3.6.1-linux-amd64.tar.gz"
    tar -xzf $HELM_DIR/helm.tar.gz -C $HELM_DIR
  fi

  mv $(find ${HELM_DIR} -type f -name helm) $KODEROVER_BIN/helm
  chmod +x $KODEROVER_BIN/helm
  rm -rf $HELM_DIR
  echo "succeed to install helm client: $(helm version)"
}

cleanup() {
  rm -rf "${KODEROVER_HOME}"
}

install_zadig() {
  cleanup
  ensure_parameter
  if ! checkCmdExists "helm" ; then
    install_helm
  fi
  echo "installing zadig ..."
  helm repo add koderover-chart "${HELM_REPO}"
  helm repo update
  helm upgrade --timeout 15m --install --create-namespace -n "${NAMESPACE:-zadig}"${INSTALL_PARAMETER} --version="${ZADIG_VERSION}" "zadig-${NAMESPACE:-zadig}" koderover-chart/zadig

  printf "\nTHIS KEY WILL BE USED FOR POSSIBLE FUTURE REINSTALLATION, PLEASE SAVE THIS KEY CAREFULLY:\n"
  printf -- "- Encryption Key: ${ENCRYPTION_KEY}\n"
  cleanup
}

install_zadig
