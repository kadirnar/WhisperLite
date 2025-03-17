import whisperlite
import time
model = whisperlite.load_model("turbo")
start = time.time()
result = model.transcribe("test_v0.mp3")
print(result["text"])
print(f'{time.time() - start:.2f} seconds')