#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser
from datetime import datetime
from os.path import isdir, join, abspath, splitext


def main(argv):
    parser = ArgumentParser()
    parser.add_argument('paths', metavar='PATH', nargs='+', help="image file path list")
    parser.add_argument('-o', '--offset-hour', type=int, default=6, help="offset hours")
    opt = parser.parse_args(argv)
    offset_hours = opt.offset_hour * 60 * 60

    for path in opt.paths:
        if not isdir(path):
            continue
        for filename in os.listdir(path):
            _, ext = splitext(filename)
            if ext[1:] not in ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'bmp']:
                continue
            fpath = join(path, filename)
            mtime = os.stat(fpath).st_mtime - offset_hours
            mtime_date = datetime.fromtimestamp(mtime)
            day_folder = mtime_date.strftime('%Y%m%d')
            day_folder_path = join(abspath(path), day_folder)
            # フォルダを作成して分類
            os.makedirs(day_folder_path, exist_ok=True)
            dst_path = join(day_folder_path, filename)
            print(dst_path)
            os.rename(fpath, dst_path)


if __name__ == '__main__':
    main(sys.argv[1:])
