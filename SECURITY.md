# Security Policy

## Supported Versions
We maintain security support only for maintained versions:

| Version     | Supported       |
|-------------|------------------|
| `main`      | ✅ Actively supported |


## Reporting Vulnerabilities
Use GitHub's **private security advisories** if enabled.  
Alternatively, send encrypted email to `security@fermat-mcp.org`.

Reports should include:
- Repro steps, version info, environment
- Minimal code or proof-of-concept
- Severity and impact

We commit to acknowledging all valid reports within 48 hours and publish a public advisory alongside any release.

## Disclosure Workflow
1. Confidential report
2. Patch development and review
3. Simultaneous release and public advisory
4. Label issue with `security`

## Developer Guidelines
- Keep dependencies up-to-date (e.g., via Dependabot)
- Avoid `eval`, validate inputs, sanitize outputs
- Use CI tools (CodeQL, dependency alerts) to enforce security

## Recognition
Contributors reporting valid vulnerabilities will be credited in release notes or in this file.

---

This focused policy helps build credibility, enables secure reporting, and sets clear expectations—surpassing basic default templates.  
GitHub’s default only provides contact info and version table, without timelines, encrypted reporting, or security practices guidance :contentReference[oaicite:1]{index=1}.
