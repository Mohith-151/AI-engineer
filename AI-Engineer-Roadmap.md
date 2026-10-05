# AI Engineer Roadmap: 60-Day Checklist

**Days 1-40 = core roadmap. Days 41-60 = extension (job-ready push).**
Tick a box by changing `[ ]` to `[x]` (or click it on GitHub).

## How this works

- **Hours:** 4h/day on Days 1-14, **6h/day from Day 15**.
- **70/30 rule:** 4h day = ~2h50 practical + ~1h10 theory. 6h day = ~4h10 practical + ~1h50 theory.
- **Rule 1:** Write the code yourself first. Ask AI only to explain errors or review your code afterwards.
- **Rule 2:** Commit to GitHub every day, even a small commit.
- **Rule 3:** Write your daily log (use `daily-log-template.md`) in the last 10-15 minutes. Use your own words.
- **Rule 4:** Every 7th day (7, 14, 21, ...) also write a weekly summary in `weekly/week-XX.md`.
- **No GPU?** Use Google Colab or Kaggle notebooks for deep learning. Your Ryzen laptop is enough for everything else.
- **Suggested day order:** Theory first (fresh mind) -> practical blocks -> log + commit.

### Suggested repo structure

```
ai-engineer-journey/
├── README.md          # progress overview + links to best projects
├── ROADMAP.md         # this checklist
├── daily-logs/        # day-01.md ... day-60.md
├── weekly/            # week-01.md ...
├── notebooks/         # .ipynb files (Colab: File -> Save a copy in GitHub)
└── projects/          # mini-project-1 ... capstone
```

Commit message style: `Day 07: EDA mini-project + log`

---

# PHASE 1: Python, Data, Tools (Days 1-7) | 4h/day

### Day 1: Python data structures + Git setup
- [ ] 🛠 Rewrite `count_words(text)` from memory (no AI). Do 15 dict/list/function exercises. Install Git, create repo `ai-engineer-journey`, make your first commit.
- [ ] 📖 Python data structures (list, tuple, dict, set). How Git works (commit, push).
- [ ] 🎯 Repo live with README + `daily-logs/day-01.md`
- [ ] 📝 Log written + committed

### Day 2: OOP + calling APIs
- [ ] 🛠 Build a `DataCleaner` class (`__init__`, `drop_nulls`, `strip_text`...). Call a public API with `requests` and parse the JSON.
- [ ] 📖 OOP: `class`, `__init__`, `self`. HTTP basics (GET, status codes, JSON).
- [ ] 🎯 Working class + working API script in repo
- [ ] 📝 Log written + committed

### Day 3: NumPy and matrices
- [ ] 🛠 NumPy arrays and broadcasting. Write matrix multiplication by hand with loops, then compare with `@`. Predict the output shape of 10 operations *before* running them.
- [ ] 📖 Vectors, matrices, shapes, dot product.
- [ ] 🎯 Notebook with your hand-written matmul matching NumPy
- [ ] 📝 Log written + committed

### Day 4: pandas for messy data
- [ ] 🛠 Clean a messy dataset: missing values, duplicates, dtypes, merge/join, groupby.
- [ ] 📖 Handling missing data (drop vs impute). Tidy data.
- [ ] 🎯 Cleaned dataset + cleaning notebook
- [ ] 📝 Log written + committed

### Day 5: EDA and statistics
- [ ] 🛠 EDA on a new Kaggle dataset: histograms, boxplots, correlation heatmap (matplotlib/seaborn).
- [ ] 📖 Mean, median, mode, std, outliers. When median beats mean.
- [ ] 🎯 5 written insights from the data
- [ ] 📝 Log written + committed

### Day 6: SQL + Git branching
- [ ] 🛠 SQLite: write 20 queries yourself (SELECT, WHERE, GROUP BY, JOIN). Create a Git branch, merge it, resolve one conflict.
- [ ] 📖 Relational DB basics: primary key, foreign key.
- [ ] 🎯 `queries.sql` file in repo
- [ ] 📝 Log written + committed

### Day 7: Mini-project 1
- [ ] 🛠 Full EDA notebook on a fresh dataset + README with findings, pushed to GitHub.
- [ ] 📖 Review week: redo the quiz questions you missed. Write a weak-spot list.
- [ ] 🎯 **Mini-project 1 done**
- [ ] 📝 Log + weekly summary (`week-01.md`) committed

---

# PHASE 2: Classical ML Properly (Days 8-14) | 4h/day

### Day 8: Gradient descent
- [ ] 🛠 Gradient descent from scratch (NumPy) to fit a line. Plot the loss curve. Try 3 learning rates.
- [ ] 📖 Derivative, gradient, learning rate (3Blue1Brown / Khan Academy videos).
- [ ] 🎯 Loss-curve plot showing learning-rate effects
- [ ] 📝 Log written + committed

### Day 9: Linear regression + loss functions
- [ ] 🛠 Linear regression from scratch vs sklearn. Evaluate with MSE, R², MAE.
- [ ] 📖 Loss functions (MSE vs MAE).
- [ ] 🎯 Notebook comparing scratch vs sklearn
- [ ] 📝 Log written + committed

### Day 10: Classification metrics
- [ ] 🛠 Logistic regression. Confusion matrix, precision, recall, F1, ROC-AUC.
- [ ] 📖 Probability basics, sigmoid, why accuracy lies.
- [ ] 🎯 Metrics report on one dataset
- [ ] 📝 Log written + committed

### Day 11: Fix your insurance project
- [ ] 🛠 Redo the insurance project: correct regression metrics, 5-fold cross-validation, Ridge/Lasso. Compare with your old result.
- [ ] 📖 Bias-variance, overfitting, regularization.
- [ ] 🎯 "Before vs after" section in the README
- [ ] 📝 Log written + committed

### Day 12: Tree models and boosting
- [ ] 🛠 Random Forest and XGBoost. Tune with GridSearch/Optuna. Plot feature importance.
- [ ] 📖 Bagging vs boosting.
- [ ] 🎯 Tuned model + comparison table
- [ ] 📝 Log written + committed

### Day 13: Pipelines and imbalance
- [ ] 🛠 sklearn `Pipeline` + `ColumnTransformer`. Stratified split, class weights, SMOTE on a fraud dataset.
- [ ] 📖 Data leakage, class imbalance.
- [ ] 🎯 Leak-free pipeline notebook
- [ ] 📝 Log written + committed

### Day 14: Mini-project 2
- [ ] 🛠 End-to-end imbalanced classifier (pipeline, CV, proper metrics, README). Practice KMeans + PCA.
- [ ] 📖 Unsupervised learning.
- [ ] 🎯 **Mini-project 2 done** (you can start small freelance gigs: data cleaning, EDA, tabular models)
- [ ] 📝 Log + weekly summary (`week-02.md`) committed

> ⏫ **From Day 15 you study 6h/day.**

---

# PHASE 3: Deep Learning (Days 15-26) | 6h/day

### Day 15: Neural net from scratch
- [ ] 🛠 Tiny neural network in NumPy: forward pass, loss, one backprop step by hand.
- [ ] 📖 Neurons, activations (ReLU, sigmoid), backprop idea.
- [ ] 🎯 Working forward + backward pass
- [ ] 📝 Log written + committed

### Day 16: PyTorch basics
- [ ] 🛠 PyTorch tensors and autograd. Write your own training loop (no AI-generated code) on a Colab GPU.
- [ ] 📖 Chain rule, computation graph.
- [ ] 🎯 Training loop that you can explain line by line
- [ ] 📝 Log written + committed

### Day 17: MLP on MNIST
- [ ] 🛠 MLP on MNIST with DataLoader, batches, epochs, Adam. Plot train vs validation loss.
- [ ] 📖 Optimizers (SGD, momentum, Adam), learning-rate effects.
- [ ] 🎯 Accuracy > 97% with plots
- [ ] 📝 Log written + committed

### Day 18: Fight overfitting
- [ ] 🛠 Add dropout, weight decay, early stopping, data augmentation. Compare the curves.
- [ ] 📖 Regularization in deep learning.
- [ ] 🎯 Before/after overfitting plots
- [ ] 📝 Log written + committed

### Day 19: CNNs
- [ ] 🛠 CNN on Fashion-MNIST or CIFAR-10.
- [ ] 📖 Convolutions, pooling, receptive field.
- [ ] 🎯 CNN beating your MLP
- [ ] 📝 Log written + committed

### Day 20: Transfer learning
- [ ] 🛠 Fine-tune a pretrained ResNet on a custom Kaggle image dataset.
- [ ] 📖 Transfer learning (freeze vs fine-tune).
- [ ] 🎯 Fine-tuned model + results table
- [ ] 📝 Log written + committed

### Day 21: Mini-project 3
- [ ] 🛠 Image classifier with a Gradio demo on Hugging Face Spaces. Look at 20 wrong predictions and write what you notice.
- [ ] 📖 Error analysis.
- [ ] 🎯 **Mini-project 3 done** (live demo link in README)
- [ ] 📝 Log + weekly summary (`week-03.md`) committed

### Day 22: Text and embeddings
- [ ] 🛠 Tokenize with a Hugging Face tokenizer. Build a TF-IDF + logistic regression baseline, then an embedding-based classifier.
- [ ] 📖 Tokens, embeddings.
- [ ] 🎯 Two text classifiers compared
- [ ] 📝 Log written + committed

### Day 23: Self-attention
- [ ] 🛠 Implement self-attention in PyTorch (~30 lines).
- [ ] 📖 Attention, transformers (read "The Illustrated Transformer").
- [ ] 🎯 Working attention module with shape comments
- [ ] 📝 Log written + committed

### Day 24: Fine-tune DistilBERT
- [ ] 🛠 Fine-tune DistilBERT on Colab with Hugging Face.
- [ ] 📖 Pretraining vs fine-tuning.
- [ ] 🎯 Fine-tuned model with metrics
- [ ] 📝 Log written + committed

### Day 25: Experiment tracking
- [ ] 🛠 Add W&B or TensorBoard tracking. Push the model to the Hugging Face Hub with a model card.
- [ ] 📖 Reproducibility, random seeds, model cards.
- [ ] 🎯 Public model on HF Hub
- [ ] 📝 Log written + committed

### Day 26: Mini-project 4
- [ ] 🛠 Fine-tuned text classifier + demo app.
- [ ] 📖 Review and catch-up buffer: revisit anything shaky from Days 15-25.
- [ ] 🎯 **Mini-project 4 done**
- [ ] 📝 Log written + committed

---

# PHASE 4: LLMs and Deployment (Days 27-33) | 6h/day

### Day 27: LLM APIs
- [ ] 🛠 Call an LLM API from Python (free tier). Keep keys in `.env`. Handle errors and rate limits.
- [ ] 📖 Tokens, context window, temperature.
- [ ] 🎯 Script that works without exposing your key (check `.gitignore`!)
- [ ] 📝 Log written + committed

### Day 28: Structured output and tools
- [ ] 🛠 JSON outputs, tool calling, CLI chatbot with memory.
- [ ] 📖 Prompt patterns.
- [ ] 🎯 CLI chatbot in repo
- [ ] 📝 Log written + committed

### Day 29: Vector search
- [ ] 🛠 Embeddings + vector search with FAISS or Chroma. Try 3 chunk sizes.
- [ ] 📖 Cosine similarity, approximate nearest neighbours.
- [ ] 🎯 Search that returns relevant chunks
- [ ] 📝 Log written + committed

### Day 30: RAG app
- [ ] 🛠 Build "chat with your PDFs". Write 15 test questions and score the answers.
- [ ] 📖 RAG vs fine-tuning.
- [ ] 🎯 Working RAG app + test score (you can now take RAG/chatbot gigs)
- [ ] 📝 Log written + committed

### Day 31: Serve a model
- [ ] 🛠 FastAPI endpoint serving one of your earlier models. Validate with Pydantic. Test through Swagger/curl.
- [ ] 📖 REST, request/response.
- [ ] 🎯 `/predict` endpoint working
- [ ] 📝 Log written + committed

### Day 32: Docker + deploy
- [ ] 🛠 Write a Dockerfile, build and run locally, deploy to Render/Railway/HF Spaces.
- [ ] 📖 Containers: image vs container.
- [ ] 🎯 Live public URL
- [ ] 📝 Log written + committed

### Day 33: Mini-project 5
- [ ] 🛠 Deployed RAG app or model API with a simple front end.
- [ ] 📖 Review week.
- [ ] 🎯 **Mini-project 5 done**
- [ ] 📝 Log written + committed

---

# PHASE 5: Capstone and Job-Readiness (Days 34-40) | 6h/day

### Day 34: Capstone, part 1
- [ ] 🛠 Pick the problem (e.g. churn predictor with explanations, or a domain RAG app). Collect data, run EDA, build a baseline.
- [ ] 📖 MLOps overview: the full ML lifecycle.
- [ ] 🎯 Problem statement + baseline in README
- [ ] 📝 Log written + committed

### Day 35: Capstone, part 2
- [ ] 🛠 Improve the model, evaluate properly, do error analysis.
- [ ] 📖 Model monitoring and data drift.
- [ ] 🎯 Final model + metrics
- [ ] 📝 Log + weekly summary (`week-05.md`) committed

### Day 36: Capstone, part 3
- [ ] 🛠 FastAPI service + Dockerfile + tests for the endpoint.
- [ ] 📖 API design basics.
- [ ] 🎯 Containerized API running locally
- [ ] 📝 Log written + committed

### Day 37: Capstone, part 4
- [ ] 🛠 Demo front end, deploy, write README with an architecture diagram.
- [ ] 📖 None. Practical day.
- [ ] 🎯 **Capstone deployed**
- [ ] 📝 Log written + committed

### Day 38: Portfolio cleanup
- [ ] 🛠 Clean READMEs, pin your best 4 repos, record two 2-minute demo videos.
- [ ] 🎯 GitHub profile looks professional
- [ ] 📝 Log written + committed

### Day 39: Resume and interview prep
- [ ] 🛠 Write resume + LinkedIn. Practice 20 ML interview questions out loud.
- [ ] 📖 Interview theory (bias-variance, metrics, overfitting, transformers).
- [ ] 🎯 Resume finished
- [ ] 📝 Log written + committed

### Day 40: Mock interview + freelance profile
- [ ] 🛠 Mock interview (ask a friend or record yourself). Set up freelance profile with 2-3 gig offers.
- [ ] 🎯 **Core roadmap complete 🎉**
- [ ] 📝 Log + 40-day retrospective committed

---

# EXTENSION (Days 41-60) | 6h/day

> **New daily habit from Day 41:** 30 minutes of applications/outreach (2 job applications or freelance proposals, or 1 message to someone in the field). It counts as practical time.

## PHASE 6: Competitive ML on Kaggle (Days 41-46)

### Day 41: Pick a competition
- [ ] 🛠 Choose a Kaggle Playground (tabular) competition. Set up cross-validation, build a baseline, make your first submission.
- [ ] 📖 Kaggle workflow, CV score vs leaderboard score.
- [ ] 🎯 First submission made
- [ ] 📝 Log + applications done + committed

### Day 42: Feature engineering
- [ ] 🛠 Feature engineering and encoding (frequency/target encoding, interactions). Track every CV change in a table.
- [ ] 📖 Feature engineering principles.
- [ ] 🎯 Experiment table with CV gains
- [ ] 📝 Log + weekly summary (`week-06.md`) + applications done

### Day 43: Gradient boosting
- [ ] 🛠 LightGBM / CatBoost / XGBoost with Optuna tuning.
- [ ] 📖 What boosting hyperparameters do to fit.
- [ ] 🎯 Best single model
- [ ] 📝 Log + applications done + committed

### Day 44: Ensembling
- [ ] 🛠 Blending and stacking using out-of-fold predictions.
- [ ] 📖 Why ensembles work, leakage in stacking.
- [ ] 🎯 Ensemble beating the best single model
- [ ] 📝 Log + applications done + committed

### Day 45: Final submission
- [ ] 🛠 Final submissions, error analysis, post-mortem write-up.
- [ ] 📖 Read two top solution write-ups.
- [ ] 🎯 Post-mortem written
- [ ] 📝 Log + applications done + committed

### Day 46: Mini-project 6
- [ ] 🛠 Clean the Kaggle notebook into a reproducible script + README, then publish.
- [ ] 📖 Review and catch-up.
- [ ] 🎯 **Mini-project 6 done**
- [ ] 📝 Log + applications done + committed

## PHASE 7: LLM Fine-Tuning and MLOps (Days 47-53)

### Day 47: LoRA setup
- [ ] 🛠 Pick a small open model (~0.5-1B parameters) and a dataset. Set up Colab with Transformers + PEFT. Run base-model inference as a baseline.
- [ ] 📖 LoRA/QLoRA: low-rank adapters, quantization.
- [ ] 🎯 Baseline outputs saved
- [ ] 📝 Log + applications done + committed

### Day 48: Fine-tune with LoRA
- [ ] 🛠 Fine-tune with LoRA/QLoRA (TRL `SFTTrainer`) on Colab.
- [ ] 📖 SFT data formatting, chat templates.
- [ ] 🎯 Trained adapter saved
- [ ] 📝 Log + applications done + committed

### Day 49: Evaluate and publish
- [ ] 🛠 Compare fine-tuned vs base on a held-out set. Push the adapter to HF Hub.
- [ ] 📖 LLM evaluation basics.
- [ ] 🎯 Model card with evaluation results
- [ ] 📝 Log + weekly summary (`week-07.md`) + applications done

### Day 50: MLflow
- [ ] 🛠 Log params, metrics and artifacts to MLflow for your earlier experiments.
- [ ] 📖 Experiment tracking and model registry.
- [ ] 🎯 MLflow UI screenshot in README
- [ ] 📝 Log + applications done + committed

### Day 51: DVC + CI
- [ ] 🛠 Version data with DVC. Add a GitHub Actions workflow that runs lint + tests.
- [ ] 📖 CI/CD for ML.
- [ ] 🎯 Green checkmark on a commit
- [ ] 📝 Log + applications done + committed

### Day 52: Testing and structure
- [ ] 🛠 `pytest` for data/model code, logging, YAML config. Refactor one notebook into a package.
- [ ] 📖 Reproducible ML project structure.
- [ ] 🎯 Refactored project with tests
- [ ] 📝 Log + applications done + committed

### Day 53: Mini-project 7
- [ ] 🛠 Serve the fine-tuned LLM through FastAPI in Docker, with request logging.
- [ ] 📖 Monitoring, data drift.
- [ ] 🎯 **Mini-project 7 done**
- [ ] 📝 Log + applications done + committed

## PHASE 8: Agents and Interview Prep (Days 54-58)

### Day 54: Agent from scratch
- [ ] 🛠 Build an agent loop with tool calling (calculator + an API tool). Loop until the task is done, no framework.
- [ ] 📖 Agent patterns (ReAct, planning).
- [ ] 🎯 Agent solving a multi-step task
- [ ] 📝 Log + applications done + committed

### Day 55: Multi-tool agent
- [ ] 🛠 Add more tools, guardrails, error handling, a max-steps limit. Try LangGraph or a similar framework.
- [ ] 📖 When agents are worth it, and when they aren't.
- [ ] 🎯 Agent demo with README
- [ ] 📝 Log + applications done + committed

### Day 56: DSA and SQL
- [ ] 🛠 Solve 5 LeetCode problems (arrays, strings, hashmaps, two pointers) in Python. Solve 5 SQL interview problems.
- [ ] 📖 Big-O notation.
- [ ] 🎯 10 problems solved
- [ ] 📝 Log + weekly summary (`week-08.md`) + applications done

### Day 57: More DSA + pandas
- [ ] 🛠 5 problems on stacks/queues, sorting, binary search, recursion. Do 3 pandas interview tasks.
- [ ] 📖 Recursion and complexity of common algorithms.
- [ ] 🎯 8 problems solved
- [ ] 📝 Log + applications done + committed

### Day 58: ML interview drill
- [ ] 🛠 Answer 30 ML questions out loud or in writing. Implement k-NN or logistic regression from scratch in 30 minutes, timed.
- [ ] 📖 ML system design basics (design a fraud detector or recommender).
- [ ] 🎯 Question bank with your own answers
- [ ] 📝 Log + applications done + committed

## PHASE 9: Launch (Days 59-60)

### Day 59: Portfolio and applications
- [ ] 🛠 Profile README, pin repos, add screenshots/GIFs to READMEs. Send 10 job applications and 5 freelance proposals.
- [ ] 📖 How ML hiring screens work (recruiter, technical, take-home).
- [ ] 🎯 Portfolio ready to share
- [ ] 📝 Log + committed

### Day 60: Mock interview + retrospective
- [ ] 🛠 Full mock interview (technical + project walkthrough). Write a retrospective: what worked, what didn't.
- [ ] 📖 Pick your specialization for Days 61+ (computer vision, NLP/LLMs, MLOps, or tabular/data science).
- [ ] 🎯 **60-day roadmap complete 🎉**, plan for Days 61+ written
- [ ] 📝 Log + 60-day retrospective committed

---

## Milestones (tick when reached)

- [ ] Mini-project 1: EDA (Day 7)
- [ ] Mini-project 2: imbalanced classifier (Day 14), freelance gigs possible
- [ ] Mini-project 3: image classifier demo (Day 21)
- [ ] Mini-project 4: fine-tuned text classifier (Day 26)
- [ ] RAG app built (Day 30), RAG/chatbot gigs possible
- [ ] Mini-project 5: deployed app (Day 33)
- [ ] Capstone deployed (Day 37)
- [ ] Mini-project 6: Kaggle write-up (Day 46)
- [ ] Mini-project 7: fine-tuned LLM API (Day 53)
- [ ] 60 daily logs committed
