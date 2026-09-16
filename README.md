# ai-resources

Personal repository of AI utilities to reuse across projects.

## Resources

| Folder | Contents |
| --- | --- |
| [prompts](prompts/README.md) | Instructions for specific tasks. |
| [skills](skills/README.md) | Reusable capabilities with instructions and supporting resources. |
| [agents](agents/README.md) | Agent definitions and configurations. |
| [rules](rules/README.md) | Rules and conventions for projects and assistants. |
| [workflows](workflows/README.md) | Procedures that combine steps and resources. |
| [scripts](scripts/README.md) | Executable automations. |
| [docs](docs/README.md) | Guides, references, and notes. |

## How to use this repository

1. Find the category or task you need.
2. Read the resource's requirements and compatibility information.
3. Copy or adapt the content to the target project; replace variables and example paths.
4. Check the result in that project and document reusable improvements here.

No dependencies need to be installed to read the documentation. Each script or resource that needs them must explain its own installation.

With [ripgrep](https://github.com/BurntSushi/ripgrep) installed, you can search from the root:

```powershell
rg --files
rg -n "keyword" prompts skills agents rules workflows scripts docs
```

## How to add a resource

- Save it in the appropriate category with a descriptive name in `kebab-case`.
- Explain its purpose, compatibility, requirements, usage, and expected output.
- Use variables such as `{{context}}` for data that changes between projects and explain what to replace.
- Write documentation in English, respecting the names and formats required by each tool.
- Record the source and license when adapting third-party content.
- Add a link in the category's README to make it easy to find.
- Keep examples free of credentials and private data.

If a resource consists of several files, group them in a folder with its own guide. Add subcategories when there is enough content to need them.

The scope and maintenance criteria are in [SPEC.md](SPEC.md).
