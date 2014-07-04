#! /bin/bash

sed 's@\(.*\),\(.*\),\(.*\),\(.*\),\(.*\)@\2,\3,\4,\5,\1@g' user_edges.txt>output.txt
