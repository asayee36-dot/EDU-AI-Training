# Session 3 — Google Colab & Hugging Face

**Day 1 · 13:45 – 15:15**

In this session you will run real AI code in your browser — no installation — and use a
model that somebody else already trained.

---

## 1. Open Google Colab

**Colab** is a free service from Google. Your code runs on Google's computers, not yours.

1. Go to **<https://colab.research.google.com>**
2. Sign in with a **Google account**
3. Click **New notebook**

You now have an empty notebook. Each grey box is a **cell** where you type code.

### Opening the course notebook instead

1. **File → Open notebook**
2. Click the **GitHub** tab
3. Paste: `keduog/EDU-AI-Training`
4. Click the notebook you want

---

## 2. Change the runtime (turn on the GPU)

A **GPU** makes AI code run much faster. Colab gives you one for free.

1. Click **Runtime** in the top menu
2. Click **Change runtime type**
3. Under *Hardware accelerator*, choose **T4 GPU**
4. Click **Save**

The notebook restarts. That is normal.

**To check it worked**, type this in a cell and run it:

```python
!nvidia-smi
```

If you see a table of GPU information, you have a GPU.
If you see *command not found*, you are still on CPU — everything below still works,
just a little slower.

---

## 3. Run a cell

| What you want | How to do it |
|---|---|
| Run one cell | Click it, then press **Shift + Enter** |
| Run all cells | **Runtime → Run all** |
| Add a new cell | Click **+ Code** at the top |
| Stop a running cell | Click the **■** stop button |
| Start over | **Runtime → Restart session** |

While a cell is running you see a spinning circle on its left.
When it finishes, the output appears below the cell.

**Try it.** Type this in the first cell and press Shift+Enter:

```python
print("Hello from Google Colab!")
```

---

## 4. Load a model from Hugging Face

**Hugging Face** (<https://huggingface.co>) is a website that stores AI models that are
already trained. You download one and use it — you do not train anything yourself.

### Step 1 — install the library

In a new cell:

```python
!pip -q install transformers
```

Press Shift+Enter. This takes about 30 seconds. Do this once per session.

### Step 2 — load the model

In the next cell:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

print("Model is ready.")
```

The first time, this downloads about 250 MB. That download **is** the model — the result
of somebody else's expensive training.

---

## 5. Run inference

**Inference** means using a trained model to get an answer.

In the next cell:

```python
result = classifier("The training today was excellent!")
print(result)
```

Output:

```
[{'label': 'POSITIVE', 'score': 0.9998}]
```

- **label** — what the model decided
- **score** — how confident it is, from 0 to 1

### Try several sentences at once

```python
sentences = [
    "The training today was excellent!",
    "I am tired and the room is too hot.",
    "Our team will win this exercise!",
]

for sentence in sentences:
    answer = classifier(sentence)[0]
    print(answer["label"], round(answer["score"], 2), "-", sentence)
```

Output:

```
POSITIVE 1.0 - The training today was excellent!
NEGATIVE 1.0 - I am tired and the room is too hot.
POSITIVE 0.99 - Our team will win this exercise!
```

---

## 6. The complete code

Copy this into a Colab notebook. Four cells, top to bottom.

**Cell 1**
```python
!pip -q install transformers
```

**Cell 2**
```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print("Model is ready.")
```

**Cell 3**
```python
sentences = [
    "The training today was excellent!",
    "I am tired and the room is too hot.",
    "Our team will win this exercise!",
]

for sentence in sentences:
    answer = classifier(sentence)[0]
    print(answer["label"], round(answer["score"], 2), "-", sentence)
```

**Cell 4 — your turn**
```python
my_sentences = [
    "Write your own sentence here.",
    "And another one.",
]

for sentence in my_sentences:
    answer = classifier(sentence)[0]
    print(answer["label"], round(answer["score"], 2), "-", sentence)
```

There is a ready-made notebook in this folder: **`session3_demo.ipynb`**

---

## 7. Try a different task

The same `pipeline` does other jobs. Just change the name inside the brackets.

**Question answering:**

```python
qa = pipeline("question-answering")

context = "PaLM has 540 billion parameters and was trained on TPU pods for several weeks."

print(qa(question="How many parameters does PaLM have?", context=context))
```

**Text generation:**

```python
writer = pipeline("text-generation", model="gpt2")

print(writer("Artificial intelligence is", max_length=30)[0]["generated_text"])
```

---

## 8. Save your notebook

Colab does **not** save to GitHub automatically. When you finish:

1. **File → Save a copy in GitHub**
2. Choose your repository: `YOUR-USERNAME/EDU-AI-Training`
3. Write a commit message: `Add Session 3 notebook`
4. Click **OK**

Now the notebook is in your GitHub, with your outputs saved inside it.

---

## If something goes wrong

**`No module named 'transformers'`**
You skipped Cell 1. Run `!pip -q install transformers` first.

**The download is very slow**
It is a few hundred megabytes the first time. After that it is instant.

**Everything stopped working after a break**
Colab disconnects if you leave it idle. Just run the cells again from the top.

**My code disappeared**
You closed the tab without saving. Always use **File → Save a copy in GitHub**.

---

## Checklist

- [ ] I opened Google Colab and signed in
- [ ] I changed the runtime to **T4 GPU**
- [ ] I ran a cell with **Shift + Enter**
- [ ] I installed `transformers`
- [ ] I loaded a model with `pipeline("sentiment-analysis")`
- [ ] I ran inference on my own sentences
- [ ] I saved the notebook to my GitHub
