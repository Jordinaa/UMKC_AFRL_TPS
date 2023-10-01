from pymvalink import mavutil
import time

# MAVLink parameter names
PARAM_NAMES = [
    "AIRSPEED", "ALTITUDE", "LATITUDE", "LONGITUDE", "ROLL_ANGLE", "PITCH_ANGLE", "HEADING",
    "ROLL_RATE", "PITCH_RATE", "YAW_RATE", "X_ACCEL", "Y_ACCEL", "Z_ACCEL", "AILERON",
    "ELEVATOR", "RUDDER", "THROTTLE", "FLAPS", "GROUNDSPEED", "LCL_POSN_X", "LCL_POSN_Y",
    "LCL_POSN_Z", "LCL_VEL_X", "LCL_VEL_Y", "LCL_VEL_Z", "CLIMB_RATE", "ATTITUDE_CMD_Q1",
    "ATTITUDE_CMD_Q2", "ATTITUDE_CMD_Q3", "ATTITUDE_CMD_Q4", "ROLL_RATE_CMD", "PITCH_RATE_CMD",
    "YAW_RATE_CMD"
]

def main(connection_string, output_port):
    # Connect to the MAVLink device
    master = mavutil.mavlink_connection(connection_string, baud=57600)
    
    # Request parameters
    for param in PARAM_NAMES:
        master.param_fetch_one(param)
    
    # Infinite loop to handle MAVLink messages
    while True:
        msg = master.recv_match(type='PARAM_VALUE', blocking=True)
        if msg.param_id.decode() in PARAM_NAMES:
            # Handle or forward the parameter value as needed
            # For example, you can forward to another port or print to the console
            print(f"{msg.param_id}: {msg.param_value}")

if __name__ == "__main__":
    # Connect to the device (adjust as needed)
    connection_string = "YOUR_DEVICE_STRING_HERE"
    
    # Output port (adjust as needed)
    output_port = "YOUR_OUTPUT_PORT_HERE"
    
    main(connection_string, output_port)
