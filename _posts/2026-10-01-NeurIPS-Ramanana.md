---
layout: post
title: "One View Is Enough: In-the-Wild Monocular Pretraining for Novel View Generation"
categories: publications
authors: Adrien Ramanana Rahary, Nicolas Dufour, Patrick Perez, David Picard
venue: "NeurIPS"
arxiv: https://arxiv.org/abs/2603.23488
image: /images/ovie.png
---

Monocular novel-view synthesis has long required multi-view image pairs for supervision, limiting training to a narrow set of purpose-built datasets. We propose in-the-wild monocular pretraining: a frozen depth estimator lifts each source image into 3D and reprojects under sampled poses to yield pseudo-target views; masked losses restrict supervision to valid regions and an adversarial objective covers disoccluded areas. Scaled to 30 million uncurated images, this produces OVIE, requiring only a source image and target pose at inference.
