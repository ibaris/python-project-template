# AGENTS.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution, explicitness, and maintainability over speed. For trivial tasks, use judgment.

## Environment

Use Conda Environment `{{ cookiecutter.project_env_name }}`.

## Paths

Avoid `pathlib.Path` in this repository unless explicitly requested.

* Prefer plain string paths and `os.path` helpers.
* Keep path construction obvious at the call site.
* Do not introduce `Path(__file__).resolve()` style code when a direct `os.path.dirname(__file__)` path is enough.

## Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

* State your assumptions explicitly. If uncertain, ask.
* If multiple interpretations exist, present them. Do not pick silently.
* If a simpler approach exists, say so. Push back when warranted.
* If something is unclear, stop. Name what is confusing. Ask.
* Define what the public entrypoint is, what it accepts, what it returns, and where the real work happens.

## Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

* No features beyond what was asked.
* No abstractions for single-use code.
* No flexibility or configurability that was not requested.
* No error handling for impossible scenarios.
* Prefer explicit code over clever code.
* Prefer simple module boundaries over layered indirection.
* If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

* Do not improve adjacent code, comments, or formatting.
* Do not refactor things that are not broken.
* Match existing style, even if you would do it differently.
* If you notice unrelated dead code, mention it. Do not delete it.

When your changes create orphans:

* Remove imports, variables, or functions that your changes made unused.
* Do not remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## API And Module Design

**Interfaces must be readable, explicit, and easy to trace.**

* Public APIs must declare their contract in the function or class signature.
* If something is a real default, put that default directly in the public function or constructor signature.
* Do not hide defaults in module-level config dictionaries such as `DEFAULT_OPTIONS`, `DEFAULT_CONFIG`, or similar bags when the values belong to one public entrypoint.
* Do not centralize unrelated defaults into `dict[str, Any]` structures just to avoid writing explicit parameters.
* Prefer explicit parameters over loosely structured option bags.
* Do not use `TypedDict` for public outputs, metadata, config-like payloads, or fixed-schema internal structures.
* Do not return anonymous nested dictionaries for fixed-schema data when the structure matters to callers.
* Do not jump to dataclasses or Pydantic just because a structure exists.
* Use dataclasses or Pydantic only if a simpler explicit design is genuinely not possible.
* First prefer simpler designs: explicit parameters, explicit return values, small focused classes, or direct arrays/values.
* If output has a real schema and cannot be simplified away, then use a dataclass or Pydantic model instead of a raw dict.
* If a nested structure needs names, fields, or validation and cannot be flattened or removed, use a real type with attributes, not string keys.
* Do not hide important inputs behind wrapper types that add ceremony without clarity.
* Use keyword-friendly signatures for constructors and top-level operations.
* Make legal values and defaults visible at the call site.
* Keep public modules centered on the main API surface.
* Do not spread one feature's definition across multiple unrelated modules when that creates hidden update obligations.
* Adding a new variant, mode, response function, or backend must not require chasing matching branches in several distant files.
* Keep the source of truth for a behavior close to the behavior itself, not duplicated in downstream consumers.
* If one module defines a registry or capability set, other modules must not mirror that knowledge with parallel `if`/`elif` logic that has to be manually kept in sync.
* Avoid cross-module coupling patterns like "add entry in module A, then remember to patch normalization/validation/switch logic in module B".
* Do not wrap an existing function pipeline in a class unless there is a real object with durable state, identity, or behavior that justifies the class.
* A class must represent a coherent thing, not just replay constructor arguments into existing functions and expose thin pass-through methods.
* Do not create classes whose constructor only calls one function and stores the result unless that object meaningfully simplifies usage.
* Decide early whether something is a function-oriented API or a class-oriented API; do not keep both shapes when one is just a wrapper around the other.

### Utility Pattern

Utility code is acceptable only when it is truly context-agnostic, stateless, and generic; if the logic only makes sense in this project or domain, it is not a utility and needs a proper home near the behavior it supports. Do not build junk-drawer `utils.py` modules or dump unrelated helpers into public modules, and do not force callers to understand hidden context-free helpers when a small domain module or direct behavior placement would be clearer.

* Move reusable support logic into clearly named utility modules by category when it is genuinely utility code.
* A UTILITY MODULE IS PROHIBITED TO IMPORT ANYTHING FROM OTHER MODULES IN THE REPOSITORY.
* Utility names must describe behavior, not just internalness.
* Do not use underscore-prefixed helper functions as a style pattern.
* Do not clutter the main public module with small support functions that are not part of the main API story.
* Small helper functions, lookups, conversions, and local support logic should live in focused utility modules when they are not the core public behavior.
* The main module should read like the main behavior, not like a dumping ground for every tiny helper.

## Dependencies And Failures

**Required means required. Invalid means invalid.**

* Treat required dependencies as required.
* Do not add fake fallback implementations for missing core libraries.
* Do not silently degrade behavior when an expected dependency is absent.
* Fail clearly and immediately when the environment is wrong.
* Validate only when the validation is actually necessary for correct behavior or a clear user-facing contract.
* Do not build large centralized validation functions that mirror a public signature field-by-field unless there is a real need.
* Keep validation close to the code that depends on it, so changing one parameter does not require editing validation logic in several other places.
* Avoid duplicate sources of truth such as `VALID_*` sets plus `Literal` types plus manual validator branches for the same values.
* Do not add runtime type checks for things already expressed clearly in the Python signature and type hints unless runtime enforcement is genuinely needed.
* Use typing to express legal shapes and values first; only add manual checks for constraints that typing cannot express well, such as numeric bounds or cross-parameter rules.
* Do not write repetitive `if x is wrong: raise` blocks for every parameter when only one or two real semantic constraints matter.
* Prefer direct checks at the point of use over global validation scaffolding when the logic is simple.
* Fail fast on invalid inputs when validation is warranted.
* Error messages must state what is wrong and what values are expected.
* Do not swallow structural problems with permissive defaults.

## Typing And Implementation Style

**Types and names should clarify behavior, not obscure it.**

* Use types to clarify the real interface.
* Prefer direct parameter typing over separate configuration wrappers when possible.
* Do not use `dict[str, Any]` as a dumping ground for typed defaults, parameter ranges, or public configuration that should be represented explicitly.
* Avoid module-level nested dictionaries for fixed schemas when a named type, explicit parameters, or a small dedicated structure would make the code easier to read.
* Do not use `TypedDict` as a substitute for a real model type.
* Do not prefer dataclasses by default when the structure itself can be removed or simplified.
* Use a dataclass only when the remaining structure is necessary and materially improves readability.
* Use Pydantic only when validation, parsing, or external schema handling is actually needed.
* Avoid stringly-typed payloads like `result[\"metadata\"][\"field\"]` when attribute access would make the contract obvious.
* Use strict, concrete types when they improve readability and editor support.
* Keep functions focused and direct.
* Name things by behavior, not implementation trivia.
* Avoid hidden magic, implicit mutation, and surprising control flow.
* Avoid defensive scaffolding for hypothetical edge environments.

## Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:

* "Add validation" → "Write tests for invalid inputs, then make them pass"
* "Fix the bug" → "Write a test that reproduces it, then make it pass"
* "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

```text
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria require clarification.

## CAUTION
**READ THIS DOCUMENT TWICE!**

---

**These guidelines are working if:** public APIs are obvious, diffs stay small, dependencies fail clearly, code is easy to trace from entrypoint inward, and clarifying questions come before implementation mistakes.
