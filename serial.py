import argparse
from antlr4 import *
from build.SerialLexer import SerialLexer
from build.SerialParser import SerialParser
from build.SerialVisitor import SerialVisitor
from build.SerialListener import SerialListener
from time import sleep
from os import environ

# set the environment variable to hide the pygame print statement
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


pygame.mixer.init()


SOUNDS = {}
for note in ["do", "re", "mi", "fa", "sol", "la", "ti"]:
    SOUNDS[note] = pygame.mixer.Sound("sounds/%s.wav" % note)

class TestVisitor(SerialVisitor):

    # Visit a parse tree produced by SerialParser#serial_file.
    def visitSong(self, ctx:SerialParser.SongContext):
        print("file")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SerialParser#chord.
    def visitChord(self, ctx:SerialParser.ChordContext):
        sounds = [SOUNDS[note.getText().lower()] for note in ctx.note()]
        for sound in sounds:
            sound.play()
        while pygame.mixer.get_busy():
            sleep(.1)
        return sounds


    # Visit a parse tree produced by SerialParser#note.
    def visitNote(self, ctx:SerialParser.NoteContext):
        return self.visitChildren(ctx)

# This class defines a complete listener for a parse tree produced by SerialParser.
class TestListener(SerialListener):

    # Enter a parse tree produced by SerialParser#chord.
    def enterChord(self, ctx:SerialParser.ChordContext):
        sounds = [SOUNDS[note.getText().lower()] for note in ctx.note()]
        for sound in sounds:
            sound.play()

    # Exit a parse tree produced by SerialParser#chord.
    def exitChord(self, ctx:SerialParser.ChordContext):
        while pygame.mixer.get_busy():
            sleep(.1)


def main(file_stream):
    if file_stream is not None:
        input_stream = FileStream(file_stream)
    else:
        input_stream = StdinStream()
    lexer = SerialLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SerialParser(stream)
    tree = parser.song()
    #visitor = TestVisitor()
    #return visitor.visit(tree)
    listener = TestListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)


arg_parser = argparse.ArgumentParser(description="Run .serial files.")
arg_parser.add_argument("file", nargs='?', help="File to sight read [default: stdin]")
 
if __name__ == '__main__':
    args = arg_parser.parse_args()
    main(args.file)