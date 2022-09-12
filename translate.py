#!/usr/bin/python3

__author__ = "Richard Jarry"
__version__ = "0.0.2"

import fire
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers.pipelines import pipeline


def translate(text: str, source: str, target: str, **kwargs):

    """Translates input text offline using a Transformer Seq2SeqLM."""

    model_name = kwargs.get("model", "facebook/nllb-200-distilled-600M")

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    p = pipeline(
        "translation",
        model=model,
        tokenizer=tokenizer,
        src_lang=source,
        tgt_lang=target,
        **kwargs)

    # TODO: Add verbose option with progressbar

    return p(text)

# TODO: Add ISO (?) language code dictionary

if __name__ == "__main__":
    fire.Fire(translate)
