---
title: image-space radiance cascades
date: 2026-02-18
slug: radiance-cascades
tags: [radiance cascades, global illumination, vulkan]
description: research project for radiance cascades global illumination
thumbnail: /assets/images/cornell.png
---
## Radiance Cascades Global Illumination

I am working on a global illumination solution that uses an old and rarely used spherical ray marching technique, and radiance cascades, to be a weird middle ground between reflective shadow maps and screen space global illumination. I have a lot of work to do on it but the basic proof-of-concept is together and the performance and quality results are very promising. 

I wrote this thing on it that goes through some of the literature background, and details what I want done by around October. If it all goes well, I am aiming to write an article on this technique for publication. My university Honours thesis covers the history of lighting for computer graphics.

<a href="/assets/pdf/assignment-redacted.pdf">Research proposal paper</a> its not perfect and was first a university coursework submission but it covers what I am trying to do and why.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/Wq1lF0P.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/LDfWs6S.mp4" type="video/mp4">
</video>

The technique started from wanting to get the original specular reflection technique going in a custom Vulkan renderer I spun up at the beginning of the year.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/mybsUOE.mp4" type="video/mp4">
</video>

From there I started exploring some SSGI-like techniques using the same ray traversal proxy.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/DaOegEI.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/uTI2QBe.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/LUkMqra.mp4" type="video/mp4">
</video>

Then I was led to radiance cascades, and became almost completely immersed in global illumination literature, transport theory, and the history of global illumination techniques. Very cool stuff.

<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/gZCstBp.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/kceyhWa.mp4" type="video/mp4">
</video>
<video class="lazy-video" controls autoplay muted loop playsinline width="540" preload="none">
  <source src="https://imgur.com/nqdSgb2.mp4" type="video/mp4">
</video>

There will be a LOT more to come in here, as this is actively WIP. I post live updates on my X and in my Discord server.

<script src="/assets/js/lazy-videos.js"></script>

