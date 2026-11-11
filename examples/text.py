import time
from retico_ollama import OllamaModule, TerminalInputModule, TerminalOutputModule

terminal_in = TerminalInputModule()
ollama = OllamaModule(model="llama3.2:1b")
terminal_out = TerminalOutputModule()

terminal_in.subscribe(ollama)
ollama.subscribe(terminal_out)

print("starting")

terminal_in.run()
ollama.run()
terminal_out.run()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    terminal_in.stop()
    ollama.stop()
    terminal_out.stop()