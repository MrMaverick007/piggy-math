# Piggy Math

A fast, lightweight math trainer built with Python and Tkinter. Practice your arithmetic with customizable number ranges and instant feedback.

---

## Preview

> *Title screen → Pick a mode → Set your bounds → Answer as fast as you can*

---

## Features

- **5 game modes** — Addition, Subtraction, Multiplication, Division, and Mix
- **Custom bounds** — set your own number range so problems match your skill level
- **Instant feedback** — correct answers flash green, wrong answers flash red
- **Anti-spam** — input is locked briefly after a wrong answer so you can't brute force it
- **Decimal support** — division answers are rounded to 2 decimal places
- **Clean navigation** — back button on every screen

---

## Getting Started

### Requirements

- Python 3.x
- Tkinter (included with most Python installations)

### Run it

```bash
git clone https://github.com/yourusername/piggy-math.git
cd piggy-math
python piggy_math.py
```

No external dependencies. Just run it.

---

## How to Play

1. Launch the app and hit **Play Game**
2. Choose an arithmetic mode
3. Enter a lower and upper bound (e.g. `1` to `12`)
4. Hit **Start Game**
5. Type your answer and press **Enter**
6. Keep going — problems generate automatically after each correct answer

> For division, round your answer to **2 decimal places**

---

## Project Structure

```
piggy-math/
└── piggy_math.py    # entire app, single file
```

---

## Built With

- [Python](https://www.python.org/) — language
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI framework
- `operator` module — arithmetic operations
- `random` module — problem generation

---

## License

MIT — do whatever you want with it.