#!/bin/sh

## Usage:
##   . ./env.sh ; $COMMAND
##   . ./env.sh ; echo ${ENV_VAR}

unamestr=$(uname)
if [ "$unamestr" = 'Linux' ]; then

  export $(grep -v '^#' .env | xargs -d '\n')

elif [ "$unamestr" = 'Darwin' ]; then

    export $(grep -v '^#' .env | xargs -0)

elif [ "$unamestr" = 'FreeBSD' ]; then

  export $(grep -v '^#' .env | xargs -0)

fi
