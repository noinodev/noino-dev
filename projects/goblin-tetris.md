---
title: goblin tetris
date: 2024-06-01
slug: goblin-tetris
tags: [java awt]
description: tetris game about crushing goblins, complete with multiplayer
thumbnail: /assets/images/goblin.png
---

##Goblin Tetris

<a href="github.com/noinodev/goblin-tetris">github respository</a>

In a 2nd-year class at university all about object-oriented Java, we were given a 5-person group project to create Tetris to meet certain specifications, specifically including an AI controller, and a multiplayer gamemode. We were expected to use AWT/Swing and produce a simple Java tetris game over a few weeks.

We were also given the option of undertaking the project solo. I did what I do best and started making a game engine in Java. By the end of the day, Tetris was complete.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/R84vNRD.mp4" type="video/mp4">
</video>

Deciding what to do with the game next was the hard part. From there I worked on some basic tile lighting, a particle system, and simple animations for the game. In a very short time it went from a Tetris clone to a kind of nice Tetris clone.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/yLuU1v6.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/8R1zPz7.mp4" type="video/mp4">
</video>

One of the requirements for the assignment was an 'extended mode' where the game was different to normal Tetris. This needed to be done for the end of the semester, but we were made aware during the first part of the project, which made me think about what 'extended mode' I wanted to have. The example given to us was a multiplayer mode where you play against a bot or another player. 

I thought of doing some nonsense like Tetris-becomes-Snake under certain conditions but I could never figure out how that would be even slightly fun. Suddenly I had the best stroke of game design genius of my entire life, and thought about the hardest part of Tetris. Recovering from a bad board state. There were two parts to the idea: clearing prebuilt structures from the board, and crushing moving enemies in and around the structures. From this, Goblin Tetris was created.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/vhGygO9.mp4" type="video/mp4">
</video>

The objective in Goblin Tetris is to clear structures and crush goblins, working through 10 handmade stages of increasing difficulty. The final form of this gamemode is a surprisingly addictive and very difficult Tetris experience, which landed me a solid 100%. If you've seen my CerebroID game, or an indie game called Kingdom, you'll catch the visual design language right away. I'm quite shameless for recycling art.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/aMxpAPE.mp4" type="video/mp4">
</video>

The next step in development was multiplayer. I wanted to challenge myself and adapt this singleplayer game into a PvP multiplayer game, where one player plays Tetris, and the rest play as the goblins. To do that, I had to create the goblin gameplay. I experimented with environment resource gathering, and both creation and destruction of tile structures. 

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/L8LXuzC.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/hG2kMsq.mp4" type="video/mp4">
</video>

The next task was combining the two modes and actually implementing multiplayer. I went for a P2P hole-punching architecture, with a simple matchmaking server that did just that to the extent I understood it at the time.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/lIfQja5.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/ttnEcuH.mp4" type="video/mp4">
</video>

Soon I settled on what I believe is a simple but fun gameplay loop of asymmetrical PvP. The goblins build structures and dig themselves out of holes, and the Tetris player has to clear them out and crush the goblins. 

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/airZwIP.mp4" type="video/mp4">
</video>

You can even bring the bot controller into it to make it particularly unfair for the goblins.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/xTo3mGj.mp4" type="video/mp4">
</video>

I would say overall that this is my most 'functionally complete' game, but because its made in Java it is horribly annoying to build and package for distribution, and it kind of runs terribly because I was under immense time pressure. I want to make a serious attempt at producing this game sometime soon though! Maybe something that builds for web or is at least distributable easily on itch.io. Art is one of my biggest blockers and its already 95% complete in that regard, so whipping up another game engine might be a fun exercise. :)

The <a href="github.com/noinodev/goblin-tetris">github respository</a> has .jar builds of the project, if you want to try it out yourself!

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/v9ThA8y.mp4" type="video/mp4">
</video>

<script src="/assets/js/lazy-videos.js"></script>