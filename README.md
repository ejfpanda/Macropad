# Lily-Pad

## Note: I didn't understand how to use github until today so things probably aren't laid out properly.

It has 6 keys -> 5 switches + 1 rotary encoder switch , a rotary encoder, an OLED display and 2 SK6812 MINI - E LEDs. It uses kmk firmware and circuit python.

## PCB:

<img width="525" height="635" alt="Screenshot 2026-07-18 003036" src="https://github.com/user-attachments/assets/e4d317a6-ea11-41a1-930c-7002000ada9b" />
<img width="1137" height="632" alt="image-2" src="https://github.com/user-attachments/assets/c2ffbd00-446e-4db3-bfe0-786d80fcf794" />


## CAD Case:

<img width="1022" height="717" alt="image-1" src="https://github.com/user-attachments/assets/121c8ffb-4aac-4472-87f9-bdb9f3dd2fea" />

<img width="1056" height="677" alt="image" src="https://github.com/user-attachments/assets/e0dd09f8-aad0-4239-ad80-09d15535de61" />

<img width="357" height="332" alt="image" src="https://github.com/user-attachments/assets/595624c3-fd34-4759-88aa-12f7873c85e2" />


## Firmware:

I used kmk firmware and circuit python.

I have two layers: base layer 0 and layer 1.

On base the keys are copy, paste, save, undo, mute and hold key 6 for layer 1.

While key 6 is held keys are play/pause, next, previous and a macro string saying 'sent from my Lily-Pad'


The encoder in layer 0 is volume up and down (clockwise and counter) and in layer 1 is brightness up and down.

The OLED display shows title, current layer and also it shows last key pressed.

The LEDs flash briefly when you press a key.


## Required parts:

| Component | Amount |
| :--- | :---: |
| **Seeed XIAO RP2040** | 1x |
| **MX-Style switches** | 5x |
| **1N4148 Diodes** | 6x | 
| **EC11 Rotary encoder** | 1x |
| **0.91 inch OLED display** | 1x |
| **DSA keycaps** | 5x |
| **SK6812 MINI-E LED** | 2x |
| **M3x16mm screw** | 4x |
| **Case** (2 printed parts) | 1x |
| **PCB** | 1x |
