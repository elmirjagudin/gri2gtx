#!/usr/bin/env python3

import sys
import struct
from os import path


def file_names():
    if len(sys.argv) < 2:
        print("usage: %s <gri-file>" % sys.argv[0])
        sys.exit(1)

    gri_file = sys.argv[1]
    name, _ = path.splitext(gri_file)
    gtx_file = name + ".gtx"

    return gri_file, gtx_file


def write_gtx_file(gtx_file, gri):
    print("creating '%s'" % gtx_file)

    # convert the grid table header from GRI style
    # to GTX flavor
    xorigin = gri.min_lat
    yorigin = gri.min_long
    xstep = gri.lat_step
    ystep = gri.long_step
    columns = int((gri.max_long - gri.min_long) / gri.long_step) + 1
    rows = int((gri.max_lat - gri.min_lat) / gri.lat_step) + 1

    with open(gtx_file, "wb") as f:
        # write table header
        f.write(struct.pack(">ddddii", xorigin, yorigin, xstep, ystep, rows,
                            columns))

        # write the table cels
        for y in range(rows):
            for x in range(columns):
                #
                # The GRI grid values rows starts at
                # the maximum latitude, where is
                # GTX rows start at min latitude, thus
                # we need to swap the rows order
                #
                i = (rows - 1 - y) * columns + x
                f.write(struct.pack(">f", gri.heights[i]))


#
# Simple GRI file parser
#
class GriFile:
    def __init__(self, gri_file):
        print("parsing '%s'" % gri_file)
        with open(gri_file) as f:
            # load the whole file into memory
            data = f.read()
            # 'strip out' all the white space and
            # parse the ASCII numbers as floats
            vals = [float(x) for x in data.split()]

            # store the first 6 number as table header parameters
            self.min_lat = vals[0]
            self.max_lat = vals[1]
            self.min_long = vals[2]
            self.max_long = vals[3]
            self.lat_step = vals[4]
            self.long_step = vals[5]

            # store the rest as heights data list
            self.heights = vals[6:]

    def __str__(self):
        return "lat (%s - %s) long (%s - %s) step %s %s" % \
            (self.min_lat, self.max_lat,
             self.min_long, self.max_long,
             self.lat_step, self.long_step)


def main():
    gri_file, gtx_file = file_names()
    write_gtx_file(gtx_file, GriFile(gri_file))


main()
