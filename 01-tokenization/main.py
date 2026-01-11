import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, world!"
tokens = enc.encode(text)

print("Tokens:", tokens)

decoded = enc.decode(tokens)
print("Decoded text:", decoded)