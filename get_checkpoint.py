#! /usr/bin/env python

import argparse
import tensorflow as tf
import shutil

"""
Get a checkpoint from the checkpoints dir using the provided
condition.

Currently only 'latest' checkpoint can be retrieved
TODO: Add other choices
"""

# Parse command line args
# ==================================================
parser = argparse.ArgumentParser(description='Get particular checkpoint from dir')

parser.add_argument('-i', '--checkpoints_dir', required=True,
    help='Checkpoints dir')
parser.add_argument('-c', '--choice', required=True, default='latest', 
    choices=['latest'], help='Method to choose checkpoint from dir')
parser.add_argument('-o', '--checkpoint', required=True,
    help='Path to chosen checkpoint')

args = parser.parse_args()

# Convert args to dict
vargs = vars(args)

print("\nArguments:")
for arg in vargs:
    print("{}={}".format(arg, getattr(args, arg)))

if args.choice == 'latest':
    try:
        checkpoint_file = tf.train.latest_checkpoint(args.checkpoints_dir)
        shutil.copy2(checkpoint_file, args.checkpoint)
    except Exception as exc:
        raise Exception("Could not locate or copy latest checkpoint. Error: {}".format(exc))
else:
    raise NotImplementedError("Choice {} is not implemented yet".format(args.choice))

print("\n{} checkpoint written to {}".format(args.choice, args.checkpoint))