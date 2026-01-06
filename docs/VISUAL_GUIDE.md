# 🎨 VISUAL GUIDE - Countdown Timer UI Layout

## Application Window Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  Countdown Timer                                          ▭ □ ✕ │  ← Window Title Bar
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│   ┌───────────────────── CONTROL PANEL ─────────────────────┐   │
│   │                                                           │   │
│   │      Minutes: [____]    Seconds: [____]                 │   │  ← Input Fields
│   │                                                           │   │
│   │      [  Start  ]  [  Pause  ]  [  Reset  ]              │   │  ← Control Buttons
│   │                                                           │   │
│   └───────────────────────────────────────────────────────────┘   │
│                                                                   │
│                                                                   │
│                          ┌───────────┐                           │
│                          │           │                           │
│                          │   05:30   │                           │  ← Large Countdown
│                          │           │                           │     (120px Font)
│                          └───────────┘                           │
│                                                                   │
│                                                                   │
│   ┌────────────────── BOTTOM CONTROLS ────────────────────┐     │
│   │                                                         │     │
│   │  [🌓 Toggle Theme] [⛶ Fullscreen] [📌 Always on Top]  │     │  ← Mode Buttons
│   │                                                         │     │
│   └─────────────────────────────────────────────────────────┘     │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

        Default Size: 800x600 pixels
        Default Theme: Dark Mode (Black BG, White Text)
```

## Dark Mode (Default)

```
Background Colors:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Main Background:     #000000  (Pure Black)
Entry Background:    #1a1a1a  (Very Dark Gray)
Button Background:   #333333  (Dark Gray)

Text Colors:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
All Text:           #FFFFFF  (Pure White)
Countdown Display:  #FFFFFF  (Pure White)
Button Text:        #FFFFFF  (Pure White)
```

## Light Mode

```
Background Colors:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Main Background:     #FFFFFF  (Pure White)
Entry Background:    #F0F0F0  (Light Gray)
Button Background:   #E0E0E0  (Light Gray)

Text Colors:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
All Text:           #000000  (Pure Black)
Countdown Display:  #000000  (Pure Black)
Button Text:        #000000  (Pure Black)
```

## Fullscreen Mode

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                 ┃
┃   ┌─────────────────────────────────────────────────────────┐  ┃
┃   │  Minutes: [____]  Seconds: [____]                       │  ┃
┃   │  [  Start  ]  [  Pause  ]  [  Reset  ]                  │  ┃
┃   └─────────────────────────────────────────────────────────┘  ┃
┃                                                                 ┃
┃                                                                 ┃
┃                          ┌─────────────┐                       ┃
┃                          │             │                       ┃
┃                          │             │                       ┃
┃                          │    10:45    │  ← Even Larger        ┃
┃                          │             │    Display            ┃
┃                          │             │                       ┃
┃                          └─────────────┘                       ┃
┃                                                                 ┃
┃                                                                 ┃
┃   ┌─────────────────────────────────────────────────────────┐  ┃
┃   │  [🌓 Toggle Theme] [⛶ Exit Fullscreen] [📌 Unpin]      │  ┃
┃   └─────────────────────────────────────────────────────────┘  ┃
┃                                                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

          Borderless, Full Screen
          Press ESC to exit
```

## Font Specifications

```
Element              Font Family    Size    Weight
──────────────────────────────────────────────────
Countdown Display    Arial          120px   Bold
Input Labels         Arial          12px    Normal
Input Fields         Arial          12px    Normal
Buttons              Arial          11px    Bold
Bottom Buttons       Arial          10px    Normal
```

## Button States

### Start Button
```
State: ENABLED   → When timer is not running
State: DISABLED  → When timer is running
```

### Pause/Resume Button
```
State: DISABLED  → When timer is not running
State: ENABLED   → When timer is running
Label: "Pause"   → When timer is running
Label: "Resume"  → When timer is paused
```

### Reset Button
```
State: ENABLED   → Always enabled
```

### Theme Button
```
Label: "🌓 Toggle Theme"  → Always same
```

### Fullscreen Button
```
Label: "⛶ Fullscreen"      → In normal mode
Label: "⛶ Exit Fullscreen" → In fullscreen mode
```

### Always-on-Top Button
```
Label: "📌 Always on Top"  → When not pinned
Label: "📌 Unpin Window"   → When pinned
```

## Input Fields

```
┌─────────────────────────────┐
│  Minutes: [____0____]       │  ← Default: 0
│  Seconds: [____0____]       │  ← Default: 0
└─────────────────────────────┘

Width: 8 characters
Alignment: Center
Accept: Integer numbers only
Range: 0 - 999 (minutes), 0 - 59 (seconds)
```

## Countdown Display Format

```
Format: MM:SS

Examples:
────────────
00:00  ← Initial / Reset
00:30  ← 30 seconds
01:00  ← 1 minute
05:30  ← 5 minutes 30 seconds
25:00  ← 25 minutes (Pomodoro)
99:59  ← Maximum display
```

## Color Transitions

```
Theme Toggle:
═════════════

Dark Mode              →  [CLICK]  →              Light Mode
┌──────────────┐                         ┌──────────────┐
│ ████████████ │                         │ ░░░░░░░░░░░░ │
│ ████░░░░████ │                         │ ░░░░████░░░░ │
│ ████░05:30░█ │        Instant          │ ░░░░05:30░░░ │
│ ████░░░░████ │      Transition         │ ░░░░████░░░░ │
│ ████████████ │                         │ ░░░░░░░░░░░░ │
└──────────────┘                         └──────────────┘
  Black BG                                  White BG
  White Text                                Black Text
```

## Spacing & Layout

```
Padding:
────────
Top Panel:       20px all sides
Display Area:    Centered (50%, 50%)
Bottom Panel:    20px all sides
Button Spacing:  5px between buttons
Frame Spacing:   10px vertical gaps
```

## Window Behavior

```
Normal Mode:
────────────
Size: 800x600
Resizable: Yes
Borders: Yes
Title Bar: Yes

Fullscreen Mode:
────────────────
Size: Full Screen
Resizable: No
Borders: No
Title Bar: No
```

## Cursor & Interaction

```
Input Fields:    Text cursor (I-beam)
Buttons:         Hand cursor (pointer)
General:         Default arrow
```

## Timer States Visualization

```
IDLE STATE:
═══════════
[  Start  ] ← ENABLED
[  Pause  ] ← DISABLED
[  Reset  ] ← ENABLED
Display: 00:00
Inputs: ENABLED


RUNNING STATE:
══════════════
[  Start  ] ← DISABLED
[  Pause  ] ← ENABLED
[  Reset  ] ← ENABLED
Display: Counting down
Inputs: DISABLED


PAUSED STATE:
═════════════
[  Start  ] ← DISABLED
[ Resume  ] ← ENABLED
[  Reset  ] ← ENABLED
Display: Frozen
Inputs: DISABLED


FINISHED STATE:
═══════════════
[  Start  ] ← ENABLED
[  Pause  ] ← DISABLED
[  Reset  ] ← ENABLED
Display: 00:00
Inputs: ENABLED
Sound: BEEP! 🔔
Message: "Timer Complete!"
```

## Responsive Behavior

```
Window Resize:
──────────────
- Countdown stays centered
- Control panels adjust width
- Buttons maintain positions
- No overlap or clipping

Fullscreen:
───────────
- All elements scale proportionally
- Countdown remains centered
- Controls stay at top/bottom
- ESC key always works
```

## Accessibility Features

```
✓ Large readable fonts (120px countdown)
✓ High contrast colors (black/white)
✓ Clear visual state changes
✓ Keyboard support (ESC for fullscreen)
✓ Sound feedback on completion
✓ Clear button labels
✓ Centered, focused layout
```

## Visual Feedback

```
Button Press:     Visual depression effect
Theme Change:     Instant color swap
Timer Start:      Button states change
Timer Complete:   Sound + Message box
Pause:            Button label changes
Fullscreen:       Seamless transition
```

---

This visual guide helps understand the UI layout and behavior
without running the application. Use it as reference for
customization or understanding the code structure.
