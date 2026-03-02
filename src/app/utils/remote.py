import lirc


def listen():
    client = lirc.Client("dailyvid", cache=True)

    print("LIRC client connected. Press remote buttons...")

    while True:
        try:
            # Read the next command from the LIRC daemon.
            # This is a blocking call unless a timeout is set on the client.
            code = client.blocking_receive()

            if code:
                # lirc.blocking_receive() returns a list of button names
                for button_name in code:
                    print(f"Received button: {button_name}")
            else:
                # Code will be None if a timeout occurred and no data was received
                pass

        except KeyboardInterrupt:
            # Handle user interruption (Ctrl+C)
            print("Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break


listen()
