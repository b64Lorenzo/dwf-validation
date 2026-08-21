# Rayleigh Comparison Study

## Overview

The Rayleigh Comparison Study is a multi-study validation and benchmarking workflow for comparing wave-elevation statistics across multiple simulations.

The workflow:

1. Loads wave-elevation data from one or more studies.
2. Uses cached data when available.
3. Applies metadata filters.
4. Groups results by selected variables.
5. Computes wave-height statistics.
6. Generates comparison plots.

---

# Features

- Multi-study comparison
- Reference-study based percentage differences
- Rayleigh PDF generation
- Exceedance analysis
- Mean and standard deviation statistics
- Automatic caching
- Flexible filtering system
- Flexible grouping system

---

# Architecture

```text
src/python/
│
├── rayleigh/
│   ├── main.py
│   ├── config.py
│   │
│   ├── analyses/
│   │   └── run_comparison_study.py
│   │
│   └── plotting/
│       └── comparison_plot.py
│
└── utils/
    ├── filters.py
    ├── positions.py
    ├── statistics.py
    └── utils.py
```

---

# Running the Analysis

```bash
python -m rayleigh.main
```

Select the workflow in:

```python
ANALYSIS_TYPE = "comparison"
```

---

# Configuration

All configuration is controlled from:

```python
rayleigh/config.py
```

## Study Definition

```python
COMPARISON_STUDY = {
    "reference_study": "DWF",
    "studies": {
        "DWF": [
            (
                Path("..."),
                "cache_name"
            )
        ]
    }
}
```

## Reference Study

The reference study is used for percentage-difference calculations:

```python
"reference_study": "DWF"
```


Mathematically:

\[
\mathrm{Difference}[\%] =
100 \times
\frac{Q_{study}-Q_{ref}}{Q_{ref}}
\]


---

# Cache System

Processed results are stored as:

```text
cache/*.npy
```

First run:

```text
Read CSV
Extract waves
Build cache
```

Subsequent runs:

```text
Load cache
Filter
Group
Plot
```

---

# Time Window

```python
TIME_WINDOW = (
    None,
    None,
)
```

Examples:

```python
(None, None)
(100, None)
(100, 600)
```

---

# DT Mode

```python
DT_MODE = "ppp"
```

Supported:

- raw
- order
- ppp

PPP:

```text
PPP = 2π / (ω dt)
```

---

# Filtering

Example:

```python
{
    "freq": (None, None),
    "angle": (30, 150),
    "dt": (None, None),
    "dx": (2.5, 2.5),
    "depth": (22.5, 50),
    "pos": None,
}
```

Supported filter types:

- None
- Exact value
- Tuple range
- List
- Set

---

# Grouping

Examples:

```python
["freq"]
["angle"]
["depth"]
["pos"]
["dt"]
```

Combined grouping:

```python
["freq", "dt"]
["depth", "dt"]
["pos", "dt"]
```

---

# Supported Positions

```text
-2xHC
-1xHC
HC
+1xHC
+2xHC
```

Positions are sorted using:

```python
pos_to_order()
```

---

# Generated Figures

Each figure contains:

## Rayleigh PDF

Upper-left panel.

## Exceedance Curve

Upper-right panel.

## Mean & Standard Deviation

Bottom panel.

Mean:

```text
Solid line with markers
```

Standard deviation:

```text
Dashed line
```

## Percentage Difference

Secondary y-axis:

```text
100 * (study - reference) / reference
```

---

# Plot Styling

Top plots:

- Color = grouping variable
- Line style = study

Bottom plots:

- Color = study
- Marker = mean
- Dashed line = standard deviation
- Solid line = percentage difference

---

# Output Files

Example:

```text
compare_freq_ppp_angle30-150_dx2.5-2.5_depth22.5-50_timemin-max.png
```

The filename contains:

- grouping variable
- dt mode
- filter definition
- time window

---

# Typical Workflow

1. Configure studies.
2. Select a reference study.
3. Define filters.
4. Define groupings.
5. Run:

```bash
python -m rayleigh.main
```


# Signal Processing

## Mean Removal

Given a signal:

\[
\eta(t)
\]

The mean is removed:

\[
\eta'(t)=\eta(t)-\bar{\eta}
\]

---

## Wave Height Extraction

For each peak:

\[
H = \eta_{peak}-\eta_{trough}
\]

A wave-height distribution is then assembled.

---

# Statistical Quantities

## Variance

The variance is:

\[
m_0 = \mathrm{Var}(\eta)
\]

implemented as:

```python
np.var(signal)
```

---

## Mean Wave Height

\[
\mu_H = \frac{1}{N}
\sum_{i=1}^{N} H_i
\]

---

## Standard Deviation

\[
\sigma_H=
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
(H_i-\mu_H)^2
}
\]

---

# Rayleigh Distribution

The Rayleigh probability density function used in the plots is:

\[
f(H)=
\frac{H}{4m_0}
\exp\left(
-\frac{H^2}{8m_0}
\right)
\]

where:

\[
m_0
\]

is the variance of the original signal.

---

# Exceedance Distribution

For sorted wave heights:

\[
H_{(1)} \le H_{(2)} \le \dots \le H_{(N)}
\]

The exceedance probability is approximated as:

\[
P(H>h)
=
1-
\frac{i}{N}
\]

---

# DT Transformation Modes

## raw

\[
dt
\]

## order

\[
10^{\lfloor \log_{10}(dt) \rfloor}
\]

## ppp (Points Per Period)

\[
PPP=
\frac{2\pi}{\omega\,dt}
\]

where:

- \(\omega\) = angular frequency [rad/s]
- \(dt\) = numerical timestep [s]

---

# Filters

Example:

```python
{
    "freq": (None, None),
    "angle": (30, 150),
    "dt": (None, None),
    "dx": (2.5, 2.5),
    "depth": (22.5, 50),
    "pos": None,
}
```

Supported forms:

```python
None
90
(30,150)
[30,45,60]
{30,45,60}
```

---

# Grouping

Examples:

```python
["freq"]
["angle"]
["depth"]
["pos"]
["dt"]
```

Combined groupings:

```python
["freq", "dt"]
["angle", "dt"]
["depth", "dt"]
["pos", "dt"]
```

---

# Position System

Supported locations:

```text
-2xHC
-1xHC
HC
+1xHC
+2xHC
```

Ordering:

```text
-2xHC
-1xHC
HC
+1xHC
+2xHC
```

implemented through:

```python
pos_to_order()
```

---

# Generated Figure Layout

```text
+----------------+----------------+
| Rayleigh PDF   | Exceedance     |
+----------------+----------------+
|                                  |
|          Mean & Std              |
|     + % Difference Axis          |
|                                  |
+----------------------------------+
```

## Top Figures

Colour:

```text
grouping variable
```

Line style:

```text
study
```

## Bottom Figure

Colour:

```text
study
```

Visual encodings:

```text
Mean             → solid line + circle markers
Standard Deviation → dashed line
% Difference     → solid line, no markers
```

---

# Output Files

Example:

```text
compare_freq_ppp_angle30-150_dx2.5-2.5_depth22.5-50_timemin-max.png
```

Includes:

- grouping variable
- dt mode
- filters
- time window

---

# Adding New Studies

```python
"NewStudy": [
    (
        Path(r"..."),
        "new_study_cache",
    )
]
```

No source-code changes should be required.

---

# Troubleshooting

## No Progress Bar

Caches are being loaded.

Delete:

```text
cache/*.npy
```

if full processing is required.

## Position Plot Failure

Ensure position-based axes use:

```python
np.arange(len(position_values))
```

for interpolation and not raw strings.

## Empty Plot

Usually caused by overly restrictive filters.

---

# Future Improvements

- Excel report generation
- Automated summary tables
- Statistical significance tests
- Plotly dashboards
- HTML reporting
- Multi-reference comparison mode

---

# Author

Lorenzo Zambelli

## Version

2.0.0
