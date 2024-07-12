# Reliable P2P File Sharing

This project was developed using Python on Ubuntu 20.4.

## Overview

This project is a peer-to-peer chatting application that enables file sharing and direct message sending between peers. The chat messages are sent via an application-layer reliable UDP connection, while file sharing is facilitated through a separate TCP connection.

## Network Emulation for Testing

- To simulate packet loss, use the netem tool in the Linux terminal:

    - sudo tc qdisc add dev lo root netem loss 70%, lo refers to the localhost.

- You can also use other netem commands to simulate different network conditions such as delays.

## How to Run the Application

1. Download and unzip the project files.

2. Open the file directory in the terminal.

3. Run the following commands in two separate terminal windows from the project directory:

    ```
    python peer1.py
    ```
    ```
    python peer2.py
    ```

4. Send messages between the peers by typing them in the terminal.

5. To enter sender/receiver mode for file sharing, type in each terminal:

    ```
    sr
    ```

6. When sending a file:
    - Input the file name with the complete path and file extension on the sending peer.
    - Input "n/a" on the receiving peer (after sending the file name on the sender side).

## Other Collaborators

Shoushy Kojayan - Sarah Khalifeh - Layan Yamani