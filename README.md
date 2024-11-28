
# NourishNet (Using ICP - Kybra)
NourishNet uses decentralized collaboration services offered by ICP (Internet Computer Protocol) to facilitate seamless communication and coordination among stakeholders, ensuring efficient resource allocation and effective response to community needs.

### Solution and Functions:
<p align="center">
  <img src="https://github.com/anuragbejju/FoodLedger/blob/main/docs/imgs/FoodLedger5.jpg" width="1000" title="hover text" align="center">
</p>

### Dependencies
Follow the instructions exactly as stated below to avoid issues.
You should be using a *nix environment (Linux, Mac OS, WSL if using Windows) with bash and have the following installed on your system:

- Python 3.10.7
- dfx 0.19.0
- Python VS Code Extension
- Python 3.10.7
It is highly recommended to install Python 3.10.7 using pyenv. To do so, use the pyenv installer as shown below:


## Overview
**NourishNet** is a groundbreaking platform designed to transform the efficiency and transparency of food bank operations through the power of blockchain and decentralized technology. By streamlining supply chain management, optimizing resource allocation, and fostering trust among stakeholders, NourishNet aims to ensure that essential food resources reach those who need them most.

## Problem Statement
Millions of Canadians rely on food banks, especially during economic crises. However, these organizations face significant challenges:
- **Overwhelming Demand:** Rising costs and an increasing number of beneficiaries put pressure on food banks.
- **Inefficient Logistics:** Limited tools make it difficult to manage food flow, monitor expiration dates, and optimize deliveries.
- **Lack of Transparency:** Inefficient tracking and limited oversight can lead to trust issues and potential misuse of resources.

## Key Features
**NourishNet** addresses these challenges with:
- **Streamlined Operations:** Connects donors, food banks, and beneficiaries through efficient logistics and real-time data sharing.
- **Expiration and Demand Management:** Uses smart contracts to track food items, predict consumption patterns, and reduce food waste.
- **Enhanced Accessibility:** Provides a platform for beneficiaries to discover and access food resources quickly and fairly.
- **Transparency and Trust:** Decentralized ledger ensures all transactions are traceable, creating accountability and reducing fraud.

## Technology Stack
- **Blockchain Platform:** Astrakode (low-code development for smart contract deployment)
- **Decentralized Services:** ICP (Internet Computer Protocol) for collaboration and microservice architecture
- **Programming Languages:** Solidity for smart contracts, Python for backend logic
- **Deployment Tools:** dfx, Kybra

## How It Works
- **Smart Contract Deployment:** Leveraging Astrakode to create and deploy smart contracts that manage donation tracking, inventory, and logistics.
- **Microservice Architecture:** Using ICP's Kybra to design microservices that enable food banks to perform essential CRUD operations and help beneficiaries find food resources nearby.
- **Real-Time Data:** Integration of blockchain technology for transparent and secure data storage, ensuring food traceability and reducing the potential for fraud.

## Benefits
- **Improved Efficiency:** Automated processes save time and reduce manual errors.
- **Greater Trust:** All interactions are verifiable, boosting confidence among donors, food banks, and beneficiaries.
- **Reduced Waste:** Smart tracking prevents overstocking and expiration issues, leading to better food resource management.

## Achievements
- **Successfully Deployed Microservice:** Launched a functional platform that connects beneficiaries to food banks within specific areas.
- **Award-Winning Solution:** Winner of the Community Voting Prize, ICP.Hub CA & US Challenge Prize, AstraKode Challenge Prize, and Devcash Bounties at BlockHack 2024 Spring.
- **Comprehensive Testing:** Conducted thorough testing to ensure robust and reliable performance.

## Future Plans
- **Smart Contract Optimization:** Enhance and fine-tune smart contract logic to provide more advanced features.
- **Web3 Integration:** Develop a user-friendly web application to improve interaction with the NourishNet services.
- **Community Engagement:** Collaborate with food banks and stakeholders to gather feedback and iterate on features for real-world impact.


##### install pyenv
```'
curl https://pyenv.run | bash
````


##### install Python 3.10.7
````
~/.pyenv/bin/pyenv install 3.10.7
````

dfx
Run the following command to install dfx 0.19.0:
````
DFX_VERSION=0.19.0 sh -ci "$(curl -fsSL https://sdk.dfinity.org/install.sh)"
````
If after trying to run dfx commands you encounter an error such as dfx: command not found, you might need to add $HOME/bin to your path. Here's an example of doing this in your .bashrc:
````
echo 'export PATH="$PATH:$HOME/bin"' >> "$HOME/.bashrc"
````


### Execution

create and source a virtual environment:
````
~/.pyenv/versions/3.10.7/bin/python -m venv venv
source venv/bin/activate
````

Now install Kybra:
````
pip install kybra
````

Go inside NourishNet folder and deploy

### Local deployment
Let's deploy to our local replica.

First startup the replica:

````
dfx start --background
````
If you want an extra speedy deploy:

````
dfx start --background --artificial-delay 0
````
Then deploy the canister:

````
dfx deploy
````


### Interacting with your canister from the web UI
After deploying your canister, you should see output similar to the following in your terminal:
````
Deployed canisters.
URLs:
  Backend canister via Candid interface:
    kybra_hello_world: http://127.0.0.1:8000/?canisterId=ryjl3-tyaaa-aaaaa-aaaba-cai&id=rrkah-fqaaa-aaaaa-aaaaq-cai
````


### Credits
This code and documentation is referenced from https://demergent-labs.github.io/kybra/the_kybra_book.html




