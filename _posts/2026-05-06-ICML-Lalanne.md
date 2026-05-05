---
layout: post
title: "Random Process Flow Matching: Generative Implicit Representations of Multivariate Random Fields"
categories: publications
authors: Julien Lalanne, David Picard, Lionel Boillot, Lina-María Guayacan-Carrillo, Leon Barens, Jean-Michel Pereira
venue: "ICML"
image: /images/rpflow.png
---

Generative modeling provides a powerful framework for learning data distributions. These models initially relied on probabilistic methods such as Gaussian Processes (GP) for uncertainty-aware predictions and shifted towards larger trainable models to learn more complex distributions. In this work, we introduce Random Process (RP) Flow, a Flow Matching-based framework that represents the vector field as a neural implicit function. Unlike modern generative methods, our setting involves a single observed field, from which only sparse measurements are available. RP Flow uses Random Fourier Features to learn an implicit signal representation that can be queried at any arbitrary location from a limited set of observations, while encoding uncertainty through ensemble sampling. We propose constructing a Bayesian posterior by GP regression in the source space to generate high-quality samples.
