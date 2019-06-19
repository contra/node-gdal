#!/bin/bash

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/libexpat"

EXPAT_VERSION=2.2.6
dir_expat=./expat

#
# download expat source
#

rm -rf $dir_expat
if [[ ! -f expat.tar.gz ]]; then
	curl -L "https://fossies.org/linux/www/expat-${EXPAT_VERSION}.tar.gz" -o expat.tar.gz
fi
tar -xzf expat.tar.gz
mv expat-${EXPAT_VERSION} $dir_expat
