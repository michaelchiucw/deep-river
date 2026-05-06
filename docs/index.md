---
title: deep-river
---

# Online deep learning with PyTorch and river

<section class="landing-hero">
  <div class="landing-hero-content">
    <img class="landing-logo" src="img/logo.png" alt="deep-river">
    <p class="landing-eyebrow">deep-river</p>
    <p class="landing-lead">
      Train PyTorch models incrementally on data streams with river's familiar
      <code>predict_one</code>, <code>learn_one</code>, metrics, and pipeline APIs.
    </p>
    <div class="landing-cta-row">
      <a class="landing-cta landing-cta-primary" href="getting_started/">Get started</a>
      <a class="landing-cta" href="examples/">Examples</a>
      <a class="landing-cta" href="reference/">API reference</a>
      <a class="landing-cta" href="https://github.com/online-ml/deep-river">GitHub</a>
    </div>
  </div>
</section>

<section class="landing-grid landing-intro-grid">
  <div class="landing-panel">
    <h2>Install</h2>
    <pre><code>pip install deep-river</code></pre>
    <p>or install through river extras:</p>
    <pre><code>pip install "river[deep]"</code></pre>
  </div>
  <div class="landing-panel landing-code-panel">
    <h2>Streaming model loop</h2>
    <pre><code>metric = metrics.Accuracy()

for x, y in stream:
    y_pred = model.predict_one(x)
    metric.update(y, y_pred)
    model.learn_one(x, y)</code></pre>
  </div>
</section>

## Why deep-river

<div class="landing-card-grid">
  <div class="landing-card">
    <h3>Online updates</h3>
    <p>Learn from one sample or mini-batch at a time with stream-first estimators.</p>
  </div>
  <div class="landing-card">
    <h3>PyTorch modules</h3>
    <p>Bring your own architectures, losses, optimizers, and representation learning setup.</p>
  </div>
  <div class="landing-card">
    <h3>river ecosystem</h3>
    <p>Compose with river preprocessing, datasets, metrics, and pipelines.</p>
  </div>
</div>

## Start here

- [Getting started](getting_started.md): build and evaluate your first online classifier.
- [Examples](examples/index.md): run complete workflows for classification, regression, anomaly detection, and continual learning.
- [API Reference](reference/index.md): inspect estimator parameters, methods, and module-level utilities.
- [Benchmarks](benchmarks/index.md): compare model behavior across standard streaming datasets.
