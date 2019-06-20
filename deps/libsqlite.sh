#!/bin/bash

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/libsqlite"

SQLITE_VERSION=3280000
dir_sqlite=./sqlite

#
# download sqlite source
#

rm -rf $dir_sqlite
if [[ ! -f sqlite.tar.gz ]]; then
  curl -L https://www.sqlite.org/2019/sqlite-autoconf-${SQLITE_VERSION}.tar.gz -o sqlite.tar.gz
fi
tar -xzf sqlite.tar.gz
mv sqlite-autoconf-${SQLITE_VERSION} $dir_sqlite
