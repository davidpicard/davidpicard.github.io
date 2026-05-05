---
layout: post
title: "MIRO: MultI-Reward cOnditioned pretraining improves T2I quality and efficiency"
categories: publications
authors: Nicolas Dufour, Lucas Degeorge, Arijit Ghosh, Vicky Kalogeiton, David Picard
venue: "ICML"
arxiv: https://arxiv.org/abs/2510.25897
image: /images/miro.png
---

The default paradigm of post-training text-to-image generators includes post-hoc selection of generated images, and subsequent training with one reward model to align the generator to the reward, typically user preference. This discards informative data as well as optimizes only for a single reward, hence harming diversity, semantic fidelity and efficiency. Instead, we propose MIRO, a method that conditions the model on multiple rewards during training, thus letting the model learn user preferences directly. MIRO pre-training both improves the visual quality of the generated images and speeds up the training, achieving state of the art on the GenEval compositional benchmark and user-preference scores (PickAScore, ImageReward, HPSv2).
