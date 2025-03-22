---
layout: post
title: "Around the World in 80 Timesteps: A Generative Approach to Global Visual Geolocation"
categories: publications
authors: Nicolas Dufour, David Picard, Vicky Kalogeiton, Loic Landrieu
venue: "CVPR"
arxiv: https://arxiv.org/abs/2412.06781
code: https://nicolas-dufour.github.io/plonk
image: /images/diffplonk.png
---

Global visual geolocation predicts where an image was captured on Earth. Since images vary in how precisely they can be localized, this task inherently involves a significant degree of ambiguity. We propose the first generative geolocation approach based on diffusion and Riemannian flow matching, where the denoising process operates directly on the Earth's surface. In addition, we introduce the task of probabilistic visual geolocation, where the model predicts a probability distribution over all possible locations instead of a single point.
