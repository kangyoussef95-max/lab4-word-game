# Project Report — Guess The Word Game

## First Impressions

### Initial Thoughts
The assignment seemed straightforward at first — it's basically Hangman, which everyone knows. But when I started thinking about the actual implementation constraints (no `while True`, no string replacement, pure functions, separated logic/UI), it became clear there was more design work involved than I expected.

### Assumptions Made
- The word list would be hardcoded rather than loaded from a file
- Case sensitivity should be handled everywhere (normalize to lowercase internally)
- "No string replacement functions" means no `.replace()` — building the masked word with a generator/join approach instead

### Points Needing Clarification
I wasn't sure at first whether "no while True" meant no `while` loops at all or just no infinite ones. I went with bounded `for` loops using `range()` and `break` to stay safe.

## Key Learnings

### Computer Science Concepts and Technical Skills
- **Pure functions**: Writing `update_game_state` as a pure function forced me to think about immutability. Using list concatenation (`list + [item]`) instead of `.append()` to avoid mutating the input was a small but important detail.
- **Separation of concerns**: Keeping all `print()`/`input()` calls out of the logic layer made the code way easier to test. The logic functions just take data and return data, which makes unit testing simple.
- **Bounded loops**: Using `for _ in range(n)` with a break condition is a clean alternative to `while True`. The upper bound acts as a safety net.

### Insights about Using CoPilot Effectively
- Ask mode is great for brainstorming — getting CoPilot to list possible states, variables, and bugs helped me think of things I might have missed (like the immutability bug).
- Being specific in prompts gets better results. "Can you review my update_game_state function?" worked better than a vague "review my code."
- CoPilot tends to over-engineer when you give it free rein. Keeping it in Ask mode for advice and doing the actual coding myself kept things under control.

### New Concepts or Tools Encountered
- pytest as a testing framework — I'd used simple assert statements before but never structured test functions with the `test_` prefix convention.
- The journal-logger agent concept was new. Having a structured log of every interaction made it easier to write this report.

## CoPilot Prompting Experience

### Types of prompts that worked well
- **Design questions**: "What states does a Word Game like Hangman need?" gave a solid enumeration I could pick from.
- **Bug brainstorming**: "What are possible bugs in Word Guess / Hangman implementations" surfaced edge cases like case sensitivity and off-by-one errors.
- **Targeted code review**: "Can you review my update_game_state function?" gave focused, actionable feedback.
- **Test generation**: "Can you help me write tests for this function?" produced a reasonable set of test cases that covered the main paths.

### Types of prompts that did not work well or failed
- Vague prompts like just asking CoPilot to "help with the game" tended to produce overly broad responses.
- When CoPilot was in Socratic mode, it kept asking me questions instead of giving direct answers, which was sometimes frustrating when I just wanted a quick check. Switching modes helped.

## Limitations, Hallucinations and Failures

### Examples
- CoPilot suggested adding **thread safety** as a concern for a single-threaded console game — clearly irrelevant.
- It recommended a "paused" game state, which makes no sense for a terminal app where the program just blocks on `input()`.
- During the code review, CoPilot suggested adding type-checking inside `update_game_state` for the `guess` parameter (checking `isinstance(guess, str)`). This is Python — if someone passes an int, that's their problem. The `validate_guess` function already handles this at the UI boundary.

### Analysis
These issues happened because CoPilot generalizes from many different types of applications. It doesn't know our game is a simple console script, so it brings in patterns from web apps or multi-threaded systems. The suggestions weren't harmful, just unnecessary.

### Impact on the Project
Minimal. The irrelevant suggestions were easy to filter out. No bugs were introduced by following CoPilot's advice.

## AI Trust

### When did I trust the AI?
- For listing states, variables, and potential bugs — it's good at enumeration.
- For generating test cases — it covered the obvious paths and a few I hadn't thought of.
- For documentation — it writes clean docstrings faster than I do.

### When did I stop trusting it?
- When it suggested over-engineered solutions (thread safety, difficulty enums, score tracking) for a simple lab.
- When it gave code review feedback that applied to general Python but not to this specific architecture (like type-checking inside a pure logic function).

### Patterns indicating low reliability
- Overly generic advice that doesn't account for the project's scope.
- Suggestions that sound right but don't match the constraints (like recommending `.replace()` when string replacement was banned).

## What I Learned

### About software development
- Thinking about design before coding (states, variables, invariants) saves time during implementation.
- Pure functions are easier to test and reason about.
- Separating logic from UI is worth the extra effort even for small projects.

### About using AI tools
- AI is most useful as a brainstorming partner and reviewer, less useful as a code generator for small, constrained projects.
- Always filter AI suggestions through your own understanding of the project constraints.
- The quality of the output depends heavily on the quality of the prompt.

## Reflection

### Did AI make you faster?
Yes, especially during the design phase and testing. Writing the MY_NOTES.md took 10 minutes of my own thinking plus 10 minutes of reviewing CoPilot's suggestions, but the result was more thorough than what I would have produced alone. Test generation also saved time.

### Did you feel in control of the code?
Yes. I wrote the core function myself and made all the architectural decisions. CoPilot helped fill in boilerplate (UI functions, test cases) but the structure was mine.

### Would you use AI the same way next time?
Mostly yes. I'd spend more time in the design phase with AI and less time asking it to review obvious code. I'd also try to use it more for edge case testing — that's where it added the most value.