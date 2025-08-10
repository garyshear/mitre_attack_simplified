# MITRE Attack Simplified

**Creates a JSON to programmatically work with MITRE ATT&CK**

A lightweight Python package that transforms MITRE ATT&CK data into a simplified JSON format for easy programmatic access.
<br>Shrinks the 42mb STIX file to 1.7mb.

---

## Overview

This repository provides:
- `mitre_data.py` – a script (or module) to parse and extract MITRE ATT&CK data.
- `mitre_attack_functions.py` – utility functions to help interact with and manipulate the simplified data.
- `mitre_simplified.json` – the resulting simplified JSON representation of MITRE ATT&CK.

The goal is to make ATT&CK data easier to work with in custom integrations, tools, or analyses.

---

## Features

- Transforms complex ATT&CK datasets (likely STIX format) into a concise JSON structure.
- Offers utility functions to query, filter, or manipulate ATT&CK data in simplified form.
- Minimizes dependencies and complexity to support quick scripting and automation tasks.

---

## Functions

The `mitre_attack_functions.py` script provides helper functions to interact with the simplified MITRE ATT&CK dataset.

- **`get_all_tactics()`** – Returns a list of all tactics.
- **`get_tactic(tactic)`** – Gets details about a specific tactic.
- **`get_techniques_from_tactic(tactic)`** – Lists techniques under a given tactic.
- **`get_technique(technique)`** – Gets details about a specific technique.
- **`get_subtechniques_from_technique(technique_name)`** – Lists subtechniques for a given technique.
- **`get_subtechnique(subtech_name)`** – Gets details about a specific subtechnique.
- **`get_ttp_by_id(id)`** – Retrieves a tactic, technique, or subtechnique by MITRE ATT&CK ID.
- **`get_ttp_by_name(name)`** – Retrieves details for a tactic, technique, or subtechnique by name.
- **`get_random_ttp()`** – Returns details for a random tactic, technique, or subtechnique.



