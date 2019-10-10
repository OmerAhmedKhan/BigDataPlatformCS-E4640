#!/usr/bin/bash
for i in {1..100}
do
  python3 testmydataIngest.py &
done
