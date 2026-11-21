
# Week 11: Update Your GitHub Fork Without Losing Week 10 Work

**Goal:** Save your Week 10 changes, bring the teacher's Week 11 files into your own fork, and update the project in VS Code.

**Important:** Do not make a new fork or delete your existing project!

## Step 1: Save Your Week 10 Work

1. Open your existing project in **VS Code**.

2. Save all your files:
   - Mac: `Cmd + S`
   - Windows: `Ctrl + S`

3. Open the VS Code terminal:
   - Click **Terminal → New Terminal**.

4. Check your current branch and changes:

   ```bash
   git branch --show-current
   git status
   ```

   These instructions assume you're on the `main` branch.

5. **Make sure your API key is protected!**

   Your `.env` file should never be uploaded to GitHub.

   Check whether Git is ignoring it:

   ```bash
   git check-ignore .env
   ```

   If your `.env` file is in another folder, use its actual path.

   If this command shows nothing, or if your `.env` file is tracked by Git, ask your teacher for help before continuing.

6. Stage your Week 10 files:

   ```bash
   git add path/to/week10/
   git status
   ```

   Replace `path/to/week10/` with your actual Week 10 folder.

   Check that your `.env` file and API key are not included.

7. Save your changes with a commit:

   ```bash
   git commit -m "Complete Week 10 assignment"
   ```

   If Git says `nothing to commit`, your work may already be saved.

8. Push your work to your GitHub fork:

   ```bash
   git push origin main
   ```

   Your Week 10 code should now be saved in your own GitHub repository.

   **If the push is rejected, ask your teacher for help. Do not force the push.**

## Step 2: Update Your Fork on GitHub

1. Open [GitHub](https://github.com).

2. Navigate to **your forked repository**, not the teacher's original repository.

3. Make sure you're on the `main` branch.

4. Near the top of the repository, click **Sync fork**.

5. Click **Update branch**.

This brings the teacher's latest code into your fork, including the new Week 11 assignment.

Your committed Week 10 work should remain in your repository if the changes merge successfully.

**IMPORTANT:** If GitHub reports a merge conflict or asks whether you want to discard your commits, stop and ask your teacher for help. Do not discard your work.

## Step 3: Update Your Project in VS Code

Now that your fork is updated on GitHub, you need to get those changes onto your computer.

1. Return to **VS Code**.

2. Open the terminal in your existing project folder.

3. Run:

   ```bash
   git pull origin main
   ```

This downloads the latest files from your fork.

You should now have:
- Your existing Week 10 work
- The new Week 11 files
- Any other updates from the teacher

**Do not delete your old project or clone the repository again.**

If Git reports that local changes would be overwritten, stop and ask your teacher for help.

## Step 4: Check That Everything Worked

In your VS Code terminal, run:

```bash
git status
```

If everything is up to date, you may see:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Now check:

- [ ] My Week 10 code is still there.
- [ ] I can see the new Week 11 folder and `app.py`.
- [ ] My `.env` file is still private.
- [ ] My project opens correctly in VS Code.

## Step 5: Start Week 11

Open your new Week 11 `app.py` file.

Make sure you're using the same Python virtual environment and Gemini API setup from Week 10.

Run the application:

```bash
streamlit run path/to/week11/app.py
```

Replace the placeholder with the actual location of your Week 11 file.

Alternatively, navigate into your Week 11 folder and run:

```bash
streamlit run app.py
```

You're ready for Week 11!

---

## Quick Reference: Updating Your Fork Every Week

### 1. Save Your Previous Work

Make sure `.env` is ignored, then stage your assignment files and run:

```bash
git commit -m "Complete previous assignment"
git push origin main
```

### 2. Update Your Fork on GitHub

Go to your fork and click:

**Sync fork → Update branch**

### 3. Update VS Code

```bash
git pull origin main
```

### 4. Start the New Assignment

Open the new week's folder and follow the instructions.

---

**Need help?** If Git gives you an error, especially a merge conflict, ask your teacher before running more commands. Never use `git reset --hard` or force-push to fix an error without guidance.
