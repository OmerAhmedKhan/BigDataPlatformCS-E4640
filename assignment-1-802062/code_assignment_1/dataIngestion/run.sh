#!/usr/bin/bash
for i in {1..50}
do
  python3 testmydataIngest.py &
done
