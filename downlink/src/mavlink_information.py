from pymavlink import mavutil
import time
import socket

# MAVLink parameter names
# PARAM_NAMES = [
#     "AIRSPEED", "ALTITUDE", "LATITUDE", "LONGITUDE", "ROLL_ANGLE", "PITCH_ANGLE", "HEADING",
#     "ROLL_RATE", "PITCH_RATE", "YAW_RATE", "X_ACCEL", "Y_ACCEL", "Z_ACCEL", "AILERON",
#     "ELEVATOR", "RUDDER", "THROTTLE", "FLAPS", "GROUNDSPEED", "LCL_POSN_X", "LCL_POSN_Y",
#     "LCL_POSN_Z", "LCL_VEL_X", "LCL_VEL_Y", "LCL_VEL_Z", "CLIMB_RATE", "ATTITUDE_CMD_Q1",
#     "ATTITUDE_CMD_Q2", "ATTITUDE_CMD_Q3", "ATTITUDE_CMD_Q4", "ROLL_RATE_CMD", "PITCH_RATE_CMD",
#     "YAW_RATE_CMD"]

PARAM_NAMES = [
    "VFR_HUD", "VFR_HUD", "GLOBAL_POSITION_INT", "GLOBAL_POSITION_INT", "ATTITUDE", "ATTITUDE",
    "VFR_HUD", "ATTITUDE", "ATTITUDE", "ATTITUDE", "SCALED_IMU", "SCALED_IMU", "SCALED_IMU",
    "ACTUATOR_CONTROL_TARGET", "ACTUATOR_CONTROL_TARGET", "ACTUATOR_CONTROL_TARGET", "ACTUATOR_CONTROL_TARGET",
    "ACTUATOR_CONTROL_TARGET", "VFR_HUD", "LOCAL_POSITION_NED", "LOCAL_POSITION_NED", "LOCAL_POSITION_NED",
    "LOCAL_POSITION_NED", "LOCAL_POSITION_NED", "LOCAL_POSITION_NED", "VFR_HUD", "ATTITUDE_TARGET",
    "ATTITUDE_TARGET", "ATTITUDE_TARGET", "ATTITUDE_TARGET", "ATTITUDE_TARGET", "ATTITUDE_TARGET", "ATTITUDE_TARGET"
]


# PC you want to send it to 
UDP_IP = "10.0.0.39"  # Target machine's IP address
UDP_PORT = 14569  # Chosen port number

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_data(data):
    sock.sendto(data, (UDP_IP, UDP_PORT))

def main(connection_string):
    # Connect to the MAVLink device
    master = mavutil.mavlink_connection(connection_string, baud=57600)
    
    # Request parameters
    for param in PARAM_NAMES:
        master.param_fetch_one(param)
    
    # Infinite loop to handle MAVLink messages
    while True:
        msg = master.recv_match(type='PARAM_VALUE', blocking=True)
        if msg and msg.param_id.decode() in PARAM_NAMES:
            # Format and send data over UDP
            data_str = f"{msg.param_id}: {msg.param_value}"
            send_data(data_str.encode('utf-8'))
            # Additionally, print to the console if needed
            print(data_str)

if __name__ == "__main__":
    connection_string = "/dev/ttyUSB0"
    main(connection_string)
