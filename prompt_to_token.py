import sys
import sentencepiece as spm

TOKENIZER_MODEL = "tokenizer.model" # the llama sentencepiece tokenizer model
sp = spm.SentencePieceProcessor(model_file=TOKENIZER_MODEL)

ids = sp.encode(sys.argv[1])

with open(sys.argv[2], 'w') as f:
    f.write(f"{len(ids)}\n")
    for i in ids:
        f.write(f"{i}\n")