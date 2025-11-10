#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import numpy as np
from mpmath import mp, zeta
import bisect
import os

mp.dps = 50  # precision

# ============================================================
# Load known zeros (zeros6.txt must exist in same folder)
# ============================================================

def load_known_zeros(path="zeros6.txt"):
    if not os.path.exists(path):
        print("⚠️  zeros6.txt not found, assuming no known zeros.")
        return []
    with open(path) as f:
        return [float(x.strip()) for x in f if x.strip()]

KNOWN_ZEROS = load_known_zeros()


# ============================================================
# Known zero lookup helper
# ============================================================

def known_zeros_in_tile(a, b):
    left = bisect.bisect_left(KNOWN_ZEROS, a)
    right = bisect.bisect_left(KNOWN_ZEROS, b)
    return right - left


# ============================================================
# Zeta evaluation helpers
# ============================================================

def eval_z(t):
    return zeta(0.5 + 1j * t)

def eval_z_np(ts):
    return np.array([complex(zeta(0.5 + 1j * float(t))) for t in ts])


# ============================================================
# Local certificate — returns (#zeros, dt_used, samples, refinements)
# ============================================================

def certified_arg_local(a, b, N0, step_scale, refine_cap, min_dt):
    dt = (b - a) / N0
    if dt < min_dt:
        dt = min_dt

    ts = np.arange(a, b + dt, dt)
    vals = eval_z_np(ts)

    args_unwrapped = np.unwrap(np.angle(vals))
    dtheta = args_unwrapped[-1] - args_unwrapped[0]

    zero_est = int(round(dtheta / np.pi))

    if abs(zero_est) <= 1 or refine_cap <= 0:
        return zero_est, dt, len(ts), 0

    mid = 0.5 * (a + b)
    z1, dt1, s1, r1 = certified_arg_local(a, mid, int(N0 * 1.3), step_scale, refine_cap - 1, min_dt)
    z2, dt2, s2, r2 = certified_arg_local(mid, b, int(N0 * 1.3), step_scale, refine_cap - 1, min_dt)

    return z1 + z2, min(dt1, dt2), s1 + s2, r1 + r2 + 1


# ============================================================
# ✅ NEW ADAPTIVE / CONSENSUS TILE PROCESSOR
# ============================================================

def process_tile(a, b, N0, Nmax, step_scale, min_dt):

    def run_cert(N, scale):
        cnt, dt, smp, ref = certified_arg_local(
            a, b, int(N),
            step_scale=scale,
            refine_cap=6,
            min_dt=min_dt
        )
        return cnt, dt, smp, ref

    # Best ladder from testing
    ladder_pairs = [
        (max(5, N0), min(30, Nmax)),
        (max(30, N0), min(60, Nmax)),
        (max(60, N0), min(120, Nmax)),
        (max(120, N0), min(240, Nmax)),
        (max(300, N0), min(500, Nmax)),
        (max(500, N0), min(800, Nmax)),
    ]
    ladder_pairs = [(lo, hi) for (lo, hi) in ladder_pairs if lo <= hi]

    def try_ladder(scale):
        total_samples = 0
        total_refines = 0
        best_dt = None
        best_N = None

        for lo, hi in ladder_pairs:
            cnt1, dt1, s1, r1 = run_cert(lo, scale)
            cnt2, dt2, s2, r2 = run_cert(hi, scale)

            total_samples += (s1 + s2)
            total_refines += (r1 + r2)

            best_dt = min(dt1, dt2)
            best_N = hi

            # ✅ CONSENSUS RULE
            if cnt1 == cnt2:
                return cnt2, best_N, best_dt, total_samples, total_refines

        # No consensus → take final high N result
        cnt3, dt3, s3, r3 = run_cert(best_N, scale)
        return cnt3, best_N, dt3, (total_samples + s3), (total_refines + r3)

    cnt, NN, dt, samples, refines = try_ladder(step_scale)

    suspicious = (dt <= 1.05 * min_dt) or (cnt > 6)
    if suspicious and step_scale > 0.5:
        cnt2, NN2, dt2, s2, r2 = try_ladder(step_scale * 0.6)
        if dt2 < dt or cnt2 <= cnt:
            cnt, NN, dt = cnt2, NN2, dt2
        samples += s2
        refines += r2

    return cnt, NN, dt, samples, refines


# ============================================================
# Main driver
# ============================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=float, required=True)
    parser.add_argument("--end", type=float, required=True)
    parser.add_argument("--tiles", type=int, default=60)
    parser.add_argument("--N0", type=int, default=30000)
    parser.add_argument("--Nmax", type=int, default=80000)
    parser.add_argument("--step_scale", type=float, default=0.22)
    parser.add_argument("--min_dt", type=float, default=1e-4)
    args = parser.parse_args()

    a0, b0 = args.start, args.end
    width = (b0 - a0) / args.tiles

    print(f"=== Certifying [ {a0} , {b0} ]  using {args.tiles} tiles ===")
    print(f"N0={args.N0}  Nmax={args.Nmax}  step-scale={args.step_scale}")
    print()

    total = 0

    for i in range(args.tiles):
        a = a0 + width * i
        b = a + width

        est, NN, dt_used, samples, refi = process_tile(
            a, b, args.N0, args.Nmax, args.step_scale, args.min_dt
        )

        known = known_zeros_in_tile(a, b)
        match = "✅ match" if est == known else "❌ MISMATCH"

        print(f"[{a:.6f},{b:.6f}] zeros={est} (known={known})  "
              f"N={NN}  dt={dt_used:.5f}  samples={samples}  refs={refi}  {match}")

        total += est

    print(f"\n✅ CERTIFIED ZERO COUNT: {total}")


if __name__ == "__main__":
    main()
