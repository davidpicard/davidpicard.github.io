---
layout: post
title: "Latent reweighting, an almost free improvement for GANs"
categories: publications
authors: Thibaut Issenhuth, Ugo Tanielian, David Picard, Jérémie Mary
venue: "IEEE/CVF Winter Conference on Applications of Computer Vision"
arxiv: https://arxiv.org/abs/2110.09803
image: /images/latentrs.jpg
---

Standard formulations of GANs, where a continuous function deforms a connected latent space, have been shown to be misspecified when fitting different classes of images. In particular, the generator will necessarily sample some low-quality images in between the classes. Rather than modifying the architecture, a line of works aims at improving the sampling quality from pre-trained generators at the expense of increased computational cost. Building on this, we introduce an additional network to predict latent importance weights and two associated sampling methods to avoid the poorest samples.
