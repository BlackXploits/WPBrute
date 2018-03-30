# WordPress Bruteforce Login

### Install requirements
```
pip install -r requirements.txt
```

## Features
* 1 Million Wordlist Added
* Standard mode or xml-rpc brute force mode
* http and https protocols supported
* Big wordlist size supported
* Multithreading

### Usage
  * Standard Mode:
```
python wpbrute.py -s -t [TARGET] -u [USERNAME] -w [WORDLIST] [--timeout TIMEOUT VALUE]
```
  * xml-rpc Mode:
```
 python wpbrute.py -x [-t TARGET] [-u USERNAME] [-w WORDLIST] [--timeout TIMEOUT VALUE]
```

### Screenshot
![wp-brute](https://user-images.githubusercontent.com/35635224/38136385-3c26dcb4-3448-11e8-80ca-c676ec02e2f1.png)
