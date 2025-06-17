# 🔷 Rotated & Squashed Grid in Pygame

[Pygame](https://www.pygame.org/) 

- Draw a grid of squares 💠  
- Rotate each square by 45° 🌀  
- Squash the entire grid vertically to give an **isometric/diamond** look 💎  

Perfect for learning:
- Coordinate transforms
- Rotation with trigonometry
- Y-axis scaling (squash)
- Drawing polygons with math!

---

## 🎮 What It Looks Like

A dreamy diamond grid, like a tactical RPG board or early isometric game world.

+-----------------------+
| /\ |
| /\ / \ /\ |
| /\ /\ |
| |
+-----------------------+



(It's a failed project, okay? 😅)

---

## 🚀 Getting Started

### 🧰 Requirements

- Python 3.x  
- `pygame` library  

### 📦 Install Pygame:
```bash
pip install pygame
```
## 🧠 How It Works
* Define a regular grid of squares (rectangles).

* Rotate each square’s corners around the center of the screen using a rotation matrix.

* Apply a vertical "squash factor" to make everything look flat (isometric-style).

* Draw each squashed, rotated square using pygame.draw.polygon().

