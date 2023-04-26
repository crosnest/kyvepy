<h1 align="center">
    <b>kyvepy</b>
</h1>

<p align="center">
A python library for interacting with Chain4energy blockchain<br>
based on the CosmPy library
</p>

<p align="center">
  <a href="https://pypi.org/project/kyvepy/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/kyvepy">
  </a>
  <a href="https://pypi.org/project/kyvepy/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/kyvepy">
  </a>
  <a href="https://github.com/crosnest/kyvepy/blob/master/LICENSE">
    <img alt="License" src="https://img.shields.io/pypi/l/kyvepy">
  </a>
  <br />
  <a>
    <img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/kyvepy">
  </a>
  <a href="https://github.com/crosnest/kyvepy/actions/workflows/workflow.yml">
    <img alt="CosmPy sanity checks and tests" src="https://github.com/crosnest/kyvepy/actions/workflows/workflow.yml/badge.svg">
  </a>
  <a href="https://pypi.org/project/kyvepy/">
    <img alt="Download per Month" src="https://img.shields.io/pypi/dm/kyvepy">
  </a>
</p>

## To Install

```bash
pip3 install kyvepy
```

## Getting Started

Below is a simple example for querying an account's balances:

```python
from kyvepy.aerial.client import LedgerClient, NetworkConfig

# connect to Fetch.ai network using default parameters
ledger_client = LedgerClient(NetworkConfig.chain4energy_mainnet())

alice: str = 'kyve1t62t32vvkr78zdws3jvu9rxjkz3fy0ex4v7e7l'
balances = ledger_client.query_bank_all_balances(alice)

# show all coin balances
for coin in balances:
    print(f'{coin.amount}{coin.denom}')
```

## Documentation

The Cosmpy documentation can be found [here](https://docs.fetch.ai/CosmPy/).

## Examples

Under the `examples` directory, you can find examples of basic ledger interactions using `kyvepy`, such as transferring tokens, staking.

## Contributing

All contributions are very welcome! Remember, contribution is not only PRs and code, but any help with docs or helping other developers solve their issues are very appreciated!

Read below to learn how you can take part in the CosmPy or derivative projects like kyvepy.

### Code of Conduct

Please be sure to read and follow our [Code of Conduct][coc]. By participating, you are expected to uphold this code.

### Contribution Guidelines

Read our [contribution guidelines][contributing] to learn about our issue and PR submission processes, coding rules, and more.

### Development Guidelines

Read our [development guidelines][developing] to learn about the development processes and workflows when contributing to different parts of the CosmPy project.

### Issues, Questions and Discussions

We use [GitHub Issues][issues] for tracking requests and bugs.

## License

The kyvePy and CosmPy projects are licensed under [Apache License 2.0][license].

[contributing]: https://github.com/crosnest/kyvepy/blob/master/CONTRIBUTING.md
[developing]: https://github.com/crosnest/kyvepy/blob/master/DEVELOPING.md
[coc]: https://github.com/crosnest/kyvepy/blob/master/CODE_OF_CONDUCT.md
[issues]: https://github.com/crosnest/kyvepy/issues
[license]: https://github.com/crosnest/kyvepy/blob/master/LICENSE