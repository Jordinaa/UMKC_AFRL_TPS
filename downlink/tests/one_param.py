from pymavlink import mavutil

def main(connection_string):
    # Establish a connection to the MAVLink device
    master = mavutil.mavlink_connection(connection_string, baud=57600)
    
    # Desired message types
    # desired_messages = ["AIRSPEED", "ALTITUDE", "LATITUDE", "LONGITUDE", "ROLL_ANGLE", "PITCH_ANGLE", "HEADING",
    # "ROLL_RATE", "PITCH_RATE", "YAW_RATE", "X_ACCEL", "Y_ACCEL", "Z_ACCEL", "AILERON",
    # "ELEVATOR", "RUDDER", "THROTTLE", "FLAPS", "GROUNDSPEED", "LCL_POSN_X", "LCL_POSN_Y",
    # "LCL_POSN_Z", "LCL_VEL_X", "LCL_VEL_Y", "LCL_VEL_Z", "CLIMB_RATE", "ATTITUDE_CMD_Q1",
    # "ATTITUDE_CMD_Q2", "ATTITUDE_CMD_Q3", "ATTITUDE_CMD_Q4", "ROLL_RATE_CMD", "PITCH_RATE_CMD",
    # "YAW_RATE_CMD"]

    # Infinite loop to process received MAVLink messages
    while True:
        # Read a MAVLink message
        # msg = master.recv_match(type='ATTITUDE')
        msg = master.recv_match(type='Y_ACCEL')

        print(msg)
        # if msg and msg.get_type() in desired_messages:
            # Print the received message if it's one of the desired types
            # print(msg)

if __name__ == "__main__":
    # Connection string; adjust as needed based on your setup
    # For USB: "/dev/ttyUSB0", for telemetry radio on a serial port: "/dev/ttyAMA0", etc.
    connection_string = "/dev/ttyUSB0"
    main(connection_string)