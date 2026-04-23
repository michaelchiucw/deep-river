# Online deep learning for data streams

<div class="landing-hero">
  <p class="landing-eyebrow">deep-river + river + PyTorch</p>
  <p class="landing-lead">
    deep-river is a research-oriented library for incremental deep learning. It combines river's
    streaming machine learning API with PyTorch modules to support reproducible experimentation,
    continual model updates, and evaluation under non-stationary data streams.
  </p>
  <div class="landing-cta-row">
    <a class="landing-cta landing-cta-primary" href="getting_started/">Read getting started</a>
    <a class="landing-cta" href="examples/">Review notebooks</a>
    <a class="landing-cta" href="reference/">Read API docs</a>
  </div>
</div>

## Install

```bash
pip install deep-river
```

or install through river extras:

```bash
pip install "river[deep]"
```

## Why deep-river

- **Online training:** Update your model incrementally with `learn_one` and `learn_many`.
- **PyTorch flexibility:** Use custom modules, losses, and optimizers.
- **river compatibility:** Compose with preprocessing, metrics, and pipelines from river.

## Suggested reading path

1. Install the package with `pip`.
2. Follow [Getting started](getting_started.md) to build a baseline online classifier.
3. Use [Examples](examples/index.md) to reproduce end-to-end task workflows.
4. Inspect [Benchmarks](benchmarks/index.md) to compare model behavior across datasets.
5. Consult [API Reference](reference/index.md) for estimator details and parameter semantics.

## Explore

- [Getting started](getting_started.md)
- [Examples](examples/index.md)
- [Benchmarks](benchmarks/index.md)
- [API Reference](reference/index.md)
- [GitHub](https://github.com/online-ml/deep-river)
- [PyPI](https://pypi.org/project/deep-river/)
