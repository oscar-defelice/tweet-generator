import fire
from pathlib import Path
from transformers import AutoTokenizer
from transformers import Trainer, TrainingArguments, AutoModelWithLMHead
from transformers import TextDataset, DataCollatorForLanguageModeling

from tweegen import log
from tweegen import config as cfg

tokenizer = AutoTokenizer.from_pretrained(cfg.PRETRAINED_MODEL)

def _load_dataset():

    train_dataset = TextDataset(
          tokenizer=tokenizer,
          file_path=cfg.DATA,
          block_size=128)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )
    return train_dataset, data_collator

def _get_trainer():
    model = AutoModelWithLMHead.from_pretrained(cfg.PRETRAINED_MODEL)

    training_args = TrainingArguments(
                        output_dir= cfg.MODEL_DIR, #The output directory
                        overwrite_output_dir=True, #overwrite the content of the output directory
                        num_train_epochs=cfg.EPOCHS, # number of training epochs
                        per_device_train_batch_size=cfg.BATCH_SIZE, # batch size for training
                        eval_steps = cfg.STEPS, # Number of update steps between two evaluations.
                        save_steps=cfg.STEPS, # after # steps model is saved
                        warmup_steps=cfg.STEPS,# number of warmup steps for learning rate scheduler
                        )

    train_dataset, data_collator = _load_dataset()

    return Trainer(
                    model=model,
                    args=training_args,
                    data_collator=data_collator,
                    train_dataset=train_dataset,
                    )

@log("Model Training")
def train(name):
    path = Path(cfg.DATA_DIR) / name
    trainer = _get_trainer()
    trainer.train()
    trainer.save_model()

@log("Fake Tweets generating")
def _generate():
    model = pipeline('text-generation',
                    model = cfg.MODEL_DIR,
                    tokenizer = 'gpt2',
                    config = {'max_length': 280})
    text_lines = model(
                        cfg.INPUT_TEXT,
                        num_return_sequences = cfg.RETURN_SEQUENCES
                        )

    return text_lines


def generate():
    text_lines = _generate()
    for text_dict in text_lines:
        print(text_dict['generated_text'])
        print('\n')


if __name__ == "__main__":
    fire.Fire()
