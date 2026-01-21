# japanese_filter.py
import fugashi

# Reuse the Tagger (it has initialization cost)
tagger = fugashi.Tagger()

# UniDic POS examples look like:
#   助詞-格助詞, 助動詞, 補助記号-句点, etc. [page:2]
DROP_POS_PREFIXES = (
    "助詞",      # particles
    "助動詞",    # auxiliary verbs
    "補助記号",  # punctuation/symbols
)

def content_tokens(text: str):
    kept = []
    for tok in tagger(text):
        pos = tok.feature.pos  # UniDic POS string [page:2]
        if any(pos.startswith(p) for p in DROP_POS_PREFIXES):
            continue
        kept.append(tok.surface)  # surface form [page:2]
    return kept

if __name__ == "__main__":
    text = "AI（人工知能）とは、人間の知能や行動を再現したコンピュータシステム、またはソフトウェアの総称です。"
    print(content_tokens(text))
