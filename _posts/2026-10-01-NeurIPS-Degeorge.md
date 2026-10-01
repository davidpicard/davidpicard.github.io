---
layout: post
title: "Balancing Frequencies and Pixels in Flow Matching"
categories: publications
authors: Lucas Degeorge, Paul Couairon, Arijit Ghosh, Alexei A. Efros, David Picard, Vicky Kalogeiton
venue: "NeurIPS"
arxiv: https://arxiv.org/abs/2609.02748
image: /images/fvloss.png
---

Natural images follow a 1/f² spectral distribution: most signal energy lies in the low spatial frequencies, while the perceptually important structures such as textures and edges occupy sparse high-frequency bands. Pixel-space reconstruction objectives, however, treat all spatial errors uniformly, causing low frequencies to dominate the optimization signal and delaying the learning of fine-scale details. In this work, we identify this objective-level spectral imbalance as a key inefficiency in training pixel-space flow models. To address it, we propose a Focal Log-Frequency Loss (f-loss), a spectrally balanced objective that equalizes the learning signal across frequencies, emphasizing high-frequency components that are otherwise underrepresented in pixel-space objectives.
