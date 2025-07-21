# Fermat MCP

This project provides a FastMCP server for mathematical computations, including numerical and symbolic calculations, as well as plotting.

## Modules

### 1. mpl_mcp - Matplotlib Integration

| Feature | Description |
|---------|-------------|
| `plot_barchart` | Plots bar charts of given data values |
| `plot_scatter` | Creates scatter plots from data points |
| `plot_chart` | Plots line, scatter, or bar charts |
| `plot_stem` | Creates stem plots for discrete data |
| `plot_stack` | Generates stacked area/bar charts |
| `eqn_chart` | Plots mathematical equations |

### 2. numpy_mcp - NumPy Integration

| Category | Operations |
|----------|------------|
| **Basic Math** | add, sub, mul, div, power, abs, exp, log, sqrt |
| **Trigonometric** | sin, cos, tan |
| **Statistics** | mean, median, std, var, min, max, argmin, argmax, percentile |
| **Linear Algebra** | dot, matmul, inv, det, eig, solve, svd |
| **Matrix Operations** | create, zeros, ones, full, arange, linspace |
| **Array Manipulation** | reshape, flatten, concatenate, transpose, stack |

### 3. sympy_mcp - SymPy Integration

| Category | Operations |
|----------|------------|
| **Algebra** | simplify, expand, factor, collect |
| **Calculus** | diff, integrate, limit, series |
| **Equations** | solve, solveset, linsolve, nonlinsolve |
| **Matrix Operations** | create, det, inv, rref, eigenvals |

## Setup

### Requirements

- Python 3.12 or higher (To install Python3.12 follow [Python Download](https://www.python.org/downloads/))

- uv (To install uv follow [uv Installation](https://docs.astral.sh/uv/getting-started/installation/))

#### Clone the repository

```bash
git clone https://github.com/abhiphile/fermat-mcp
```

### Visual Studio Code, Windsurf

Add the following to your `settings.json`:

```json
{
  "mcpServers": {
    "fmcp": {
      "command": "bash",
      "args": ["/path/to/fermat-mcp/setup.sh"],
      "description": "fmcp server is for mathematical computations, including numerical and symbolic calculations, as well as plotting."
    }
  }
}
```

### Gemini CLI
- Open your Gemini settings JSON located in ~/.gemini/settings.json where ~ is your home directory.

- Add the following to your settings.json:

```json
{
  "mcpServers": {
    "fmcp": {
      "command": "bash",
      "args": ["/path/to/fermat-mcp/setup.sh"],
      "description": "fmcp server is for mathematical computations, including numerical and symbolic calculations, as well as plotting."
    }
  }
}
```

### Example Usage
