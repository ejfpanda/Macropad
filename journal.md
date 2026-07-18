title: Macropad
author: Edward Fangzhou
description: 
created_at: 07/13/2026

# July 13th DAY 1 CUMULATIVE TIME: 3.2 HOURS

Downloaded KiCad. Completely new to this, so I used tutorial hackpad. Will add to the tutorial in future with more keys or something like that but for now I'll just follow it.

Took me a long time to figure out how to download footprint libraries, but got there in the end. Spent a lot of other time faffing around.

Opened schematic editor and added my components - microcontroller and 3 switches. Wired components together and connected ground wires.

<img width="849" height="564" alt="Screenshot 2026-07-13 232948" src="https://github.com/user-attachments/assets/0eee3a66-8df8-45d3-843e-b58ab5613b4c" />

Then went to PCB editor and updated PCB from schematic. 

I then flipped the footprint of the microcontroller to the other side.

Then I routed the PCB.

Finally, Edge.cuts was used. This took me a long time because I am stupid and didn't realise I needed to click on the square. 

<img width="332" height="733" alt="Screenshot 2026-07-13 233436" src="https://github.com/user-attachments/assets/3df04f16-8b3a-45f3-b1a0-3a73e3600e1c" />


Next for creating the case, I used Free CAD because I couldn't get Fusion360 as in the guide.

I made a new sketch and drew a rectangle with same dimensions as PCB earlier, but added 0.4mm on both sides so after addition: 49.90mm and 20.40mm

Outer rectangles: same deal - so 69.90mm and 41.40mm (10mm between)

Absolute disaster because I've never used CAD before and was trying to teach myself. It wasn't too hard but I spent ages trying to find the right thing to do.

I got a whole structure done in 2D before I realised I couldn't extrude the base because I'd done it in the wrong section thingy, I was meant to use sketch instead of draft.

Then I didn't attach the sketch to the body at the start and then there was a dependency loop. I really made it much harder than it really was, but at least I now know very well how to centre a rectangle inside another because I had to do that multiple times.

Most frustrating of all was when everything just grayed out on the toolbar for no reason and I couldn't click on anything. Great.

4 different versions later, I've still got a hollow base so tomorrow I'll try to fill that in.

It was a very frustrating session but learning has happened, maybe, and tomorrow is hopefully better. My mind is fried as well because I've been sitting in the same position for 4 hours and it's almost 3 am. An ok shift today and here's what I've done: PCB and CAD partially. Screenshots to come.

<img width="582" height="300" alt="Screenshot 2026-07-14 024058" src="https://github.com/user-attachments/assets/d601dc72-6e5c-4a61-a692-4b1deed5874c" />
<img width="1656" height="866" alt="Screenshot 2026-07-14 024252" src="https://github.com/user-attachments/assets/da3e4acc-fa1c-4e0f-93d1-082c91db019a" />
<img width="1615" height="885" alt="Screenshot 2026-07-14 024332" src="https://github.com/user-attachments/assets/0ad92389-cca3-4ceb-a894-aae5f798fb02" />


# JULY  14th DAY 2 CUMULATIVE TIME: 6.9 HOURS

# I'd already done days 2 3 and 4 in this journal, but because I've been editing straight into github at the start and doing a lot of git pushes and pulls I've lost that progress.

# Therefore this might not be as detailed as I would have liked to do because screenshots are gone and I've forgotten my exact thought process.

After not figuring out FreeCAD for so long I switched to onshape because someone told me it was better. There I created the base and the lid of my keyboard, but in a very simple way to begin with - just extrusions and sketches.

Screenshots of my CAD v1:

Base:

<img width="977" height="623" alt="Screenshot 2026-07-18 001353" src="https://github.com/user-attachments/assets/e26a4b12-b3e8-49ce-8c49-72e387309808" />

Lid:

<img width="1115" height="593" alt="Screenshot 2026-07-18 001429" src="https://github.com/user-attachments/assets/ad00ae04-7214-45d7-973d-9f6b127e52eb" />

Then I went over to KiCAD and tried to make upgrades by adding 7 switches.

I was really struggling trying to route on the PCB because it was really disorganised and I didn't really know how to structure everything. I saw online to use vias so I think I tried that.

Here's the schematic I got with 7 switches:

<img width="519" height="270" alt="Screenshot 2026-07-18 001713" src="https://github.com/user-attachments/assets/878bf6d1-ee83-4aed-a107-0dd5312ea351" />



# JULY 15th DAY 3 CUMULATIVE TIME: 8.4 HOURS

On this day I learnt matrix wiring from youtube and also the hackpad guide. It was kinda difficult to get my head round at first but then it was alright. 

I also added a rotary encoder and was struggling a bit finding how to put the global labels because I didn't know what they were meant to be but found it in the end.

Schematic screenshot:

<img width="469" height="622" alt="Screenshot 2026-07-18 002222" src="https://github.com/user-attachments/assets/36e47a30-d28f-482b-b3e4-2320ffb75542" />

The PCB work was the hardest part because I was struggling even more with so many diodes and finding where to place them in a good way.

The final result was a bit ugly with tons of vias:

<img width="661" height="340" alt="Screenshot 2026-07-18 002309" src="https://github.com/user-attachments/assets/e3be5ad8-9c99-4113-a8ee-a9588372b42c" />

I also added an OLED display to the schematic:

<img width="413" height="249" alt="Screenshot 2026-07-18 002435" src="https://github.com/user-attachments/assets/a51af866-d1be-42b5-ac09-9a0b5ac8b08e" />


# JULY 16th DAY 4 CUMULATIVE TIME: 15.3 HOURS

On day 4, I assigned footprints to everything again with the OLED now there.

I also added 2 LEDs to the schematic:

<img width="824" height="380" alt="Screenshot 2026-07-18 002706" src="https://github.com/user-attachments/assets/0388c136-6a6f-4903-861a-dabdfad777da" />


A lot of my time was spent rearranging the components in order to look nice when complete and also to look neat in the actual PCB design.

I tried my best to keep everything on one layer if possible and only using the other side if there was no other option. I did have to use 1 via though.

The structure that came out was quite nice I think.

After routing and adding 4 mounting holes, here it is:

<img width="525" height="635" alt="Screenshot 2026-07-18 003036" src="https://github.com/user-attachments/assets/af5c9038-b88c-4aa5-bc32-ba1d7447972a" />

(I also added silkscreen later)


Then I added 3D models from Grabcad and in the end the 3d viewer looked something like this:

<img width="678" height="592" alt="Screenshot 2026-07-18 003307" src="https://github.com/user-attachments/assets/d8f75fd8-d40b-4d1c-902a-4bfa2a535e9a" />


I spent the next almost 4 hours doing the CAD.

It was very painful.

Especially because I wasn't very used to all the features of it up till that point but I'd like to think that I am now.

I had to remove some parts because they were covering some of the PCB.

Here's the different parts and the final assembly:

Base:

<img width="357" height="337" alt="image" src="https://github.com/user-attachments/assets/2bfd905d-51b3-45bb-8782-fadb46a0f13b" />

Lid:

<img width="1056" height="677" alt="image" src="https://github.com/user-attachments/assets/586f4fb4-1b81-4b89-8516-cc42ba4ceec5" />

Final assembly:
<img width="1022" height="717" alt="image-1" src="https://github.com/user-attachments/assets/7d166f43-aacb-4a62-bb46-18b4262e8ea2" />



# JULY 17th DAY 5 CUMULATIVE TIME:21.4 HOURS

Also I renamed the thing Lily-Pad because it kind of looks like one because I made it green.

I did the firmware code today. I used kmk firmware and circuit python to code it.

I can't screenshot for some reason but it's in repo. 

And that's pretty much my project done.



I've learnt a lot and had to look up tons of stuff but it was a very successful first project I think, having known nothing before. Very fun.











