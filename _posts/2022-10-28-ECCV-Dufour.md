---
layout: post
title: "SCAM! Transferring Humans Between Images with Semantic Cross Attention Modulation"
categories: publications
authors: Nicolas Dufour, David Picard, Vicky Kalogeiton
venue: "ECCV 2022"
arxiv: https://arxiv.org/abs/2210.04883
code:https://github.com/nicolas-dufour/SCAM
image: /images/scam.jpg
---

We introduce SCAM (Semantic Cross Attention Modulation), a system that encodes rich and diverse information in each semantic region of the image (including foreground and background), thus achieving precise generation with emphasis on fine details. This is enabled by the Semantic Attention Transformer Encoder that extracts multiple latent vectors for each semantic region, and the corresponding generator that exploits these multiple latents by using semantic cross attention modulation. It is trained only using a reconstruction setup, while subject transfer is performed at test time. Our analysis shows that our proposed architecture is successful at encoding the diversity of appearance in each semantic region.
