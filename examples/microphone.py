import retico_core
import time
from retico_core.audio import MicrophoneModule
from retico_core.debug import DebugModule
from retico_whisperasr import WhisperASRModule
from retico_ollama import OllamaModule, TerminalOutputModule

mic = MicrophoneModule()
asr = WhisperASRModule()
ollama = OllamaModule(model="llama3.1", mode="mic")
terminal_out = TerminalOutputModule()

mic.subscribe(asr)
asr.subscribe(ollama)
ollama.subscribe(terminal_out)

mic.run()
asr.run()
ollama.run()
terminal_out.run()

print("Network is running")
# input()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    mic.stop()
    asr.stop()
    ollama.stop()
    terminal_out.stop()