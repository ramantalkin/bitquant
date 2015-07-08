#!/bin/bash
# sudo portion of npm package installations

echo "Running npm root installation"
ROOT_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
. $ROOT_SCRIPT_DIR/rootcheck.sh
SCRIPT_DIR=$1
ME=$2

# put yelp_uri in back to override downloaded version
for repo in ijavascript ; do
npm install -g $repo
done