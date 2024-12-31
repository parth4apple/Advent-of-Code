#!/usr/bin/env bash

for i in {1..25}; do
  echo "Day $i:"
  python3 "$i.py" < "$i.in"
  echo ""
done
