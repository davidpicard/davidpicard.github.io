---
layout: post
title: "Don’t drop your samples! Coherence-aware training benefits Conditional diffusion"
categories: publications
authors: Nicolas Dufour, Victor Besnier, Vicky Kalogeiton, David Picard
venue: "CVPR"
arxiv: https://arxiv.org/abs/2405.20324
code: https://github.com/nicolas-dufour/CAD
image: /images/cad.jpg
---

We propose the Coherence-Aware Diffusion (CAD), a novel method that integrates coherence in conditional information into diffusion models, allowing them to learn from noisy annotations without discarding data. We assume that each data point has an associated coherence score that reflects the quality of the conditional information. We then condition the diffusion model on both the conditional information and the coherence score. In this way, the model learns to ignore or discount the conditioning when the coherence is low. 
