ANTLR = java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool

default: build/SerialVisitor.py

build/SerialVisitor.py:
	$(ANTLR) -o build -Dlanguage=Python3 Serial.g4 -no-listener -visitor

clean:
	rm -rf build