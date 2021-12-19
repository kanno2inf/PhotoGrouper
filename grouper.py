#!/usr/bin/env python
import os
import re
import sys
from argparse import ArgumentParser
from datetime import datetime
from os.path import isdir, join, abspath, splitext, basename

VRC_PICTURE_FOLDER_MATCH = re.compile(r'\D+\d\d\d\d-\d+$')


def group_by_mtime(dir_path, file_path, offset_hours):
    if isdir(file_path):
        if not VRC_PICTURE_FOLDER_MATCH.match(file_path):
            return
        for filename in os.listdir(file_path):
            group_by_mtime(dir_path, join(file_path, filename), offset_hours)
        return

    _, ext = splitext(file_path)
    if ext[1:] not in ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'bmp']:
        return  # 画像ファイルでない

    mtime = os.stat(file_path).st_mtime - offset_hours
    mtime_date = datetime.fromtimestamp(mtime)

    # 日付フォルダを生成
    day_folder = mtime_date.strftime('%Y%m%d')
    day_folder_path = join(dir_path, day_folder)
    # フォルダを作成して分類
    os.makedirs(day_folder_path, exist_ok=True)
    dst_path = join(day_folder_path, basename(file_path))
    print(dst_path)
    os.rename(file_path, dst_path)


def group_by_mtime_in_dir(dir_path, offset_hours):
    if not isdir(dir_path):
        return
    for filename in os.listdir(dir_path):
        file_path = join(dir_path, filename)
        group_by_mtime(dir_path, file_path, offset_hours)


def main(argv):
    parser = ArgumentParser()
    parser.add_argument('paths', metavar='PATH', nargs='+', help="image file path list")
    parser.add_argument('-o', '--offset-hour', type=int, default=6, help="offset hours")
    opt = parser.parse_args(argv)
    offset_hours = opt.offset_hour * 60 * 60

    for dir_path in opt.paths:
        group_by_mtime_in_dir(abspath(dir_path), offset_hours)


if __name__ == '__main__':
    main(sys.argv[1:])
