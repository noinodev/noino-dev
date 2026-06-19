---
title: cerebroid
date: 2019-01-01
slug: cerebroid
tags: [gamemaker]
description: first big game project
thumbnail: /assets/images/projects/cerebroid-spider.png
---

##cerebroID game

I started this game when I was still in highschool and using gamemaker studio 1.4. At the time I was playing a lot of Escape From Tarkov and really enjoyed the weapon customisation and inventory system, so I replicated that in a 2D-sidescrolling game. This game was effectively my first exposure to graphics programming, writing shaders, and managing memory. Even though I achieved a lot with this project, using it as a learning tool also led to it being unfinishable in its current form. I really liked the idea for this game though, so if I had the time I would definitely want to remake it knowing what I know now. :)

<img src=/assets/images/projects/cerebroid-plate.png>

The idea for the game was that you play as a nerd in his basement who missed the AI apocalypse happening right outside his door. The whole world, drunk on these black mirror / neuralink kind of brain devices, is suddenly enslaved by the AI. The game was set to begin with one of these enslaved people, who happens to be a action-hero type of character, stumbling into the filthy basement. The basement is so disgusting that the chip crashes, giving the protagonist the chance to hack into it and interface the action hero in VR through a weird program called 'CerebroID' that suddenly appeared on the computer. From there you play as this awkward dichotomous pair, trying to gather as much computation power as possible (seems very relevant these days) to use CerebroID to stop all the brain chips. Then the basement dweller is forced by necessity to leave the basement right at the end, to save the guy who saved him at the beginning. Really heartwarming stuff and not at all inspired by Neon Genesis Evangelion and the entire loser subgenre around it. Is what I would say if it wasn't written in the notes I took for the game's story. 

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/uoNewUu.mp4" type="video/mp4">
</video>

Developing this game was kind of my introduction to graphics and systems. The terrain specifically was quite challenging at the time, as I was just learning to manage large amounts of data to be drawn, while also ensuring persistence. I settled on a chunk-based system with a texture for each chunk, which allowed me to subtract individual pixels for granular, satisfying destruction.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/VA3CNoI.mp4" type="video/mp4">
</video>

The entire aesthetic and style I actually lifted from a throwaway drawing someone did in the GameMaker discord in 2018 or so. Bloom effects were used in this drawing, which is also why the light effects in this game are simply raster sprites with additive blending. I thought it looked decent at the time. The first real shaders I ever wrote were for the outdoor global lighting, such as the god rays through foliage, and the fade to black in the ground. 

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/IAUnKKW.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/7h6nmO6.mp4" type="video/mp4">
</video>

I would say my two favourite parts of this game were the animations and the item system. The animations were entirely procedural for all characters, so I explored different interpolation methods, inverse kinematics, and other procedural techniques to make the characters look interesting.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/KGnful5.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/zRtMr2a.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/9anmX39.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/rx8FRzz.mp4" type="video/mp4">
</video>

The item system, on the other hand, was a lot heavier than it probably needed to be. The idea was for it to be as dynamic as possible, and the hammer tool I knew of at the time was hashmaps. So every item in the level is an entry in a hashmap, potentially containing pointers to other hashmaps. In my multiplayer tests, and in serialisation, this became annoying because I had to convert the pointer to real data, and then into JSON, which was surprisingly difficult to get right (from what I remember). 

All of the weapons, armour, deployable objects, and so on were completely runtime dynamic and loaded through various JSON files, so the item properties were not hardcoded and new ones could be added easily.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/w2nemD9.mp4" type="video/mp4">
</video>

I also experimented a LOT in this project. 2D physics, multiplayer, map editors, world layering, enemy AI, the list of things I wanted to add was endless. In hindsight this is what killed the game. The core idea I believe is good, but getting sidetracked on different sub-loops, instead of doing 'chores' of the main game like UI and level design, as well as the overwhelming technical debt that comes from starting a game project when you're in highschool, ultimately sunk any hope of this project being finished,

Got some cool videos out of it though, and most of all this was the foundation of almost everything I know about graphics today.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/RzK2IQw.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/MPcuqY2.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/nGknG55.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/LlEVdez.mp4" type="video/mp4">
</video>

I compiled a 3 minute youtube video of development progress through its life cycle. I basically stopped working on it as soon as I started studying at university. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/QuWgdgaP8_Y?si=YTXw9O5lOqvlxoDD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<script src="/assets/js/lazy-videos.js"></script>