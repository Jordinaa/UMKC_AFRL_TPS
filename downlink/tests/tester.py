from pymavlink import mavutil
import time
import socket

# MAVLink parameter names
PARAM_NAMES = [
    "airspeed", "alt", "latitude", "longitude", "roll", "pitch", "heading",
    "rollspeed", "pitchspeed", "yawspeed", "X_ACCEL", "Y_ACCEL", "Z_ACCEL", "AILERON",
    "ELEVATOR", "RUDDER", "throttle", "FLAPS", "groundspeed", "LCL_POSN_X", "LCL_POSN_Y",
    "LCL_POSN_Z", "LCL_VEL_X", "LCL_VEL_Y", "LCL_VEL_Z", "climb", "ATTITUDE_CMD_Q1",
    "ATTITUDE_CMD_Q2", "ATTITUDE_CMD_Q3", "ATTITUDE_CMD_Q4", "ROLL_RATE_CMD", "PITCH_RATE_CMD",
    "YAW_RATE_CMD"
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
        msg = master.recv_match()
        if msg:  # Check if the msg is not None
            mav_dict = msg.to_dict()
            for param in PARAM_NAMES:
                if param in mav_dict:
                    print(f'{param}: {mav_dict[param]}')
                else:
                    print(f"{param} not found in mav_dict")


if __name__ == "__main__":
    connection_string = "/dev/ttyUSB0"
    main(connection_string)
