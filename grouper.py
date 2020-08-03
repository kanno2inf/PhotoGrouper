#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser
from datetime import datetime
from os.path import isdir, join


def main(argv):
    parser = ArgumentParser()
    parser.add_argument('paths', metavar='PATH', nargs='+', help="image file path list")
    parser.add_argument('-o', '--offset-hour', type=int, default=6, help="offset hours")
    opt = parser.parse_args(argv)
    offset_hours = opt.offset_hour * 60 * 60

    for path in opt.paths:
        if not isdir(path):
            continue
        print(path)
        for filename in os.listdir(path):
            fpath = join(path, filename)
            mtime = os.stat(fpath).st_mtime - offset_hours
            mtime_date = datetime.fromtimestamp(mtime)
            day_folder = mtime_date.strftime('%Y%m%d')
            # フォルダを作成して分類
            os.makedirs(day_folder, exist_ok=True)
            dst_path = join(day_folder, filename)
            print(dst_path)
            os.rename(fpath, dst_path)


if __name__ == '__main__':
    main(sys.argv[1:])
