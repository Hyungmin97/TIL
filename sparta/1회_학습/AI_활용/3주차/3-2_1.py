from transformers import BertTokenizer, BertForSequenceClassification
from datasets import load_dataset
import torch
import numpy as np
from sklearn.metrics import accuracy_score

dataset = load_dataset("imdb")

test_dataset = dataset['test'].shuffle(seed=42).select(range(500))

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

#데이터셋에 tokenizing 진행
test_dataset = test_dataset.map(tokenize_function, batched=True)

test_dataset.set_format(type="torch", columns=['input_ids', 'attention_mask', 'label'])

model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

#모델을 평가 모드로 변경
model.eval()

#예측 및 평가
all_preds = []
all_labels = []

for batch in torch.utils.data.DataLoader(test_dataset, batch_size=8):
    with torch.no_grad():
        outputs = model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'])
    logits = outputs.logits
    preds = np.argmax(logits.cpu().numpy(), axis=1)
    all_preds.extend(preds)
    all_labels.extend(batch['label'].numpy())

#정확도 계산
accuracy = accuracy_score(all_labels, all_preds)
print(f'Accuracy without fine-tuning: {accuracy:.4f}')