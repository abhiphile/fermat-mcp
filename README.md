# Fermat MCP

This project provides a FastMCP server for mathematical computations, including numerical and symbolic calculations, as well as plotting.

## Modules

- **mpl_mcp**: Matplotlib integration for plotting.
- **numpy_mcp**: NumPy integration for numerical computation.
- **sympy_mcp**: SymPy integration for symbolic computation.

## Development

### Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for our commit messages. This helps maintain a clean and consistent project history.

#### Commit Message Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### Commit Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semicolons, etc.)
- **refactor**: Code changes that don't fix bugs or add features
- **perf**: Performance improvements
- **test**: Adding or modifying tests
- **chore**: Changes to build process or auxiliary tools/libraries

#### Examples

```
feat(api): add user authentication endpoint

docs(readme): update installation instructions

fix(auth): resolve login timeout issue

refactor(core): optimize data processing pipeline

style: format code with black

test(api): add tests for user registration
```

#### Best Practices

- Keep the subject line under 50 characters
- Use imperative mood ("add" not "added" or "adds")
- Leave a blank line between the subject and body
- Wrap the body at 72 characters
- Reference issues and pull requests in the footer

Example with body:

```
feat(api): implement user profile endpoint

Add new endpoint for retrieving and updating user profiles. This includes:
- GET /api/users/{id}/profile
- PUT /api/users/{id}/profile

Closes #123
```
