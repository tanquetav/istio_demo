#!/bin/bash

if [ $# -eq 0 ]
then
	echo "passar um parametro"
	exit 1
fi

kubectl $1 -f counter.yaml
kubectl $1 -f date.yaml
kubectl $1 -f flask.yaml
