---
layout: post
title: "SSP-Net: Scalable sequential pyramid networks for real-Time 3D human pose regression"
categories: publications
authors:  Diogo C Luvizon, Hedi Tabia, David Picard
venue: "Pattern Recognition"
arxiv: [https://arxiv.org/abs/2210.02231](https://arxiv.org/abs/2009.01998)
image: /images/sppnet.jpg
---

In this paper we propose a highly scalable convolutional neural network, end-to-end trainable, for real-time 3D human pose regression from still RGB images. We call this approach the Scalable Sequential Pyramid Networks (SSP-Net) as it is trained with refined supervision at multiple scales in a sequential manner. Our network requires a single training procedure and is capable of producing its best predictions at 120 frames per second (FPS), or acceptable predictions at more than 200 FPS when cut at test time. We show that the proposed regression approach is invariant to the size of feature maps, allowing our method to perform multi-resolution intermediate supervisions and reaching results comparable to the state-of-the-art with very low resolution feature maps. 
    
