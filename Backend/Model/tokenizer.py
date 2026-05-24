class Tokenizer:
    def __init__(self):
        self.char_to_idx = {}
        self.idx_to_char = {}
        self.vocab_size = 0

    def build_vocab(self, text):
        unique_chars = sorted(set(text))
        self.char_to_idx = {ch: i for i, ch in enumerate(unique_chars)}
        self.idx_to_char = {i: ch for i, ch in enumerate(unique_chars)}
        self.vocab_size = len(unique_chars)
        print(f"Vocabulary size: {self.vocab_size}")

    def encode(self, text):
        return [self.char_to_idx[ch] for ch in text]

    def decode(self, indices):
        return ''.join([self.idx_to_char[i] for i in indices])


# Test it
if __name__ == "__main__":
    tokenizer = Tokenizer()
    
    sample_text = "hello this is my notes simplifier"
    tokenizer.build_vocab(sample_text)
    
    encoded = tokenizer.encode("hello")
    print(f"Encoded: {encoded}")
    
    decoded = tokenizer.decode(encoded)
    print(f"Decoded: {decoded}")