import sys
from antlr4 import *
from SerialLexer import SerialLexer
from SerialParser import SerialParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SerialLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SerialParser(stream)
    
 
if __name__ == '__main__':
    main(sys.argv)