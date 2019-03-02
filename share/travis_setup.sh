#!/bin/bash
set -evx

mkdir ~/.ukkeycore

# safety check
if [ ! -f ~/.ukkeycore/.ukkey.conf ]; then
  cp share/ukkey.conf.example ~/.ukkeycore/ukkey.conf
fi
