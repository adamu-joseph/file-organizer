# ADR-0001: File Organizer Configuration Structure

## Status
Accepted

## Context
We need a clean and scalable configuration system for a file organizer script that categorizes files into folders based on file extensions. The configuration should be easy to extend, readable, and portable.

## Decision
We will use a YAML-based configuration structure to define:
- Target folder location
- File category mappings (folder name → list of extensions)

## Rationale
- YAML is human-readable and easy to modify
- Separates logic from configuration
- Makes it easy to add new file types without changing code
- Works well for small automation tools and scripts

## Implementation Details
The configuration will be loaded into Python and used for file sorting logic.

## Consequences

###Positive
- Easy to extend categories
- Clean separation of config and logic
- Beginner-friendly and maintainable

### Negative
- Requires YAML parsing dependency (pyyaml)
- No strict schema validation unless added later

## Alternatives Considered
- Hardcoding dictionaries in Python → rejected (not scalable)
- JSON configuration → rejected (less readable than YAML)
- Database-driven config → overkill for this project

## Future Improvements
- Add validation schema (e.g., Pydantic)
- Support nested categories (e.g., Images → Photos, Icons)
- Add GUI for editing config
- Auto-detect file types using MIME detection