grammar Serial;

serial_file: chord? (ENDLINE chord)* ENDLINE? EOF?;

chord: note (SEP note)+;

note: DO | RE | MI | FA | SOL | LA | TI | DO ;

/* tokens for lexer */
DO: [dD][oO];
RE: [rR][eE];
MI: [mM][iI];
FA: [fF][aA];
SOL: [sS][oO][lL];
LA: [lL][aA];
TI: [tT][iI];

SEP: [ \t]+;

ENDLINE: '\r'?'\n';