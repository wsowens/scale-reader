ANTLR = java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool

default: build/ScaleListener.py

build/ScaleListener.py:
	$(ANTLR) -o build -Dlanguage=Python3 Scale.g4

clean:
	rm -rf build