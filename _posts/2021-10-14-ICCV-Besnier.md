---
layout: post
title: "Triggering Failures: Out-of-Distribution Detection by Learning From Local Adversarial Attacks in Semantic Segmentation "
categories: publications
authors: Victor Besnier, Andrei Bursuc, David Picard, Alexandre Briot 
venue: "International Conference on Computer Vision"
arxiv: http://arxiv.org/abs/2108.01634
code: https://github.com/valeoai/obsnet
image: /images/obsnet.jpg
---

In this paper, we tackle the detection of out-of-distribution (OOD) objects in semantic segmentation. By analyzing the literature, we found that current methods are either accurate or fast but not both which limits their usability in real world applications. To get the best of both aspects, we propose to mitigate the common shortcomings by following four design principles: decoupling the OOD detection from the segmentation task, observing the entire segmentation network instead of just its output, generating training data for the OOD detector by leveraging blind spots in the segmentation network and focusing the generated data on localized regions in the image to simulate OOD objects. 
