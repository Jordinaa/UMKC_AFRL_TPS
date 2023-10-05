from pymavlink import mavutil

def main(connection_string):
    # Establish a connection to the MAVLink device
    master = mavutil.mavlink_connection(connection_string, baud=57600)
    
    # Request all parameters
    master.param_fetch_all()

    # Variables to keep track of received parameters and total parameters
    num_params_received = 0
    total_params = None

    while total_params is None or num_params_received < total_params:
        # Wait for a PARAM_VALUE message
        msg = master.recv_match(type='PARAM_VALUE', blocking=True)
        if msg:
            # Update total_params if it's not set
            if total_params is None:
                total_params = msg.param_count

            print(f"Param {msg.param_id.decode('utf-8')}: {msg.param_value}")
            num_params_received += 1

if __name__ == "__main__":
    # Connection string; adjust as needed based on your setup
    connection_string = "/dev/ttyUSB0"
    main(connection_string)
