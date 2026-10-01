# Mnemosync MVP

A simple in-memory memory manager using FastAPI.

## Usage

### Demo
```bash
python -c "from main import demo; demo()"
```

### Tests
```bash
pytest -q
```

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[Client] -->|HTTP| B(FastAPI App)
    B -->|Route| C[MemoryManager]
    C -->|Store/Retrieve| D[In-Memory Dict]
    D -->|Data| C
    C -->|Response| B
    B -->|JSON| A
```

</details>
