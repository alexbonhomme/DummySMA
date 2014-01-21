#! /usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Created on 19 janv. 2014

@author: Alexandre Bonhomme
'''
from wator.WatorFrame import WatorFrame
from wator.WatorSMA import WatorSMA
import logging as log

log.basicConfig(level = log.WARN)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(dest = "grid_rows",
                        help = "number of rows in the grid",
                        type = int)
    parser.add_argument(dest = "grid_cols",
                        help = "number of columns in the grid",
                        type = int)
    parser.add_argument(dest = "grid_box_size",
                        help = "size of a box in the grid",
                        type = int)
    parser.add_argument(dest = "waiting_time_millis",
                        help = "time in milliseconds between each cycle",
                        type = int)
    parser.add_argument("--fishes",
                        dest = "fishes",
                        help = "initial number of fishes",
                        type = int,
                        default = 100)
    parser.add_argument("--fishes_breed",
                        dest = "fishes_breed",
                        help = "breeding age of fishes",
                        type = int,
                        default = 2)
    parser.add_argument("--sharks",
                        dest = "sharks",
                        help = "initial number of sharks",
                        type = int,
                        default = 25)
    parser.add_argument("--sharks_breed",
                        dest = "sharks_breed",
                        help = "breeding age of sharks",
                        type = int,
                        default = 5)
    parser.add_argument("--sharks_starv",
                        dest = "sharks_starv",
                        help = "starvation time of sharks",
                        type = int,
                        default = 3)
    parser.add_argument("-c",
                        "--cycles",
                        dest = "cycles",
                        help = "number of cycles",
                        type = int)
    parser.add_argument("-o",
                        dest = "output",
                        help = "FILE to write data",
                        metavar = "FILE")
    args = parser.parse_args()

    # hack here we consider that "rows" = the x size (e.i. the width)
    GRID_ROWS, GRID_COLS = args.grid_cols, args.grid_rows
    BOX_SIZE = args.grid_box_size
    WIN_WIDTH, WIN_HEIGHT = GRID_ROWS * BOX_SIZE, GRID_COLS * BOX_SIZE

    sma = WatorSMA(GRID_COLS, GRID_ROWS, logFilename = args.output)
    sma.initFishes(args.fishes, args.fishes_breed)
    sma.initSharks(args.sharks, args.sharks_breed, args.sharks_starv)

    frame = WatorFrame(WIN_HEIGHT, WIN_WIDTH, BOX_SIZE, sma)
    if args.cycles:
        frame.repeat(args.cycles, args.waiting_time_millis, sma.runOnce)
    else:
        frame.after(args.waiting_time_millis, sma.runOnce)

    frame.run()
