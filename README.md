## Basic Web API

### Steps to Set Up and Run

1. **Create Virtual Environment**:
    ```sh
    python -m venv venv
    ```

2. **Activate Virtual Environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```sh
    python main.py
    ```

## TCP Server-Client

### Steps to Set Up and Run

1. **Run the Server**:
    Open a terminal and navigate to the correct directory, then run:
    ```sh
    python server.py
    ```

2. **Run the Client**:
    Open another terminal and navigate to the correct directory, then run:
    ```sh
    python client.py
    ```

3. **Interact with the Client**:
    Enter messages in the client terminal to send them to the server. The server will echo the messages back to the client. Type `exit` to close the client connection.

### Configuration

The `config.json` file contains the configuration for the server and client. Logs will be written to the app.log as specified. 