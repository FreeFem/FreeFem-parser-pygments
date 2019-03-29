[FreeFEM](https://freefem.org/) parser for `pygments`

This parser is used to build the [FreeFem-doc](https://github.com/FreeFem/FreeFem-doc)

## Usage

This file must be added, for example under Ubuntu 16.04, in:
```bash
/usr/lib/python2.7/site-packages/pygments/lexers
```
And run:
```bash
cd /usr/lib/python2.7/site-packages/pygments/lexers/ && sudo python _mapping.py
```

On arch, the pygments path is:
```bash
/usr/lib/python3.6/site-packages/pygments/lexers
```

On MacOS, the pygments path is:
```bash
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pygments/lexers
```

## Authors

| Author | Github | Website |
|:----|:----|:----|
| Franck Lahaye | https://github.com/franckl |  |
| Simon Garnotel | https://github.com/sgarnotel  |  |
