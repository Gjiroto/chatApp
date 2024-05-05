##**Simple Chat Application with Python and Tkinter**
-----------------------------------------------

This project implements a basic client-server chat application using Python's socket library for networking and Tkinter for the graphical user interface (GUI).

**Components**

*   **Client.py:** The client-side script responsible for connecting to the server and providing the GUI for user interaction.
    
*   **Server.py:** The server-side script that manages multiple client connections and broadcasts messages.
    

**How it Works**

1.  **Server Initialization:**
    
    *   The server starts and listens for incoming client connections on a specified port (default 5000).
        
    *   When a client connects, the server adds it to a list of active clients.
        
2.  **Client Connection:**
    
    *   The client establishes a connection to the server using the server's IP address and port.
        
    *   The client GUI provides fields for the user's name and messages.
        
3.  **Message Exchange:**
    
    *   **Client Sending:** When the client clicks "Send", their message, along with their name, is encoded and transmitted to the server.
        
    *   **Server Broadcasting:** The server receives the message and relays it to all connected clients, including the sender.
        
    *   **Display:** Both the client and other connected clients display the received messages in the chat window.
        

**GUI Elements (Client.py)**

*   chat\_area (Text): Displays the chat history.
    
*   name\_label (Label): A label for the "Name" field.
    
*   name\_entry (Entry): Allows the user to input their name.
    
*   message\_entry (Entry): Allows the user to type messages.
    
*   send\_button (Button): Triggers the sending of a message.
    

**Prerequisites**

*   Python 3 ([https://www.python.org/](https://www.python.org/))
    
*   Tkinter (usually included in standard Python installations) if no:
*   Install Tkinter (Python 3.x): If you're using Python 3.x, tkinter should be included in the standard library. However, on some systems, it might not be installed by default. You can install it using the package manager for your system. For         example, on Ubuntu, you can use sudo apt-get install python3-tk.
*   Install Tkinter (Python 2.x): If you're using Python 2.x, tkinter is known as Tkinter. You can install it using the package manager for your system. For example, on Ubuntu, you can use sudo apt-get install python-tk.


    

**Instructions**

1.  **Start the Server:**
    
    *   Run Server.py
        
    *   (Optional) Specify a different port number by entering it in the GUI.
        
2.  **Launch Clients:**
    
    *   Run Client.py multiple times to create several chat participants.
        
