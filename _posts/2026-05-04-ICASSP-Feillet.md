---
layout: post
title: "Polynomial Mixing for Efficient Self-supervised Speech Encoders"
categories: publications
authors: Eva Feillet, Ryan Whetten, David Picard, Alexandre Allauzen
venue: "ICASSP"
arxiv: https://arxiv.org/abs/2603.00683
image: /images/pomspeech.png
---

State-of-the-art speech-to-text models typically employ Transformer-based encoders that model token dependencies via self-attention mechanisms. However, the quadratic complexity of self-attention in both memory and computation imposes significant constraints on scalability. In this work, we propose a novel token-mixing mechanism, the Polynomial Mixer (PoM), that computes a polynomial representation of the input with linear complexity with respect to the input sequence length. We integrate PoM into a self-supervised speech representation learning framework based on BEST-RQ and evaluate its performance on downstream speech recognition tasks.
