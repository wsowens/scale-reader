#!/usr/bin/env python3
import argparse
from antlr4 import *
from build.ScaleLexer import ScaleLexer
from build.ScaleParser import ScaleParser
from build.ScaleListener import ScaleListener
from time import sleep
from os import environ

# set the environment variable to hide the pygame print statement
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


pygame.mixer.init()


SOUNDS = {}
for note in ["do", "re", "mi", "fa", "sol", "la", "ti"]:
    SOUNDS[note] = pygame.mixer.Sound("sounds/%s.wav" % note)

# This class defines a complete listener for a parse tree produced by ScaleParser.
class TestListener(ScaleListener):

    # Enter a parse tree produced by ScaleParser#chord.
    def enterChord(self, ctx:ScaleParser.ChordContext):
        sounds = [SOUNDS[note.getText().lower()] for note in ctx.note()]
        for sound in sounds:
            sound.play()

    # Exit a parse tree produced by ScaleParser#chord.
    def exitChord(self, ctx:ScaleParser.ChordContext):
        while pygame.mixer.get_busy():
            sleep(.1)


def main(file_stream):
    if file_stream is not None:
        input_stream = FileStream(file_stream)
    else:
        input_stream = StdinStream()
    lexer = ScaleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ScaleParser(stream)
    tree = parser.song()
    #visitor = TestVisitor()
    #return visitor.visit(tree)
    listener = TestListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


arg_parser = argparse.ArgumentParser(description="Run .scale files. Created by William Owens and licensed under the Apache License version 2.0.")
arg_parser.add_argument("file", nargs='?', help="File to sight read [default: stdin]")
 
if __name__ == '__main__':
    args = arg_parser.parse_args()
    main(args.file)
