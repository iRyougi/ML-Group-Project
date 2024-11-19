import os
import json
from sklearn.model_selection import train_test_split
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# 数据预处理函数
def load_dataset(dataset_path):
    data = []
    labels = []
    for folder in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder)
        if os.path.isdir(folder_path):
            try:
                # 读取错误代码和正确代码
                with open(os.path.join(folder_path, f"{folder}_e.py"), "r") as f_err, \
                     open(os.path.join(folder_path, f"{folder}.py"), "r") as f_correct:
                    err_code = f_err.read()
                    correct_code = f_correct.read()
                    data.append((err_code, correct_code))
                    labels.append(1)  # 假设正确代码的标签为1
            except Exception as e:
                print(f"Error loading {folder}: {e}")
    return data, labels

# 特征提取与标注
def preprocess_data(data):
    processed_data = []
    for err_code, correct_code in data:
        # 这里假设每一行代码是一个输入单元
        for err_line, correct_line in zip(err_code.splitlines(), correct_code.splitlines()):
            processed_data.append({
                "input": err_line,
                "label": correct_line
            })
    return processed_data

# 加载数据
dataset_path = "path_to_dataset"  # 替换为实际路径
data, labels = load_dataset(dataset_path)
processed_data = preprocess_data(data)

# 分割训练集和测试集
train_data, test_data = train_test_split(processed_data, test_size=0.2, random_state=42)

# 使用 Transformer 模型
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["input"], padding="max_length", truncation=True)

train_encodings = tokenizer([d["input"] for d in train_data], truncation=True, padding=True, max_length=512)
test_encodings = tokenizer([d["input"] for d in test_data], truncation=True, padding=True, max_length=512)

# 转换为 PyTorch 数据集
import torch
class CodeDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = CodeDataset(train_encodings, [d["label"] for d in train_data])
test_dataset = CodeDataset(test_encodings, [d["label"] for d in test_data])

# 模型定义
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# 训练参数
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer
)

# 模型训练
trainer.train()

# 模型保存
model.save_pretrained("./code_indentation_model")
tokenizer.save_pretrained("./code_indentation_model")
