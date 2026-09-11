from TokenEmbedding import TokenEmbedding
import torch
import torch.nn as nn
import math
from PositionalEncoding import PositionalEncoding
class InputEmbedding(nn.Module):
    def __init__(self, vocab_size, d_model, max_len, dropout):
        super().__init__()
        self.TokenEmb = TokenEmbedding(vocab_size, d_model)
        self.PosEnc = PositionalEncoding(d_model, max_len, dropout)
    def forward(self, x:torch.Tensor) -> torch.Tensor:
        return self.PosEnc(self.TokenEmb(x))
    
if __name__ == "__main__":

    vocab_size = 10000
    d_model = 512
    seq_len = 20
    batch_size = 2

    embedder = InputEmbedding(vocab_size, d_model, max_len = 5000, dropout=0.1)
    src = torch.randint(0, vocab_size, (batch_size, seq_len))
    output = embedder(src)
    print(output)