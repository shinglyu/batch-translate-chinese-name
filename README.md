# Batch convert Chinese name to English (Pinyin)

## Usage

```
pip3 install pinyin
python3 convert input.txt > output.txt
```

## Input file format
Input file must be a list of names, each name is a separate line. You can mix Chinese names with English names, but English names will not be modified.

* Input:

```
王小明
李大華
Jason Smith
```

* Output without `--rearrange`:

```
Wang Xiao Ming
Li Da Hua
Jason Smith
```

* Output with `--rearragne`:

```
Xiao-ming Wang
Da-hua Li
Jason Smith
```

## Options

```
optional arguments:
  -h, --help       show this help message and exit
  --rearrange, -r  Rearrange into <first-name> <last name> format
```

* `--rearrange` or `-r`
  * With `-r`: 王小明 => Xiao-ming Wang
  * Without `-r`: 王小明 => Wan xiao ming
