# PhotoGrouper
更新時刻でファイルをフォルダに日付分類するやつ

## 使い方
フォルダを指定すると中のファイルを日付ごとに分類します

ファイルの更新時刻をもとにフォルダに分類されます

```bash
python3 grouper.py -h
usage: grouper.py [-h] [-o OFFSET_HOUR] PATH [PATH ...]

positional arguments:
  PATH                  image file path list

optional arguments:
  -h, --help            show this help message and exit
  -o OFFSET_HOUR, --offset-hour OFFSET_HOUR
                        offset hours
```

* -oオプションを使用すると日付を超えていても同日に含めることができます。4を指定すると朝4時までは前日に含まれます。
* -o オプションはデフォルトで6が指定されています

Windows環境ではgrouper.batにフォルダをドラッグすると自動で分類されます。