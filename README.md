# InboxZero CLI 🧠✉️

**InboxZero: An AI-powered Gmail cleanup tool using BERT and secure OAuth authentication.**

---

## 🚀 What is InboxZero?

InboxZero is a command-line Python tool that connects to your Gmail account, analyzes your most recent emails using a BERT-based sentiment classifier, and automatically deletes high-confidence spam or negative messages — all securely and privately on your device.

---

## 📁 Project Structure

```
inboxzero/               # Python package source
setup.py                 # Installer script
README.md                # Documentation
```

---

## 📦 Requirements

- Python 3.10+
- pip
- Google account with Gmail
- Internet access

---

## 🧰 Installation

### 1. Clone the repository

```bash
git clone https://github.com/abrarxploit/inboxzero.git
cd inboxzero
```

### 2. Create a virtual environment

```bash
python -m venv inboxenv
inboxenv\Scripts\activate  # On Windows
```

### 3. Install the package and dependencies

```bash
pip install -e .
pip install -r requirements.txt
```

---

## 🔐 How to Create `credentials.json`

Each user must set up Gmail API credentials. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a **new project** or select an existing one
3. In the dashboard, go to **APIs & Services > Library**
4. Search for and enable the **Gmail API**
5. Now go to **OAuth consent screen**:
   - Select **External**
   - Add your Gmail account as a **Test User**
6. Go to **Credentials > Create Credentials > OAuth client ID**
   - Application Type: **Desktop App**
   - Name it anything (e.g., InboxZeroClient)
7. Click **Download JSON** — this is your `credentials.json`
8. Place it in the root folder of the cloned project

✅ You’re now ready to authenticate Gmail access.

---

## ▶️ How to Run InboxZero

```bash
python -m inboxzero
```

You will be prompted to authorize access. After login, InboxZero:

- Analyzes your **20 most recent emails**
- Classifies them with BERT
- Deletes messages classified with high-confidence as NEGATIVE
- Keeps the rest

---

## 📊 Sample Output

```
[ANALYSIS] 'Alert: Free Crypto!' => NEGATIVE (9911.25%)
🗑️ Deleted: 'Alert: Free Crypto!'

[ANALYSIS] 'Zoom Invoice' => POSITIVE (9883.77%)
✅ Kept: 'Zoom Invoice'

Summary:
Kept Emails   : 13
Deleted Emails: 7
```

---

## 🔐 Security Highlights

- OAuth 2.0 with Test User access only
- Secure token hashed with SHA-3 + hardware binding
- No data leaves your machine

---

## 📈 Future Scope

- Full inbox pagination support
- GUI dashboard
- Email label filtering
- Automated scheduling and reporting
- Will be able to scan more than 20 emails at a time or full inbox.

---

## 👤 Developer

- [abrarxploit](https://github.com/abrarxploit)

## 📜 License

MIT License

