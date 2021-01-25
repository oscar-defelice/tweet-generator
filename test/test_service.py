from tweegen.service import load_model, _split, generate, upload
from transformers import pipeline

def test_load_model():
    assert type(load_model()) == pipelines.text_generation.TextGenerationPipeline


def test_split():
    assert _split("a<|endoftext|>a") == ["a", "a"]


def test_generate():
    assert type(generate()) == list


# def test_upload():
