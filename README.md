# README

## Overview
This script runs `FINAL_CODE.py` with automatically calculated parameters.

It takes two arguments, start (`S`) and end (`E`), that compose a window.
The script will compute the number of tiles as `60*(E-S)/7.5` to accurately detect zeros.

Note that the program will validate found zeros up to ~1M. 
Beyond that the program has no records of zeros and thus will label them as errors (they may or may not be without a ground truth).
You can update the zeros6.txt file to include more zeros as ground truths.

---

## Usage

### 1. Make the script executable
```bash
chmod +x run.sh
```

### 2. Run the file
```bash
./run.sh 100 250
```

---

## Example

```bash
./run 100 107.5

=== Certifying [ 100.0 , 107.5 ]  using 60 tiles ===
N0=20  Nmax=1000  step-scale=0.22

[100.000000,100.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.125000,100.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.250000,100.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.375000,100.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.500000,100.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.625000,100.750000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.750000,100.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[100.875000,101.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.000000,101.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.125000,101.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.250000,101.375000] zeros=1 (known=1)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.375000,101.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.500000,101.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.625000,101.750000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.750000,101.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[101.875000,102.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.000000,102.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.125000,102.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.250000,102.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.375000,102.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.500000,102.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.625000,102.750000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.750000,102.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[102.875000,103.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.000000,103.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.125000,103.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.250000,103.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.375000,103.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.500000,103.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.625000,103.750000] zeros=1 (known=1)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.750000,103.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[103.875000,104.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.000000,104.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.125000,104.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.250000,104.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.375000,104.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.500000,104.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.625000,104.750000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.750000,104.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[104.875000,105.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.000000,105.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.125000,105.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.250000,105.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.375000,105.500000] zeros=1 (known=1)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.500000,105.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.625000,105.750000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.750000,105.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[105.875000,106.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.000000,106.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.125000,106.250000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.250000,106.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.375000,106.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.500000,106.625000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.625000,106.750000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.750000,106.875000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[106.875000,107.000000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[107.000000,107.125000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[107.125000,107.250000] zeros=1 (known=1)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[107.250000,107.375000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match
[107.375000,107.500000] zeros=0 (known=0)  N=30  dt=0.00417  samples=52  refs=0  ✅ match

✅ CERTIFIED ZERO COUNT: 4
```
