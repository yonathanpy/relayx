![Security Banner](https://publicdomainpictures.net/pictures/250000/t2/cyber-security-1515836154wzI.jpg)
# RELAYX

Lightweight TCP relay designed for controlled traffic forwarding and network flow observation.

---

## Overview

RELAYX acts as an intermediary between a local listener and a remote endpoint, forwarding traffic in both directions.

It is built to simulate pivoting behavior in segmented environments without unnecessary abstraction.

---

## Execution Flow

1. Bind to local port
2. Accept incoming connection
3. Establish outbound connection
4. Forward traffic bidirectionally

---

## Structure

```id="rstruct"
main.py
```

---

## Run

```id="rrun"
python main.py
```

---

## Characteristics

* Thread-based session handling
* Direct socket communication
* Minimal overhead
* Transparent data flow

---

## Use Cases

* Lab-based network testing
* Traffic inspection setups
* Controlled relay scenarios

---

## Design

RELAYX avoids frameworks and keeps execution close to the system level.

---
