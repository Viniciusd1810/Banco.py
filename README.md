# Banking System with Python

Console banking system built in Python to practice object-oriented programming, business rules and code organization.

The project started as a simple banking exercise and was later refactored into multiple domain classes instead of keeping all logic in a single script.

## Features

- Customer registration
- Bank account creation
- Account login/session handling
- Deposits
- Withdrawals
- Transaction history
- Balance display
- Basic input validation and exception handling

> Transfer is currently present in the menu but has not been implemented yet.

## Project Structure

```text
.
├── cliente.py
├── conta.py
├── endereco.py
├── historico.py
├── main.py
├── sessao.py
├── transacao.py
└── .github/
    └── workflows/
        └── python-app.yml
```

The code separates responsibilities into classes for customers, accounts, addresses, sessions, transaction history and transaction types.

## Technologies

- Python
- `decimal.Decimal` for monetary values
- Object-Oriented Programming
- GitHub Actions
- Flake8
- Pytest configuration in CI

## Running Locally

Clone the repository:

```bash
git clone https://github.com/Viniciusd1810/Banco.py.git
cd Banco.py
```

Run the application:

```bash
python main.py
```

## Current Status

This is a learning project and is still evolving.

Current improvement opportunities include:

- Implement transfers
- Add automated tests
- Separate CLI/input-output logic from domain logic
- Improve validation and error handling
- Persist data instead of storing everything only in memory
- Add type hints and improve code documentation

## Why This Project Matters

This repository represents my progression from procedural exercises toward better separation of responsibilities and object-oriented design in Python. It is also a practical base for studying testing, refactoring and software quality practices.
