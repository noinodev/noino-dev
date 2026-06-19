---
title: tank combat simulator
date: 2025-03-01
slug: tanksim
tags: [raylib]
description: ros noetic tank combat simulator and clients
thumbnail: /assets/images/projects/tanksim.png
---
##Tank Combat Simulator

<a href=https://github.com/noinodev/ros-tanksim>github repository</a>

This project was a very fast prototype of a multi-agent robotics simulation for a 3rd-year course. We were required to use ROS Noetic, which is very old, and had no windows support at all. Just for this project, I actually bought a (very terrible) laptop and installed bare-metal Linux for the first time. Xubuntu 20.04 specifically. It's an AMD 3020e Lenovo IdeaPad, and it was so bad that even the lightest distro google gave to me was still way too slow. I do not know why these things even come preloaded with windows it was completely unusable. 

I do not have access to the toolchain to run the program anymore, so I have very little footage of it working. The basic idea was two parts. S raylib + ODE based simulation engine, with a ROS Noetic interface for multi-agent sensor and actuator subscription through dynamic runtime namespaces. 

The requirements of the assignment were to use a high-level motion planning library called PAT, and the Gazebo simulator, but I chose a custom engine for two reasons: this stack cannot actually do the multi-agent simulation we needed, and I was very stubborn and wanted to stretch my legs a bit. I was coming off a high of a data structures and algorithms course, where I wrote some nasty data structures in C, so stepping back down to a raylib+ODe pair was actually a breath of fresh air. 

THe simulator came together very quickly. Tank agents could be added and namespaced, with a real-time sensor protocol for GPS, gyro and spinning LIDAR. I then wrote a ROS client to interface with the engine, where multiple individual instances could control an individual agent in the simulator. 

The engine itself was backed by a custom Entity-Component system, which allowed runtime composition of robots and hierarchical parts for them. For example, the tank body and turret are separate entities entirely, linked through a parenting system of the ECS. Individual sensors are each components that can be attached to an entity, and everything is automatically passed through the interface in real-time.

The navigation stack used is a hybrid between Vector Field Histogram (VFH), which is a fancy way of saying how far away each angular bin of a spinning LIDAR system is, Reactive Potential Field (RPF), which calculates a 'pushing' force from the VFH to avoid flat surfaces and prefer flat terrain.

Then finally global pathing is calculated through A*, where the terrain heightfield is reconstructed from LIDAR data through a SLAM-lite method. Linear and angular PID are also used for acceleration and differential steering.

These combined methods enable real-time navigation of completely unknown environments, including uneven terrain, through effective tuning of these techniques. There were further planned features, such as team-combat dynamics and objectives, but I ran out of time for the assignment. 

Overall it was a great learning experience, especially for navigation algorithms, spatial partitioning, learning spatial transforms like quaternions, asynchronous systems and parallelism, and much more. 

If I were to start this again I probably would aim for a more parallelised or distributed architecture, and a more 'real-world' sensor protocol to possibly analogue real devices. In terms of agent control, exploring reinforcement learning has been a long-term goal of mine. Libraries like Pufferlib would be great for that, because the environment models are raylib-based, and I may be able to make something interesting from that.

Anyway here is a really awful clip I took. It's not perfect because the tanks are told to navigate to a random point, and when its unreachable it just drives into the wall. The angular PID is also kind of fiddly so sometimes it prefers to drive backwards.

<iframe width="560" height="315" src="https://www.youtube.com/embed/uQ2flGaD-WY?si=o-8P2GL3isB0fptH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
