grammar Serial;

serial_file: (line ';')+ EOF?;

line: word (WS word)+;

word: 'foo' | 'bar' | 'baz';

/* tokens for lexer */
WS: [\t ]+;