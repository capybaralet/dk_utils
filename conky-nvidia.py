#!/usr/bin/env python2

#import os
#os.putenv("DISPLAY", ":8")

import argparse
from subprocess import Popen, PIPE

def nvidia_attr(gpu, query, type = str, default = 0):
    gpu  = int(gpu)
    args = ["nvidia-settings", "--terse", "--query=[gpu:%d]/%s" % (gpu, query)]

    proc = Popen(args, 0, None, PIPE, PIPE, PIPE)
    sout = proc.stdout.read()

    if not sout:
        return type(default)

    return type(sout)

def nvidia_attr_csv(gpu, query, key, type = str, default = 0):
    attr = nvidia_attr(gpu, query)

    for pair in attr.split(", "):
        pair = pair.split("=", 2)

        if len(pair) < 2:
            continue

        k, v = tuple(pair)

        if k == key:
            return type(v)

    return type(default)

def percentage(total, current):
    total   = int(total)
    current = int(current)

    if total < 1 or total < current:
        return 0

    return int((float(current) / float(total)) * 100)

def size_format(size):
    size = int(size)

    if size >= 1024:
        size = float(size)
        return "%.2fGiB" % (float(size / 1024))

    return "%dMiB" % (size)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument(
        "gpu",
        type    = int,
        metavar = "GPU",
        help    = "index of the GPU"
    )

    parser.add_argument(
        "display",
        type    = str,
        metavar = "DISPLAY",
        help    = "name of data to display"
    )

    args = parser.parse_args()
    args.display = args.display.lower()

    if args.display == "gpu":
        print nvidia_attr_csv(args.gpu, "GPUUtilization", "graphics", int)
    elif args.display == "memperc":
        total = nvidia_attr(args.gpu, "TotalDedicatedGPUMemory", int)
        used  = nvidia_attr(args.gpu, "UsedDedicatedGPUMemory",  int)
        print percentage(total, used)
    elif args.display == "mem":
        used  = nvidia_attr(args.gpu, "UsedDedicatedGPUMemory",  int)
        print size_format(used)
    elif args.display == "memfree":
        total = nvidia_attr(args.gpu, "TotalDedicatedGPUMemory", int)
        used  = nvidia_attr(args.gpu, "UsedDedicatedGPUMemory",  int)
        print size_format(total - used)
    elif args.display == "memmax":
        total = nvidia_attr(args.gpu, "TotalDedicatedGPUMemory", int)
        print size_format(total)
    elif args.display == "temp":
        print nvidia_attr(args.gpu, "GPUCoreTemp", int)

if __name__ == "__main__":
    main()
