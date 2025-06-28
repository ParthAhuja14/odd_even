# 🎮 Odd Even Toss & Cricket Game

A fun two-player **hand gesture-based Python game** that combines the classic **Odd-Even toss** with a mini cricket match simulation.

---

## 🧠 Game Concept

This game mimics the classic street-style **"Odd-Even Toss"** used to decide who bats or bowls first — followed by a simple cricket game using number inputs!

---

## 👥 Players Required

- **2 Players** (Player 1 & Player 2)
- Played with **numbers using hand gestures** (1–10)

---

## 🎲 Game Flow

### 1. **Toss Phase (Odd-Even)**

- Each player selects **Odd** or **Even**
- Both show a number (1–10) using hand gestures
- The numbers are **added together**
- If the sum is:
  - 🔢 **Even** → Player who chose *Even* wins the toss
  - 🔢 **Odd** → Player who chose *Odd* wins the toss
- Toss winner selects **Batting** or **Bowling**

---

### 2. **Match Phase**

#### 🏏 First Innings:

- Batter inputs a number (1–10)
- Bowler inputs a number (1–10)
- If numbers **match**, batter is **OUT**
- If not, batter's number is **added to score**

#### 🔁 Second Innings:

- Roles are reversed
- Second player tries to beat or match the target score

#### 🏆 Result:

- Player with the **higher score** at the end wins!

---

## 📄 Example Gameplay

```bash
Player 1 chooses: Odd
Player 2 chooses: Even

Player 1 shows: 3
Player 2 shows: 6
Total: 9 → Odd → Player 1 wins the toss!

Player 1 chooses to Bat

First Innings:
Player 1 (bat): 4
Player 2 (bowl): 6 → Not out → Score = 4
Player 1 (bat): 7
Player 2 (bowl): 7 → OUT → Final Score = 4

Second Innings:
Player 2 (bat): 5
Player 1 (bowl): 6 → Not out → Score = 5 → Player 2 wins!
