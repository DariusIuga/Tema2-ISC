#!/usr/bin/env bash

for i in {1..5}; do
  nc -l -p 13236 &
  nc -l -p 14998 &
done &
