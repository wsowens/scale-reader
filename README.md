# Scale Reader
For reading musical files. (Name subject to change.)

## Getting Started
This project depends on `antlr4` for parsing files and `pygame` for producing media. (`pygame` essentially functions as a wrapper for SDL.)

Install the packages below for 
```sh
pip install antlr4-python3-runtime
pip install pygame
```
You must install `antlr4` to generate the parser code. Refer to [their documentation](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md) for instructions.

Once you have `antlr4` set up as described above, you can run simply run `make`. If your system does not have `make` installed you can run the command below:
```
java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:CLASSPATH" org.antlr.v4.Tool -o build -Dlanguage=Python3 Scale.g4`
```

Then, simply run `python scale.py` to start reading files!

## License
This project is licensed under the Apache License version 2.0. See [LICENSE.md](./LICENSE.md) for details.
