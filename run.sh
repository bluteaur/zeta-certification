#!/bin/bash

S=$1
E=$2
TILES=$(echo "scale=0; 60*($E-$S)/7.5" | bc)

python3 FINAL_CODE.py \
  --start "$S" \
  --end "$E" \
  --tiles "$TILES" \
  --N0 20 \
  --Nmax 1000
