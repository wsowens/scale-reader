import sys
from antlr4 import *
from build.SerialLexer import SerialLexer
from build.SerialParser import SerialParser
from build.SerialVisitor import SerialVisitor
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


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SerialLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SerialParser(stream)
    tree = parser.song()

    visitor = TestVisitor()
    return visitor.visit(tree)

    
 
if __name__ == '__main__':
    main(sys.argv)
