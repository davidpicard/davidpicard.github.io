---
layout: post
title: "Learning Uncertainty for Safety-Oriented Semantic Segmentation in Autonomous Driving"
categories: publications
authors: Victor Besnier, David Picard, Alexandre Briot 
venue: "International Conference on Image Processing"
arxiv: https://arxiv.org/abs/2105.13688
image: /images/icip21.jpg
---

In this paper, we show how uncertainty estimation can be leveraged to enable safety critical image segmentation in autonomous driving, by triggering a fallback behavior if a target accuracy cannot be guaranteed. We introduce a new uncertainty measure based on disagreeing predictions as measured by a dissimilarity function. We propose to estimate this dissimilarity by training a deep neural architecture in parallel to the task-specific network. It allows this observer to be dedicated to the uncertainty estimation, and let the task-specific network make predictions. We propose to use self-supervision to train the observer, which implies that our method does not require additional training data.
