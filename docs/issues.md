Lilypad is developing a serverless, distributed compute network that enables internet-scale data processing, AI, ML & other arbitrary computation, while unleashing idle processing power & unlocking a new marketplace for compute.

You can use Lilypad to run AI workload models including Stable Diffusion and Stable Diffusion Video, or you can add your own module to run on the Lilypad Network. Using Lilypads distributed compute nodes, you can build and run your own containerized workloads that require high-performance computing.

Overview
Lilypad provides distributed computational services underpinned by the Bacalhau Project. The network provides infrastructure for use cases like AI inference, ML training, DeSci and more. Lilypad strategically collaborates with decentralized infrastructure networks, such as Filecoin, to formulate a transparent, efficient, and accessible computational ecosystem.

Perform off-chain decentralized compute over data, with on-chain guarantees. Call this functionality directly from a smart contract, CLI, and an easy to use abstraction layer.

In the video above, Ally Haire, Co-Founder of Lilypad, provides an introduction to the project and its goals.
The network is actively laying groundwork for multi-chain integration and the deployment of an incentivized testnet.

Lilypad has evolved from earlier versions (v0, v1 & v2), where the network served as a proof of concept for verifiable, decentralized compute directly from smart contracts. These earlier iterations established the groundwork for what is now a robust, scalable platform with expanded features and multichain support.

Bacalhau has been integral to Lilypad since its early versions (v0 and v1), serving as the backbone for verifiable off-chain compute. In these early iterations, Bacalhau was used for Proof of Concept projects, helping users execute decentralized compute jobs from smart contracts.

Find Lilypad on GitHub or visit the blog.

Objective and problem statement
Lilypad aims to mitigate the challenges predominantly associated with the accessibility of high-performance computational hardware. At present, numerous barriers impede developers and organizations from smoothly integrating projects that require high-performance computing, such as AI technologies, into their applications.

Unlike conventional centralized systems, where access to powerful compute hardware is restricted and costly, Lilypad endeavors to democratize this access. Through its verifiable, trustless, and decentralized computational network, Lilypad extends unrestricted, global access to computational power. By leveraging decentralized infrastructure networks such as Filecoin, Lilypad is strategically positioned to enhance the efficiency, transparency, and accessibility of high-performance computing hardware.

Applications
Perform off-chain decentralized compute over data, with on-chain guarantees, and to call this functionality directly from a smart contract, CLI, API and an easy to use abstraction layer, opens the door to a multitude of possible applications including:

Inference AI jobs

ML training jobs

Invoking & supporting generic ZK computations

Cross-chain interoperability complement to bridge protocols

Utilising inbuilt storage on IPFS

Federated Learning consensus (with Bacalhau insulated jobs)

IOT & Sensor Data integrations

Providing a platform for Digital twins

Supply chain tracking & analysis

ETL & data preparation jobs

Key features
Some of the key features of Lilypad include:

Verifiable Serverless Decentralized Compute Network: Lilypad is a decentralized compute network that aims to provide global, permissionless access to compute power. The Network orchestrates off-chain compute (a global GPU marketplace) and uses on-chain verification (Arbitrum L2 on Ethereum) to provide guarantees of compute success.

Mainstream Web3 Application Support: Lilypad is designed to enable mainstream web3 applications to use its compute network with the Lilypad CLI and Smart Contracts. It aims to make decentralized AI compute more accessible, efficient, and transparent for developers and users.

Open Compute Network: Lilypad is an open compute network allowing users to access and run AI models/other programs in a serverless manner. Module creators and general users can access a curated set of modules or can easily create their own Lilypad module to run an AI model/other program on the network.

Multichain Support: The Lilypad Incentivized Testnet first launched on Arbitrum in June 2024 with plans to go multi-chain in the near future. Supporting multiple blockchain networks will increase the scalability and interoperability of the network, allowing users to choose the blockchain that best suits their needs.

Incentivized Test Net: The Lilypad IncentiveNet is live! The IncentiveNet program provide users with Lilybit\_ rewards to participate in running nodes, testing, and improving the network. Learn more by checking out the IncentiveNet Leaderboard.

Decentralization of Mediators: The team also aims to decentralize the mediators in the network. This means that the decision-making process and governance of the network will be distributed among multiple participants, ensuring a more decentralized and resilient system.

What is the Bacalhau Project?
Bacalhau is a peer to peer computation network enabling compute over data jobs like GPU-enabled AI, ML, analytics, data engineering, data science, de-sci and more.

With the open-source Bacalhau Project, you can streamline your existing workflows without rewriting by running Docker containers and WebAssembly (WASM) images as tasks. This architecture is also referred to as Compute Over Data (or CoD).

Issue 1: Bacalhau Problem in Docker, v2.10.0

I am trying to run my RP with Docker. This always worked until v2.10.0 was released. I tried using the Docker-Compose method but that was hopeless, so I am trying to run my RP using the normal Docker method. It seems to almost be working except that the RP container keeps restarting and gives this error:

[DEBUG] GET http://localhost:1234/api/v1/agent/alive: retrying in 8s (1 left)
[ERR] GET http://localhost:1234/api/v1/agent/alive request failed: Get "http://localhost:1234/api/v1/agent/alive": dial tcp [::1]:1234: connect: connection refused
Error: Bacalhau is not currently available. Please ensure that Bacalhau is running, then try again. GET http://localhost:1234/api/v1/agent/alive giving up after 5 attempt(s): Get "http://localhost:1234/api/v1/agent/alive": dial tcp [::1]:1234: connect: connection refused

I do not know why Bacalhau is not available in this latest version of the RP container. In previous versions it used to work fine just by running the resource-provider container, producing PoWs on my GPU and gaining points each day. My setup, as before, is a fresh install of Ubuntu server, dedicated solely to Lilypad, with these:

- Ubuntu 22.04.5 LTS
- Nvidia driver v535.216.03 (server)
- Cuda v12.2
- Docker Engine (Community) v27.3.1
- NVIDIA Container Runtime Hook version 1.17.3 (nvidia-container-toolkit)

Support: I was having the same problem on my RP, try this it worked for me:

- stop bacalhau and lilypad-resource-provider
- stop ipfs node & close terminal window
- new terminal, start ipfs node (ipfs daemon)
- start bacalhau (give it a 5-10 seconds to start)
- start lilypad-resource-provider

User: I think you are using the Linux method. I need help with the Docker method.

Support: Was sharing this info to try to identify what's possibly happening on the docker RP with regards to the bacalhau error and ipfs node. How does the ipfs container look? Are there any errors in the logs? With docker-compose a separate ipfs container is setup. Since you used the normal docker method, is there an ipfs container setup?

User: I've only seen an IPFS and Bacalhau containers when trying out the new Docker-Compose method, but I couldn't get that method to work for me.

I am using the normal Docker method, which only produces a single container called 'resource-provider'. Up until this version it was sufficient, RP worked perfectly, I believe it had the other components within it somehow. My only other containers were Uptime Kuma and watchtower.

With docker-compose method I was able to pull all the layers and they seemed to start okay, but my RP still would not work and gave this error:
Error response from daemon: driver failed programming external connectivity on endpoint ipfs (a853ee118aad8aaffe7a6a87f2cefdfc7dd5872d6b5f2a50eda999b5ab65bfcc): failed to bind port 127.0.0.1:8080/tcp: Error starting userland proxy: listen tcp4 127.0.0.1:8080: bind: address already in use

Resolution: Need to kill old ipfs that's already using the port. After reinstalling Ubuntu, got it working using the Linux method.

Issue 2: Use multiple GPUs

Question: I have more than one gpu on the machine I'm running lily pad on and I'm wondering how to use more than one GPU. Any tips are appreciated?

Support: You can definitely do it but suggest waiting for rewards to be right before setting multiple up. For docker you just make each container/instance point at a single gpu each.

Same for Linux by adding the line to the lilypad service file:

```
[Service]
Environment="LOG_TYPE=json"
Environment="LOG_LEVEL=debug"
Environment="HOME=/app/lilypad_$i"
Environment="OFFER_GPU=1"
Environment="CUDA_VISIBLE_DEVICES=0"
EnvironmentFile=/app/lilypad_$i/resource-provider-gpu.env
Restart=always
RestartSec=5s
ExecStart=/usr/local/bin/lilypad resource-provider
```

CUDA_VISIBLE_DEVICES would be changed for each GPU/instance. You need a service file for each lilypad resource-provider you run. In the service file, they each have a different CUDA_VISIBLE_DEVICES value, a different private key and/or a rpc url.

Q: Is it possible to use same address for all miners?
A: Not currently.

Issue 3: WebSocket error fix

Description: After running the lilypad node for a certain period of time, the message from the title appears and the node stops working (no more POWs worked on).

Hardware Info: Ubuntu 22.04.5 Jammy Jellyfish

Error output:

```
websocket: failed to close network connection: close tcp 172.17.0.2:52932->145.40.118.135:443: use of closed network connection
[DEBUG] GET http://localhost:1234/api/v1/orchestrator/nodes
WRN pkg/publicapi/middleware/version.go:41 > received request from client without version [ClientID:] [ClientVersion:] [NodeID:n-90099d3c] [RequestID:] [ServerVersion:1.3.2]
INF pkg/publicapi/middleware/logger.go:50 > [ClientID:] [Duration:3.05849] [JobID:] [Method:GET] [NodeID:n-90099d3c] [Referer:] [RemoteAddr:::1] [RequestID:] [Size:2246] [StatusCode:200] [URI:/api/v1/orchestrator/nodes] [UserAgent:Go-http-client/1.1]
```

Workaround: Stop docker and start docker again. This is reported to be an issue with rate limiting because there's too much traffic. Private RPC usage may help but issue persists.

Note from support: We have a rate limiter on the solver, which limits by IP address and route. Too many attempts could lead to abnormal closure messages. Could also be general connectivity issues. Current limits are set at 50 requests over 10 seconds per route, which was thought to be a generous allowance. But could see there may be issues if an RP was running many nodes behind the same IP address.

Issue 4:
No Points Despite POW Submission
User: IN THE photo it shows i received 0 points but in the other photos you can see im submitting POW
Support: Can you provide:

lilypad version
docker-compose or just linux
wallet address
more than one gpu on the instance?
errors in logs

User Response:

newest version
linux
0xa5aE4FB19fD264e5269d6Ed7487179f657be9a58
one GPU
proofs are submitting

Status: Team investigating the issue and will provide updates through updates-rp channel.

Issue 5: WebSocket Error with Docker
User: Wallet: 0xf9083493ea6d0124f7d674a2a9b1bcf5b192c4f6
Error in logs:
ERR ../../local/go/src/runtime/asm_amd64.s:1695 > websocket error error="websocket: close 1006 (abnormal closure): unexpected EOF"
System Details:

Private RPC
Official docker
Version 1.5.1
NodeID: n-69a0db0c

Log Output:
INF pkg/version/update.go:101 > A new version is available! Update by running the following command
WRN pkg/publicapi/middleware/version.go:41 > received request from client without version
INF pkg/publicapi/middleware/logger.go:50 > [ClientID:] [Duration:0.133179] [JobID:] [Method:GET] [Status:200]
Support Analysis:

Issue may be related to Arbitrum RPC rate limiting during high traffic
Connection to solver might be affected by rate limits (50 requests over 10 seconds per route)
Multiple nodes behind same IP could trigger rate limiting
Private RPC usage may help but doesn't fully resolve

Related Issue: http://localhost:1234/api/v1/agent/alive connection refused after updating to 2.10.0
System Information:
Ubuntu 22.04.5 LTS
Nvidia driver v535.216.03 (server)
Cuda v12.2
Docker Engine (Community) v27.3.1
NVIDIA Container Runtime Hook version 1.17.3
Troubleshooting Steps:

Container pulls latest version: ghcr.io/lilypad-tech/resource-provider:latest
Verification of container startup and logs
Check for GPU detection and CUDA functionality
Test nvidia-smi output
Attempt Docker Compose configuration
Add GPU device configuration to docker-compose.yml
Check runtime configuration using nvidia-ctk

Current Status:

Docker installations experiencing connection issues after v2.10.0 update
Linux installations appear more stable
Team working on permanent fix
Temporary workaround: Allow container to attempt reconnection several times

Resolution Path:

Fresh Ubuntu installation
Switch to Linux method instead of Docker
Ensure proper GPU detection and CUDA setup
Configure proper runtime environment

Note: Users should be aware that bacalhau may take time to become available and container restarts are normal during initialization.

Issue 6: IPFS Node Configuration Issues

Initial Error
User: Getting an ERROR in journalctl -u bacalhau.service -f - your programs version (15) is lower than your repos (16). Please update ipfs to a version that supports the existing repo, or run a migration in reverse.
Support: Try running:
sudo apt update && sudo apt upgrade ipfs
User: Unable to locate package
Support: Check version with ipfs --version. You can install IPFS manually:
wget https://dist.ipfs.tech/go-ipfs/v0.16.0/go-ipfs_v0.16.0_linux-amd64.tar.gz
tar -xvzf go-ipfs_v0.16.0_linux-amd64.tar.gz
cd go-ipfs
sudo install.sh
Environment Configuration
Problem: Program version shows 15 while IPFS version returns 16 (REPO version 16)
Troubleshooting Steps:

Check IPFS_PATH:

echo $IPFS_PATH

Make IPFS_PATH persistent:

echo 'export IPFS_PATH=/app/data/ipfs' >> ~/.rc && source ~/.rc

Check ownership:

ls -ld /app/data/ipfs
If not correct user: sudo chown -R $USER:$USER /app/data/ipfs
Service Configuration
Updated bacalhau.service configuration:
[Unit]
Description=Lilypad V2 Bacalhau
After=network-online.target
Wants=network-online.target systemd-networkd-wait-online.service

[Service]
Environment="LOG_TYPE=json"
Environment="LOG_LEVEL=debug"
Environment="HOME=/app/lilypad"
Environment="BACALHAU_SERVE_IPFS_PATH=/app/data/ipfs"
Restart=always
RestartSec=5s
ExecStart=/usr/bin/bacalhau serve --node-type compute,requester --peer none --private-internal-ipfs=false --ipfs-connect "/ip4/127.0.0.1/tcp/5001"

[Install]
WantedBy=multi-user.target
Running IPFS Daemon
To run IPFS daemon detached:
nohup ipfs daemon &
Troubleshooting Steps for Connection Issues

Stop services:

sudo systemctl stop bacalhau
sudo systemctl stop lilypad-resource-provider

Ensure IPFS daemon is running

Check for port conflicts on 5001
Verify IPFS version (should be 0.30)
Run IPFS daemon in separate terminal

Start services in order:

sudo systemctl start bacalhau
sudo systemctl start lilypad-resource-provider
Notes

Some connection failures may resolve after a few retries
IPFS daemon should be running before starting other services
Verify no port conflicts exist for 5001
Service configs should be updated to latest versions
When using Alchemy websocket, connection should show as working
If services fail initially, allow some time for retry attempts

Important: Run IPFS daemon in a separate terminal window from bacalhau and lilypad-resource-provider services.i

Issue 7:
Bacalhau Connection Issues
Initial Problem
System: Ubuntu 22.04 LTS
Error Message:
Bacalhau is not currently available. Please ensure that Bacalhau is running, then try again.
GET http://localhost:1234/api/v1/agent/alive giving up after 5 attempt(s):
Get "http://localhost:1234/api/v1/agent/alive": dial tcp 127.0.0.1: connect: connection refused

systemd[1]: lilypad-resource-provider.service: Main process exited, code=exited, status=1/FAILURE
systemd[1]: lilypad-resource-provider.service: Failed with result 'exit-code'
Troubleshooting Steps

1. Check Bacalhau Logs
   Command:
   journalctl -u bacalhau -n 250
   Output shows IPFS connection error:
   error creating IPFS client: failed to connect to '/ip4/127.0.0.1/tcp/5001'
2. Verify IPFS Daemon Status
   IPFS Daemon Output:
   Initializing daemon...
   Kubo version: 0.30.0
   Repo version: 16
   System version: amd64/linux
   Golang version: go1.22.7
   Swarm listening on 127.0.0.1:4001 (TCP+UDP)
   Swarm listening on 172.17.0.1:4001 (TCP+UDP)
   Swarm listening on 172.30.210.160:4001 (TCP+UDP)
   Swarm listening on [::1]:4001 (TCP+UDP)
   RPC API server listening on /ip4/127.0.0.1/tcp/5001
   WebUI: http://127.0.0.1:5001/webui
   Gateway server listening on /ip4/127.0.0.1/tcp/8080
   Daemon is ready
3. Port Usage Investigation

Check for port conflicts on 5001 and 8080
Command to check port usage: ss -lptn 'sport = :8080'
Note: RPC API and WebUI may share port 5001 (this is normal)

Common Solutions

Wait for Services to Initialize

Sometimes the service resolves itself after waiting
Initial connection attempts may fail but eventually succeed

System Restart

Full system restart can resolve persistent issues
Restart sequence:

Restart PC
Start IPFS daemon
Start Bacalhau service
Start resource provider

Port Conflict Resolution

Check for processes using required ports (5001, 8080)
Stop conflicting services if necessary
Ensure proper service shutdown before restart

Notes

Issue can sometimes resolve itself with patience
Both RPC API and WebUI can share port 5001
System restart has proven effective for multiple users
Important to check for port conflicts when experiencing connection issues
Service initialization order matters: IPFS → Bacalhau → Resource Provider

ssue 8: RP Error
User: What is this error about? Also, can a wallet address run to multiple nodes?
Support: "Nonce too low" generally implies that the nonce used for a transaction is outdated or incorrect, potentially due to a concurrency issue or repeated transaction attempt.
Important Notes:

Each wallet address can only be used for a single node
Ensure wallet has both ETH and LP tokens
Reference: https://docs.lilypad.tech/lilypad/hardware-providers/run-a-node/linux#fund-your-wallet-with-eth-and-lp

Issue 9: Cant See New Nodes on Leaderboard
User: How long does it take for new nodes to appear on the leaderboard?
Support: Please post your wallet address for verification. Typically, it takes 24 hours before a new node will appear on the leaderboard.

Issue 10: No POW Activity Troubleshooting

Ensure running latest Lilypad version
Verify network activity on Arbiscan (Sepolia)
Check RP online status in Leaderboard and node dashboard
Verify sufficient Lilypad Tokens (LP) and Arbitrum ETH
Regular updates and restarts recommended

Issue 11: Version Tracking and Updates

Monitor updates-rp Discord channel
Check Lilypad updates page
Follow installation guides for Linux/Docker environments
Regular version checks recommended

Issue 12: Node Setup and Monitoring
Verification steps:

Check wallet balances (ETH and LP)
Monitor Arbiscan transactions (hourly)
View Leaderboard for points
Use status commands:

sudo systemctl status lilypad-resource-provider
sudo journalctl -u lilypad-resource-provider.service -f

Issue 13: Hardware Requirements

GPU required for Lilybit rewards
CPU-only nodes can run but won't receive rewards
Linux installation required (Windows = experimental)
One RP per GPU policy enforced

Issue 14: Common Technical Errors

Bacalhau IPFS init error:

export IPFS_PATH=/app/data/ipfs

CompatNotSupportedOnDevice:

CUDA version mismatch with GPU driver
Follow Nvidia GPU Driver guide

Error Code 222:

Incorrect CUDA version
Install appropriate CUDA version for GPU type

Issue 15: Service Management
Restart sequence:
sudo systemctl restart lilypad
sudo systemctl restart bacalhau
Version update process:
sudo systemctl stop bacalhau
sudo systemctl stop lilypad-resource-provider
sudo rm -rf /usr/bin/bacalhau

Reinstall following docs
sudo systemctl start bacalhau
sudo systemctl start lilypad-resource-provider
Issue 15: Rewards and Slashing
Reward Schedule:

Updates daily at 00:10 UTC
24-hour verification period
4X daily multiplier based on 4-hour windows

Slashing Tiers:

1-5 days offline: 2.5% slash per day
5-10 days offline: 5% slash per day

10 days offline: 10% slash per day

Grace period: 2 days per 30 days of uptime

Issue 16: Wallet Configuration
Common Issues:

"Invalid hex character 'r'" = Using seed phrase instead of private key
Private key format: 64 hexadecimal characters
Follow MetaMask guide for private key retrieval
Custom network setup required for Lilypad
Token import process needed for LP

Issue 17: Resource Management
Multiple GPU Setup:

Use Proxmox guide for multiple GPU configuration
One RP per GPU requirement
Resource splitting not allowed
Custom RPC setup available for Arbitrum Sepolia

Issue 18: Wait, didn’t Lilypad used to rely on determinism and optimistic reproducibility for verifiable compute?

Previously, Lilypad required deterministic jobs on the network and used optimistic reproducibility to randomly re-run jobs to ensure trust, however this method has been deprecated due to:

the limitation the determinism requirement placed on what jobs were available to run on the network

the inability to realistically be able to determine a “deterministic” job to be deterministic easily

Issue 19: Has Lilypad raised VC money?
Yes, Lilypad closed our seed round of funding in March 2024.

Issue 20: Launch Timeline
Q: When will the Incentivized Testnet launch?

Launched in mid June 2024
Updates available through Lilypad Discord

Issue 21: LilyBit* Reward System
Q: How do LilyBit* rewards work?
Reward Structure:

Based on network uptime (up to 4x multiplier)
Rewards for compute power contribution
Redeemable for Lilypad ERC20 Utility Token at Mainnet Launch
5-10% of total token supply allocated (depends on demand and tokenomics)
Progress tracked via RP Leaderboard

Issue 22: Reward Eligibility
Q: Who can earn LilyBit\_ rewards?
Phase 1:

Focused on Resource Providers (nodes)
Earlier participation = higher reward potential

Phase 2+:

Rewards for Lilypad module creation
Rewards for developer tools/apps
Continued node rewards

Issue 23: Reward Tracking
Q: How do I check my Lilybit\_ rewards?
Tracking Interfaces:

Grafana dashboard
Lilypad leaderboard
Open Source contributor dashboard

Issue 24: Blockchain Integration
Q: How does Lilypad use blockchain, and why do I need both ETH and Lilypad tokens?
Blockchain Usage:

Payment infrastructure
Deal storage and transparency
Dispute and result recording

Token Requirements:

Lilypad Tokens:

Network transaction processing
Payment for job execution
Resource provider collateral

ETH:

Gas fees for smart contracts
Transaction record fees
Dispute documentation fees

Issue 25: LilyBit* Reward System
Q: How do LilyBit* rewards work?
Reward Structure:

Based on network uptime (up to 4x multiplier)
Rewards for compute power contribution
Redeemable for Lilypad ERC20 Utility Token at Mainnet Launch
5-10% of total token supply allocated (depends on demand and tokenomics)
Progress tracked via RP Leaderboard

Issue 26: Reward Eligibility
Q: Who can earn LilyBit\_ rewards?
Phase 1:

Focused on Resource Providers (nodes)
Earlier participation = higher reward potential

Phase 2+:

Rewards for Lilypad module creation
Rewards for developer tools/apps
Continued node rewards

Issue 27: Reward Tracking
Q: How do I check my Lilybit\_ rewards?
Tracking Interfaces:

Grafana dashboard
Lilypad leaderboard
Open Source contributor dashboard

Issue 28: Blockchain Integration
Q: How does Lilypad use blockchain, and why do I need both ETH and Lilypad tokens?
Blockchain Usage:

Payment infrastructure
Deal storage and transparency
Dispute and result recording

Token Requirements:

Lilypad Tokens:

Network transaction processing
Payment for job execution
Resource provider collateral

ETH:

Gas fees for smart contracts
Transaction record fees
Dispute documentation fees
