# Docs at robotpy.readthedocs.org
import wpilib

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.drive = wpilib.RobotDrive(0, 1, 2, 3)

        self.leftStick = wpilib.Joystick(1)
        self.middleStick = wpilib.Joystick(2)
        self.rightStick = wpilib.Joystick(3)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)    #Stop robot

    def teleopPeriodic(self):

         # Driving with left and middle sticks

        '''

        right trigger = ball intake (LEDs change color)
        right top button = rev up wheels for shooting (press again to stop)
        right top bottom button = shoot (flip ball up to cannon, stop by limit switch)

        middle top button + bottom button = extend arm


        ultrasonic sensor
        camera with TrackerBox
        '''


if __name__ == "__main__":
    wpilib.run(MyRobot)
