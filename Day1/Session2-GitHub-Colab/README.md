# Session 2 — GitHub Basics

**Day 1 · 10:45 – 12:45**

In this session you will get a GitHub account, make your own copy of the course
repository, download it to your computer, change it, and send it back.

We work only on the **main branch**. Nothing else.

---

## 1. Create a GitHub account

1. Go to **<https://github.com>**
2. Click **Sign up** (green button, top right)
3. Enter your **email address**
4. Create a **password**
5. Choose a **username** — use `firstname-lastname`, for example `yourname-fathername`
6. Enter the code GitHub sends to your email
7. Choose the **Free** plan

**Write your username down.** You will use it all week.

---

## 2. Navigate another person's GitHub

Open the course repository: **<https://github.com/keduog/EDU-AI-Training>**

This is what you see:

| What you see | What it means |
|---|---|
| `keduog / EDU-AI-Training` | Owner name / repository name |
| **Code** tab | The files. This is the main view. |
| Folder list (`Day1`, `Day2`, …) | Click a folder to go inside it |
| `main` dropdown | The branch you are viewing. Leave it on `main`. |
| **Fork** button | Make your own copy (section 3) |
| Green **`<> Code`** button | Get the link to download it (section 5) |
| **Issues** / **Pull requests** | Team discussion. We don't need these today. |

**Try it now:** click `Day1`, look inside, then click a file to read it.
Click the repository name at the top to go back.

---

## 3. What is a fork?

A **fork** is your own copy of somebody else's repository, saved under your account.

- The original stays untouched
- Your copy is yours — you can change anything in it
- It lives on GitHub, not on your computer

**Why fork?** You cannot change other people's repositories. So you make a copy first,
then work on your copy.

### How to fork

1. Go to <https://github.com/keduog/EDU-AI-Training>
2. Click **Fork** (top right)
3. Owner: **your username**
4. Click **Create fork**

You are now at `https://github.com/YOUR-USERNAME/EDU-AI-Training`.

Under the title it says *forked from keduog/EDU-AI-Training*. That is your copy.

---

## 4. What is cloning?

A **clone** is a copy of a repository on **your own computer**.

| | Fork | Clone |
|---|---|---|
| Where is the copy? | On GitHub | On your computer |
| What is it for? | So you have your own version | So you can open and edit the files |

**Why clone?** You cannot edit files in a web browser comfortably. You clone so you can
work in VS Code, then send your changes back.

**The order is always: fork first, then clone your fork.**

---

## 5. Install what you need

| Tool | Where |
|---|---|
| **Git** | <https://git-scm.com/downloads> — run the installer, accept all defaults |
| **VS Code** | <https://code.visualstudio.com> — run the installer, accept all defaults |

Check they work. Open a terminal (Windows: search **Git Bash**. Mac/Linux: **Terminal**):

```bash
git --version
```

You should see a version number.

**Tell Git who you are** (only needed once, ever):

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Use the same email as your GitHub account.

---

## 6. Clone your fork

### Get the link

1. Go to **your fork**: `https://github.com/YOUR-USERNAME/EDU-AI-Training`
2. Click the green **`<> Code`** button
3. Make sure **HTTPS** is selected
4. Click the copy icon

### Run the commands

In your terminal:

```bash
cd Desktop
git clone https://github.com/YOUR-USERNAME/EDU-AI-Training.git
cd EDU-AI-Training
```

| Command | What it does |
|---|---|
| `cd Desktop` | Go to your Desktop folder |
| `git clone <link>` | Download the whole repository |
| `cd EDU-AI-Training` | Go inside the folder that was just created |

Now open it in VS Code:

```bash
code .
```

> `code` then a space then a **dot**. The dot means "this folder".
>
> If it says *command not found*: on Windows, reinstall VS Code and tick
> **"Add to PATH"**. On Mac, open VS Code, press `Cmd+Shift+P`, type `shell command`,
> and choose **Install 'code' command in PATH**. Then open a new terminal.

You can also open the folder from inside VS Code: **File → Open Folder…**

**Check it worked:** the bottom-left corner of VS Code shows **`main`**.
That means VS Code sees this as a Git folder.

---

## 7. The full cycle: change → save → send back

This is the loop you will repeat every day. Do it now.

### Step 1 — Make a change

In VS Code, click **New File** in the Explorer panel.
Name it `my-notes.md` and type something inside:

```
# My notes from Day 1
Today I learned how to fork and clone.
```

Press **Ctrl+S** to save.

### Step 2 — Open Source Control

Click the **Source Control** icon in the left bar (it looks like a branch).
Your file appears under **Changes**.

### Step 3 — Write a message and commit

1. Type a short message in the box at the top, for example: `Add my notes`
2. Click the **✓ Commit** button

If VS Code asks *"Would you like to stage all your changes?"* → click **Yes**.

Your change is now saved **on your computer**. GitHub does not know about it yet.

### Step 4 — Push to GitHub

Click **Sync Changes** (or **Push**).

The first time, a browser window opens — click **Authorize**. Then it uploads.

### Step 5 — Check

Go to `https://github.com/YOUR-USERNAME/EDU-AI-Training` in your browser and refresh.

**Your file is there.** You have completed the full cycle.

---

## The cycle in one picture

```
   GitHub (keduog)
         |
      FORK  ->  Your GitHub copy
                     |
                  CLONE  ->  Your computer  ->  open with: code .
                                   |
                              edit files
                                   |
                               COMMIT  (save with a message)
                                   |
                                PUSH  ->  back to your GitHub copy
```

---

## Same thing with commands (optional)

If you prefer the terminal instead of clicking in VS Code:

```bash
git add .                      # take all my changes
git commit -m "Add my notes"   # save them with a message
git push                       # send them to GitHub
```

And before you start working each day:

```bash
git pull                       # get the newest version first
```

---

## If something goes wrong

**`git: command not found`**
Git is not installed, or the terminal was open before you installed it.
Close the terminal, open a new one.

**`code: command not found`**
See the note in section 6.

**It asks for a password and rejects it**
GitHub does not accept your normal password in the terminal.
Easiest fix: use VS Code's **Sync Changes** button instead — it signs you in through
the browser automatically.

**`Updates were rejected`**
Someone changed the repository before you. Run `git pull`, then push again.

---

## Checklist

- [ ] I created a GitHub account
- [ ] I can navigate the `keduog/EDU-AI-Training` repository
- [ ] I forked it to my own account
- [ ] Git and VS Code are installed
- [ ] I cloned my fork to my computer
- [ ] I opened it with `code .`
- [ ] I made a change, committed it, and pushed it
- [ ] I can see my change on GitHub in my browser
